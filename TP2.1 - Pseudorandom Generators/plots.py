# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns

# Scatter Plots (Separated)
def graphing_scatterplots(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values):
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

    # Scatter Plots (Simultaneously)
    fig = plt.figure()
    fig.canvas.set_window_title("Simultaneous Scatter Plots")
    
    sns.scatterplot(data=multiplicative_random_values, color="green", label="Multiplicative LCG")
    sns.scatterplot(data=mixed_random_values, color="blue", label="Mixed LCG")
    sns.scatterplot(data=pog_mt_values, color="orange", label="Mersenne Twister")
    
    plt.title("Scatter Plots")
    plt.setp(fig.get_axes(), xlabel="Number", ylabel="Random Value")
    plt.legend()
    plt.tight_layout()


def graphing_histograms(msm_values, multiplicative_random_values, mixed_random_values, pog_mt_values):
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

    # Histograms (Simultaneously)
    fig = plt.figure()
    fig.canvas.set_window_title("Simultaneous Histograms")

    sns.distplot(msm_values, color="red", label="Middle Square Method")
    sns.distplot(multiplicative_random_values, color="green", label="Multiplicative LCG")
    sns.distplot(mixed_random_values, color="blue", label="Mixed LCG")
    sns.distplot(pog_mt_values, color="orange", label="Mersenne Twister")

    plt.title("Histograms")
    plt.setp(fig.get_axes(), xlabel="Number", ylabel="Random Value")
    plt.legend()
    plt.tight_layout()


def graphing_show_all():
    plt.show()
