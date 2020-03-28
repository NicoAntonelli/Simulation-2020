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

if __name__ == "__main__":
    print("Simulación de Ruleta")

    # Total Iterations
    iterations = abs(int(input("Iteraciones (Tiradas): ")))

    # All 'European' Roulette Numbers from 0 to 36
    numbers = np.arange(0, 36)

    # Expected Values
    rfr_expected = round(1/len(numbers), 3)     # Relative Frecuency Expected
    print("Frecuencia Relativa Esperada: "+str(rfr_expected))
    # avg_expected = round(np.mean(numbers), 3)   # Average (Mean) Expected
    # print("Valor Promedio Esperado: "+str(avg_expected))
    # var_expected = round(np.var(numbers), 3)    # Deviation Expected
    # print("Varianza Esperada: "+str(var_expected))
    # dev_expected = round(np.std(numbers), 3)    # Variance Expected
    # print("Desvío Esperado: "+str(dev_expected))
    print()

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
    
    # Graphs
    fig, axs = plt.subplots(2, 2)
    fig.canvas.set_window_title("Simulación de Ruleta: Análisis (de 0 a "+str(iterations)+" tiradas)")
    axs[0, 0].plot(rfr_array, 'tab:blue')
    axs[0, 0].set_title("Frecuencia Relativa")
    axs[0, 0].axhline(rfr_expected, color='red', linestyle='--')
    plt.setp(axs[0, 0], ylabel="FR del Número "+str(one_number))

    axs[0, 1].plot(avg_array, 'tab:orange')
    axs[0, 1].set_title('Valor Promedio')
    # axs[0, 1].axhline(avg_expected, color='red', linestyle='--')

    axs[1, 0].plot(var_array, 'tab:green')
    axs[1, 0].set_title('Varianza')
    # axs[1, 0].axhline(var_expected, color='red', linestyle='--')

    axs[1, 1].plot(dev_array, 'tab:purple')
    axs[1, 1].set_title('Desvío')
    # axs[1, 1].axhline(dev_expected, color='red', linestyle='--')

    for ax in fig.get_axes():
        ax.grid(True)
        plt.setp(ax, xlabel="Número de Tiradas")
    fig.tight_layout()
    plt.show()
