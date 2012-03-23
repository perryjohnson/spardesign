vabs_filename = 'bimaterial_cs.dat'

# ----------------------------------------------------------------------------------

# parse the ABAQUS-formatted file
import truegrid.ABAQUSutilities as au
print "STATUS: interpret the ABAQUS file..."
(nodeArray, elemArray, esetArray, number_of_nodes, number_of_elements) = au.parseABAQUS('truegrid/bimaterial_cs_abq.txt', debug_flag=True)

# ----------------------------------------------------------------------------------

# create VABS objects for nodes, elements, materials, layups, etc.
import VABS.VABSobjects as vo

# set the number of materials
#   2 materials used: uniaxial, biaxial
number_of_materials = 2

# set the number of layers
#   2 layers used:  layer_no  material    theta3 (layup angle)
#                   --------  ----------  --------------------
#                       1     1 (uniax)          0 deg
#                       2     2 (biax)           0 deg
number_of_layers = 2


# create VABS objects for materials and layers
print "STATUS: create VABS materials and layers..."

layer = []        # create an empty list of layer objects
material = []     # create an empty list of material objects

vo.fillLayerObjects(number_of_layers, layer)
vo.fillMaterialObjects(number_of_materials, material)

### assign materials ###
# uniax
material[1].orth_flag = 0
material[1].material_name = 'spar cap uniax'
material[1].E = 41.8E+09
material[1].nu = 0.28
material[1].rho = 1920
# biax
material[2].orth_flag = 0
material[2].material_name = 'shear web biax'
material[2].E = 13.6E+09
material[2].nu = 0.51
material[2].rho = 1780

### assign layers ###
# layer 1
layer[1].layer_no = 1           # layer 1
layer[1].material = material[1] # uniaxial GFRP
layer[1].theta3 = 0.0           # 0 degrees, layup angle
# layer 2
layer[2].layer_no = 2           # layer 2
layer[2].material = material[2] # biaxial GFRP
layer[2].theta3 = 0.0           # 0 degrees, layup angle

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
    print "  ***WARNING*** some elements were not reordered properly!"

x1 = -0.85
x2 = -0.75
x3 = -x2
x4 = -x1

y4 = 1.0
y3 = 0.85
y2 = -y3
y1 = -y4


nan_flag = False
for i in range(1,number_of_elements+1):
    if str(element[i].theta1) == 'nan':
        nan_flag = True
        (x,y) = element[i].middle()
        if x > x1 and x < x2 and y > y1 and y < y4:  # left shear web
            element[i].theta1 = 90.0
        elif x > x3 and x < x4 and y > y1 and y < y4:  # right shear web
            element[i].theta1 = 270.0
        elif x > x2 and x < x3 and y > y3 and y < y4: # top spar cap
            element[i].theta1 = 0.0
        elif x > x2 and x < x3 and y > y1 and y < y2: # bottom spar cap
            element[i].theta1 = 180.0
        else:
            print '  ***ERROR*** element #' + str(element[i].elem_no) + ' still has theta1=nan!'
if nan_flag:
    print "  theta1 nans were found and corrected!"

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

# check the VABS input file for errors
vabs_OK = vu.checkVABSfileForErrors(vabs_filename)

# if vabs_OK and runVABS_flag:
#     # run the input file with VABS from the Windows command line
#     print ""
#     print "RUNNING VABS....."
#     vabs_command = r'.\VABS\VABSIII .\ '[:-1] + vabs_filename
#     os.system(vabs_command)