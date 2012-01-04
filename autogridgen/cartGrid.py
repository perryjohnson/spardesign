import numpy as np
import matplotlib.pyplot as plt
import VABSobjects as vo
import elementMap as em


### build an array that stores all the (x,y) grid points ###
###		input:	nrows <int>, the desired number of grid cell rows
###				ncols <int>, the desired number of grid cell columns
###				corners <np.array>, an array of x&y coordinates for each corner of the grid (4 entries)
###		output:	gridpts <np.array>, an array of x&y coordinates for each grid point
def storeGridPoints(nrows,ncols,corners):
	## check if the entries in the corners array make a rectangle (and not some other shape, like a parallelogram)
	y0 = corners[0,1]
	y1 = corners[1,1]
	y2 = corners[2,1]
	y3 = corners[3,1]
	x0 = corners[0,0]
	x2 = corners[2,0]
	x1 = corners[1,0]
	x3 = corners[3,0]
	flagT = (y0 == y1) # are y-coords of top edge equal?
	flagB = (y2 == y3) # are y-coords of bottom edge equal?
	flagL = (x0 == x2) # are x-coords of left edge equal?
	flagR = (x1 == x3) # are x-coords of right edge equal?
	gridpts = np.zeros(((nrows+1)*(ncols+1),2))  # initialize the array of grid points
	if (flagT and flagB and flagL and flagR):
		## build the array of grid points ##
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

	else:
		## print error msg(s) corresponding to each problem edge and return array of gridpoints with all entries equal to zero
		if (not flagT):
			print "ERROR: y-coords of top edge are NOT EQUAL"
		if (not flagB):
			print "ERROR: y-coords of bottom edge are NOT EQUAL"
		if (not flagL):
			print "ERROR: x-coords of left edge are NOT EQUAL"
		if (not flagR):
			print "ERROR: x-coords of right edge are NOT EQUAL"
	return gridpts


### build an array that stores all the (x,y) grid points ###   ***VERSION 2***
###		input:	nrows <int>, the desired number of grid cell rows
###				ncols <int>, the desired number of grid cell columns
###				corners <np.array>, an array of x&y coordinates for each corner of the grid (4 entries)
###		output:	gridpts <np.array>, an array of x&y coordinates for each grid point
def storeGridPoints2(nrows,ncols,corners):
	## check if the entries in the corners array make a rectangle (and not some other shape, like a parallelogram)
	y0 = corners[0,1]
	y1 = corners[1,1]
	y2 = corners[2,1]
	y3 = corners[3,1]
	x0 = corners[0,0]
	x2 = corners[2,0]
	x1 = corners[1,0]
	x3 = corners[3,0]
	flagT = (y0 == y1) # are y-coords of top edge equal?
	flagB = (y2 == y3) # are y-coords of bottom edge equal?
	flagL = (x0 == x2) # are x-coords of left edge equal?
	flagR = (x1 == x3) # are x-coords of right edge equal?
	gridpts = np.zeros(((nrows+1)*(ncols+1),2))  # initialize the array of grid points
	if (flagT and flagB and flagL and flagR):
		## calculate the number of elements and nodes for the region inside these corners ##
		number_of_elements = nrows * ncols
		number_of_nodes = (nrows+1) * (ncols+1)

		## initialize objects for the VABSobjects module ##
		unique_node = []  # create an empty list of node objects
		element = []      # create an empty list of element objects

		## call functions from the VABSobjects module ##
		vo.fillNodeObjects(number_of_nodes, unique_node)
		vo.fillElementObjects(number_of_elements, element)

		## build the array of grid points ##
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
		
		## assign x&y coordinates to each node object ##
		vo.assignCoordinatesToNodes(number_of_nodes, gridpts, unique_node)
		# print "test of unique_node[1] x&y coordinates"
		# for i in range(1,number_of_nodes+1):
		# 	print unique_node[i].x2, unique_node[i].x3
		# print nrows, ncols
		# print number_of_elements, number_of_nodes

		## assign nodes to elements ##
		(element,elementMap) = em.genElementMap(nrows,ncols,number_of_elements,number_of_nodes,element,unique_node)

		# ## check if the function correctly assigned the element connectivity ##
		# for i in range(1,number_of_elements+1):
		# 	print element[i].node1.node_no, element[i].node2.node_no, element[i].node3.node_no, element[i].node4.node_no
		
		# print "check coords of element 1, node 4"
		# print element[1].node4.x2, element[1].node4.x3

	else:
		## print error msg(s) corresponding to each problem edge and return array of gridpoints with all entries equal to zero
		if (not flagT):
			print "ERROR: y-coords of top edge are NOT EQUAL"
		if (not flagB):
			print "ERROR: y-coords of bottom edge are NOT EQUAL"
		if (not flagL):
			print "ERROR: x-coords of left edge are NOT EQUAL"
		if (not flagR):
			print "ERROR: x-coords of right edge are NOT EQUAL"
	return (gridpts,unique_node,element,number_of_nodes,number_of_elements,elementMap)


