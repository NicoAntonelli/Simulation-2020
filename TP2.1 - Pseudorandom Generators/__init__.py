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

import matplotlib.pyplot as plt
from tests import testEvenOdd
from generators import linear_congruential_generator, middle_square_method, python_generator
from plots import graphing_scatterplots, graphing_histograms

# Main
if __name__ == '__main__':
    # General Parameters (all parameters can also be asked)
    total_numbers = 300

    # LGC Parameters
    M = 2**31 - 1
    A = 1103515245
    C = 0
    seed = 876543210 # X0

    print("PSEUDORANDOM GENERATORS")
    print()

    # Middle Square Method
    msm_values = middle_square_method(9731, total_numbers)
    print("Middle Square Method")
    print(msm_values)
    print()

    # Congruential Multiplicative Generator (C = 0)
    multiplicative_random_values = linear_congruential_generator(M, A, C, seed, total_numbers)
    print("Multiplicative LCG")
    print(multiplicative_random_values)
    print()

    # Congruential Mixed Generator (C != 0)
    C = 42
    mixed_random_values = linear_congruential_generator(M, A, C, seed, total_numbers)
    print("Mixed LCG")
    print(mixed_random_values)
    print() 
    
    # Python's own generator (Mersenne Twister)
    pog_mt_values = python_generator(total_numbers)
    print("Python's own generator (Mersenne Twister)")
    print(pog_mt_values)
    print()

    # Tests
    print("TESTS: Middle Square Method")
    testEvenOdd(msm_values)  # 5787 passes the test, 9731 does not
    print("TESTS: Multiplicative Linear Congruential Generator")
    testEvenOdd(multiplicative_random_values)
    print("TESTS: Mixed Linear Congruential Generator")
    testEvenOdd(mixed_random_values)
    print("TESTS: Python's own generator (Mersenne Twister)")
    testEvenOdd(pog_mt_values)

    # Plots
    graphing_scatterplots(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values)
    graphing_histograms(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values)
    plt.show()
