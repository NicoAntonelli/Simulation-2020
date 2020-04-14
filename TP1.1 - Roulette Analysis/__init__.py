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


# Global Variables
calculate_time = True   # Time Measurement (True = Yes, False = No)
save = True             # Save Graphics (True = Yes, False = No)
save_route = "graphs/"  # Graphs Folder


# Mean (Average)
def calc_mean(population):
    return np.mean(population)

# Variance
def calc_variance(population):
    return np.var(population)

# Deviation
def calc_deviation(population):
    return np.std(population)

# Deviation from Variance
def calc_deviation_from_variance(variance):
    # Standard Deviation is the square root of the Variance
    return (variance ** 0.5)

# Load (for Plotting) One Array of Results
# Graphs Loaded: Relative Frecuency, Mean, Variance, Deviation (4-Graph Stack)
def load_one_result_graphs(frecuencies, averages, variances, deviations, save, final=False):
    # Subplots Config
    fig, axs = plt.subplots(2, 2)

    # Title and Names Config
    if final:
        filename="final_"
        message="3er 4-Stack de Gráficos"
        fig.canvas.set_window_title("Análisis 3er Stack: Promedio de Arrays de Resultados (de 0 a "+str(iterations)+" tiradas)")
    else:
        filename="simple_"
        message="1er 4-Stack de Gráficos"
        fig.canvas.set_window_title("Análisis 1er Stack: 1 Array de Resultados (de 0 a "+str(iterations)+" tiradas)")

    # Set Window Position
    manager = plt.get_current_fig_manager() # Current Window's Manager
    screen_x, screen_y = manager.window.wm_maxsize() # Screen Size
    if final:
        coord_x = str(int(screen_x/4))
        coord_y = str(int(screen_y/2))
    else:
        coord_x = ("0")
        coord_y = ("0")
    manager.window.wm_geometry("+" + coord_x + "+" + coord_y) # Set Values

    # Relative Frecuencies Graph
    axs[0, 0].plot(frecuencies, 'tab:blue', label="FRN")
    axs[0, 0].set_title("Frecuencia Relativa")
    axs[0, 0].axhline(rfr_expected, color='red', linestyle='--', label="FRE")
    plt.setp(axs[0, 0], ylabel="FR del Número "+str(one_number))

    # Averages Graph
    axs[0, 1].plot(averages, 'tab:orange', label="VPN")
    axs[0, 1].set_title('Valor Promedio')
    axs[0, 1].axhline(avg_expected, color='red', linestyle='--', label="VPE")

    # Variances Graph
    axs[1, 0].plot(variances, 'tab:green', label="VVN")
    axs[1, 0].set_title('Varianza')
    axs[1, 0].axhline(var_expected, color='red', linestyle='--', label="VVE")

    # Deviations Graph
    axs[1, 1].plot(deviations, 'tab:purple', label="VDN")
    axs[1, 1].set_title('Desvío')
    axs[1, 1].axhline(dev_expected, color='red', linestyle='--', label="VDE")
    
    # Details Config
    for ax in fig.get_axes():
        ax.grid(True)
        ax.legend()
        plt.setp(ax, xlabel="Número de Tiradas")
    fig.tight_layout()
    
    # Save Plot (PNG Image)
    if save:
        try:
            plt.savefig(save_route + filename + "graph_iterations_" + str(iterations) + ".png")
            print(message + " Guardado Correctamente")
        except:
            print(message + " NO fue guardado porque hubo un problema")
        print()

