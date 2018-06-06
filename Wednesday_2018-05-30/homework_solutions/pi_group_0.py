# script to estimate pi with a Monte Carlo simulation

# The script is an exact translations of the steps outlined
# on the exercise sheet - no further comments

import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
import matplotlib  # to be able to modify fonts etc.

# font size of labels etc,
matplotlib.rcParams['font.size'] = 18
# line width of coordinate axes
matplotlib.rcParams['axes.linewidth'] = 2.0

x = nr.random_sample(5000)
y = nr.random_sample(5000)

mask_in = (x**2 + y**2) <= 1.0
mask_out = (x**2 + y**2) > 1.0

plt.scatter(x[mask_in], y[mask_in], color='red')
plt.scatter(x[mask_out], y[mask_out], color='blue')

# plot the quarter circle. A circle with radius 1
# follows the implicit equation x**2 + y**2 = 1:
x_func = np.linspace(0.0, 1.0, 100)
y_func = np.sqrt(1 - x_func**2)

plt.plot(x_func, y_func, color='black', linewidth=5)

plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)

plt.xlabel('x')
plt.ylabel('y')

# without the following command the resulting plot is stretched
# and the aspect ratio of both axes is not equal. The circle segment
# would appear as ellipse-segment etc.
plt.axes().set_aspect('equal')
plt.title('$\pi$ with Monte-Carlo')

plt.savefig('pi.png', dpi=200)
#plt.show()

# now estimate pi:
pi_estimate = 4.0 * (len(x[mask_in]) / len(x))

print("We estimate pi to: %f" % (pi_estimate))
