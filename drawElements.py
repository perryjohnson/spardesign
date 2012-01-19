import numpy as np
import VABSobjects as vo

nodes = np.loadtxt('nodes.txt')
connectivity = np.loadtxt('connectivity.txt', dtype='int')

unique_node = []  # create an empty list of node objects
element = []      # create an empty list of element objects

number_of_nodes = 150
number_of_elements = 84

coordinates_array = nodes[:,1:]
connectivity_array = connectivity[:,1:5]

vo.fillNodeObjects(number_of_nodes, unique_node)
vo.fillElementObjects(number_of_elements, element)
vo.assignCoordinatesToNodes(number_of_nodes, coordinates_array, unique_node)
vo.assignNodesToElements(number_of_elements, connectivity_array, element, unique_node)
vo.assignBordersToElements(number_of_elements, element)

print "STATUS: plotting the grid..."
import plotgrid as pg
pg.setxyMaxMin(-2,2,-3,3)
pg.setPlotAspectRatioEqual()
pg.plotNodesConnected(number_of_elements, element)
pg.showPlot()
