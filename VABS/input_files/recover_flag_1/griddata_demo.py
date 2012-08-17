# from numpy.random import uniform, seed
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np

# set bounds of cross-section
sw_height = 0.508
sw_base   = 0.003 + 0.080 + 0.003
sc_height = 0.005
sc_base   = 1.5
(x2i,x3i) = (sc_base/2.0, sw_height/2.0-sc_height)  # inside bounds
(x2o,x3o) = (sc_base/2.0+sw_base, sw_height/2.0)    # outside bounds

#   *----*-------------------*----*(x2o,x3o)
#   |    |                   |    |
#   |    *-------------------*    |
#   |    |          (x2i,x3i)|    |
#   |    |                   |    |
#   |    |                   |    |
#   |    *-------------------*    |
#   |    |                   |    |
#   *----*-------------------*----*


# get data
print "getting data..."
# x2,x3,s11,s12,s13,s22,s23,s33 = np.loadtxt('spar_station_24.dat.S', unpack=True)
node_no,x2,x3,u1,u2,u3 = np.loadtxt('spar_station_24.dat.U', unpack=True)

# define grid.
print "defining grid..."
# tol = 0.000001# set tolerance
x2_interp = np.linspace(-x2o, x2o, 1000)
x3_interp = np.linspace(-x3o, x3o, 1000)

# grid the data.
print "interpolating the data onto the grid..."
# s11_interp = griddata(x2,x3,s11,x2_interp,x3_interp)
u1i = griddata(x2,x3,u1,x2_interp,x3_interp, interp='nn')


# mask the interior points (-x2i<x2<x2i, -x3i<x3<x3i)
# x2_interp_mask_start = np.nonzero(x2_interp<-x2i)[0][-1]
# x2_interp_mask_end = np.nonzero(x2_interp>x2i)[0][0]
# x3_interp_mask_start = np.nonzero(x3_interp<-x3i)[0][-1]
# x3_interp_mask_end = np.nonzero(x3_interp>x3i)[0][0]
# u1i[x2_interp_mask_start:x2_interp_mask_end,x3_interp_mask_start:x3_interp_mask_end] = np.nan

# contour the gridded data, plotting dots at the nonuniform data points.
print "contour the gridded data..."
CS = plt.contour(x2_interp,x3_interp,u1i,15,linewidths=0.5,colors='k')
CS = plt.contourf(x2_interp,x3_interp,u1i,15,cmap=plt.cm.jet)
plt.colorbar() # draw colorbar

# plot data points.
print "plot data points..."
plt.scatter(x2,x3,marker='o',c='b',s=5,zorder=10)
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.title('spar station #24')
plt.show()