### plot the grid points and the corners ###
###		input:	gridpts <np.array>, an array of x&y coordinates for each grid point
###				corners <np.array>, an array of x&y coordinates for each corner of the grid (4 entries)
###		output:	plot of all grid points
def plotGridPoints(gridpts, corners):
	plt.axes().set_aspect('equal')
	plt.plot(gridpts[:,0], gridpts[:,1], 'b+')
	plt.plot(corners[:,0], corners[:,1], 'ro')
	plt.xlabel('x [m]')
	plt.ylabel('y [m]')
	plt.title('Cartesian grid')
	plt.show()

### determine the number of cells needed for a Cartesian grid with low aspect ratio cells ###
###		input:	dim1 <double>, 1st dimension of grid area (e.g. length)
###				n1 <int>, desired number of cells to be distributed along dim1
###				maxAR <double>, desired maximum aspect ratio for any cell in the grid
###				dim2 <double>, 2nd dimension of grid area (e.g. width)
###		output:	n1 <int>, number of cells to be distributed along dim1 (may be updated from input n1)
###				n2 <int>, number of cells to be distributed along dim2
def calcCellNums(dim1,n1,maxAR,dim2):
	if type(n1) != type(1):                 # check if input value for n1 is an integer
		print "ERROR: input value for n1 must be an INTEGER!"
		n1 = 0
		n2 = 0
	else:
		flag = True
		while (flag):
			# print 'n1        =', n1
			cell_dim1 = dim1/float(n1)      # calculate the cell dimension in the dim1 direction
			# print 'cell_dim1 =', cell_dim1
			# print 'maxAR     =', maxAR
			cell_dim2 = cell_dim1 * maxAR   # calculate the cell dimension in the dim2 direction
			# print 'cell_dim2 =', cell_dim2
			n2 = dim2/cell_dim2             # see how many cells of size cell_dim2 will fit in the dim2 direction
			n2 = int(n2) + 1                # round the result up to the next integer
			# print 'n2        =', n2
			cell_dim2 = dim2/float(n2)      # recalculate the cell dimension in the dim2 direction
			# print 'cell_dim2 =', cell_dim2
			AR = cell_dim1/cell_dim2        # calculate the current cell aspect ratio
			if AR < 1.0:                    # if aspect ratio is less than 1...
				AR = 1.0/AR                 # ...take its reciprocal (aspect ratio is defined as > 1)
			# print 'AR        =', AR
			# print 'maxAR     =', maxAR
			if AR < maxAR:					# if the aspect ratio is less than the specified max aspect ratio...
				flag = False                # ...exit this loop
			else:
				n1 = n1 * 2                 # otherwise, double the number of cells in the dim1 direction and reiterate this loop
	### optional print statements for debugging ###
	# print 'dim1      =', dim1
	# print 'dim2      =', dim2
	# print 'cell_dim1 =', cell_dim1
	# print 'cell_dim2 =', cell_dim2
	# print 'n1        =', n1
	# print 'n2        =', n2
	# print 'AR        =', AR
	# print 'maxAR     =', maxAR
	return (n1,n2)

### determine dimensions of a grid, given the x&y coordinates of its corners ###
###		input:	corners <nd.array>, an array of x&y coordinates for each corner of the grid (4 entries)
###		output:	dimH <double>, horizontal dimension of grid area
###				dimV <double>, vertical dimension of grid area
def calcCornerDims(corners):
	dimH = abs(corners[0,0] - corners[1,0])  # subtract the x-coords of the top left and top right corners
	dimV = abs(corners[0,1] - corners[2,1])  # subtract the y-coords of the top left and bottom left corners
	return (dimH,dimV)

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