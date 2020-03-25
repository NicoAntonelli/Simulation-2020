#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UTN FRRO - Simulation 2020
TP1 - Roulette Analysis

-Analyze the Obtained Numebers' Frecuency on a Roulette and Plot it on a Graph
-Show the obtained Average Number

Author: Antonelli, Nicolás (44852)
Final Date: 25/03/2020
"""

import random
import matplotlib.pyplot as plt
import statistics as stat

print("Roulette Simulation (Numeral Analysis)")

# Total Iterations
iterations = abs(int(input("Iterations: ")))

# All 'American' Roulette Numbers from 0 to 36, initialized in 0
numbers = [0] * 37

# Playing Roulette and Analyzing the Obtained Numbers' Frecuency
for i in range (0, iterations):
    n = random.randint(0, 36)
    numbers[n] += 1

# Show the Average Number
avg = round(stat.mean(numbers), 3)
print("The Average Quantity (Mean) of each obtained Number is: "+str(avg))

# Show the Absolut Frecuency of the Obtained Numbers
# plt.plot(numbers)
plt.stem(numbers)
title = "FRECUENCY ANALYSIS ("+str(iterations)+" ITERATIONS)"
plt.title(title)
plt.grid(True)
plt.axis([-1, len(numbers), 0, max(numbers)*1.1])
plt.ylabel("Absolut Frecuency")
plt.xlabel("Roulette Number")
plt.show()
