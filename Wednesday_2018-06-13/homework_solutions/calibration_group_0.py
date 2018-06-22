#!/usr/bin/env python3

# script to perform stellar locus repression

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['axes.linewidth'] = 2.0
matplotlib.rcParams['font.size'] = 14

# read star data for the B, R and I bands. We assume that the
# R-band magnitudes are well calibrated and we need to refine
# calibration for B and I:
data = np.loadtxt('../data/stars_BRI_data.asc')
model = np.loadtxt('../data/stars_BRI_model.asc')

# split up arrays for convenience:
b_data, r_data, i_data = data[:,0], data[:,1],  data[:,2]
b_model, r_model, i_model = model[:,0], model[:,1], model[:,2]

rmi_data, bmr_data = r_data - i_data,  b_data - r_data
rmi_model, bmr_model = r_model - i_model, b_model - r_model

# first plot raw data without any correction:
plt.plot(rmi_data, bmr_data, 'bo', label='data')
plt.plot(rmi_model, bmr_model, 'ro', label='model')
plt.xlabel('R-I')
plt.ylabel('B-R')
plt.title('Raw data before correction')
plt.legend()
plt.savefig('uncorrected.png')

# get distances from all model to all data points:
rmi_distances = (rmi_data[:,np.newaxis] - rmi_model[np.newaxis,:]).flatten()
bmr_distances = (bmr_data[:,np.newaxis] - bmr_model[np.newaxis,:]).flatten()

shift = []
binwidth = 0.1
for dist in [ rmi_distances, bmr_distances ]:
    histo = np.histogram(dist, bins=np.arange(min(dist),
                                              max(dist) + binwidth, binwidth))
    maxbin = np.argmax(histo[0])
    shift.append((histo[1][maxbin] + histo[1][maxbin + 1]) / 2.)

# plot one of the histograms for demonstration purposes:
plt.clf()
plt.hist(bmr_distances, bins = np.arange(min(bmr_distances),
                                         max(bmr_distances) + binwidth,
                                         binwidth))
plt.xlabel('B-R')
plt.ylabel('2*N')
plt.title('histogram of B-R distances (data minus model)')
plt.savefig('bmr_histo.png')

# apply shift and plot again the corrected data:
rmi_data, bmr_data = rmi_data - shift[0],  bmr_data - shift[1]

plt.clf()
plt.plot(rmi_data, bmr_data, 'bo', label='data')
plt.plot(rmi_model, bmr_model, 'ro', label='model')
plt.xlabel('R-I')
plt.ylabel('B-R')
plt.title('corrected data')
plt.legend()
plt.savefig('corrected.png')
