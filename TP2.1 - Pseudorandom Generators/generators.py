import numpy as np
import random as rand

# Linear Congruential Generator (LGC)
def linear_congruential_generator(M, A, C, X0, total):
    x_values = [X0]
    for _ in range (total-1):
        x_values.append((x_values[-1] * A + C) % M)
    x_values = np.array(x_values)
    return lgc_bounded(x_values, M)

# LGC values into an uniform U(0, 1) distribution
def lgc_bounded(array, M):
    return np.array([x for x in array / M])


# Middle Square Method
def middle_square_method(seed, total):
    newSeed = seed
    x_values = []
    for _ in range(total):
        newSeed = newSeed**2
        value_str = list(map(int, str(newSeed)))
        for i in range(8-len(value_str)):
            value_str.insert(0, 0)
        
        newSeed = ''
        for i in range(2, 6):
            value_str[i] = str(value_str[i])
            newSeed += value_str[i]
        newSeed = int(newSeed)
        x_values.append(newSeed)
    for i in range(total):
        x_values[i] = x_values[i] / 10000
    return x_values


# Python's Own Generator
def python_generator(n):
    # rand.seed() ?
    x_values = []
    for _ in range(n):
        nextRand = rand.random()
        x_values.append(nextRand)
    return x_values