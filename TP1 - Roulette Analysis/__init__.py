#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UTN FRRO - Simulation 2020
TP1 - Roulette Analysis

Author: Antonelli, Nicolás (44852)
Professor: Torres, Juan
Final Date: 15/04/2020

Python Libraries/Modules Used:
    - Numpy: Random Numbers, Statistical Functions, Array Manipulation
    - Pyplot: Matplotlib Module for Graph Plotting
    - Time: Module used for processing time measurement

Note: All Printed Messages and Plotted Graphs are in SPANISH
"""

import numpy as np
import matplotlib.pyplot as plt
import time


if __name__ == "__main__":
    print("SIMULACIÓN DE RULETA")
    print()
    
    # All 'European' Roulette Numbers from 0 to 36 (Total: 37)
    numbers = np.arange(0, 37)
    
    # Expected Values
    rfr_expected = round(1/len(numbers), 6)     # Relative Frecuency Expected (1/37)
    avg_expected = round(np.mean(numbers), 6)   # Average (Mean) Expected (666/37)
    var_expected = round(np.var(numbers), 6)    # Variance Expected (114)
    dev_expected = round(np.std(numbers), 6)    # Deviation Expected (Square Root of 114)
    print("Frecuencia Relativa Esperada: "+str(rfr_expected))
    print("Valor Promedio Esperado: "+str(avg_expected))
    print("Varianza Esperada: "+str(var_expected))
    print("Desvío Esperado: "+str(dev_expected))
    print()

    # Total "Results" to Plot at the Same Time (For the 2nd 4-Stack of Graphs):
    # Recommended: Between 5 and 10
    results = 6

    # Total Iterations (Example: Try with 500)
    iterations = 0
    while (iterations==0):
        # Validation
        iterations = abs(int(float(input("Ingrese Iteraciones (Tiradas): "))))
    print()

    # Any Number for the Analysis
    one_number = 37
    while (one_number>36):
        # Validation
        one_number = abs(int(float(input("Ingrese su Número (Entre 0 y 36): "))))
    print()
    
    # Timer (Execution Time Measurement)
    start_time = time.time()

    # For Every Iteration: Mean-Deviaton-Variance Values & Relative Frecuency of One Number
    # Matix Re-Size: Arrays of Arrays, Needed for the Graph with few "Results" simultaniously
    rfr_array = np.zeros((results, iterations+1)) # Relative Frecuencies of One Number Array Initialization
    avg_array = np.zeros((results, iterations+1)) # Average (Mean) Arry Initialization
    var_array = np.zeros((results, iterations+1)) # Variance Array Initialization
    dev_array = np.zeros((results, iterations+1)) # Deviation Array Initialization
    roulette_values = np.zeros(37, dtype=int) # Initialization for Obtained Roulette's Values
    print("Cargando "+str(iterations)+" iteraciones...")
    acum_load_time = 0 # Variable Needed for Time Measurement
    for i in range(results):
        for n in range(1, iterations+1):
            # Playing Roulette and Analyzing the Obtained Numbers
            roulette_values = np.random.randint(0, 37, n) # Random Numbers Generator (Total = N Numbers)
            # Occurrences Counter of One_Number (The Input Number)
            one_number_occurrences = np.count_nonzero(roulette_values == one_number)
            # Filling Important Arrays (In the Matrix Position for the Actual Results Array)
            rfr_array[i][n] = one_number_occurrences / n                    # Relative Frecuency of "One_Number"
            avg_array[i][n] = round(np.mean(roulette_values), 6)            # Average (Mean)
            var_array[i][n] = variance = round(np.var(roulette_values), 6)  # Variance
            dev_array[i][n] = round(variance ** 0.5, 6)                     # Standard Deviation (Square Root of Variance)
        # Calculate and Show intermediate processing Time
        last_load_time = time.time() - start_time - acum_load_time
        acum_load_time = time.time() - start_time
        print("Array Resultado "+str(i+1)+" de "+str(results)+" completado en "+str(round(last_load_time, 6))+ " segundos")

    # Total Calculation Time
    final_time = round(time.time() - start_time, 6)
    print("Todos los Arrays de Resultados fueron completados en "+str(final_time)+ " segundos")
    print()
    
    # First Array of Results' Graphs
    fig, axs = plt.subplots(2, 2)
    fig.canvas.set_window_title("Simulación de Ruleta: Análisis (de 0 a "+str(iterations)+" tiradas) - Stack 1")

    axs[0, 0].plot(rfr_array[0], 'tab:blue', label="FRN")
    axs[0, 0].set_title("Frecuencia Relativa")
    axs[0, 0].axhline(rfr_expected, color='red', linestyle='--', label="FRE")
    plt.setp(axs[0, 0], ylabel="FR del Número "+str(one_number))

    axs[0, 1].plot(avg_array[0], 'tab:orange', label="VPN")
    axs[0, 1].set_title('Valor Promedio')
    axs[0, 1].axhline(avg_expected, color='red', linestyle='--', label="VPE")

    axs[1, 0].plot(var_array[0], 'tab:green', label="VVN")
    axs[1, 0].set_title('Varianza')
    axs[1, 0].axhline(var_expected, color='red', linestyle='--', label="VVE")

    axs[1, 1].plot(dev_array[0], 'tab:purple', label="VDN")
    axs[1, 1].set_title('Desvío')
    axs[1, 1].axhline(dev_expected, color='red', linestyle='--', label="VDE")
    
    for ax in fig.get_axes():
        ax.grid(True)
        ax.legend()
        plt.setp(ax, xlabel="Número de Tiradas")
    
    fig.tight_layout()
    plt.savefig("TP1 - Roulette Analysis/graphs/graph_iterations_"+str(iterations)+".png")
    print("1er 4-Stack de Gráficos Guardado Correctamente")
    print()

    # Now, Comparing all the Results Array at the same Time
    fig, axs = plt.subplots(2, 2)
    fig.canvas.set_window_title("Simulación de Ruleta: Análisis (de 0 a "+str(iterations)+" tiradas) - Stack 2")

    axs[0, 0].plot(rfr_array[0], 'tab:blue')
    axs[0, 0].plot(rfr_array[1], 'tab:orange')
    axs[0, 0].plot(rfr_array[2], 'tab:green')
    axs[0, 0].plot(rfr_array[3], 'tab:purple')
    axs[0, 0].plot(rfr_array[4], 'tab:pink')
    axs[0, 0].plot(rfr_array[5], 'tab:brown')
    axs[0, 0].set_title("Frecuencia Relativa")
    axs[0, 0].axhline(rfr_expected, color='red', linestyle='--', label="FRE")
    plt.setp(axs[0, 0], ylabel="FR del Número "+str(one_number))

    axs[0, 1].plot(avg_array[0], 'tab:blue')
    axs[0, 1].plot(avg_array[1], 'tab:orange')
    axs[0, 1].plot(avg_array[2], 'tab:green')
    axs[0, 1].plot(avg_array[3], 'tab:purple')
    axs[0, 1].plot(avg_array[4], 'tab:pink')
    axs[0, 1].plot(avg_array[5], 'tab:brown')
    axs[0, 1].set_title('Valor Promedio')
    axs[0, 1].axhline(avg_expected, color='red', linestyle='--', label="VPE")

    axs[1, 0].plot(var_array[0], 'tab:blue')
    axs[1, 0].plot(var_array[1], 'tab:orange')
    axs[1, 0].plot(var_array[2], 'tab:green')
    axs[1, 0].plot(var_array[3], 'tab:purple')
    axs[1, 0].plot(var_array[4], 'tab:pink')
    axs[1, 0].plot(var_array[5], 'tab:brown')
    axs[1, 0].set_title('Varianza')
    axs[1, 0].axhline(var_expected, color='red', linestyle='--', label="VVE")

    axs[1, 1].plot(dev_array[0], 'tab:blue')
    axs[1, 1].plot(dev_array[1], 'tab:orange')
    axs[1, 1].plot(dev_array[2], 'tab:green')
    axs[1, 1].plot(dev_array[3], 'tab:purple')
    axs[1, 1].plot(dev_array[4], 'tab:pink')
    axs[1, 1].plot(dev_array[5], 'tab:brown')
    axs[1, 1].set_title('Desvío')
    axs[1, 1].axhline(dev_expected, color='red', linestyle='--', label="VDE")
    
    for ax in fig.get_axes():
        ax.grid(True)
        ax.legend()
        plt.setp(ax, xlabel="Número de Tiradas")
    
    fig.tight_layout()
    plt.savefig("TP1 - Roulette Analysis/graphs/multi_graph_iterations_"+str(iterations)+".png")
    print("2do 4-Stack de Gráficos Guardado Correctamente")
    print()

    # Plotting all the Graphs
    plt.show()
