# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import chi2, uniform, norm, expon, gamma
from plots import cdf_plots


# A list of pseudorandom number passes the mean and deviation tests within an acceptance intervale
acceptance_margin = 0.15
acceptance_interval = [1 - acceptance_margin, 1 + acceptance_margin]

# Simulated vs Analytic Statistic Parameters Calculation - Mean Test and Variance Test
def statistics_parameters_test(numbers_list, real_parameter_result, parameter_name):
    if (parameter_name == "Mean"): simulated_result = np.mean(numbers_list)
    if (parameter_name == "Variance"): simulated_result = np.var(numbers_list)
    print(parameter_name + " value is", simulated_result)
    print("And it is expected to be", real_parameter_result)
    relation = simulated_result / real_parameter_result
    if (acceptance_interval[0] <= relation <= acceptance_interval[1]):
        print(parameter_name + " Test PASSED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    else:
        print(parameter_name + " Test REJECTED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    print()

# Kolmogorov_Smirnov Test
def test_Kolmogorov_Smirnov(uniform_values):
    print('------------KOLMOGOROV SMIRNOV TEST------------')
    test_array = np.array(uniform_values)
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
        print("Null hypothesis REJECTION, the list of values doesn't correspond to an uniform U(a,b) distribution")
        result = "Rejected"
    else: 
        print("Null hypothesis ACCEPTATION, the list of values does correspond to an uniform U(a,b) distribution")
        result = "Approved"
    print()
    
# Simulated vs Analytic Plot of the cumulative distribution functions
def cdf_comparative_test(numbers_list, distribution_name, loc_p, scale_p, save):
    sim_x = np.sort(numbers_list)
    sim_y = np.arange(1, len(sim_x)+1) / len(sim_x)
    if(distribution_name == 'uniform'):
        rv = uniform()
    elif(distribution_name == 'normal'):
        rv = norm(loc=loc_p, scale=scale_p)
    elif(distribution_name == 'exponential'):
        rv = expon(loc=loc_p, scale=scale_p)
    elif(distribution_name == 'gamma'):
        rv = gamma(a=loc_p/2, loc=1, scale=(1/scale_p)+0.14)
         # Scale generalization problem, adjusted for 500 iterations
    else:
        print("Critical Error")
        exit()
    x = np.linspace(np.maximum(rv.dist.a, min(sim_x)), np.minimum(rv.dist.b, max(sim_x)))
    cdf_plots(x, rv.cdf(x), sim_x, sim_y, distribution_name, save)
