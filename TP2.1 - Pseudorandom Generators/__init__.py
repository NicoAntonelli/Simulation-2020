# -*- coding: utf-8 -*-

'''
UTN FRRO - Simulation 2020
TP2.1 - Pseudorandom Generators

Authors: Joshua Acciarri (44823) & Nicolás Antonelli (44852)
Professor: Torres, Juan
Final Date: 16/05/2020

Python Libraries/Modules Used:
    - Numpy:    Random Numbers and Array Manipulation
    - Pyplot:   Matplotlib Module for Graph Plotting
    - Seaborn:  Statistical and Scientific Graphs
    - Scypy:    Distributions like χ2
(?) - Pandas:   THE TABLE...

Other Files:
    - generators:   File with our pseudorandom numbers generators
    - tests:        File with our randomization tests
    - plots:        File with our plotting functions (and the complete saving route (?))
'''

from tests import goodness_fit_test, even_odd_test, test_Kolmogorov_Smirnov, test_gaps
from generators import linear_congruential_generator, middle_square_method, python_generator
from plots import graphing_scatterplots, graphing_histograms, graphing_show_all


# Main
if __name__ == '__main__':
    # General Parameters (all parameters can also be asked)
    total_numbers = 380
    # TO-DO: Save and directory parameters

    print("PSEUDORANDOM GENERATORS")
    print()

    # Middle Square Method
    seed = 9731
    msm_values = middle_square_method(seed, total_numbers)
    print("Middle Square Method")
    print(msm_values)
    print()

    # Congruential Multiplicative Generator (C = 0)
    M = 2**31 - 1
    A = 1103515245
    C = 0
    seed = 876543210
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
    print()
    goodness_fit_test(msm_values)
    even_odd_test(msm_values)  # 5787 passes the test, 9731 does not
    test_Kolmogorov_Smirnov(msm_values)
    test_gaps(msm_values)
    print('-----------------------------------\n')

    print("TESTS: Multiplicative Linear Congruential Generator")
    print()
    goodness_fit_test(multiplicative_random_values)
    even_odd_test(multiplicative_random_values)
    test_Kolmogorov_Smirnov(multiplicative_random_values)
    test_gaps(multiplicative_random_values)
    print('-----------------------------------\n')

    print("TESTS: Mixed Linear Congruential Generator")
    print()
    goodness_fit_test(mixed_random_values)
    even_odd_test(mixed_random_values)
    test_Kolmogorov_Smirnov(mixed_random_values)
    test_gaps(mixed_random_values)
    print('-----------------------------------\n')
    
    print("TESTS: Python's own generator (Mersenne Twister)")
    print()
    goodness_fit_test(pog_mt_values)
    even_odd_test(pog_mt_values)
    test_Kolmogorov_Smirnov(pog_mt_values)
    test_gaps(pog_mt_values)

    print('-----------------------------------\n')

    # TO-DO: Make other 2 tests...

    # TO-DO: Pandas --> Tests Table...

    # Plots
    graphing_scatterplots(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values)
    graphing_histograms(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values)
    graphing_show_all()

    # TO-DO: Optional save method (try-catched)...
