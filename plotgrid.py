import matplotlib.pyplot as plt      # import the pyplot module from matplotlib; rename it as plt
from pylab import savefig            # import the savefig function (which saves plots to the hard disk) from the pylab module
import numpy as np                   # import the numpy module; rename it as np


## set the plot labels, title, and grid
##    input: plotTitle <string> title for this plot
##    output: <none>
def setPlotLabelsTitleAndGrid(plotTitle):
	plt.xlabel('x  [meters]')
	plt.ylabel('y  [meters]')
	plt.title(plotTitle)
	plt.grid(True)
	return


## set the plot aspect ratio to 1:1 (equal)
##    input: <none>
##    output: <none>
def setPlotAspectRatioEqual():	
	plt.axes().set_aspect('equal')
	return


## plot the node coordinates as unconnected points
##    input: coordinates <array>, numpy array of x&y coordinates of each node in this grid
##    output: <none>
def plotNodesUnconnected(coordinates):
	plt.plot(coordinates[:,0], coordinates[:,1], 'r+')
	return


## plot the node coordinates as connected points to form each element as a grid cell
##    input: nelem <int>, number of elements in this grid
##           elem <object>, list of element objects
##    output: <none>
def plotNodesConnected(nelem, elem):
	print "        - connecting the nodes with gridlines"
	for i in range(1,nelem+1):
		# look up the x,y coordinates of each node
		x1 = elem[i].node1.x2
		y1 = elem[i].node1.x3
		x2 = elem[i].node2.x2
		y2 = elem[i].node2.x3
		x3 = elem[i].node3.x2
		y3 = elem[i].node3.x3
		x4 = elem[i].node4.x2
		y4 = elem[i].node4.x3

		# draw a line from node1 to node2
		plt.plot([x1,x2], [y1,y2], 'black')
		# draw a line from node2 to node3
		plt.plot([x2,x3], [y2,y3], 'black')
		# draw a line from node3 to node4
		plt.plot([x3,x4], [y3,y4], 'black')
		# draw a line from node4 to node1
		plt.plot([x4,x1], [y4,y1], 'black')

		if i % 50 == 0:  # print progress to screen
			print '          drawing lines for element #' + str(elem[i].elem_no) + '/' + str(nelem)
	return


## fill each element with a color corresponding to that material
##    input: nelem <int>, number of elements in this grid
##           elem <object>, list of element objects
##           equal_flag <logical>, true if plot should have aspect ratio 1:1, false otherwise
##           grid_flag <logical>, true if plot should element grid lines, false otherwise
##    output: <none>
def colorElementsByMaterial(nelem, elem, equal_flag, grid_flag):
	plt.figure()
	setPlotLabelsTitleAndGrid('Elements colored by material')
	if equal_flag: setPlotAspectRatioEqual()
	if grid_flag: plotNodesConnected(nelem, elem)
	for i in range(1,nelem+1):
		fillcolor = elem[i].layer.material.color
		if elem[i].layer.material.material_no == np.nan:
			print 'WARNING: material of element #' + elem[i].elem_no + ' could NOT be determined'

		# fill the element with a color corresponding to its material
		x_temp = elem[i].lower_border_x
		y1_temp = elem[i].lower_border_y
		y2_temp = elem[i].upper_border_y
		plt.fill_between(x_temp, y1_temp, y2_temp, color=fillcolor)

	return


## fill each element with a color corresponding to that layer
##    input: nelem <int>, number of elements in this grid
##           elem <object>, list of element objects
##           equal_flag <logical>, true if plot should have aspect ratio 1:1, false otherwise
##           grid_flag <logical>, true if plot should element grid lines, false otherwise
##    output: <none>
def colorElementsByLayer(nelem, elem, equal_flag, grid_flag):
	plt.figure()
	setPlotLabelsTitleAndGrid('Elements colored by layer')
	if equal_flag: setPlotAspectRatioEqual()
	if grid_flag: plotNodesConnected(nelem, elem)
	for i in range(1,nelem+1):
		fillcolor = elem[i].layer.color
		if elem[i].layer.layer_no == np.nan:
			fillcolor = 'white'
			print 'WARNING: layer of element #' + elem[i].elem_no + ' could NOT be determined'

		# fill the element with a color corresponding to its material
		x_temp = elem[i].lower_border_x
		y1_temp = elem[i].lower_border_y
		y2_temp = elem[i].upper_border_y
		plt.fill_between(x_temp, y1_temp, y2_temp, color=fillcolor)

		if i % 5000 == 0:  # print progress to screen
			print '          filling element #' + str(elem[i].elem_no) + '/' + str(nelem)

	return


## print a legend for the material colors
##    input: nmate <int>, number of materials in this grid
##           matl <object>, list of material objects
##    output: <none>
def printLegendForMaterialColors(nmate, matl):
	print '\n          Legend for material colors:'
	print '   --------------------------------------------------'
	print 'color'.rjust(10), \
	      'material_no'.rjust(13), \
	      'orth_flag'.rjust(11), \
	      '  material_name'
	print '   --------------------------------------------------'
	for i in range(1,nmate+1):
		print matl[i].color.rjust(10), \
		      '%13i' % matl[i].material_no, \
		      '%11i' % matl[i].orth_flag, \
		      ('  ' + matl[i].material_name)
	print '   --------------------------------------------------'
	print ''
	return


## print a legend for the layer colors
##    input: nlayer <int>, number of layers in this grid
##           layer_list <object>, list of layer objects
##    output: <none>
def printLegendForLayerColors(nlayer, layer_list):
	print '\n          Legend for layer colors:'
	print '   --------------------------------------------'
	print 'color'.rjust(10), \
	      'layer_no'.rjust(9), \
	      'theta3'.rjust(9), \
	      '  material_name'
	print '   --------------------------------------------'
	for i in range(1,nlayer+1):
		print layer_list[i].color.rjust(10), \
		      '%9i' % layer_list[i].layer_no, \
		      '%9.1f' % layer_list[i].theta3, \
		      ('  ' + layer_list[i].material.material_name)
	print '   --------------------------------------------'
	print ''
	return


## show the plot
##    input: <none>
##    output: <none>
def showPlot():
	plt.show()
	return