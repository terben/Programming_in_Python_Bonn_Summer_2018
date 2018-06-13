#!/usr/bin/env python3

# script for the numpy random walk problem:
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

n_stories = 1000     # number of walkers
n_time_steps = 200  # number of time steps

# get a two-dimensional array of random numbers -1 and 1. We create an
# array with the random numbers 0 and 1, multiply by 2 (which give
# random numbers 0 and 2) and subtract 1 to finally get an array of
# random numbers -1 and 1. Note that the following commad immediately
# gives us an array with the correct shape:
#steps = 2 * nr.random_integers(0, 1,
#                               (n_stories, n_time_steps)) - 1

# As an alternative we could substitute the 0's in the original
# random array with -1's to obtain a array with random 1's and
# -1's:
steps = nr.random_integers(0, 1, (n_stories, n_time_steps))
steps[steps == 0] = -1

# the travelled distance for each walker is the cumulated
# sum of his steps over time:
distance = np.cumsum(steps, axis=1) # axis = 1: dimension of time
sq_distance = distance * distance

# The follwing mean is built over the different walkers:
mean_distance = np.mean(distance, axis=0)
mean_sq_distance = np.mean(sq_distance, axis=0)

# and plot the results:
time = np.arange(n_time_steps)
plt.plot(time, mean_distance, 'r.',
         time, np.zeros(len(time)), 'b-')
plt.plot(time, np.sqrt(mean_sq_distance), 'g.',
         time, np.sqrt(time), 'b-')
plt.xlabel(r"$t$") 
plt.ylabel(r"$\langle \Delta x\rangle$; $\sqrt{\langle (\Delta x)^2 \rangle}$")

plt.show()
