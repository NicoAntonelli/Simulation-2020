# -*- coding: utf-8 -*-

from numpy.random import random
from numpy import floor, log as ln, exp


# Uniform Distribution Generator
def uniform(a, b):
    r = random()
    x = a + (b - a) * r
    return x

# Normal Distribution Generator
def normal(m, d):
    sum = 0
    for _ in range(12):
        r = random()
        sum += r
    x = d * (sum - 6) + m
    return x

# Exponential Distribution Generator
def exponential(ex):
    r = random()
    x = -ex * ln(r)
    return x

# Gamma Distribution Generator
def gamma(k, alpha):
    tr = 1
    for _ in range(k):
        r = random()
        tr = tr * r
    x = -ln(tr) / alpha
    return x

# Binomial Distribution Generator
def binomial(n, p):
    x = 0
    for _ in range(1, n):
        r = random()
        if (r - p <= 0):
            x += 1
    return x

# Pascal (Negative Binomial) Distribution Generator
def pascal(k, p):
    tr = 1
    qr = ln(1-p)
    for _ in range(k):
        r = random()
        tr = tr * r
    x = floor(ln(tr)/qr)
    return x

# Hypergeometric Distribution Generator
def hypergeometric(N, n, p):
    x = 0
    for i in range(1, n):
        r = random()
        if (r - p <= 0):
            s = 1
            x = x + 1
        else:
            s = 0
        p = (N * p - s) / (N - 1)
        N = N - 1
    return x

# Poisson Distribution Generator
def poisson(L):
    x = 0
    b = exp(-L)
    tr = 1
    while(tr-b >= 0):
        r = random()
        tr = tr * r
        x += 1
    return x

# Empirical Distribution Definition for the Generator
empirical_distribution = {
    0: {"probability": 0.06, "accumulated": 0.06},
    1: {"probability": 0.12, "accumulated": 0.18},
    2: {"probability": 0.08, "accumulated": 0.26},
    3: {"probability": 0.09, "accumulated": 0.35},
    4: {"probability": 0.11, "accumulated": 0.46},
    5: {"probability": 0.16, "accumulated": 0.60},
    6: {"probability": 0.05, "accumulated": 0.65},
    7: {"probability": 0.15, "accumulated": 0.80},
    8: {"probability": 0.16, "accumulated": 0.96},
    9: {"probability": 0.04, "accumulated": 1.00},
}

# Empirical Distribution Analytic Parameters Initialization
def empirical_init():
    mean = sum([key * value["probability"] for (key, value) in empirical_distribution.items()])
    variance = sum([( (key - mean)**2 ) * value["probability"] for (key, value) in empirical_distribution.items()])
    return mean, variance

# Empirical Distribution Generator 
def empirical():
    r = random()
    for (key, value) in empirical_distribution.items():
        if (r <= value["accumulated"]):
            return key
