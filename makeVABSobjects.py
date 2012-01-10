import autogridgen.genGrid as gg
import VABSobjects as vo
import autogridgen.read_layup as rl
import time


# record the time when the code starts
start_time = time.time()


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
print "STATUS: create VABS objects for materials and layups..."

layer = []        # create an empty list of layer objects
material = []     # create an empty list of material objects

vo.fillLayerObjects(number_of_layers, layer)
vo.fillMaterialObjects(number_of_materials, material)
vo.assignMaterials(number_of_materials, material)
vo.assignLayers(layer, material)


# create VABS objects for nodes and elements
print "STATUS: create VABS objects for nodes and elements..."

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

(RB_T_nodes, RB_T_elements, RB_T_number_of_nodes, RB_T_number_of_elements, RB_T_elementMap,
 RB_B_nodes, RB_B_elements, RB_B_number_of_nodes, RB_B_number_of_elements, RB_B_elementMap) = gg.genRootBuildup(data,spar_stn)
(SC_T_nodes, SC_T_elements, SC_T_number_of_nodes, SC_T_number_of_elements, SC_T_elementMap,
 SC_B_nodes, SC_B_elements, SC_B_number_of_nodes, SC_B_number_of_elements, SC_B_elementMap) = gg.genSparCaps(data,spar_stn)
(SW_L_biaxL_nodes, SW_L_biaxL_elements, SW_L_biaxL_number_of_nodes, SW_L_biaxL_number_of_elements, SW_L_biaxL_elementMap,
 SW_L_foam_nodes,  SW_L_foam_elements,  SW_L_foam_number_of_nodes,  SW_L_foam_number_of_elements,  SW_L_foam_elementMap,
 SW_L_biaxR_nodes, SW_L_biaxR_elements, SW_L_biaxR_number_of_nodes, SW_L_biaxR_number_of_elements, SW_L_biaxR_elementMap,
 SW_R_biaxL_nodes, SW_R_biaxL_elements, SW_R_biaxL_number_of_nodes, SW_R_biaxL_number_of_elements, SW_R_biaxL_elementMap,
 SW_R_foam_nodes,  SW_R_foam_elements,  SW_R_foam_number_of_nodes,  SW_R_foam_number_of_elements,  SW_R_foam_elementMap,
 SW_R_biaxR_nodes, SW_R_biaxR_elements, SW_R_biaxR_number_of_nodes, SW_R_biaxR_number_of_elements, SW_R_biaxR_elementMap) = gg.genShearWebs(data,spar_stn)


# define the layer (and material) for each element
print "STATUS: define the layer (and material) for each element"

### root buildup, triaxial GFRP ###
# top root buildup
for j in range(1,RB_T_number_of_elements+1):
	RB_T_elements[j].theta1 = 0.0  # top of layer faces up (+y direction)
	# RB_T_elements[j].layer = layer[]  # layer_no = 
# bottom root buildup
for j in range(1,RB_B_number_of_elements+1):
	RB_B_elements[j].theta1 = 180.0  # top of layer faces down (-y direction)
	# RB_B_elements[j].layer = layer[]  # layer_no = 

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
# right shear web, external (right) biaxial laminate
for j in range(1,SW_R_biaxL_number_of_elements+1):
	SW_R_biaxR_elements[j].theta1 = 270.0  # top of layer faces right (+x direction)
# left shear web, internal (right) biaxial laminate
for j in range(1,SW_L_biaxR_number_of_elements+1):
	SW_L_biaxR_elements[j].theta1 = 90.0  # top of layer faces left (-x direction)
# left shear web, external (left) biaxial laminate
for j in range(1,SW_L_biaxL_number_of_elements+1):
	SW_L_biaxL_elements[j].theta1 = 90.0  # top of layer faces left (-x direction)


# vo.defineLayerForEachElement(spar_cap_width,
#                              shear_web_biaxial_width,
#                              shear_web_foam_width,
#                              shear_web_height,
#                              root_buildup_height,
#                              number_of_elements,
#                              element,
#                              t_uniaxialGFRP_layer,
#                              t_biaxialGFRP_layer,
#                              t_triaxialGFRP_layer,
#                              layer)











# calculate the time it took to run the code
elapsed_time_tot = time.time() - start_time

print "program completed in", ("%.2f" % round(elapsed_time_tot,2)), "seconds"
