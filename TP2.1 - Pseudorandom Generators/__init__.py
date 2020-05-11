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
from tests import testEvenOdd
from generators import linear_congruential_generator, middle_square_method, python_generator




# Main
if __name__ == '__main__':
    # General Parameters (all parameters can also be asked)
    total_numbers = 150
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
    print("Multiplicative LCG")
    print(multiplicative_random_values)
    print()

    # Congruential Mixed Generator (C != 0)
    C = 42
    mixed_random_values = np.array(linear_congruential_generator(M, A, C, X0, total_numbers))
    print("Mixed LCG")
    print(mixed_random_values)
    print()

    # Middle square Method
    msm_values = middle_square_method(9731, total_numbers)
    print("Middle Square Method")
    print(msm_values)
    print()
    
    # Python's Own Generator
    pog_values = np.array(python_generator(total_numbers))
    print("Python's Own Generator")
    print(pog_values)
    print()


    # Tests
    testEvenOdd(msm_values)  # 5787 passes the test, 9731 does not
    testEvenOdd(pog_values)
    testEvenOdd(mixed_random_values)


    # Scatter Plots (Simultaneously)
    sns.scatterplot(data=multiplicative_random_values)
    sns.scatterplot(data=mixed_random_values)
    sns.scatterplot(data=pog_values)
    plt.show()

    # Do NOT forget: Histograms
