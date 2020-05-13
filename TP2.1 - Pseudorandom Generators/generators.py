# -*- coding: utf-8 -*-

import numpy as np


# Linear Congruential Generator (LGC)
def linear_congruential_generator(M, A, C, seed, total):
    x_values = [seed]
    for _ in range (total-1):
        x_values.append((x_values[-1] * A + C) % M)
    x_values = np.array(x_values)
    return lgc_bounded(x_values, M)

# LGC values into an uniform U(0, 1) distribution
def lgc_bounded(array, M):
    return np.array([x for x in array / M])


# Middle Square Method
def middle_square_method(seed, total):
    newSeed = seed
    x_values = []
    for _ in range(total):
        newSeed = newSeed**2
        value_str = list(map(int, str(newSeed)))

        for i in range(8 - len(value_str)):
            value_str.insert(0, 0)

        newSeed = int(''.join(str(i) for i in value_str[2:6]))
        x_values.append(newSeed)
    x_values = np.array(x_values) / 10000
    return x_values


# Python's own generator (Mersenne Twister)
def python_generator(n):
    return np.random.random_sample(n)