# Load (for Plotting) Every Array of Results Simultaneously
# Graphs Loaded: Relative Frecuency, Mean, Variance, Deviation (4-Graph Stack)
def load_every_result_graphs(frecuencies, averages, variances, deviations, save):
    # Subplots Config
    fig, axs = plt.subplots(2, 2)

    # Title Config
    fig.canvas.set_window_title("Análisis 2do Stack: Todos los Arrays de Resultados (de 0 a "+str(iterations)+" tiradas)")

    # Set Window Position
    manager = plt.get_current_fig_manager() # Current Window's Manager
    screen_x, screen_y = manager.window.wm_maxsize() # Screen Size
    coord_x = str(int(screen_x/2))
    coord_y = "0"
    manager.window.wm_geometry("+" + coord_x + "+" + coord_y) # Set Values

    # Relative Frecuencies Graph
    axs[0, 0].plot(frecuencies[0], 'tab:blue')
    axs[0, 0].plot(frecuencies[1], 'tab:orange')
    axs[0, 0].plot(frecuencies[2], 'tab:green')
    axs[0, 0].plot(frecuencies[3], 'tab:purple')
    axs[0, 0].plot(frecuencies[4], 'tab:pink')
    axs[0, 0].plot(frecuencies[5], 'tab:brown')
    axs[0, 0].set_title("Frecuencia Relativa")
    axs[0, 0].axhline(rfr_expected, color='red', linestyle='--', label="FRE")
    plt.setp(axs[0, 0], ylabel="FR del Número "+str(one_number))

    # Averages Graph
    axs[0, 1].plot(averages[0], 'tab:blue')
    axs[0, 1].plot(averages[1], 'tab:orange')
    axs[0, 1].plot(averages[2], 'tab:green')
    axs[0, 1].plot(averages[3], 'tab:purple')
    axs[0, 1].plot(averages[4], 'tab:pink')
    axs[0, 1].plot(averages[5], 'tab:brown')
    axs[0, 1].set_title('Valor Promedio')
    axs[0, 1].axhline(avg_expected, color='red', linestyle='--', label="VPE")

    # Variances Graph
    axs[1, 0].plot(variances[0], 'tab:blue')
    axs[1, 0].plot(variances[1], 'tab:orange')
    axs[1, 0].plot(variances[2], 'tab:green')
    axs[1, 0].plot(variances[3], 'tab:purple')
    axs[1, 0].plot(variances[4], 'tab:pink')
    axs[1, 0].plot(variances[5], 'tab:brown')
    axs[1, 0].set_title('Varianza')
    axs[1, 0].axhline(var_expected, color='red', linestyle='--', label="VVE")

    # Deviations Graph
    axs[1, 1].plot(deviations[0], 'tab:blue')
    axs[1, 1].plot(deviations[1], 'tab:orange')
    axs[1, 1].plot(deviations[2], 'tab:green')
    axs[1, 1].plot(deviations[3], 'tab:purple')
    axs[1, 1].plot(deviations[4], 'tab:pink')
    axs[1, 1].plot(deviations[5], 'tab:brown')
    axs[1, 1].set_title('Desvío')
    axs[1, 1].axhline(dev_expected, color='red', linestyle='--', label="VDE")
    
    # Details Config
    for ax in fig.get_axes():
        ax.grid(True)
        ax.legend()
        plt.setp(ax, xlabel="Número de Tiradas")
    fig.tight_layout()

    # Save Plot (PNG Image)
    if save:
        try:
            plt.savefig(save_route + "multi_graph_iterations_" + str(iterations) + ".png")
            print("2do 4-Stack de Gráficos Guardado Correctamente")
        except:
            print("2do 4-Stack de Gráficos NO fue guardado porque hubo un problema")
        print()

# Time Measurement
def measure_time():
    return time.perf_counter()


# Main
if __name__ == "__main__":
    print("SIMULACIÓN DE RULETA")
    print()
    
    # All 'European' Roulette Numbers from 0 to 36 (Total: 37)
    numbers = np.arange(0, 37)
    
    # Expected Values
    rfr_expected = round(1/len(numbers), 6)             # Relative Frecuency Expected (1/37)
    avg_expected = round(calc_mean(numbers), 6)         # Average (Mean) Expected (666/37)
    var_expected = round(calc_variance(numbers), 6)     # Variance Expected (114)
    dev_expected = round(calc_deviation(numbers), 6)    # Deviation Expected (Square Root of 114)
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
    start_time = measure_time()

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
            rfr_array[i][n] = one_number_occurrences / n                            # Relative Frecuency of "One_Number"
            avg_array[i][n] = round(calc_mean(roulette_values), 6)                  # Average (Mean)
            var_array[i][n] = variance = round(calc_variance(roulette_values), 6)   # Variance
            dev_array[i][n] = round(calc_deviation_from_variance(variance), 6)      # Standard Deviation (Square Root of Variance)
            
        # Feedback: Calculate and Show intermediate processing Time
        if calculate_time:
            last_load_time = measure_time() - start_time - acum_load_time
            acum_load_time = measure_time() - start_time
            print("Array Resultado " + str(i+1) + " de "+str(results) + " completado en " + str(round(last_load_time, 6)) + " segundos")
        else:
            print("Array Resultado " + str(i+1) + " de "+str(results) + " completado")

    # Total Calculation Time
    if calculate_time:
        final_time = round(measure_time() - start_time, 6)
        print("Todos los Arrays de Resultados fueron completados en " + str(final_time) + " segundos")
    else:
        print("Todos los Arrays de Resultados fueron completados")
    print()
    
    # PLOTTING

    # First Array of Results' Graphs
    load_one_result_graphs(rfr_array[0], avg_array[0], var_array[0], dev_array[0], save)
    
    # Now, Comparing all the Results Array at the same Time
    load_every_result_graphs(rfr_array, avg_array, var_array, dev_array, save)

    # New Result Array with the Average of all Results Arrays
    final_rfr_array = (rfr_array[0] + rfr_array[1] + rfr_array[2] + rfr_array[3] + rfr_array[4] + rfr_array[5]) / results
    final_avg_array = (avg_array[0] + avg_array[1] + avg_array[2] + avg_array[3] + avg_array[4] + avg_array[5]) / results
    final_var_array = (var_array[0] + var_array[1] + var_array[2] + var_array[3] + var_array[4] + var_array[5]) / results
    final_dev_array = (dev_array[0] + dev_array[1] + dev_array[2] + dev_array[3] + dev_array[4] + dev_array[5]) / results

    load_one_result_graphs(final_rfr_array, final_avg_array, final_var_array, final_dev_array, save, final=True)

    # Plotting all the Graphs
    plt.show()
