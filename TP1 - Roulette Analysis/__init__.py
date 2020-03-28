#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UTN FRRO - Simulation 2020
TP1 - Roulette Analysis

Author: Antonelli, Nicolás (44852)
Professor: Torres, Juan
Date: 15/04/2020
"""

import random as rand
import numpy as np
import matplotlib.pyplot as plt

# Graphication Function
def graph(array, expected_val, title, ylabel):
    plt.plot(array)
    # plt.stem(array)
    plt.axhline(expected_val, color='red', linestyle='--')
    plt.grid(True)
    plt.title(title)
    plt.axis([-1, len(array), 0, max(array)*1.1])
    plt.xlabel("Tiradas de Ruleta")
    plt.ylabel(ylabel)
    plt.show()

if __name__ == "__main__":
    print("Roulette Simulation (Numeral Analysis)")

    # Total Iterations
    iterations = abs(int(input("Iterations (example=100000): ")))

    # All 'European' Roulette Numbers from 0 to 36
    numbers = np.arange(0, 36)

    # Expected Values
    rfr_expected = round(1/len(numbers), 3)     # Relative Frecuency Expected
    avg_expected = round(np.mean(numbers), 3)   # Average (Mean) Expected
    var_expected = round(np.var(numbers), 3)    # Deviation Expected
    dev_expected = round(np.std(numbers), 3)    # Variance Expected

    # I need any number for the Analysis too, so I will use a Random One
    one_number = rand.randint(0, 36)

    # For Every Iteration: Mean-Deviaton-Variance Values & Relative Frecuency of One Number
    rfr_array = [0] # Relative Frecuencies of One Number Array Initialization
    avg_array = [0] # Average (Mean) Arry Initialization
    var_array = [0] # Variance Array Initialization
    dev_array = [0] # Deviation Array Initialization
    numbers = np.zeros(37, dtype=int) # Initialization for Obtained Roulette's Values
    for i in range(1, iterations):
        for j in range(0, i):
            # Playing Roulette and Analyzing the Obtained Numbers
            n = rand.randint(0, 36)
            numbers[n] += 1
        # Filling Important Arrays
        rfr_array.append(numbers[one_number]/sum(numbers))
        avg_array.append(round(np.mean(numbers), 6))
        var_array.append(round(np.var(numbers), 6))
        dev_array.append(round(np.std(numbers), 6))
        numbers = np.zeros(37, dtype=int) # Reset for all Obtained Roulette's Values

    # Show the Relative Frecuency (Of One Number) Array
    graph(rfr_array, rfr_expected, "ANÁLISIS DE FRECUENCIA (0 A "+str(iterations)+" TIRADAS)", "Frecuencia Relativa del Número "+str(one_number))
    
    # Show the Averages (Means) Array
    graph(avg_array, avg_expected, "ANÁLISIS DE LA MEDIA (0 A "+str(iterations)+" TIRADAS)", "Valor Promedio de las Tiradas")
    
    # Show the Variance Array
    graph(var_array, var_expected, "ANÁLISIS DE LA VARIANZA (0 A "+str(iterations)+" TIRADAS)", "Varianza de las Tiradas")
    
    # Show the Deviation Array
    graph(dev_array, dev_expected, "ANÁLISIS DE LA DESVIACIÓN (0 A "+str(iterations)+" TIRADAS)", "Desvío de las Tiradas")
