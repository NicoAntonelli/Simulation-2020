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

# (DELETE)Middle Square Method just for understaing
def middle_square_method_understanding(seed, total):
    seed = seed**2
    print('Original seed', seed)
    value_str = list(map(int, str(seed)))
    print('Before adding zeros', value_str)
    for i in range(8-len(value_str)):
        value_str.insert(0, 0)

    print('Before cutting it', value_str)
    value_str.pop(7)
    value_str.pop(6)
    value_str.pop(1)
    value_str.pop(0)
    print('After', value_str)
    
    newSeed = ''
    for i in range(0, 4):
        value_str[i] = str(value_str[i])
        newSeed += value_str[i]
    
    print('new seed', newSeed)
    print('new number seed without zeros', int(newSeed))

# Middle Square Method
def middle_square_method(seed, total):
    newSeed = seed
    x_values = []
    for _ in range(total):
        newSeed = newSeed**2
        value_str = list(map(int, str(newSeed)))
        for i in range(8-len(value_str)):
            value_str.insert(0, 0)
        
        newSeed = ''
        for i in range(2, 6):
            value_str[i] = str(value_str[i])
            newSeed += value_str[i]
        newSeed = int(newSeed)
        x_values.append(newSeed)
    return x_values

def testEvenOdd(array):
    odds = 0
    for i in range(len(array)):
        if (array[i] % 2 != 0):
            odds += 1
    print('------------PARITY TEST------------')
    print('Total length of the array:', len(array))
    print('Odds Absolute Frequency:', odds)
    print('Odds Relative Frequency:', odds/len(array))
    print('-----------------------------------')

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
    #print(multiplicative_random_values)
    print()

    # Congruential Mixed Generator (C != 0)
    C = A - 42
    mixed_random_values = np.array(linear_congruential_generator(M, A, C, X0, total_numbers))
    mixed_random_values = lgc_bounded(mixed_random_values, M)
    print("Mixed LCG")
    print(mixed_random_values)
    print()

    # Middle square Method
    # test it with different seeds, then delete
    middle_square_method_understanding(1245, 1)
    # the real one
    values = middle_square_method(9731,25)
    testEvenOdd(values)

    # Scatter Plots (Simultaneously)
    sns.scatterplot(data=multiplicative_random_values)
    sns.scatterplot(data=mixed_random_values)
    plt.show()

    # Do NOT forget: Histograms
