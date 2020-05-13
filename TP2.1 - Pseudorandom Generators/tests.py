# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import chi2


# Goodness Fit: Uniform Distribution Test (Frecuencial)
# Pearson (Chi Squared) approach
def goodness_fit_test(array):
    alpha_critic    = 0.05                              # Signification level for Critic Region validation
    n_total         = len(array)                        # All the numbers
    e_expected_frec = 10                                # Expected numbers in each class (Greater than 5)
    d_total_classes = round(n_total / e_expected_frec)  # Ammount of classes
    c_classes = np.zeros(d_total_classes)               # All classes (counters of occurrences)
    # p_probability   = 1/d_total_classes               # Occurrence probability
    
    # Calculating every class occurrences
    # It would be approx to e_expected_frec in every class in order to approve the Null Hypotesis throught this test
    for number in array:
        i_class = int((number * d_total_classes) // 1)  # Class number = integer part of (n*d)
        c_classes[i_class] += 1
    
    # Chi squared simplified calculation (Pearson)
    pearson = (d_total_classes / n_total) * sum(i*i for i in c_classes) - n_total

    # Critic region interval calculation (1-a, degrees_of_freedom-1)
    critic_min, critic_max = chi2.interval(1 - alpha_critic, d_total_classes - 1)

    # Critic region: printable presentation
    region_str = "{χ2 ≤ " + str(round(critic_min, 6)) + "} ∪ {χ2 ≥ " + str(round(critic_max, 6)) + "}"
    
    # Null Hypotesis approbation or rejection
    if (pearson <= critic_min or pearson >= critic_max):
        result = "Null hypotesis REJECTION, the numbers doesn't correspond to an uniform U(0,1) distribution\n"
        result += "This is because " + str(round(pearson, 6)) + " is on the region " + region_str
    else:
        result = "Null hypotesis ACCEPTATION, the numbers indeed correspond to an uniform U(0,1) distribution\n"
        result += "This is because " + str(round(pearson, 6)) + " is NOT on the region " + region_str
    
    print('------------UNIFORM TEST-----------')
    print(result)
    print()


# Parity Test
def even_odd_test(array):
    odds = 0
    # We create a copy in order to mantain the original 
    test_array = np.array(array)
    # print(array) # Array already shown
    for i in range(len(test_array)):
        test_array[i] = round(test_array[i]*100)
        if (test_array[i] % 2 != 0):
            odds += 1
    orf = odds/len(test_array)
    
    print('------------PARITY TEST------------')
    print('Total length of the array:', len(test_array))
    print('Odds Absolute Frequency:', odds)
    print('Odds Relative Frequency:', orf)
    if(orf<0.45 or orf>0.55):
        print('It seems that this is not a good generator, or may be more iterations are needed')
    else:
        print('It seems to be a good generator')        
    print()

    # TO-DO: Make other 2 tests...
