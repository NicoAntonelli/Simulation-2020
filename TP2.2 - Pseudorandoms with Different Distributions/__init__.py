# -*- coding: utf-8 -*-

'''
UTN FRRO - Simulation 2020
TP2.2 - Pseudorandom Numbers Generation on Different Distributions

Authors: Joshua Acciarri (44823) & Nicolás Antonelli (44852)
Professor: Torres, Juan
Final Date: 10/06/2020

Python Libraries/Modules Used:
    - Numpy:    Mersenne-Twister Generator, Functions and Array Manipulation
    - Pyplot:   Matplotlib Module for Graph Plotting
    - Scypy:    Reference Distributions for Graphical Comparison Tests 

Other Files:
    - distributions: File with our analyzed distributions' definitions
    - tests:         File with our randomization tests for different distributions
    - plots:         File with our plotting and save functions
'''

import numpy as np
from distributions import uniform, exponential, gamma, normal, binomial, pascal, hypergeometric, poisson, empirical, empirical_init
from tests import statistics_parameters_test, test_Kolmogorov_Smirnov, cdf_comparative_test
from plots import graphing_show_all


# General parameters
iterations = int(float(input("DISTRIBUTIONS ANALYSIS\nHow many pseudorandom numbers would you want to analyze?: ")))  # example: 500
save = {"mode": False, "route": "graphs/", "total": iterations} # If mode is False, the graphs won't be saved

# Uniform parameters, U ~ (a: min, b: max)
a = 10
b = 18

# Normalize function in order to run the Kolmogorov_Smirnov Test
def normalize(n):
  return (n-a) / (b-a)

# Normal parameters, N ~ (m: mean, d: deviation)
m = 10 
d = 2

# Exponential parameters, E ~ (alpha_exp: rate parameter)
alpha_exp = 3

# Gamma parameters, G ~ (k: shape parameter, alpha_gamma: scale parameter)
k_gamma = 10
alpha_gamma = 3

# Binomial parameters, B ~ (n: amount of independent experiments, p: success probability)
n_binomial = 100
p_binomial = 0.5

# Pascal parameters, NB ~ (r: success cases, p: success probability)
k_pascal = 4
p_pascal = 0.8

# Poisson parameters, P ~ (L: rate parameter)
L = 10  # Lambda

# Hypergeometric parameters, H ~ (N: population initial value,
# p: population proportion consisting of I-class elements, n: sample size)
N_hyper = 500
n_hyper = 80
p_hyper = 0.6

# Empirical initialization
mean, variance = empirical_init()


# Main
# Lists Initialization
uniform_values        = np.zeros(iterations)
normal_values         = np.zeros(iterations)
exponential_values    = np.zeros(iterations)
gamma_values          = np.zeros(iterations)
binomial_values       = np.zeros(iterations)
pascal_values         = np.zeros(iterations)
hypergeometric_values = np.zeros(iterations)
poisson_values        = np.zeros(iterations)
empirical_values      = np.zeros(iterations)

# Distributions Generation
for i in range(iterations):
    uniform_values[i]        = uniform(a, b)
    normal_values[i]         = normal(m, d)
    exponential_values[i]    = exponential(1/alpha_exp)
    gamma_values[i]          = gamma(k_gamma, alpha_gamma)
    binomial_values[i]       = binomial(n_binomial, p_binomial)
    pascal_values[i]         = pascal(k_pascal, p_pascal)
    hypergeometric_values[i] = hypergeometric(N_hyper, n_hyper, p_hyper)
    poisson_values[i]        = poisson(L)
    empirical_values[i]      = empirical()

print(iterations, "pseudorandom numbers generated of each distribution\n")

# Statistics Parameter Tests
print("//////////// STATISTICS PARAMETERS TESTS ////////////\n")

print('-----UNIFORM DISTRIBUTION------')
# print(uniform_values)
statistics_parameters_test(uniform_values, (a+b)/2, 'Mean')
statistics_parameters_test(uniform_values, ((b-a)**2)/12, 'Variance')
uniform_normalized_values = list(map(normalize, uniform_values))
print()

print('-----NORMAL DISTRIBUTION------')
# print(normal_values)
statistics_parameters_test(normal_values, m, 'Mean')
statistics_parameters_test(normal_values, d**2, 'Variance')
print()

print('-----EXPONENTIAL DISTRIBUTION------')
# print(exponential_values)
statistics_parameters_test(exponential_values, 1/alpha_exp, 'Mean')
statistics_parameters_test(exponential_values, 1/(alpha_exp**2), 'Variance')
print()

print('-----GAMMA DISTRIBUTION------')
# print(gamma_values)
statistics_parameters_test(gamma_values, k_gamma/alpha_gamma, 'Mean')
statistics_parameters_test(gamma_values, k_gamma/(alpha_gamma**2), 'Variance')
print()

print('-----BINOMIAL DISTRIBUTION------')
# print(binomial_values)
statistics_parameters_test(binomial_values, n_binomial*p_binomial, 'Mean')
statistics_parameters_test(binomial_values, (n_binomial*p_binomial*(1-p_binomial)), 'Variance')
print()

print('-----PASCAL DISTRIBUTION (NEGATIVE BINOMIAL)------')
# print(pascal_values)
statistics_parameters_test(pascal_values, (k_pascal*(1-p_pascal))/p_pascal, 'Mean')
statistics_parameters_test(pascal_values, ((k_pascal*(1-p_pascal))/p_pascal**2), 'Variance')
print()

print('-----HYPERGEOMETRIC DISTRIBUTION------')
# print(pascal_values)
statistics_parameters_test(hypergeometric_values, n_hyper*p_hyper, 'Mean')
statistics_parameters_test(hypergeometric_values, n_hyper*p_hyper*(1-p_hyper)*( (N_hyper-n_hyper)/(N_hyper-1)), 'Variance')
print()

print('-----POISSON DISTRIBUTION------')
# print(poisson_values)
statistics_parameters_test(poisson_values, L, 'Mean')
statistics_parameters_test(poisson_values, L, 'Variance')
print()

print('-----EMPIRICAL DISTRIBUTION------')
# print(empirical_values)
statistics_parameters_test(empirical_values, mean, 'Mean')
statistics_parameters_test(empirical_values, variance, 'Variance')
print()

# K-S Generalization Test
print("//////////// PSEUDORANDOM GENERATOR TEST ////////////\n")
test_Kolmogorov_Smirnov(uniform_normalized_values)

# Graphical Testings
cdf_comparative_test(uniform_normalized_values, 'uniform', a, b, save)
cdf_comparative_test(normal_values, 'normal', m, d, save)
cdf_comparative_test(exponential_values, 'exponential', 0, 1/alpha_exp, save)
cdf_comparative_test(gamma_values, 'gamma', k_gamma, alpha_gamma, save)
graphing_show_all()
