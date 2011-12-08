# script to translate VRML files from Gridgen into VABS input files
# this is the windows version (produces output file with Windows-style line endings?)
# usage: makeVABSinput.py -i FILEIN.grd -o FILEOUT.dat -p plot_flag -hsw shear_web_height -hrb root_buildup_height -hsc spar_cap_height -c curved -k1 twist_rate
## command line options:
## ---------------------
## -i    input file
## -o    output file
## -p    show plot?
## -hsw  height of the shear web
## -hrb  height of the root buildup
## -hsc  height of the spar cap
## -c    curved and/or twisted beam?
## -k1   twist rate (dimensions of rad/m)


import numpy as np        # import the numpy module; rename it as np
import sys                # import the system module
import argvParsing as ap  # import the command-line argument parsing module; rename it as ap


# parse the command line arguments to extract the input and output filenames
print ''
myargs = ap.getopts(sys.argv)
print ' input file:', myargs['-i']
grid_filename = myargs['-i']  # specify the filename of the VRML file
print 'output file:', myargs['-o']
vabs_filename = myargs['-o']  # specify the filename of the VABS input file
print '  plot_flag:', myargs['-p']
if myargs['-p'] == 'True':
  plot_flag = True
else:
  plot_flag = False
print ''
print '   shear_web_height:', myargs['-hsw']
shear_web_height = float(myargs['-hsw'])
print 'root buildup height:', myargs['-hrb']
root_buildup_height = float(myargs['-hrb'])
print '    spar cap height:', myargs['-hsc']
spar_cap_height = float(myargs['-hsc'])
print ''
print 'curve_flag:', myargs['-c']
if (myargs['-c'] == 'True'):
  curved = 1
  print '        k1:', myargs['-k1']
  twist = float(myargs['-k1'])
else:
  curved = 0
print ''


# set the number of materials
#   4 materials used: uniaxial, biaxial, triaxial GFRP, and foam
number_of_materials = 4
# set the number of layers
#   7 layers used:  layer_no  material    theta3 (layup angle)
#                   --------  ----------  --------------------
#                       1     1 (uniax)          0 deg
#                       2     2 (biax)           0 deg
#                       3     2 (biax)           0 deg
#                       4     3 (triax)          0 deg
#                       5     3 (triax)          0 deg
#                       6     3 (triax)          0 deg
#                       7     4 (foam)           0 deg
number_of_layers = 7


# parse this VRML-formatted file
print "STATUS: parsing the VRML-formatted file..."
import VRMLutilities
(coordinates_array, connectivity_array, number_of_nodes, number_of_elements) = VRMLutilities.parseVRML(grid_filename)


# create VABS objects for nodes, elements, materials, layups, etc.
print "STATUS: create VABS objects for nodes, elements, materials, layups, etc..."
import VABSobjects as vo

unique_node = []  # create an empty list of node objects
layer = []        # create an empty list of layer objects
material = []     # create an empty list of material objects
element = []      # create an empty list of element objects

vo.fillNodeObjects(number_of_nodes, unique_node)
vo.fillLayerObjects(number_of_layers, layer)
vo.fillMaterialObjects(number_of_materials, material)
vo.assignMaterials(number_of_materials, material)
vo.fillElementObjects(number_of_elements, element)
vo.assignCoordinatesToNodes(number_of_nodes, coordinates_array, unique_node)
vo.assignLayers(layer, material)
vo.assignNodesToElements(number_of_elements, connectivity_array, element, unique_node)
vo.reassignNodesOnAllBadElements(number_of_elements, element)
vo.assignBordersToElements(number_of_elements, element)
vo.rewriteConnectivity(number_of_elements, element, connectivity_array)


# define box-beam dimensions (all dimensions have units of meters)
spar_cap_width = 1.5              # constant
shear_web_biaxial_width = 0.003   # constant
shear_web_foam_width = 0.080      # constant
# shear_web_height = 5.392          # (LATER: PULL THIS FROM FILE FOR EACH STATION)
# root_buildup_height = 0.063       # (LATER: PULL THIS FROM FILE FOR EACH STATION)
# spar_cap_height = 0.013           # (LATER: PULL THIS FROM FILE FOR EACH STATION)
nlayer_uniaxialGFRP = 2           # number of layers in the uniaxial GFRP laminate
nlayer_biaxialGFRP = 8            # number of layers in the biaxial GFRP laminate
nlayer_triaxialGFRP = 6           # number of layers in the triaxial GFRP laminate
td = {'t_uniaxialGFRP': spar_cap_height,
      't_biaxialGFRP': shear_web_biaxial_width,
      't_triaxialGFRP': root_buildup_height}     # dictionary for thicknesses of all laminates
(t_uniaxialGFRP_layer, t_biaxialGFRP_layer, t_triaxialGFRP_layer) = vo.calcLayerThicknessesForAllLaminates(td['t_uniaxialGFRP'], td['t_biaxialGFRP'], td['t_triaxialGFRP'], nlayer_uniaxialGFRP,  nlayer_biaxialGFRP,  nlayer_triaxialGFRP)
vo.defineLayerForEachElement(spar_cap_width, shear_web_biaxial_width, shear_web_foam_width, shear_web_height, root_buildup_height, number_of_elements, element, t_uniaxialGFRP_layer, t_biaxialGFRP_layer, t_triaxialGFRP_layer, layer)


# plot the grid to the screen using matplotlib
if plot_flag == True:
  print "STATUS: plotting the grid..."
  import plotgrid as pg
  AR_equal = True
  element_lines = False
  print "        - coloring the elements by layer"
  pg.colorElementsByLayer(number_of_elements, element, AR_equal, element_lines)
  print "        - coloring the elements by material"
  pg.colorElementsByMaterial(number_of_elements, element, AR_equal, element_lines)
  print "        - showing the plot"
  pg.printLegendForLayerColors(number_of_layers, layer)
  pg.printLegendForMaterialColors(number_of_materials, material)
  pg.showPlot()


# write to the VABS input file
print "STATUS: writing the VABS input file"
import VABSutilities as vu
VABSflag_dictionary = {'format_flag': 1,
                       'nlayer': number_of_layers,
                       'Timoshenko_flag': 1,
                       'recover_flag': 0,
                       'thermal_flag': 0,
                       'curve_flag': curved,
                       'oblique_flag': 0,
                       'trapeze_flag': 0,
                       'Vlasov_flag': 0,
                       'k1': twist,
                       'k2': 0.0,
                       'k3': 0.0,
                       'nnode': number_of_nodes,
                       'nelem': number_of_elements,
                       'nmate': number_of_materials}
                       # package all the VABS flags into one dictionary
vu.writeVABSfile(vabs_filename, unique_node, layer, material, element, VABSflag_dictionary)


print "STATUS: done!!"