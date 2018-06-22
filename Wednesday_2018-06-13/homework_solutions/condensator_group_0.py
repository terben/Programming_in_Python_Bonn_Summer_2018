import numpy as np
import matplotlib.pyplot as plt

# we choose 101 gridpoints in x and y. Note that we use the
# same grid-coordinates in x and in y!
gridpoints = 101
coordinates = np.linspace(0.0, 1.0, gridpoints)
dh = coordinates[1] - coordinates[0] # needed to calculate Ex and Ey below

# define the initial potential.
phi = np.zeros(gridpoints * gridpoints, dtype=np.float64)
phi = phi.reshape((gridpoints, gridpoints))

# the condensator-plate positions
left_pos = 0.35
right_pos = 0.65
upper_pos = 0.65
lower_pos = 0.35

left_idx = int(left_pos * (gridpoints - 1))
right_idx = int(right_pos * (gridpoints - 1))

upper_idx = int(upper_pos * (gridpoints - 1))
lower_idx = int(lower_pos * (gridpoints - 1))

phi[lower_idx:upper_idx + 1, left_idx] = -1
phi[lower_idx:upper_idx + 1, right_idx] = 1

eps = 1.0e-04
solved = False
while solved == False:
    phi_old = phi.copy() # to compare with the new estimate
    phi_prime = 1. / 4. * (phi[2:, 1:-1] + phi[:-2, 1:-1] +
                           phi[1:-1, 2:] + phi[1:-1, :-2])

    # Note that phi_prime has dimension phi[1:-1,1:-1]!
    phi[1:-1, 1:-1] = phi_prime

    # ensure the 'border conditions' (constant potenitial) on
    # the condensator plates
    phi[lower_idx:upper_idx + 1, left_idx] = -1
    phi[lower_idx:upper_idx + 1, right_idx] = 1

    if np.max(np.abs(phi - phi_old)) < eps:
        solved = True

# obtain the electric field and plot it:
Ey, Ex = np.gradient(-phi, dh, dh)
X, Y = np.meshgrid( coordinates , coordinates)

# uncomment the following two lines and comment the 'streamplot'
# if you want to directly plot the vector field.

#slice_xy = slice(None, None, 5), slice(None, None, 5)
#plt.quiver(X[slice_xy], Y[slice_xy], Ex[slice_xy], Ey[slice_xy], angles='uv',
#           color='r', units='x', linewidths=(2,), edgecolors=('k'),
#           headaxislength=5)

plt.streamplot(X, Y, Ex, Ey)

plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.plot([left_pos, left_pos], [lower_pos, upper_pos], color='blue',
         linewidth=10)
plt.plot([right_pos, right_pos], [lower_pos, upper_pos], color='red',
         linewidth=10)
plt.axes().set_aspect('equal')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.show()
