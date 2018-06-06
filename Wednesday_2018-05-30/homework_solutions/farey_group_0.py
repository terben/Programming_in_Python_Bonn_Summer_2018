#!/usr/bin/env python3

# script to calculate and visualize the Farey-sequence

import sys
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('my_presentation')

# plot a Farey sequence:
def plot_farey(nom, denom):
    numbers = nom / denom
    mid_points = (numbers[1:] + numbers[:-1]) / 2.
    radii = (numbers[1:] - numbers[:-1]) / 2.

    for i in range(len(mid_points)):
        x = np.linspace(mid_points[i] - radii[i],
                        mid_points[i] + radii[i], 500)
        x = x[1:-1] # just exclude end-points so that numerical
                    # artefacts do not lead to negative values
                    # in the following sqrt-calculation
        y = np.sqrt(radii[i]**2 - (x - mid_points[i])**2)

        # make sure that all circles of the current sequence are
        # plotted with the same color:
        if i == 0:
            p = plt.plot(x, y)
            color = p[-1].get_color()
        else:
            plt.plot(x, y, color=color)

        ticks = [ str(p) + "/" + str(q) for (p, q) in zip(nom, denom) ]
        plt.xticks(numbers, ticks)

# we keep two numpy array for the nominators and denominators of the
# Farey sequance

# The first member of the Farey sequence F_1 is:
nom = np.array([0, 1])
denom = np.array([1, 1])
N = 5 # we want the sequence up to order N

plt.xlim(0.0, 1.0)
plt.ylim(0.0, 0.55)
plot_farey(nom, denom)
plt.title(r'$F_1$ up to $F_%d$' % (N))

# In the following we construct F_N out of F_N-1 with the method
# outlined on the Wiki page https://de.wikipedia.org/wiki/Farey-Folge
# (Konstruktion - Methode 2):
for order in range(2, N + 1):
    add = denom[1:] + denom[:-1]
    indices = np.where(add == order)[0] + 1

    nom = np.insert(nom, indices, nom[indices - 1] + nom[indices])
    denom = np.insert(denom, indices, order)
    plot_farey(nom, denom)

# save the figure
plt.savefig('farey.png')

# print the sequence:
for i in zip(nom, denom):
    print(i, end=" ")

print()
