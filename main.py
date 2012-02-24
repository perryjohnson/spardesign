# ----------------------------------------------------------------------------------

# parse the ABAQUS-formatted file
import truegrid.ABAQUSutilities as au
outputfile = 'truegrid/spar_station_04_output.txt'
print "STATUS: interpret the ABAQUS file..."
(nodeArray, elemArray, number_of_nodes, number_of_elements) = au.parseABAQUS(outputfile)

# ----------------------------------------------------------------------------------

# create VABS objects for nodes, elements, materials, layups, etc.
import VABS.VABSobjects as vo

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


# create VABS objects for materials and layers
print "STATUS: create VABS materials and layers..."

layer = []        # create an empty list of layer objects
material = []     # create an empty list of material objects

vo.fillLayerObjects(number_of_layers, layer)
vo.fillMaterialObjects(number_of_materials, material)
vo.assignMaterials(number_of_materials, material)
vo.assignLayers(layer, material)

# ----------------------------------------------------------------------------------

print "STATUS: create VABS nodes and elements..."

node = []
element = []

vo.fillNodeObjects(number_of_nodes, node)
vo.assignCoordinatesToNodes(number_of_nodes, nodeArray, node)

vo.fillElementObjects(number_of_elements, element)
vo.assignNodesAndLayersToElements(number_of_elements, elemArray, element, node, layer)

element[16825].inspect()


# ----------------------------------------------------------------------------------

# write the VABS input file
# import VABS.VABSutilities as vu
