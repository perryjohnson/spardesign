import time

# record the time when the code starts
start_time = time.time()

import autogridgen.genGrid as gg
import VABSobjects as vo
import autogridgen.read_layup as rl


# set the number of materials
#   4 materials used: uniaxial, biaxial, triaxial GFRP, and foam
number_of_materials = 4

# set the number of layers
#   7 layers used:  layer_no  material    theta3 (layup angle)
#                   --------  ----------  --------------------
#                       1     1 (uniax)          0 deg
#                       2     2 (biax)         +45 deg
#                       3     2 (biax)         -45 deg
#                       4     3 (triax)        +45 deg
#                       5     3 (triax)        -45 deg
#                       6     3 (triax)          0 deg
#                       7     4 (foam)           0 deg
number_of_layers = 7


# create VABS objects for materials and layups
print "STATUS: create VABS materials and layups..."

layer = []        # create an empty list of layer objects
material = []     # create an empty list of material objects

vo.fillLayerObjects(number_of_layers, layer)
vo.fillMaterialObjects(number_of_materials, material)
vo.assignMaterials(number_of_materials, material)
vo.assignLayers(layer, material)


# create VABS objects for nodes and elements for each structural component
print "STATUS: create VABS nodes and elements for each STRUCTURAL COMPONENT..."

# unique_node = []  # create an empty list of node objects
# element = []      # create an empty list of element objects
# vo.fillNodeObjects(number_of_nodes, unique_node)
# vo.fillElementObjects(number_of_elements, element)
# vo.assignCoordinatesToNodes(number_of_nodes, coordinates_array, unique_node)
# vo.assignNodesToElements(number_of_elements, connectivity_array, element, unique_node)
# vo.reassignNodesOnAllBadElements(number_of_elements, element)
# vo.assignBordersToElements(number_of_elements, element)
# vo.rewriteConnectivity(number_of_elements, element, connectivity_array)


data = rl.readLayupFile('autogridgen/monoplane_spar_layup.txt')  # import the data from the layup file
spar_stn = 1

(RB_T_nodes, RB_T_elements, RB_T_number_of_nodes, RB_T_number_of_elements, RB_T_nodeMap, RB_T_elementMap,
 RB_B_nodes, RB_B_elements, RB_B_number_of_nodes, RB_B_number_of_elements, RB_B_nodeMap, RB_B_elementMap) = gg.genRootBuildup(data,spar_stn)
(SC_T_nodes, SC_T_elements, SC_T_number_of_nodes, SC_T_number_of_elements, SC_T_nodeMap, SC_T_elementMap,
 SC_B_nodes, SC_B_elements, SC_B_number_of_nodes, SC_B_number_of_elements, SC_B_nodeMap, SC_B_elementMap) = gg.genSparCaps(data,spar_stn)
(SW_L_biaxL_nodes, SW_L_biaxL_elements, SW_L_biaxL_number_of_nodes, SW_L_biaxL_number_of_elements, SW_L_biaxL_nodeMap, SW_L_biaxL_elementMap,
 SW_L_foam_nodes,  SW_L_foam_elements,  SW_L_foam_number_of_nodes,  SW_L_foam_number_of_elements,  SW_L_foam_nodeMap,  SW_L_foam_elementMap,
 SW_L_biaxR_nodes, SW_L_biaxR_elements, SW_L_biaxR_number_of_nodes, SW_L_biaxR_number_of_elements, SW_L_biaxR_nodeMap, SW_L_biaxR_elementMap,
 SW_R_biaxL_nodes, SW_R_biaxL_elements, SW_R_biaxL_number_of_nodes, SW_R_biaxL_number_of_elements, SW_R_biaxL_nodeMap, SW_R_biaxL_elementMap,
 SW_R_foam_nodes,  SW_R_foam_elements,  SW_R_foam_number_of_nodes,  SW_R_foam_number_of_elements,  SW_R_foam_nodeMap,  SW_R_foam_elementMap,
 SW_R_biaxR_nodes, SW_R_biaxR_elements, SW_R_biaxR_number_of_nodes, SW_R_biaxR_number_of_elements, SW_R_biaxR_nodeMap, SW_R_biaxR_elementMap) = gg.genShearWebs(data,spar_stn)


# define the layer (and material) for each element
print "STATUS: define the layer (and material) for each element"

### root buildup, triaxial GFRP ###
# top root buildup
for j in range(1,RB_T_number_of_elements+1):
	RB_T_elements[j].theta1 = 0.0  # top of layer faces up (+y direction)
