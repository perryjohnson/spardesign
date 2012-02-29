outputfile = 'truegrid/spar_station_04_output.txt'
vabs_filename = 'spar_station_04.dat'
main_debug_flag = True

# ----------------------------------------------------------------------------------

# parse the ABAQUS-formatted file
import truegrid.ABAQUSutilities as au
print "STATUS: interpret the ABAQUS file..."
(nodeArray, elemArray, esetArray, number_of_nodes, number_of_elements) = au.parseABAQUS(outputfile)

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
vo.assignElementOrientations(esetArray, element)
print "STATUS: checking if all elements are oriented in a CCW-fashion..."
reorder_OK = vo.reorderBadElements(number_of_elements, element)
if reorder_OK:
    print "  All elements reordered properly!  :)"
else:
    print "  WARNING: some elements were not reordered properly!"
if main_debug_flag:
    # element[16001].inspect()
    print "element 1"
    element[1].angles(print_flag=True)
    print ""
    print "element 9601"
    element[9601].angles(print_flag=True)

# ----------------------------------------------------------------------------------

# write the VABS input file
print "STATUS: writing the VABS input file:", vabs_filename
import VABS.VABSutilities as vu

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
                       'nnode': number_of_nodes,
                       'nelem': number_of_elements,
                       'nmate': number_of_materials}
                       # package all the VABS flags into one dictionary
vu.writeVABSfile(vabs_filename, node, layer, material, element, VABSflag_dictionary)