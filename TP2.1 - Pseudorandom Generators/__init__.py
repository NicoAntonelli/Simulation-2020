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
    - Pandas:   Series and DataFrame table for tests results' summaring

Other Files:
    - generators:   File with our pseudorandom numbers generators
    - tests:        File with our randomization tests
    - plots:        File with our plotting and save functions
'''

from tests import goodness_fit_test, even_odd_test, test_Kolmogorov_Smirnov, test_gaps
from generators import linear_congruential_generator, middle_square_method, python_generator
from plots import graphing_scatterplots, graphing_histograms, graphing_show_all, tests_final_table


# Main
if __name__ == '__main__':
    # General Parameters
    title = "PSEUDORANDOM GENERATORS"
    print(title)
    total_numbers = int(float(input("How many pseudorandoms numbers do you want to analyze?: ")))  # example: 380
    save = {"mode": True, "route": "graphs/", "total": total_numbers } # If mode is False, the graphs won't be sabed
    print()

    # Middle Square Method
    seed = 5787 # Other: 9731
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
    # Tests also displays more detailed info on console
    print("TESTS: Middle Square Method")
    print()
    msm_results = []
    msm_results.append(goodness_fit_test(msm_values))
    msm_results.append(even_odd_test(msm_values))
    msm_results.append(test_Kolmogorov_Smirnov(msm_values))
    msm_results.append(test_gaps(msm_values))
    print('-----------------------------------\n')

    print("TESTS: Multiplicative Linear Congruential Generator")
    print()
    mult_lcg_results = []
    mult_lcg_results.append(goodness_fit_test(multiplicative_random_values))
    mult_lcg_results.append(even_odd_test(multiplicative_random_values))
    mult_lcg_results.append(test_Kolmogorov_Smirnov(multiplicative_random_values))
    mult_lcg_results.append(test_gaps(multiplicative_random_values))
    print('-----------------------------------\n')

    print("TESTS: Mixed Linear Congruential Generator")
    print()
    mix_lcg_results = []
    mix_lcg_results.append(goodness_fit_test(mixed_random_values))
    mix_lcg_results.append(even_odd_test(mixed_random_values))
    mix_lcg_results.append(test_Kolmogorov_Smirnov(mixed_random_values))
    mix_lcg_results.append(test_gaps(mixed_random_values))
    print('-----------------------------------\n')
    
    print("TESTS: Python's own generator (Mersenne Twister)")
    print()
    pog_mt_results = []
    pog_mt_results.append(goodness_fit_test(pog_mt_values))
    pog_mt_results.append(even_odd_test(pog_mt_values))
    pog_mt_results.append(test_Kolmogorov_Smirnov(pog_mt_values))
    pog_mt_results.append(test_gaps(pog_mt_values))
    print('-----------------------------------\n')

    # Table with tests' summaring and all generators' graphs
    print("Tests Results' Summaring")
    print()
    tests_final_table(msm_results, mult_lcg_results, mix_lcg_results, pog_mt_results, save)

    graphing_scatterplots(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values, save)
    graphing_histograms(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values, save)
    graphing_show_all()
    print()
