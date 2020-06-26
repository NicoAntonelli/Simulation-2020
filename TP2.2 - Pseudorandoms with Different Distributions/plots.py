# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


# Save any Plot
def save_plot(route, name):
    try:
        plt.savefig(route + name + ".png")
        print(name + " has been saved successfully")
    except:
        print(name + " has NOT been saved because a problem ocurred")

# Plot for a comparative between Analytic and Simulated CDFs
def cdf_plots(x, y, sim_x, sim_y, distribution_name, save):
    fig = plt.figure()
    fig.canvas.set_window_title("Analytic vs Simulated CDFs - " + distribution_name.capitalize() + " Distribution")
    plt.title(distribution_name.capitalize() + " Distribution")
    plt.plot(x, y, 'b-', label="Analytic CDF")
    plt.plot(sim_x, sim_y, 'r.', label="Simulated CDF")
    plt.xlabel("X Values")
    plt.ylabel("Probability") 

    plt.tight_layout()
    plt.margins(0.02)
    plt.grid()
    plt.legend()

    if (save["mode"]):
        route = save["route"]
        name = "graph_" + str(save["total"]) + "numbers_" + distribution_name
        save_plot(route, name)

# Show all the figures at the same time
def graphing_show_all():
    plt.show()
