import numpy as np
import VABSobjects as vo

# number_of_nodes = 6
# number_of_elements = 2
vabs_filename = 'test_input_file_simple2.dat'

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









L_gridpts = np.array([[ 0.,  1.],  # node1
                      [ 1.,  1.],  # node2
                      [ 0.,  0.],  # node3
                      [ 1.,  0.]]) # node4
L_number_of_nodes = L_gridpts.shape[0]
L_nodes = []
vo.fillNodeObjects(L_number_of_nodes, L_nodes)
vo.assignCoordinatesToNodes(L_number_of_nodes, L_gridpts, L_nodes)
L_connectivity = np.array([[3, 4, 2, 1]])
L_number_of_elements = L_connectivity.shape[0]
L_elements = []
vo.fillElementObjects(L_number_of_elements, L_elements)
vo.assignNodesToElements(L_number_of_elements, L_connectivity, L_elements, L_nodes)


R_gridpts = np.array([[ 1.,  1.],  # node1
                      [ 2.,  1.],  # node2
                      [ 1.,  0.],  # node3
                      [ 2.,  0.]]) # node4
R_number_of_nodes = R_gridpts.shape[0]
R_nodes = []
vo.fillNodeObjects(R_number_of_nodes, R_nodes)
vo.assignCoordinatesToNodes(R_number_of_nodes, R_gridpts, R_nodes)
R_connectivity = np.array([[3, 4, 2, 1]])
R_number_of_elements = R_connectivity.shape[0]
R_elements = []
vo.fillElementObjects(R_number_of_elements, R_elements)
vo.assignNodesToElements(R_number_of_elements, R_connectivity, R_elements, R_nodes)

# define the layer (and material) for each element
for j in range(1,L_number_of_elements+1):
    L_elements[j].theta1 = 0.0  # top of layer faces up (+y direction)
    L_elements[j].layer = layer[1]  # layer_no = 1
for j in range(1,R_number_of_elements+1):
    R_elements[j].theta1 = 0.0  # top of layer faces down (-y direction)
    R_elements[j].layer = layer[1]  # layer_no = 1



# create VABS objects for nodes and elements for the entire cross-section ############################################################################################
print "STATUS: create VABS nodes and elements for the ENTIRE CROSS-SECTION..."

### CREATE NODES ###
unique_node = []  # create an empty list of node objects
# sum all the nodes for each structual component together
total_number_of_nodes = (L_number_of_nodes + R_number_of_nodes)
vo.fillNodeObjects(total_number_of_nodes, unique_node)


### CREATE ELEMENTS ###
element = []      # create an empty list of element objects
# sum all the elements for each structual component together
total_number_of_elements = (L_number_of_elements + R_number_of_elements)
vo.fillElementObjects(total_number_of_elements, element)


# assign nodes and elements from each structural component to the entire cross-section ##########################################################################
### ASSIGN NODES ###              ### this section needs to be corrected, because it double-counts nodes with the same coordinates
i = 1                                            # initialize counter for the node number
for j in range(1,L_number_of_nodes+1):
    unique_node[i] = L_nodes[j]       
    unique_node[i].node_no = i             
    i = i+1
for j in range(1,R_number_of_nodes+1):
    unique_node[i] = R_nodes[j]       
    unique_node[i].node_no = i             
    i = i+1



### ASSIGN ELEMENTS ###
i = 1                                     # initialize counter for the element number
for j in range(1,L_number_of_elements+1):
    element[i] = L_elements[j]
    element[i].elem_no = i
    i = i+1
for j in range(1,R_number_of_elements+1):
    element[i] = R_elements[j]
    element[i].elem_no = i
    i = i+1






# write to the VABS input file #############################################################################################################################
print "STATUS: writing the VABS input file:", vabs_filename
import VABSutilities as vu

curved = 1  # curve flag is set to True
twist_rate = 0.0  # twist_rate = k1, which is in units of rad/m (twist rate)

VABSflag_dictionary = {'format_flag': 1,
                       'nlayer': number_of_layers,
                       'Timoshenko_flag': 1,
                       'recover_flag': 0,
                       'thermal_flag': 0,
                       'curve_flag': curved,
                       'oblique_flag': 0,
                       'trapeze_flag': 0,
                       'Vlasov_flag': 0,
                       'k1': twist_rate,
                       'k2': 0.0,
                       'k3': 0.0,
                       'nnode': total_number_of_nodes,
                       'nelem': total_number_of_elements,
                       'nmate': number_of_materials}
                       # package all the VABS flags into one dictionary
vu.writeVABSfile(vabs_filename, unique_node, layer, material, element, VABSflag_dictionary)