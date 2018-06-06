#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 18}

matplotlib.rc('font', **font)

x1 = np.linspace(0.0, np.pi, 30)
x2 = np.linspace(0.0, np.pi, 13)

width = x2[1] - x2[0]

plt.plot(x1, np.sin(x1), 'r', lw=3, label=r'$y=\sin(x)$')
plt.bar(x2, np.sin(x2), width=width, align='center')
plt.xlabel("x", fontsize=18)
plt.ylabel("y", fontsize=18)
plt.legend()
plt.savefig('sin.png', bbox_inches='tight')


x1 = np.linspace(-1.0, 2.0, 30)
x2 = np.linspace(-1.0, 2.0, 13)

width = x2[1] - x2[0]

plt.clf()
plt.plot(x1, x1**3, 'r', lw=3, label=r'$y=x^3$')
plt.bar(x2, x2**3, width=width, align='center')
plt.xlabel("x", fontsize=18)
plt.ylabel("y", fontsize=18)
plt.legend(loc='upper left')
plt.xlim((-1.2, 2.2))
plt.savefig('cubic.png', bbox_inches='tight')