for j in range(RB_T_elementMap.shape[1]):
	RB_T_elements[RB_T_elementMap[0,:][j]].layer = layer[6]  # layer_no = 6   (+y)
	RB_T_elements[RB_T_elementMap[1,:][j]].layer = layer[6]  # layer_no = 6   ( |)
	RB_T_elements[RB_T_elementMap[2,:][j]].layer = layer[5]  # layer_no = 5   ( |)
	RB_T_elements[RB_T_elementMap[3,:][j]].layer = layer[4]  # layer_no = 4   ( |)
	RB_T_elements[RB_T_elementMap[4,:][j]].layer = layer[5]  # layer_no = 5   ( |)
	RB_T_elements[RB_T_elementMap[5,:][j]].layer = layer[4]  # layer_no = 4   (-y)
# bottom root buildup
for j in range(1,RB_B_number_of_elements+1):
	RB_B_elements[j].theta1 = 180.0  # top of layer faces down (-y direction)
for j in range(RB_B_elementMap.shape[1]):
	RB_B_elements[RB_B_elementMap[0,:][j]].layer = layer[4]  # layer_no = 4   (+y)
	RB_B_elements[RB_B_elementMap[1,:][j]].layer = layer[5]  # layer_no = 5   ( |)
	RB_B_elements[RB_B_elementMap[2,:][j]].layer = layer[4]  # layer_no = 4   ( |)
	RB_B_elements[RB_B_elementMap[3,:][j]].layer = layer[5]  # layer_no = 5   ( |)
	RB_B_elements[RB_B_elementMap[4,:][j]].layer = layer[6]  # layer_no = 6   ( |)
	RB_B_elements[RB_B_elementMap[5,:][j]].layer = layer[6]  # layer_no = 6   (-y)

### spar caps, uniaxial GFRP ###
# top spar cap
for j in range(1,SC_T_number_of_elements+1):
	SC_T_elements[j].theta1 = 0.0  # top of layer faces up (+y direction)
	SC_T_elements[j].layer = layer[1]  # layer_no = 1
# bottom spar cap
for j in range(1,SC_B_number_of_elements+1):
	SC_B_elements[j].theta1 = 180.0  # top of layer faces down (-y direction)
	SC_B_elements[j].layer = layer[1]  # layer_no = 1

### shear webs, biaxial GFRP and foam ###
## right shear web ##
# right shear web, internal (left) biaxial laminate
for j in range(1,SW_R_biaxL_number_of_elements+1):
	SW_R_biaxL_elements[j].theta1 = 270.0  # top of layer faces right (+x direction)
