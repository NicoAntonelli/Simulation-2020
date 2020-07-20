# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


# Save any plot
def save_plot(route, name):
    try:
        plt.savefig(route + name + ".png")
        print(name + " has been saved successfully")
    except:
        print(name + " has NOT been saved because a problem ocurred")


# Plot for line graphs
def plot_one(measures_from_multiple_runs, expected_value, title, x_label, y_label, save, name):
    # General Config
    fig = plt.figure()
    fig.canvas.set_window_title(title)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Plot every run simultaneously
    for measures in measures_from_multiple_runs:
        x, y = zip(*measures.items())
        plt.plot(x, y)

    # Analytic expected value (if it is possible)
    if expected_value is not None:
        plt.axhline(expected_value, color="red", linestyle="--", label="Expected value")
        plt.legend()

    # Details Config
    plt.tight_layout()
    plt.margins(0.02)
    plt.grid()

    # Autosave
    if save["mode"]:
        route = save["route"]
        file_name = "graph_" + str(save["runs"]) + "runs_" + str(save["delays"]) + "delays_"
        file_name += "config" + str(save["config"]) + "_" + name
        save_plot(route, file_name)


# Plot for bar graphs
def plot_bar(results_measures, expected, title, x_label, y_label, save, name):
    # General Config
    fig = plt.figure()
    fig.canvas.set_window_title(title)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Filtering only 0 to 20 customers in queue probability (Analytic Values)
    expected_pn_shortened = expected["Pn"][:20]

    # Filtering only 0 to 20 customers in queue probability (Simulation Values)
    average_observed_pn = list(map(np.mean, zip(*results_measures)))[:20]

    # Bars Graphs for Comparison
    plt.bar(
        np.arange(len(expected_pn_shortened)),
        expected_pn_shortened,
        width=0.6,
        label="Expected values",
    )
    plt.bar(
        np.arange(len(average_observed_pn)), average_observed_pn, width=0.4, label="Observed values"
    )
    plt.xticks(np.arange(0, len(average_observed_pn) + 1, 1.0))

    # Details Config
    plt.tight_layout()
    plt.margins(0.02)
    plt.grid()
    plt.legend()

    # Autosave
    if save["mode"]:
        route = save["route"]
        file_name = "graph_" + str(save["runs"]) + "runs_" + str(save["delays"]) + "delays_"
        file_name += "config" + str(save["config"]) + "_" + name
        save_plot(route, file_name)


# Specification of all the graphs to plot
def plot_results(results, expected, save):
    # Average quantity of costumers in queue
    plot_one(
        [result["avg_num_in_queue"] for result in results],
        expected_value=expected["Lq"],
        title="Average quantity of costumers in queue",
        x_label="Time",
        y_label="q(n)",
        save=save,
        name="avg_num_in_queue",
    )

    # Average delay time in queue
    plot_one(
        [result["avg_delay_in_queue"] for result in results],
        expected_value=expected["Wq"],
        title="Average delay time in queue",
        x_label="Customer number",
        y_label="d(n)",
        save=save,
        name="avg_delay_time_in_queue",
    )

    # Average quantity of costumers in the system
    plot_one(
        [result["avg_num_in_system"] for result in results],
        expected_value=expected["L"],
        title="Average quantity of costumers in the system",
        x_label="Time",
        y_label="l(n)",
        save=save,
        name="avg_num_in_the_system",
    )

    # Average delay time in the system
    plot_one(
        [result["avg_delay_in_system"] for result in results],
        expected_value=expected["W"],
        title="Average delay time in the system",
        x_label="Customer number",
        y_label="w(n)",
        save=save,
        name="avg_delay_time_in_the_system",
    )

    # Server utilization
    plot_one(
        [result["server_utilization"] for result in results],
        expected_value=expected["Rho"],
        title="Server utilization",
        x_label="Time",
        y_label="u(n)",
        save=save,
        name="server_utilization",
    )

    # N customers in queue probability
    if expected["Lq"] is not None:
        plot_bar(
            [result["n_clients_in_system_probability_array"] for result in results],
            expected=expected,
            title="N customers in system probability",
            x_label="N customers",
            y_label="P(n)",
            save=save,
            name="n_curstomers_in_queue_probability",
        )

    # Show all the plots
    plt.show()
