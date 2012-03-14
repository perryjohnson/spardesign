# from numpy.random import uniform, seed
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np
# make up data.
#npts = int(raw_input('enter # of random points to plot:'))
# seed(0)
# npts = 200
# x = uniform(-2,2,npts)
# y = uniform(-2,2,npts)
# z = x*np.exp(-x**2-y**2)

# get data
data = np.loadtxt('spar_station_24.dat.U')
x = data[:,1]  # x2 coordinate
y = data[:,2]  # x3 coordinate
z = data[:,3]  # U1 deflection (in the beam coordinate system)

# define grid.
# xi = np.linspace(-1.1,1.1,1000)
# yi = np.linspace(-1.1,1.1,1000)
X,Y = np.meshgrid(x,y)

# grid the data.
# zi = griddata(x,y,z,xi,yi,interp='linear')
# zi[400:600,200:800] = np.nan
# # contour the gridded data, plotting dots at the nonuniform data points.
# CS = plt.contour(xi,yi,zi,15,linewidths=0.5,colors='k')
# CS = plt.contourf(xi,yi,zi,15,cmap=plt.cm.jet)
# plt.colorbar() # draw colorbar
# # plot data points.
# plt.scatter(x,y,marker='o',c='b',s=5,zorder=10)
# plt.xlim(-1,1)
# plt.ylim(-1,1)
# plt.title('spar station #24')
# plt.show()