for j in range(SW_R_biaxL_elementMap.shape[0]):
	SW_R_biaxL_elements[SW_R_biaxL_elementMap[:,0][j]].layer = layer[2]  # layer_no = 2   (-x)
	SW_R_biaxL_elements[SW_R_biaxL_elementMap[:,1][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_R_biaxL_elements[SW_R_biaxL_elementMap[:,2][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_R_biaxL_elements[SW_R_biaxL_elementMap[:,3][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_R_biaxL_elements[SW_R_biaxL_elementMap[:,4][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_R_biaxL_elements[SW_R_biaxL_elementMap[:,5][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_R_biaxL_elements[SW_R_biaxL_elementMap[:,6][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_R_biaxL_elements[SW_R_biaxL_elementMap[:,7][j]].layer = layer[3]  # layer_no = 3   (+x)
# right shear web, foam
for j in range(1,SW_R_foam_number_of_elements+1):
	SW_R_foam_elements[j].theta1 = 270.0  # top of layer faces right (+x direction)
	SW_R_foam_elements[j].layer = layer[7]  # layer_no = 7
# right shear web, external (right) biaxial laminate
for j in range(1,SW_R_biaxR_number_of_elements+1):
	SW_R_biaxR_elements[j].theta1 = 270.0  # top of layer faces right (+x direction)
for j in range(SW_R_biaxR_elementMap.shape[0]):
	SW_R_biaxR_elements[SW_R_biaxR_elementMap[:,0][j]].layer = layer[2]  # layer_no = 2   (-x)
	SW_R_biaxR_elements[SW_R_biaxR_elementMap[:,1][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_R_biaxR_elements[SW_R_biaxR_elementMap[:,2][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_R_biaxR_elements[SW_R_biaxR_elementMap[:,3][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_R_biaxR_elements[SW_R_biaxR_elementMap[:,4][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_R_biaxR_elements[SW_R_biaxR_elementMap[:,5][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_R_biaxR_elements[SW_R_biaxR_elementMap[:,6][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_R_biaxR_elements[SW_R_biaxR_elementMap[:,7][j]].layer = layer[3]  # layer_no = 3   (+x)
# left shear web, internal (right) biaxial laminate
for j in range(1,SW_L_biaxR_number_of_elements+1):
	SW_L_biaxR_elements[j].theta1 = 90.0  # top of layer faces left (-x direction)
for j in range(SW_L_biaxR_elementMap.shape[0]):
	SW_L_biaxR_elements[SW_L_biaxR_elementMap[:,0][j]].layer = layer[3]  # layer_no = 3   (-x)
	SW_L_biaxR_elements[SW_L_biaxR_elementMap[:,1][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_L_biaxR_elements[SW_L_biaxR_elementMap[:,2][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_L_biaxR_elements[SW_L_biaxR_elementMap[:,3][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_L_biaxR_elements[SW_L_biaxR_elementMap[:,4][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_L_biaxR_elements[SW_L_biaxR_elementMap[:,5][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_L_biaxR_elements[SW_L_biaxR_elementMap[:,6][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_L_biaxR_elements[SW_L_biaxR_elementMap[:,7][j]].layer = layer[2]  # layer_no = 2   (+x)
# left shear web, foam
for j in range(1,SW_L_foam_number_of_elements+1):
	SW_L_foam_elements[j].theta1 = 90.0  # top of layer faces right (-x direction)
	SW_L_foam_elements[j].layer = layer[7]  # layer_no = 7
# left shear web, external (left) biaxial laminate
for j in range(1,SW_L_biaxL_number_of_elements+1):
	SW_L_biaxL_elements[j].theta1 = 90.0  # top of layer faces left (-x direction)
for j in range(SW_L_biaxL_elementMap.shape[0]):
	SW_L_biaxL_elements[SW_L_biaxL_elementMap[:,0][j]].layer = layer[3]  # layer_no = 3   (-x)
	SW_L_biaxL_elements[SW_L_biaxL_elementMap[:,1][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_L_biaxL_elements[SW_L_biaxL_elementMap[:,2][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_L_biaxL_elements[SW_L_biaxL_elementMap[:,3][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_L_biaxL_elements[SW_L_biaxL_elementMap[:,4][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_L_biaxL_elements[SW_L_biaxL_elementMap[:,5][j]].layer = layer[2]  # layer_no = 2   ( |)
	SW_L_biaxL_elements[SW_L_biaxL_elementMap[:,6][j]].layer = layer[3]  # layer_no = 3   ( |)
	SW_L_biaxL_elements[SW_L_biaxL_elementMap[:,7][j]].layer = layer[2]  # layer_no = 2   (+x)


# create VABS objects for nodes and elements for the entire cross-section
print "STATUS: create VABS nodes and elements for the ENTIRE CROSS-SECTION..."

### CREATE NODES ###
unique_node = []  # create an empty list of node objects
# sum all the nodes for each structual component together
total_number_of_nodes = (RB_T_number_of_nodes + RB_B_number_of_nodes +
                         SC_T_number_of_nodes + SC_B_number_of_nodes + 
                         SW_L_biaxL_number_of_nodes + SW_L_foam_number_of_nodes + SW_L_biaxR_number_of_nodes +
                         SW_R_biaxL_number_of_nodes + SW_R_foam_number_of_nodes + SW_R_biaxR_number_of_nodes)
vo.fillNodeObjects(total_number_of_nodes, unique_node)


### CREATE ELEMENTS ###
element = []      # create an empty list of element objects
# sum all the elements for each structual component together
total_number_of_elements = (RB_T_number_of_elements + RB_B_number_of_elements +
                            SC_T_number_of_elements + SC_B_number_of_elements +
                            SW_L_biaxL_number_of_elements + SW_L_foam_number_of_elements + SW_L_biaxR_number_of_elements +
                            SW_R_biaxL_number_of_elements + SW_R_foam_number_of_elements + SW_R_biaxR_number_of_elements)
vo.fillElementObjects(total_number_of_elements, element)


# assign nodes and elements from each structural component to the entire cross-section
### ASSIGN NODES ###
i = 1                                            # initialize counter for the node number
for j in range(1,RB_T_number_of_nodes+1):
	unique_node[i] = RB_T_nodes[j]               # assign coordinates for top root buildup
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND RB_T_nodes[j] (b/c the previous line performs a shallow copy, not a deep copy)
	i = i+1                                      # increment counter for the node number
for j in range(1,RB_B_number_of_nodes+1):
	unique_node[i] = RB_B_nodes[j]               # assign coordinatess for bottom root buildup
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND RB_B_nodes[j]
	i = i+1
for j in range(1,SC_T_number_of_nodes+1):
	unique_node[i] = SC_T_nodes[j]               # assign coordinates for top spar cap
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SC_T_nodes[j]
	i = i+1
for j in range(1,SC_B_number_of_nodes+1):
	unique_node[i] = SC_B_nodes[j]               # assign coordinates for bottom spar cap
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SC_B_nodes[j]
	i = i+1
for j in range(1,SW_L_biaxL_number_of_nodes+1):
	unique_node[i] = SW_L_biaxL_nodes[j]         # assign coordinates for left shear web, left biax laminate
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_L_biaxL_nodes[j]
	i = i+1
for j in range(1,SW_L_foam_number_of_nodes+1):
	unique_node[i] = SW_L_foam_nodes[j]          # assign coordinates for left shear web, foam laminate
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_L_foam_nodes[j]
	i = i+1
for j in range(1,SW_L_biaxR_number_of_nodes+1):
	unique_node[i] = SW_L_biaxR_nodes[j]         # assign coordinates for left shear web, right biax laminate
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_L_biaxR_nodes[j]
	i = i+1
for j in range(1,SW_R_biaxL_number_of_nodes+1):
	unique_node[i] = SW_R_biaxL_nodes[j]         # assign coordinates for right shear web, left biax laminate
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_R_biaxL_nodes[j]
	i = i+1
for j in range(1,SW_R_foam_number_of_nodes+1):
	unique_node[i] = SW_R_foam_nodes[j]          # assign coordinates for right shear web, foam laminate
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_R_foam_nodes[j]
	i = i+1
for j in range(1,SW_R_biaxR_number_of_nodes+1):
	unique_node[i] = SW_R_biaxR_nodes[j]         # assign coordinates for right shear web, right biax laminate
	unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_R_biaxR_nodes[j]
	i = i+1


### ASSIGN ELEMENTS ###
i = 1                                     # initialize counter for the element number
for j in range(1,RB_T_number_of_elements+1):
	element[i] = RB_T_elements[j]         # assign elements for top root buildup
	element[i].elem_no = i                # overwrite the element number
	i = i+1                               # increment counter for the element number
for j in range(1,RB_B_number_of_elements+1):
	element[i] = RB_B_elements[j]         # assign elements for bottom root buildup
	element[i].elem_no = i                # overwrite the element number
	i = i+1
for j in range(1,SC_T_number_of_elements+1):
	element[i] = SC_T_elements[j]         # assign elements for top spar cap
	element[i].elem_no = i                # overwrite the element number
	i = i+1
for j in range(1,SC_B_number_of_elements+1):
	element[i] = SC_B_elements[j]         # assign elements for bottom spar cap
	element[i].elem_no = i                # overwrite the element number
	i = i+1
for j in range(1,SW_L_biaxL_number_of_elements+1):
	element[i] = SW_L_biaxL_elements[j]   # assign elements for left shear web, left biax laminate
	element[i].elem_no = i                # overwrite the element number
	i = i+1
for j in range(1,SW_L_foam_number_of_elements+1):
	element[i] = SW_L_foam_elements[j]    # assign elements for left shear web, foam laminate
	element[i].elem_no = i                # overwrite the element number
	i = i+1
for j in range(1,SW_L_biaxR_number_of_elements+1):
	element[i] = SW_L_biaxR_elements[j]   # assign elements for left shear web, right biax laminate
	element[i].elem_no = i                # overwrite the element number
	i = i+1
for j in range(1,SW_R_biaxL_number_of_elements+1):
	element[i] = SW_R_biaxL_elements[j]   # assign elements for right shear web, left biax laminate
	element[i].elem_no = i                # overwrite the element number
	i = i+1
for j in range(1,SW_R_foam_number_of_elements+1):
	element[i] = SW_R_foam_elements[j]    # assign elements for right shear web, foam laminate
	element[i].elem_no = i                # overwrite the element number
	i = i+1
for j in range(1,SW_R_biaxR_number_of_elements+1):
	element[i] = SW_R_biaxR_elements[j]   # assign elements for right shear web, right biax laminate
	element[i].elem_no = i                # overwrite the element number
	i = i+1


vo.assignBordersToElements(total_number_of_elements, element)

print "STATUS: plotting the grid..."
import plotgrid as pg
AR_equal = True
element_lines = False
print "        - coloring the elements by layer"
pg.colorElementsByLayer(total_number_of_elements, element, AR_equal, element_lines)
# print "        - coloring the elements by material"
# pg.colorElementsByMaterial(number_of_elements, element, AR_equal, element_lines)
print "        - showing the plot"
# pg.printLegendForLayerColors(number_of_layers, layer)
# pg.printLegendForMaterialColors(number_of_materials, material)
pg.showPlot()









# calculate the time it took to run the code
elapsed_time_tot = time.time() - start_time

print "program completed in", ("%.2f" % round(elapsed_time_tot,2)), "seconds"
