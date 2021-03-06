'''

machNum_plot.py by Kenneth Tochihara
Visualizing the interpolation of Mach numbers.

'''

#Import some stuff
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

#Constants and arrays
machNums = np.arange(0.0, 1.601, 0.001)
machNumsBroad = np.arange(0.0, 1.7, 0.1)
pRatio = []
pRatioBroad = []
gam = 1.4


#Calculates the pressure ratios for machNums
for m1 in machNums:
    if m1 < 1:
        #Find p01/p1
        pRatio.append(((1 + ((gam - 1)/2)*(m1 ** 2))**(gam/(gam - 1))))
    else:
        #Find p02/p1
        pRatio.append((((gam + 1)**2 * m1**2)/((4 * gam * m1**2) - 2 * (gam - 1)))**(gam /(gam - 1)) * ((1 - gam + (2 * gam * (m1**2)))/(gam + 1)))

#Calculates the pressure ratios for machNumsBroad
for m1 in machNumsBroad:
    if m1 < 1:
        #Find p01/p1
        pRatioBroad.append(((1 + ((gam - 1)/2)*(m1 ** 2))**(gam/(gam - 1))))
    else:
        #Find p02/p1
        pRatioBroad.append((((gam + 1)**2 * m1**2)/((4 * gam * m1**2) - 2 * (gam - 1)))**(gam /(gam - 1)) * ((1 - gam + (2 * gam * (m1**2)))/(gam + 1)))

#Interpolation
f = interpolate.interp1d(pRatio, machNums)

#Plotting
plt.axhline(y=1, linewidth=1, color='#A9A9A9', label='Mach 1.0')
plt.plot(pRatio, f(pRatio), 'm-', label='Interpolated Line')
plt.plot(pRatioBroad, machNumsBroad, 'bo', label='Data Points')
plt.xlabel('Pressure Ratio')
plt.ylabel('Mach Number')
plt.title('Interpolating the Mach Number')
plt.legend(loc='lower right')
plt.show()
