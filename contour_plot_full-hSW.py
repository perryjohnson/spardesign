import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import find, griddata
from matplotlib import rc, cm

# use LaTeX fonts and formatting
rc('text', usetex=True)
rc('font', family='serif')
rc('font', size=15.0)

# load up the results from a textfile into memory
data = np.loadtxt('testmatrix_results_full-hSW.txt')

# create a dictionary of keys for each column in the array "data"
colDict = {'r_j/R'            : 0,
           'g/c'              : 1,
           'tip displacement' : 2}

# set the number of levels to draw in the contour plot
start_bend = 0.25
end_bend = 0.50
step_bend = 0.05
bend_lvls = np.arange(start_bend, end_bend+step_bend, step_bend)

# bend_lvls2 = np.append(bend_lvls, 0.5639)
# bend_lvls2.sort()  # sort the array, smallest to largest
# bend_lvls2 = np.array([0.5639])

# close any open figures
plt.close('all')

# open a new figure
plt.figure()

# arrange data into three 1D arrays
x = data[:,colDict['g/c']]
plt.xlabel(r'gap-to-chord ratio, $g/c$')
plt.rcParams['xtick.major.pad'] = 10  # give some extra space between the plot edge and the x-axis tick numbers
y = data[:,colDict['r_j/R']]
plt.ylabel(r'joint length-to-span ratio, $r_j/R$')
z = data[:,colDict['tip displacement']]

# define a regularly-spaced grid (the original data is irregularly-spaced)
xi = np.linspace(0.75,1.25,100)
yi = np.linspace(0.245,0.629,100)

# grid the data, using natural neighbor interpolation to map the data from
#   the irregularly-spaced grid to the regularly-spaced grid
zi = griddata(x, y, z, xi, yi, interp='nn')

# make the contour plot
CSF = plt.contourf(xi, yi, zi, bend_lvls,
                               cmap=cm.Blues,
                               antialiased=True)
CSF_lines = plt.contour(xi, yi, zi, bend_lvls,
                                    cmap=cm.Blues,
                                    antialiased=True)
CS = plt.contour(xi, yi, zi, bend_lvls,
                             colors='k',
                             antialiased=True)
# CS2 = plt.contour(xi, yi, zi, bend_lvls2,
#                               colors='r',
#                               linestyles='dashed',
#                               antialiased=True)

# make the labels and legends
plt.clabel(CS, inline=1, fmt='%3.2f', fontsize=11)  # write the z-values on the contour lines
# plt.clabel(CS2, inline=1, fmt='%5.4f', fontsize=11)  # write the z-values on the contour lines

plt.subplots_adjust(left=0.12, bottom=0.12, right=0.98, top=0.93, wspace=0.20, hspace=0.20)
cbar = plt.colorbar(CSF, spacing='proportional')  # plot a colorbar legend
cbar.set_label('tip deflection [m]')
plt.grid(True)  # turn on grids

# plot data points
plt.scatter(x,y,marker='o',c='r',s=50,clip_on=False,zorder=10)
# ... set zorder to a large number, so it gets plotted last (otherwise, the plot's bounding box will get drawn over the red points on the edge)

# set the data limits
plt.xlim(0.75,1.25)
plt.ylim(0.2455,0.629)

# show the plot
plt.show()

# save the figure to disk
plt.savefig('constlddist_May2012_full-hSW.png')
plt.savefig('constlddist_May2012_full-hSW.pdf')
