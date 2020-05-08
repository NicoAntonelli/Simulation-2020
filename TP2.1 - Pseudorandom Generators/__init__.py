# -*- coding: utf-8 -*-

'''
UTN FRRO - Simulation 2020
TP2.1 - Pseudorandom Generators

Authors: Joshua Acciarri (44823) & Nicolás Antonelli (44852)
Professor: Torres, Juan
Final Date: 16/05/2020

Python Libraries/Modules Used:
    - Numpy: Random Numbers and Array Manipulation
    - Pyplot: Matplotlib Module for Graph Plotting
    - Seaborn: Statistical and Scientific Graphs
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Linear Congruential Generator (LGC)
def linear_congruential_generator(M, A, C, X0, total):
    x_values = [X0]
    for _ in range (total-1):
        x_values.append((x_values[-1] * A + C) % M)
    x_values = np.array(x_values)
    return x_values

# LGC values into an uniform U(0, 1) distribution
def lgc_bounded(array, M):
    return np.array([x for x in array / M])


# Main
if __name__ == '__main__':
    # General Parameters (all parameters can also be asked)
    total_numbers = 50
    sns.set()

    # LGC Parameters
    M = 2**31 - 1
    A = 1103515245
    C = 0
    X0 = 876543210

    print("Pseudorandom Generators")
    print()

    # Congruential Multiplicative Generator (C = 0)
    multiplicative_random_values = np.array(linear_congruential_generator(M, A, C, X0, total_numbers))
    multiplicative_random_values = lgc_bounded(multiplicative_random_values, M)
    print("Multiplicative LCG")
    print(multiplicative_random_values)
    print()

    # Congruential Mixed Generator (C != 0)
    C = A - 42
    mixed_random_values = np.array(linear_congruential_generator(M, A, C, X0, total_numbers))
    mixed_random_values = lgc_bounded(mixed_random_values, M)
    print("Mixed LCG")
    print(mixed_random_values)
    print()

    # Scatter Plots (Simultaneously)
    sns.scatterplot(data=multiplicative_random_values)
    sns.scatterplot(data=mixed_random_values)
    plt.show()

    # Do NOT forget: Histograms
