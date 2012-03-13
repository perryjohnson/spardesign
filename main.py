import time

# record the time when the code starts
start_time = time.time()

import os

main_debug_flag = False
runVABS_flag = True
delete_old_VABS_files = True

import truegrid.read_layup as rl
data = rl.readLayupFile('truegrid/biplane_spar_layup_20120312.txt')

spar_stn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # generate [M] and [K] matrices for these spar stations
# spar_stn_list = [15]  # generate [M] and [K] matrices for these spar stations (subset)

spar_stn_summary = []
for j in range(len(spar_stn_list)):
    spar_stn_summary.append(False)

for n in range(len(spar_stn_list)):
    spar_station = spar_stn_list[n]
    if spar_station < 10:
        basefilestr = 'spar_station_0' + str(spar_station)
    else:
        basefilestr = 'spar_station_' + str(spar_station)

    print ''
    print '***************'
    print basefilestr
    print '***************'

    ABAQUSfile = 'truegrid/' + basefilestr + '_abq.txt'
    vabs_filename = basefilestr + '.dat'

    if delete_old_VABS_files:
        if os.path.exists(basefilestr + '.dat'):
            os.remove(basefilestr + '.dat')
        if os.path.exists(basefilestr + '.dat.ech'):
            os.remove(basefilestr + '.dat.ech')
        if os.path.exists(basefilestr + '.dat.K'):
            os.remove(basefilestr + '.dat.K')
        if os.path.exists(basefilestr + '.dat.opt'):
            os.remove(basefilestr + '.dat.opt')
        if os.path.exists(basefilestr + '.dat.v0'):
            os.remove(basefilestr + '.dat.v0')
        if os.path.exists(basefilestr + '.dat.v1'):
            os.remove(basefilestr + '.dat.v1')
        if os.path.exists(basefilestr + '.dat.v1S'):
            os.remove(basefilestr + '.dat.v1S')

    # ----------------------------------------------------------------------------------

    stationData = rl.extractStationData(data,spar_station)
    if main_debug_flag:
        print stationData

    # ----------------------------------------------------------------------------------

    # parse the ABAQUS-formatted file
    import truegrid.ABAQUSutilities as au
    print "STATUS: interpret the ABAQUS file..."
    print "  " + ABAQUSfile
    (nodeArray, elemArray, esetArray, number_of_nodes, number_of_elements) = au.parseABAQUS(ABAQUSfile)

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
        print "  ***WARNING*** some elements were not reordered properly!"

    x1 = -0.836
    x2 = -0.833
    x3 = -0.753
    x4 = -0.750
    x5 = -x4
    x6 = -x3
    x7 = -x2
    x8 = -x1

    y5 = stationData['shear web height']/2.0
    y4 = y5-stationData['spar cap height']
    y6 = y5+stationData['root buildup height']
    y3 = -y4
    y2 = -y5
    y1 = -y6


    nan_flag = False
    for i in range(1,number_of_elements+1):
        if str(element[i].theta1) == 'nan':
            nan_flag = True
            (x,y) = element[i].middle()
            if x > x1 and x < x4 and y > y2 and y < y5:  # left shear web
                element[i].theta1 = 90.0
            elif x > x5 and x < x8 and y > y2 and y < y5:  # right shear web
                element[i].theta1 = 270.0
            elif x > x1 and x < x8 and y > y5 and y < y6: # top root buildup
                element[i].theta1 = 0.0
            elif x > x1 and x < x8 and y > y1 and y < y2: # bottom root buildup
                element[i].theta1 = 180.0
            elif x > x4 and x < x5 and y > y4 and y < y5: # top spar cap
                element[i].theta1 = 0.0
            elif x > x4 and x < x5 and y > y2 and y < y3: # bottom spar cap
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

    if vabs_OK and runVABS_flag:
        # run the input file with VABS from the Windows command line
        print ""
        print "RUNNING VABS....."
        vabs_command = r'.\VABS\VABSIII .\ '[:-1] + vabs_filename
        os.system(vabs_command)

    if os.path.exists(basefilestr + '.dat.K'):
        spar_stn_summary[n] = True

# ----------------------------------------------------------------------------------
# calculate the time it took to run the code
elapsed_time_tot = time.time() - start_time
elapsed_min_tot = int(elapsed_time_tot/60)  # extract minutes elapsed
elapsed_sec_tot = elapsed_time_tot % 60     # extract seconds elapsed
print ""
print "program completed in " + str(elapsed_min_tot) + ":" + ("%.2f" % round(elapsed_sec_tot,2)) + "  (min:sec)"
print ""
print "******************"
print "summary of results"
print "******************"
print "spar station     successful?"
print "------------     -----------"
for k in range(len(spar_stn_list)):
    print '     ' + ('%2d' % spar_stn_list[k]) + '             ' + str(spar_stn_summary[k])