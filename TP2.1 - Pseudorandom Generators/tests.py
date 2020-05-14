# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import chi2


# Goodness of Fit: Uniform Distribution Test (Frecuencial)
# Pearson (Chi Squared) approach
def goodness_fit_test(array):
    alpha_critic    = 0.05                              # Signification level for Critic Region validation
    n_total         = len(array)                        # All the numbers
    e_expected_frec = 10                                # Expected numbers in each class (Greater than 5)
    d_total_classes = round(n_total / e_expected_frec)  # Ammount of classes
    c_classes       = np.zeros(d_total_classes)         # All classes (counters of occurrences, stated at zero)
    
    # Calculating every class occurrences
    # It would be approx to e_expected_frec in every class in order to approve the Null Hypothesis through this test
    for number in array:
        i_class = int((number * d_total_classes) // 1)  # Class number = integer part of (n*d)
        c_classes[i_class] += 1
    
    # Chi squared simplified calculation (Pearson)
    pearson = (d_total_classes / n_total) * sum(i*i for i in c_classes) - n_total

    # Critic region interval calculation (1-a, degrees_of_freedom-1)
    critic_min, critic_max = chi2.interval(1 - alpha_critic, d_total_classes - 1)

    # Critic region: printable presentation
    region_str = "{χ2 ≤ " + str(round(critic_min, 6)) + "} ∪ {χ2 ≥ " + str(round(critic_max, 6)) + "}"
    
    # Null Hypothesis approbation or rejection
    if (pearson <= critic_min or pearson >= critic_max):
        result_msg = "Null hypothesis REJECTION, this list doesn't correspond to an uniform U(0,1) distribution\n"
        result_msg += "This is because " + str(round(pearson, 6)) + " is on the region " + region_str
        result = "Rejected"

    else:
        result_msg = "Null hypothesis ACCEPTATION, this list indeed correspond to an uniform U(0,1) distribution\n"
        result_msg += "This is because " + str(round(pearson, 6)) + " is NOT on the region " + region_str
        result = "Approved"
    
    print('------------UNIFORM TEST-----------')
    print(result_msg)
    print()
    return result


# Parity Test
def even_odd_test(array):
    odds = 0
    # We create a copy in order to mantain the original 
    test_array = np.array(array)
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
        result = "Rejected"
    else:
        print('It seems to be a good generator')        
        result = "Approved"
    print()
    return result


# Kolmogorov_Smirnov Test
def test_Kolmogorov_Smirnov(array):
    print('------------KOMOLGOROV SMIRNOV TEST------------')
    # We create a copy in order to mantain the original untouched
    test_array = np.array(array)
    n = len(test_array)
    test_array.sort()
    # Value below was extracted from table with: alpha = 0.05, n > 50
    d_kolmogorov = 1.36 / (n**0.5)
    Dn_positive = []
    Dn_negative = []
    for i in range(n):
        Dn_positive.append(i/n - test_array[i])
        Dn_negative.append(test_array[i] - (i-1)/n)

    max_dn_pos = max([x for x in Dn_positive])
    max_dn_neg = max([x for x in Dn_negative])
    
    if (max_dn_pos > max_dn_neg): 
        max_general = max_dn_pos 
    else:
        max_general = max_dn_neg

    print('is', max_general, ' < ', d_kolmogorov, ' ?')
    if max_general > d_kolmogorov:
        print("Null hypothesis REJECTION, the list of values doesn't correspond to an uniform U(0,1) distribution")
        result = "Rejected"
    else: 
        print("Null hypothesis ACCEPTATION, the list of values does correspond to an uniform U(0,1) distribution")
        result = "Approved"
    print()
    return result


# Gaps Test
def test_gaps(array):     
    print('------------GAPS TEST------------')
    
    top = 0.5 
    bottom = 0 
    prob = top - bottom # Subinterval's Probability
    
    # Checking if the number belongs to the subinterval
    binary_array = []
    for i in array:
        if (i >= bottom and i < top):
            binary_array.append(1)
        else:
            binary_array.append(0)
    
    # Length of gaps
    gaps_array = []
    count = 0
    for i in binary_array:
        if i==0:
            count += 1
        else:
            # we save how many times it appeared consecutively and then reset it
            gaps_array.append(count) 
            count = 0

    max_gap = max(gaps_array) 
    # We must set a max_generalmum value if it exceeds 15
    if (max_gap > 15): 
        max_gap = 15

    # Observed Freq
    obs_freq = []
    for i in range(max_gap - 1):
        obs_freq.append(gaps_array.count(i))
    obs_freq.append(sum(x >= 15 for x in gaps_array))
    
    # Expected Freq
    exp_freq = []
    for i in range(max_gap):
        exp_freq.append( (1-prob)**i * prob * sum(obs_freq))

    # χ2 value
    our_chi_squared_value = 0
    for i in range(max_gap):
        our_chi_squared_value += (obs_freq[i] - exp_freq[i])**2 / exp_freq[i]

    # Alpha = 0.05
    chi_squared_table_value = chi2.isf(0.05, max_gap - 1)

    print('is', our_chi_squared_value, ' < ', chi_squared_table_value, ' ?')
    if (our_chi_squared_value > chi_squared_table_value): 
      print("Null hypothesis REJECTION, these numbers are not independent according to the GAPS TEST")
      result = "Rejected"
    else: 
        print("Null hypothesis ACCEPTATION, these numbers are independent according to the GAPS TEST")
        result = "Approved"
    print()
    return result
