import numpy as np
import matplotlib.pyplot as plt

# ### this data will need to be provided by another module, or the user ###
# corners = np.array([ [-1.5, 1.2],
#                      [ 1.5, 1.2],
#                      [ 1.5,-1.2],
#                      [-1.5,-1.2] ])
# nrows = 7
# ncols = 5

def storeGridPoints(nrows,ncols,corners):
	### build an array that stores all the (x,y) gridpoints ###
	gridpts = np.zeros(((nrows+1)*(ncols+1),2))
	x_max = corners[:,0].max()
	x_min = corners[:,0].min()
	y_max = corners[:,1].max()
	y_min = corners[:,1].min()
	x = np.linspace(x_min,x_max,ncols+1)
	y = np.linspace(y_min,y_max,nrows+1)
	for i in range(len(x)):
		for j in range(len(y)):
			gridpts[i*(nrows+1)+j,0] = x[i]
			gridpts[i*(nrows+1)+j,1] = y[j]
			# print i,j,gridpts[i+j,:]
	return gridpts

if __name__ == '__main__':  # only run this block of code if this file is called directly from the command line (not if it is imported from another file)
	corners = np.array([ [-1.5, 1.2],
	                     [ 1.5, 1.2],
	                     [ 1.5,-1.2],
	                     [-1.5,-1.2] ])
	rows = 7
	cols = 5
	gridpts = storeGridPoints(rows,cols,corners)
	### plot the results ###
	# plt.figure(n)
	plt.axes().set_aspect('equal')
	# plt.axes().set_xlim(-2.0,2.0)
	# plt.axes().set_ylim(-2.0,2.0)
	plt.plot(gridpts[:,0], gridpts[:,1], 'ro')
	plt.plot(corners[:,0], corners[:,1], 'b+')
	plt.xlabel('x [m]')
	plt.ylabel('y [m]')
	plt.title('Cartesian grid')
	plt.show()