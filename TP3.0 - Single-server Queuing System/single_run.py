# -*- coding: utf-8 -*-

from processes import (
    event_report,
    initialize,
    timing,
    update_time_stats,
    arrive,
    depart,
    final_report,
)
from operator import itemgetter
import numpy as np


def run_queue_simulation(config, first):
    # Initialize Run
    model, results_time = itemgetter("model", "results_time")(initialize(config))
    if first:
        # Run Information
        print("Single-server queuing system (M/M/1)")
        print("Mean interarrival time:", round(model["mean_interarrival"], 6), "minutes")
        print("Mean service time:", round(model["mean_service"], 6), "minutes")
        print("Number of customers:", round(model["num_delays_required"], 6), "\n")

    # Run the simulation while more delays are still needed
    while model["num_customers_delayed"] < model["num_delays_required"]:
        # Determine the next event
        next_event_type, model["time"] = timing(model["event_list"])
        # Update time-average statistical accumulators
        update_time_stats(model)
        # Invoke the appropriate event function
        if next_event_type == "arrival":
            arrive(model)
        elif next_event_type == "departure":
            depart(model)
        # Invoke the partial report generator
        event_report(results_time, model)
    # Invoke the final report generator and end the current run
    return final_report(results_time, model)


# Comparison between analytic and simulation results' values
def values_comparison(results, expected):
    print("\nRESULTS")
    print("\nModel Parameters")
    print("λ  (Arrival rate):", expected["Lambda"])
    print("μ  (Service rate):", expected["Mu"])

    if expected["Lq"] is not None:
        # Analytic Performance Measures Print
        print("\nAnalytic Performance Measures")
        print("ρ  (Server utilization):", np.round(expected["Rho"], 6))
        print("Lq (Average quantity of costumers in queue):", np.round(expected["Lq"], 6))
        print("Wq (Average delay time in queue):", np.round(expected["Wq"], 6))
        print("L  (Average quantity of costumers in the system):", np.round(expected["L"], 6))
        print("W  (Average delay time in the system):", np.round(expected["W"], 6))
        print("Pn (N customers in system probability), (0 ≤ N < 20):")
        print(np.round(np.array(expected["Pn"][:20]), 6))
        print("Pd (Denial of service probability):", np.round(expected["Pd"], 6))

        print("\nSimulation Performance Measures (Runs' Average)")
        # Average Simulation Performance Measures Calculation
        Rho = np.mean([list(result["server_utilization"].values())[-1] for result in results])
        Lq = np.mean([list(result["avg_num_in_queue"].values())[-1] for result in results])
        Wq = np.mean([list(result["avg_delay_in_queue"].values())[-1] for result in results])
        L = np.mean([list(result["avg_num_in_system"].values())[-1] for result in results])
        W = np.mean([list(result["avg_delay_in_system"].values())[-1] for result in results])
        Pn = np.mean(
            [result["n_clients_in_system_probability_array"][:20] for result in results], axis=0
        )
        Pd = np.mean([result["client_not_getting_service_probability"] for result in results])
        # Average Simulation Performance Measures Print
        print("ρ  (Server utilization):", np.round(Rho, 6))
        print("Lq (Average quantity of costumers in queue):", np.round(Lq, 6))
        print("Wq (Average delay time in queue):", np.round(Wq, 6))
        print("L  (Average quantity of costumers in the system):", np.round(L, 6))
        print("W  (Average delay time in the system):", np.round(W, 6))
        print("Pn (N customers in system probability), (0 ≤ N < 20):")
        print(np.round(np.array(Pn), 6))
        print("Pd (Denial of service probability):", np.round(Pd, 6))

        # Expected VS Simulated Comparison (Main Parameters Only)
        print("\nRelation Between Analytics and Simulated Main Values")
        print("ρ  = ", np.round(expected["Rho"] / Rho, 6))
        if Lq != 0:
            print("Lq = ", np.round(expected["Lq"] / Lq, 6))
            print("Wq = ", np.round(expected["Wq"] / Wq, 6))
        print("L  = ", np.round(expected["L"] / L, 6))
        print("W  = ", np.round(expected["W"] / W, 6))
        print()

    else:
        # λ ≥ μ
        print("\nPerformance Measures")
        print("λ ≥ μ, the queue grows infinitely")
        print("ρ  (Server utilization):", expected["Rho"])
        print("It is not feasible to calculate other performance parameters...")
        print()
