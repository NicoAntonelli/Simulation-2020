# -*- coding: utf-8 -*-

"""
UTN FRRO - Simulation 2020
TP3.0 - Single-server Queuing System

Authors:
    - Joshua Acciarri (44823)
    - Nicolás Antonelli (44852)
    - Alejandro Recalde (44704)

Professor: Torres, Juan
Final Date: 08/07/2020

Python Libraries/Modules Used:
    - Numpy:    Random Numbers and Array Manipulation
    - Pyplot:   Matplotlib Module for Graph Plotting
    - Seaborn:  Statistical and Scientific Graphs
    - Pandas:   Series and DataFrame tables

Other Files:
    - single_run:  Execution for every model configuration
    - processes:   Queuing model processes and random generator
    - utils:       Useful functions modularized in this file
    - plots:       Plotting functions with optional automatic save
"""

from single_run import run_queue_simulation, values_comparison
from plots import plot_results
from utils import get_expected_values


# General Parameters
n_runs = 10          # Iterations
n_delays = 10000     # Max Customers Quantity
selected_config = 2  # Configuration option selected from configs list
save = {
    "mode": False,   # mode: True = Autosave Graphs
    "route": "graphs/",
    "runs": n_runs,
    "delays": n_delays,
    "config": selected_config,
}

# Different Configurations for the Model
results = []
configs = [
    {
        "arrival_rate": 0.5,
        "service_rate": 2,
        "num_delays_required": n_delays,
        "queue_length": "inf",
    },  # Arrival Rate = 0.25 * Service Rate
    {
        "arrival_rate": 1,
        "service_rate": 2,
        "queue_length": "inf",
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.5 * Service Rate
    {
        "arrival_rate": 1.5,
        "service_rate": 2,
        "queue_length": "inf",
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.75 * Service Rate
    {
        "arrival_rate": 2,
        "service_rate": 2,
        "queue_length": "inf",
        "num_delays_required": n_delays,
    },  # Arrival Rate = 1 * Service Rate
    {
        "arrival_rate": 2.5,
        "service_rate": 2,
        "queue_length": "inf",
        "num_delays_required": n_delays,
    },  # Arrival Rate = 1.25 * Service Rate
    {
        "arrival_rate": 1.5,
        "service_rate": 2,
        "queue_length": 0,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.5 * Service Rate && Limited Queue maxsize = 2
    {
        "arrival_rate": 1.5,
        "service_rate": 2,
        "queue_length": 2,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.5 * Service Rate && Limited Queue maxsize = 2
    {
        "arrival_rate": 1.5,
        "service_rate": 2,
        "queue_length": 5,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.5 * Service Rate && Limited Queue maxsize = 5
    {
        "arrival_rate": 1.5,
        "service_rate": 2,
        "queue_length": 10,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.5 * Service Rate && Limited Queue maxsize = 10
    {
        "arrival_rate": 1.5,
        "service_rate": 2,
        "queue_length": 50,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.5 * Service Rate && Limited Queue maxsize = 50
]
current_config = configs[selected_config]


# Main
if __name__ == "__main__":
    print("\nQUEUING SYSTEM\n")
    print("Model (" + str(n_runs) + " runs):")

    # First Run: Also Prints Model Info
    result_time = run_queue_simulation(current_config, first=True)
    results.append(result_time)
    for i in range(n_runs):
        # Result of every run
        result_time = run_queue_simulation(current_config, first=False)
        results.append(result_time)
        print("Run " + str(i + 1) + " of " + str(n_runs) + " finished")
    print()

    # Expected analytic values
    expected = get_expected_values(current_config)

    # Show Analytic vs Simulated Results in Console
    values_comparison(results, expected)

    # Plot all the run's results (comparison with analytic values)
    plot_results(results, expected, save)
