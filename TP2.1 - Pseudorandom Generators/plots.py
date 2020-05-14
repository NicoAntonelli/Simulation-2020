# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Save any Plot
def save_plot(route, name):
    try:
        plt.savefig(route + name + ".png")
        print(name + " guardado correctamente")
    except:
        print(name + " NO fue guardado porque hubo un problema")


# Scatter Plots (Separated)
def graphing_scatterplots(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values, save):
    # Initialize Seaborn Settings (Default)
    sns.set()

    # Scatter Plots (Separated)
    fig, axs = plt.subplots(ncols=2, nrows=2)
    fig.canvas.set_window_title("Scatter Plots")

    sns.scatterplot(data=msm_values, ax=axs[0,0], color="red").set_title("Middle Square Method")
    sns.scatterplot(data=multiplicative_random_values, ax=axs[0,1], color="green").set_title("Multiplicative LCG")
    sns.scatterplot(data=mixed_random_values, ax=axs[1,0], color="blue").set_title("Mixed LCG")
    sns.scatterplot(data=pog_mt_values, ax=axs[1,1], color="orange").set_title("Mersenne Twister")

    for ax in fig.get_axes():
        plt.setp(ax, xlabel="Number", ylabel="Random Value")
    plt.tight_layout()

    if (save["mode"]):
        route = save["route"]
        name = "graph_" + str(save["total"]) + "numbers_" + "scatter_separated"
        save_plot(route, name)

    # Scatter Plots (Simultaneously)
    fig = plt.figure()
    fig.canvas.set_window_title("Simultaneous Scatter Plots") # Without middle squared method
    
    sns.scatterplot(data=multiplicative_random_values, color="green", label="Multiplicative LCG")
    sns.scatterplot(data=mixed_random_values, color="blue", label="Mixed LCG")
    sns.scatterplot(data=pog_mt_values, color="orange", label="Mersenne Twister")
    
    plt.title("Scatter Plots")
    plt.setp(fig.get_axes(), xlabel="Number", ylabel="Random Value")
    plt.legend()
    plt.tight_layout()

    if (save["mode"]):
        route = save["route"]
        name = "graph_" + str(save["total"]) + "numbers_" + "scatter_simultaneous"
        save_plot(route, name)


def graphing_histograms(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values, save):
    # Initialize Seaborn Settings (Default)
    sns.set()

    # Histograms (Separated)
    fig, axs = plt.subplots(ncols=2, nrows=2)
    fig.canvas.set_window_title("Histograms")

    sns.distplot(msm_values, ax=axs[0,0], color="red").set_title("Middle Square Method")
    sns.distplot(multiplicative_random_values, ax=axs[0,1], color="green").set_title("Multiplicative LCG")
    sns.distplot(mixed_random_values, ax=axs[1,0], color="blue").set_title("Mixed LCG")
    sns.distplot(pog_mt_values, ax=axs[1,1], color="orange").set_title("Mersenne Twister")

    for ax in fig.get_axes():
        plt.setp(ax, xlabel="Number", ylabel="Random Value")
    plt.tight_layout()

    if (save["mode"]):
        route = save["route"]
        name = "graph_" + str(save["total"]) + "numbers_" + "histograms_separated"
        save_plot(route, name)

    # Histograms (Simultaneously)
    fig = plt.figure()
    fig.canvas.set_window_title("Simultaneous Histograms") # Without middle squared method

    sns.distplot(multiplicative_random_values, color="green", label="Multiplicative LCG")
    sns.distplot(mixed_random_values, color="blue", label="Mixed LCG")
    sns.distplot(pog_mt_values, color="orange", label="Mersenne Twister")

    plt.title("Histograms")
    plt.setp(fig.get_axes(), xlabel="Number", ylabel="Random Value")
    plt.legend()
    plt.tight_layout()
    
    if (save["mode"]):
        route = save["route"]
        name = "graph_" + str(save["total"]) + "numbers_" + "histograms_simultaneous"
        save_plot(route, name)


def tests_final_table(msm_results, mult_lcg_results, mix_lcg_results, pog_mt_results, save):
    # DataFrame
    tests_names = ["Pearson χ2", "Parity", "KS", "Gaps"]
    table = {
            "Middle Squared Method":    pd.Series(msm_results, index=tests_names),
            "Multiplicative LCG":       pd.Series(mult_lcg_results, index=tests_names),
            "Mixed LCG":                pd.Series(mix_lcg_results, index=tests_names),
            "Mersenne Twister":         pd.Series(pog_mt_results, index=tests_names),
    }
    table = pd.DataFrame(table)
    table.style.set_properties(**{'text-align': 'center'})
    
    # Console print
    print(table)
    print()

    # Plotting DataFrame
    size = (8, 1.5)
    fig, ax = plt.subplots(figsize = size)
    fig.patch.set_visible(False)
    fig.canvas.set_window_title("Tests Results' Summaring")
    ax.axis('off')

    colors = table.applymap(lambda x: '#98FB98' if x=='Approved' else '#FF775F') # Green and Red table
    table_fig = ax.table(cellText=table.values, colLabels=table.columns, rowLabels=table.index, loc='center', cellLoc='center',
        colColours=['black']*len(colors.columns), rowColours=['black']*len(colors), cellColours=colors.to_numpy())

    for row in range(1, len(colors.columns)+1):
        table_fig._cells[row, -1]._text.set_color('white')
    for col in range(0, len(colors)):
        table_fig._cells[0, col]._text.set_color('white')

    plt.tight_layout()

    if (save["mode"]):
        route = save["route"]
        name = "graph_" + str(save["total"]) + "numbers_" + "tests_results_summaring"
        save_plot(route, name)


def graphing_show_all():
    plt.show()
