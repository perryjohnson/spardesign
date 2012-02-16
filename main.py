"""
Description:  (last updated Februrary 2, 2012)
This program is a preprocessor for VABS (a cross-sectional analysis code maintained by Prof. Wenbin Yu at Utah State University).
Given the geometry and layup for a wind turbine spar (autogridgen/monoplane_spar_layup.txt), this program will:
    (1) make VABS objects (materials, layers, nodes, & elements)
    (2) plots the grid (and grid lines) to the screen with Mayavi
    (3) writes the VABS input file (spar_station_xx.dat)
    (4) runs VABS on the input file to calculate the mass and stiffness matrices (spar_station_xx.dat.K)
This program currently only runs spar stations 7-24, which are made of two shear webs and two spar caps
Spar stations 1-6 also includes two root buildup regions, which are not handled by this program yet.

Author:
Perry Johnson (perryjohnson@ucla.edu)
"""

import time

# record the time when the code starts
start_time = time.time()

import autogridgen.VABSobjects as vo
import autogridgen.read_layup as rl
import autogridgen.triQuadGrid as tqg
import numpy as np
import autogridgen.cartGrid as cg

# plotting flags #
plot_flag = False            # show the plot in mayavi?
gridlines_flag = True       # plot gridlines between the nodes?
zoom_flag = False           # set the view to the shear web/spar cap interface?
axes_flag = False            # show the axes on the plot?

# debugging flags #
main_debug_flag = False     # print extra debugging information to the screen?

# VABS flags #
writeVABS_flag = True       # write the VABS input file to disk?
runVABS_flag = True         # run VABS to calculate the mass and stiffness matrices?

# spar stations #
spar_file = 'autogridgen/monoplane_spar_layup.txt'
# spar_stn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # generate grids for these spar stations
# spar_stn_list = [1, 2, 3, 4, 5, 6]  # generate grids for these spar stations (subset)
spar_stn_list = [6]  # generate grids for these spar stations (subset)

# aspect ratio settings #
maxAR_master = 5.0
maxAR_uniax = 1.3
maxAR_biax  = maxAR_master # 3.5  # according to PreVABS, the cell aspect ratio is usually set from 3.0-maxAR_master ... maybe 1.2 is too small (high mem usage!)
maxAR_triax = 1.3
maxAR_foam  = 1.3

# import the data from the layup file
print 'STATUS: importing spar layup file: ' + spar_file + '  ...'
data = rl.readLayupFile(spar_file)

## set number of plies for each structural component ##
SC_plies = 2       # spar cap has 2 plies:                      [0]_2
RB_plies = 6       # root buildup has 6 plies:                  [+/-45]_2 [0]_2
SW_biax_plies = 8  # biaxial laminate in shear web has 8 plies: [+/-45]_4
SW_foam_plies = 30  # set the foam part of the shear web to some arbitrary number (the foam doesn't really have plies)




##### run this block of code for each spar station #####
for i in range(len(spar_stn_list)):
    stn_start_time = time.time()
    spar_stn = spar_stn_list[i]
    if spar_stn > 9:
        vabs_filename = 'spar_station_' + str(spar_stn) + '.dat'
    else:
        vabs_filename = 'spar_station_0' + str(spar_stn) + '.dat'
    print '********************************'
    print 'RUNNING SPAR STATION #' + str(spar_stn)
    print '********************************'
    print 'vabs filename = ', vabs_filename
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


    ################################################################################################################################################
    # create VABS objects for nodes and elements for the entire cross-section ############################################################################################
    print "STATUS: create VABS nodes and elements for the ENTIRE CROSS-SECTION..."

    # determine if root buildup exists for this cross-section
    root_buildup_height = rl.extractDataColumn(data,'root buildup height')[spar_stn-1]
    if root_buildup_height > 0.0:   # if the root buildup exists, set RB_flag to True, and EXECUTE root buildup-related operations
        RB_flag = True
    else:                           # otherwise, set RB_flag to False, and SKIP root buildup-related operations
        RB_flag = False
    
    if main_debug_flag:
        print "  root buildup height = " + str(root_buildup_height)
        print "  RB_flag = " + str(RB_flag)
    

    node = []
    element = []
    region = []
    number_of_nodes = 0
    number_of_elements = 0
    number_of_regions = 0

    

    # pull the corners of the shear webs and spar caps from the layup file that was read earlier
    SW_corners = rl.extract_SW_corners(data,spar_stn)
    SC_corners = rl.extract_SC_corners(data,spar_stn)
    if RB_flag:
        RB_corners = rl.extract_RB_corners(data,spar_stn)

    # fill index 0 of node, element, and region lists (index 0 is unused)
    (node, element, region) = tqg.fillUnusedZeroIndex(node, element, region)

    # fill in regions
    if RB_flag:
        total_regions = 10
    else:
        total_regions = 8
    for i in range(1,total_regions+1):
        (number_of_regions, region) = tqg.createNewRegion(number_of_regions, region)
    


    # *regions*
    # -cornerNodes-         (nodes marked "??" will be assigned later)
    #
    # 20--------------------------------------------------------------19
    # |::::::::::::::::::::::::::::::*10*::::::::::::::::::::::::::::::|
    # 04--03------08--07------------------------------12--11------16--15
    # |~~~~|......|~~~~|+++++++++++++*8*++++++++++++++|~~~~|......|~~~~|
    # |~~~~|......|~~~??------------------------------??~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |*1*~|.*2*..|*3*~|                              |*4*~|.*5*..|*6*~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~??------------------------------??~~~|......|~~~~|
    # |~~~~|......|~~~~|+++++++++++++*7*++++++++++++++|~~~~|......|~~~~|
    # 01--02------05--06------------------------------09--10------13--14
    # |::::::::::::::::::::::::::::::*9*:::::::::::::::::::::::::::::::|
    # 17--------------------------------------------------------------18



    # name regions
    region[1].name = 'left shear web, left biax laminate'
    region[2].name = 'left shear web, foam core'
    region[3].name = 'left shear web, right biax laminate'
    region[4].name = 'right shear web, left biax laminate'
    region[5].name = 'right shear web, foam core'
    region[6].name = 'right shear web, right biax laminate'
    region[7].name = 'bottom spar cap'
    region[8].name = 'top spar cap'
    if RB_flag:
        region[9].name = 'bottom root buildup'
        region[10].name = 'top root buildup'

    # make a dictionary mapping region.name entries to region.region_no entries
    rDict = {}
    for i in range(1,total_regions+1):
        rDict[region[i].name] = region[i].region_no

    

    ################################################################################################################################################
    # create in nodes at region corners
    print "STATUS: create nodes at region corners..."
    if RB_flag:
        cornerNodes_to_create = 20
    else:
        cornerNodes_to_create = 16
    for i in range(1,cornerNodes_to_create+1):
        (number_of_nodes, node) = tqg.createNewNode(number_of_nodes, node)


    ## left shear web ###########################################################  SW_corners[0,:,:,:]
    print "  - left shear web:      nodes 1-8"
    # left biax laminate #  SW_corners[0,0,:,:]
    (node[1].x2, node[1].x3) = (SW_corners[0,0,2,0], SW_corners[0,0,2,1])  # this is also cornerNode4 (top left corner) for the bottom root buildup (region[9])
    (node[2].x2, node[2].x3) = (SW_corners[0,0,3,0], SW_corners[0,0,3,1])
    (node[3].x2, node[3].x3) = (SW_corners[0,0,1,0], SW_corners[0,0,1,1])
    (node[4].x2, node[4].x3) = (SW_corners[0,0,0,0], SW_corners[0,0,0,1])  # this is also cornerNode1 (bottom left corner) for the top root buildup (region[10])

    # right biax laminate #  SW_corners[0,2,:,:]
    (node[5].x2, node[5].x3) = (SW_corners[0,2,2,0], SW_corners[0,2,2,1])
    (node[6].x2, node[6].x3) = (SW_corners[0,2,3,0], SW_corners[0,2,3,1])  # this is also cornerNode1 (bottom left corner) for the bottom spar cap (region[7])
    (node[7].x2, node[7].x3) = (SW_corners[0,2,1,0], SW_corners[0,2,1,1])  # this is also cornerNode4 (top left corner) for the top spar cap (region[8])
    (node[8].x2, node[8].x3) = (SW_corners[0,2,0,0], SW_corners[0,2,0,1])

    ## right shear web ###########################################################  SW_corners[1,:,:,:]
    print "  - right shear web:     nodes 9-16"
    # left biax laminate #  SW_corners[1,0,:,:]
    (node[9].x2,  node[9].x3)  = (SW_corners[1,0,2,0], SW_corners[1,0,2,1])  # this is also cornerNode2 (bottom left corner) for the bottom spar cap (region[7])
    (node[10].x2, node[10].x3) = (SW_corners[1,0,3,0], SW_corners[1,0,3,1])
    (node[11].x2, node[11].x3) = (SW_corners[1,0,1,0], SW_corners[1,0,1,1])
    (node[12].x2, node[12].x3) = (SW_corners[1,0,0,0], SW_corners[1,0,0,1])  # this is also cornerNode3 (top right corner) for the top spar cap (region[8])

    # right biax laminate #  SW_corners[1,2,:,:]
    (node[13].x2, node[13].x3) = (SW_corners[1,2,2,0], SW_corners[1,2,2,1])
    (node[14].x2, node[14].x3) = (SW_corners[1,2,3,0], SW_corners[1,2,3,1])  # this is also cornerNode3 (top right corner) for the bottom root buildup (region[9])
    (node[15].x2, node[15].x3) = (SW_corners[1,2,1,0], SW_corners[1,2,1,1])  # this is also cornerNode2 (bottom right corner) for the top root buildup (region[10])
    (node[16].x2, node[16].x3) = (SW_corners[1,2,0,0], SW_corners[1,2,0,1])

    if RB_flag:
        ## bottom root buildup #######################################################  RB_corners[1,:,:]
        print "  - bottom root buildup: nodes 17-18"
        (node[17].x2, node[17].x3) = (RB_corners[1,2,0], RB_corners[1,2,1])
        (node[18].x2, node[18].x3) = (RB_corners[1,3,0], RB_corners[1,3,1])

        ## top root buildup ##########################################################  RB_corners[0,:,:]
        print "  - top root buildup:    nodes 19-20"
        (node[19].x2, node[19].x3) = (RB_corners[0,1,0], RB_corners[0,1,1])
        (node[20].x2, node[20].x3) = (RB_corners[0,0,0], RB_corners[0,0,1])

    

    # *regions*
    # -cornerNodes-         (nodes marked "??" will be assigned later)
    #
    # 20--------------------------------------------------------------19
    # |::::::::::::::::::::::::::::::*10*::::::::::::::::::::::::::::::|
    # 04--03------08--07------------------------------12--11------16--15
    # |~~~~|......|~~~~|+++++++++++++*8*++++++++++++++|~~~~|......|~~~~|
    # |~~~~|......|~~~??------------------------------??~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |*1*~|.*2*..|*3*~|                              |*4*~|.*5*..|*6*~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~~|                              |~~~~|......|~~~~|
    # |~~~~|......|~~~??------------------------------??~~~|......|~~~~|
    # |~~~~|......|~~~~|+++++++++++++*7*++++++++++++++|~~~~|......|~~~~|
    # 01--02------05--06------------------------------09--10------13--14
    # |::::::::::::::::::::::::::::::*9*:::::::::::::::::::::::::::::::|
    # 17--------------------------------------------------------------18



    ################################################################################################################################################
    # assign corner nodes to each region
    print "STATUS: assign corner nodes to each region"
    (region[rDict['left shear web, left biax laminate']].cornerNode1,
     region[rDict['left shear web, left biax laminate']].cornerNode2,
     region[rDict['left shear web, left biax laminate']].cornerNode3,
     region[rDict['left shear web, left biax laminate']].cornerNode4) = (node[1], node[2], node[3], node[4])
    (region[rDict['left shear web, foam core']].cornerNode1,
     region[rDict['left shear web, foam core']].cornerNode2,
     region[rDict['left shear web, foam core']].cornerNode3,
     region[rDict['left shear web, foam core']].cornerNode4) = (node[2], node[5], node[8], node[3])
    (region[rDict['left shear web, right biax laminate']].cornerNode1,
     region[rDict['left shear web, right biax laminate']].cornerNode2,
     region[rDict['left shear web, right biax laminate']].cornerNode3,
     region[rDict['left shear web, right biax laminate']].cornerNode4) = (node[5], node[6], node[7], node[8])
    (region[rDict['right shear web, left biax laminate']].cornerNode1,
     region[rDict['right shear web, left biax laminate']].cornerNode2,
     region[rDict['right shear web, left biax laminate']].cornerNode3,
     region[rDict['right shear web, left biax laminate']].cornerNode4) = (node[9], node[10], node[11], node[12])
    (region[rDict['right shear web, foam core']].cornerNode1,
     region[rDict['right shear web, foam core']].cornerNode2,
     region[rDict['right shear web, foam core']].cornerNode3,
     region[rDict['right shear web, foam core']].cornerNode4) = (node[10], node[13], node[16], node[11])
    (region[rDict['right shear web, right biax laminate']].cornerNode1,
     region[rDict['right shear web, right biax laminate']].cornerNode2,
     region[rDict['right shear web, right biax laminate']].cornerNode3,
     region[rDict['right shear web, right biax laminate']].cornerNode4) = (node[13], node[14], node[15], node[16])
    (region[rDict['bottom spar cap']].cornerNode1,
     region[rDict['bottom spar cap']].cornerNode2) = (node[6], node[9])  # cornerNode3 and cornerNode4 will be assigned later
    (region[rDict['top spar cap']].cornerNode3,
     region[rDict['top spar cap']].cornerNode4) = (node[12], node[7])  # cornerNode1 and cornerNode2 will be assigned later
    if RB_flag:
        (region[rDict['bottom root buildup']].cornerNode1,
         region[rDict['bottom root buildup']].cornerNode2,
         region[rDict['bottom root buildup']].cornerNode3,
         region[rDict['bottom root buildup']].cornerNode4) = (node[17], node[18], node[14], node[1])
        (region[rDict['top root buildup']].cornerNode1,
         region[rDict['top root buildup']].cornerNode2,
         region[rDict['top root buildup']].cornerNode3,
         region[rDict['top root buildup']].cornerNode4) = (node[4], node[15], node[19], node[20])





    ################################################################################################################################################
    # assign number of cells distributed along horizontal and vertical axes
    print "STATUS: assign number of cells distributed along horizontal and vertical axes"

    print "  - left shear web"
    # left shear web, left biax laminate ############## SW_corners[0,0,:,:]
    (dimH,dimV) = cg.calcCornerDims(SW_corners[0,0,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR_biax,dimV)
    (region[rDict['left shear web, left biax laminate']].V_cells, region[rDict['left shear web, left biax laminate']].H_cells) = (nV,nH)
    # left shear web, foam core ############## SW_corners[0,1,:,:]
    (dimH,dimV) = cg.calcCornerDims(SW_corners[0,1,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_foam_plies,maxAR_foam,dimV)
    (region[rDict['left shear web, foam core']].V_cells, region[rDict['left shear web, foam core']].H_cells) = (nV,nH)
    # left shear web, right biax laminate ############## SW_corners[0,2,:,:]
    (dimH,dimV) = cg.calcCornerDims(SW_corners[0,2,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR_biax,dimV)
    (region[rDict['left shear web, right biax laminate']].V_cells, region[rDict['left shear web, right biax laminate']].H_cells) = (nV,nH)

    print "  - right shear web"
    # right shear web, left biax laminate ############## SW_corners[1,0,:,:]
    (dimH,dimV) = cg.calcCornerDims(SW_corners[1,0,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR_biax,dimV)
    (region[rDict['right shear web, left biax laminate']].V_cells, region[rDict['right shear web, left biax laminate']].H_cells) = (nV,nH)
    # right shear web, foam core ############## SW_corners[1,1,:,:]
    (dimH,dimV) = cg.calcCornerDims(SW_corners[1,1,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_foam_plies,maxAR_foam,dimV)
    (region[rDict['right shear web, foam core']].V_cells, region[rDict['right shear web, foam core']].H_cells) = (nV,nH)
    # right shear web, right biax laminate ############## SW_corners[1,2,:,:]
    (dimH,dimV) = cg.calcCornerDims(SW_corners[1,2,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR_biax,dimV)
    (region[rDict['right shear web, right biax laminate']].V_cells, region[rDict['right shear web, right biax laminate']].H_cells) = (nV,nH)

    print "  - bottom spar cap"
    # bottom spar cap ############## SC_corners[1,:,:]
    (dimH,dimV) = cg.calcCornerDims(SC_corners[1,:,:])
    (nV,nH) = cg.calcCellNums(dimV,SC_plies,maxAR_uniax,dimH)
    (region[rDict['bottom spar cap']].V_cells, region[rDict['bottom spar cap']].H_cells) = (nV,nH)

    print "  - top spar cap"
    # top spar cap ############## SC_corners[0,:,:]
    (dimH,dimV) = cg.calcCornerDims(SC_corners[0,:,:])
    (nV,nH) = cg.calcCellNums(dimV,SC_plies,maxAR_uniax,dimH)
    (region[rDict['top spar cap']].V_cells, region[rDict['top spar cap']].H_cells) = (nV,nH)

    if RB_flag:
        print "  - bottom root buildup"
        # bottom root buildup ##############  RB_corners[1,:,:]
        (dimH,dimV) = cg.calcCornerDims(RB_corners[1,:,:])
        (nV,nH) = cg.calcCellNums(dimV,RB_plies,maxAR_triax,dimH)
        (region[rDict['bottom root buildup']].V_cells, region[rDict['bottom root buildup']].H_cells) = (nV,nH)

        print "  - top root buildup"
        # top root buildup ##############  RB_corners[0,:,:]
        (dimH,dimV) = cg.calcCornerDims(RB_corners[0,:,:])
        (nV,nH) = cg.calcCellNums(dimV,RB_plies,maxAR_triax,dimH)
        (region[rDict['top root buildup']].V_cells, region[rDict['top root buildup']].H_cells) = (nV,nH)




    ################################################################################################################################################
    # make control nodes at shear web ply boundaries
    print "STATUS: make control nodes at shear web ply boundaries"
    # region 1 ################### (left shear web, left biax laminate)
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, left biax laminate'], node, number_of_nodes, 'bottom')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, left biax laminate'], node, number_of_nodes, 'top')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, left biax laminate'], node, number_of_nodes, 'left')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, left biax laminate'], node, number_of_nodes, 'right')

    # region 3 ################### (left shear web, right biax laminate)
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, right biax laminate'], node, number_of_nodes, 'bottom')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, right biax laminate'], node, number_of_nodes, 'top')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, right biax laminate'], node, number_of_nodes, 'left')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, right biax laminate'], node, number_of_nodes, 'right')

    # region 2 ################### (left shear web, foam core)
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, foam core'], node, number_of_nodes, 'bottom')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['left shear web, foam core'], node, number_of_nodes, 'top')
    region[rDict['left shear web, foam core']].edgeL = region[rDict['left shear web, left biax laminate']].edgeR
    region[rDict['left shear web, foam core']].edgeR = region[rDict['left shear web, right biax laminate']].edgeL


    # region 4 ################### (right shear web, left biax laminate)
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, left biax laminate'], node, number_of_nodes, 'bottom')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, left biax laminate'], node, number_of_nodes, 'top')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, left biax laminate'], node, number_of_nodes, 'left')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, left biax laminate'], node, number_of_nodes, 'right')

    # region 6 ################### (right shear web, right biax laminate)
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, right biax laminate'], node, number_of_nodes, 'bottom')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, right biax laminate'], node, number_of_nodes, 'top')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, right biax laminate'], node, number_of_nodes, 'left')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, right biax laminate'], node, number_of_nodes, 'right')

    # region 5 ################### (right shear web, foam core)
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, foam core'], node, number_of_nodes, 'bottom')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['right shear web, foam core'], node, number_of_nodes, 'top')
    region[rDict['right shear web, foam core']].edgeL = region[rDict['right shear web, left biax laminate']].edgeR
    region[rDict['right shear web, foam core']].edgeR = region[rDict['right shear web, right biax laminate']].edgeL















    ################################################################################################################################################
    # fill shear web regions with interior elements
    print "STATUS: fill shear web regions with interior elements"
    # # fill region 1 (left shear web, left biax laminate)
    # (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['left shear web, left biax laminate'],region,
    #                                                                                  number_of_elements,element,
    #                                                                                  number_of_nodes,node)

    # # fill region 2 (left shear web, foam core)
    # (number_of_elements,element,
    #  number_of_nodes,node,
    # coarseEdgeL,coarseEdgeR) = tqg.fillBoundaryTriElements(rDict['left shear web, foam core'],region,
    #                                                        number_of_elements,element,
    #                                                        number_of_nodes,node)
    # (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['left shear web, foam core'],region,
    #                                                        number_of_elements,element,
    #                                                        number_of_nodes,node,
    #                                                        coarse_flag=True,
    #                                                        temp_coarseEdgeL=coarseEdgeL,temp_coarseEdgeR=coarseEdgeR)

    # # fill region 3 (left shear web, right biax laminate)
    # (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['left shear web, right biax laminate'],region,
    #                                                                                  number_of_elements,element,
    #                                                                                  number_of_nodes,node)

    # # # assign all elements to layer 1, and set theta1 = 90.0 (left shear web)
    # # start_elem = 1
    # # for i in range(start_elem, number_of_elements+1):
    # #     element[i].layer = layer[1]
    # #     element[i].theta1 = 90.0
    # # start_elem = number_of_elements+1



    # fill region 4 (right shear web, left biax laminate)
    (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['right shear web, left biax laminate'],region,
                                                                                     number_of_elements,element,
                                                                                     number_of_nodes,node)

    # fill region 5 (right shear web, foam core)
    (number_of_elements,element,
     number_of_nodes,node,
    coarseEdgeL,coarseEdgeR) = tqg.fillBoundaryTriElements(rDict['right shear web, foam core'],region,
                                                           number_of_elements,element,
                                                           number_of_nodes,node)
    (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['right shear web, foam core'],region,
                                                           number_of_elements,element,
                                                           number_of_nodes,node,
                                                           coarse_flag=True,
                                                           temp_coarseEdgeL=coarseEdgeL,temp_coarseEdgeR=coarseEdgeR)

    # fill region 6 (right shear web, right biax laminate)
    (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['right shear web, right biax laminate'],region,
                                                                                     number_of_elements,element,
                                                                                     number_of_nodes,node)

    # # assign all elements to layer 1, and set theta1 = 270.0 (right shear web)
    # for i in range(start_elem, number_of_elements+1):
    #     element[i].layer = layer[1]
    #     element[i].theta1 = 270.0
    # start_elem = number_of_elements+1









    # fill region 1 (left shear web, left biax laminate)
    (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['left shear web, left biax laminate'],region,
                                                                                     number_of_elements,element,
                                                                                     number_of_nodes,node)

    # fill region 2 (left shear web, foam core)
    (number_of_elements,element,
     number_of_nodes,node,
    coarseEdgeL,coarseEdgeR) = tqg.fillBoundaryTriElements(rDict['left shear web, foam core'],region,
                                                           number_of_elements,element,
                                                           number_of_nodes,node)
    (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['left shear web, foam core'],region,
                                                           number_of_elements,element,
                                                           number_of_nodes,node,
                                                           coarse_flag=True,
                                                           temp_coarseEdgeL=coarseEdgeL,temp_coarseEdgeR=coarseEdgeR)

    # fill region 3 (left shear web, right biax laminate)
    (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['left shear web, right biax laminate'],region,
                                                                                     number_of_elements,element,
                                                                                     number_of_nodes,node)

    # # assign all elements to layer 1, and set theta1 = 90.0 (left shear web)
    # start_elem = 1
    # for i in range(start_elem, number_of_elements+1):
    #     element[i].layer = layer[1]
    #     element[i].theta1 = 90.0
    # start_elem = number_of_elements+1







    ################################################################################################################################################
    # make control nodes at spar cap ply boundaries
    print "STATUS: make control nodes at spar cap ply boundaries"
    ## BOTTOM SPAR CAP ##
    SC_top_x3 = SC_corners[1,0,1]
    SC_bottom_x3 = SC_corners[1,2,1]
    SC_middle_x3 = SC_bottom_x3 + abs(SC_top_x3 - SC_bottom_x3)/SC_plies
    ### edit the right edge of the left shear web (right biax laminate) to match the ply thicknesses of the bottom spar cap
    n = 0
    while region[rDict['left shear web, right biax laminate']].edgeR[n].x3 < SC_middle_x3:
        n += 1
    region[rDict['left shear web, right biax laminate']].edgeR[n].x3 = SC_middle_x3  # reassign the x3 value, to align the shear web gridpoint with the adjacent spar cap plies
    while region[rDict['left shear web, right biax laminate']].edgeR[n].x3 < SC_top_x3:
        n += 1
    region[rDict['left shear web, right biax laminate']].edgeR[n].x3 = SC_top_x3
    ### assign the left edge of the bottom spar cap to a subset of the right edge of the left shear web (right biax laminate)
    region[rDict['bottom spar cap']].edgeL = region[rDict['left shear web, right biax laminate']].edgeR[:n+1]
    region[rDict['bottom spar cap']].cornerNode4 = region[rDict['bottom spar cap']].edgeL[-1]

    ### edit the left edge of the right shear web (left biax laminate) to match the ply thicknesses of the bottom spar cap
    n = 0
    while region[rDict['right shear web, left biax laminate']].edgeL[n].x3 < SC_middle_x3:
        n += 1
    region[rDict['right shear web, left biax laminate']].edgeL[n].x3 = SC_middle_x3  # reassign the x3 value, to align the shear web gridpoint with the adjacent spar cap plies
    while region[rDict['right shear web, left biax laminate']].edgeL[n].x3 < SC_top_x3:
        n += 1
    region[rDict['right shear web, left biax laminate']].edgeL[n].x3 = SC_top_x3
    ### assign the right edge of the bottom spar cap to a subset of the left edge of the right shear web (left biax laminate)
    region[rDict['bottom spar cap']].edgeR = region[rDict['right shear web, left biax laminate']].edgeL[:n+1]
    region[rDict['bottom spar cap']].cornerNode3 = region[rDict['bottom spar cap']].edgeR[-1]

    ### assign the top and bottom edges (as usual)
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['bottom spar cap'], node, number_of_nodes, 'top')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['bottom spar cap'], node, number_of_nodes, 'bottom')


    ## TOP SPAR CAP ##
    SC_top_x3 = SC_corners[0,0,1]
    SC_bottom_x3 = SC_corners[0,2,1]
    SC_middle_x3 = SC_bottom_x3 + abs(SC_top_x3 - SC_bottom_x3)/SC_plies
    ### edit the right edge of left shear web (right biax laminate) to match the ply thicknesses of the top spar cap
    n = -1
    while region[rDict['left shear web, right biax laminate']].edgeR[n].x3 > SC_middle_x3:
        n -= 1
    region[rDict['left shear web, right biax laminate']].edgeR[n].x3 = SC_middle_x3  # reassign the x3 value, to align the shear web gridpoint with the adjacent spar cap plies
    while region[rDict['left shear web, right biax laminate']].edgeR[n].x3 > SC_bottom_x3:
        n -= 1
    region[rDict['left shear web, right biax laminate']].edgeR[n].x3 = SC_bottom_x3
    ### assign the left edge of the top spar cap to a subset of the right edge of the left shear web (right biax laminate)
    region[rDict['top spar cap']].edgeL = region[rDict['left shear web, right biax laminate']].edgeR[n:]
    region[rDict['top spar cap']].cornerNode1 = region[rDict['top spar cap']].edgeL[0]

    # edit the left edge of the right shear web (left biax laminate) to match the ply thicknesses of the top spar cap
    n = -1
    while region[rDict['right shear web, left biax laminate']].edgeL[n].x3 > SC_middle_x3:
        n -= 1
    region[rDict['right shear web, left biax laminate']].edgeL[n].x3 = SC_middle_x3  # reassign the x3 value, to align the shear web gridpoint with the adjacent spar cap plies
    while region[rDict['right shear web, left biax laminate']].edgeL[n].x3 > SC_bottom_x3:
        n -= 1
    region[rDict['right shear web, left biax laminate']].edgeL[n].x3 = SC_bottom_x3
    ### assign the right edge of the top spar cap to a subset of the left edge of the right shear web (left biax laminate)
    region[rDict['top spar cap']].edgeR = region[rDict['right shear web, left biax laminate']].edgeL[n:]
    region[rDict['top spar cap']].cornerNode2 = region[rDict['top spar cap']].edgeR[0]

    # assign the top and bottom edges (as usual)
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['top spar cap'], node, number_of_nodes, 'top')
    (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['top spar cap'], node, number_of_nodes, 'bottom')







    ################################################################################################################################################
    # fill spar cap regions with interior elements
    print "STATUS: fill spar cap regions with interior elements"
    # fill region 7 (bottom spar cap)
    (number_of_elements,element,
     number_of_nodes,node,
     coarseEdgeL,coarseEdgeR) = tqg.fillBoundaryTriElements(rDict['bottom spar cap'],region,
                                                            number_of_elements,element,
                                                            number_of_nodes,node,
                                                            debug_flag=False)
    (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['bottom spar cap'],region,
                                                            number_of_elements,element,
                                                            number_of_nodes,node,
                                                            coarse_flag=True,
                                                            temp_coarseEdgeL=coarseEdgeL,temp_coarseEdgeR=coarseEdgeR)

    # # assign all elements to layer 2, and set theta1 = 180.0 (bottom spar cap)
    # for i in range(start_elem, number_of_elements+1):
    #     element[i].layer = layer[2]
    #     element[i].theta1 = 180.0
    # start_elem = number_of_elements+1



    # fill region 8 (top spar cap)
    (number_of_elements,element,
     number_of_nodes,node,
     coarseEdgeL,coarseEdgeR) = tqg.fillBoundaryTriElements(rDict['top spar cap'],region,
                                                            number_of_elements,element,
                                                            number_of_nodes,node,
                                                            debug_flag=False)
    (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['top spar cap'],region,
                                                            number_of_elements,element,
                                                            number_of_nodes,node,
                                                            coarse_flag=True,
                                                            temp_coarseEdgeL=coarseEdgeL,temp_coarseEdgeR=coarseEdgeR)

    # # assign all elements to layer 2, and set theta1 = 0.0 (top spar cap)
    # for i in range(start_elem, number_of_elements+1):
    #     element[i].layer = layer[2]
    #     element[i].theta1 = 0.0
    # start_elem = number_of_elements+1



    if RB_flag:
        ################################################################################################################################################
        # make control nodes at root buildup ply boundaries
        print "STATUS: make control nodes at root buildup ply boundaries"
        ## BOTTOM ROOT BUILDUP ##
        ### assign the left, bottom, and right edges (as usual)
        (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['bottom root buildup'], node, number_of_nodes, 'left')
        (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['bottom root buildup'], node, number_of_nodes, 'bottom')
        (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['bottom root buildup'], node, number_of_nodes, 'right')
        ### construct the top edge of the bottom root buildup from the bottom edges of the adjacent spar cap and shear webs
        region[rDict['bottom root buildup']].edgeT = (region[rDict['left shear web, left biax laminate']].edgeB +
                                                      region[rDict['left shear web, foam core']].edgeB[1:] +
                                                      region[rDict['left shear web, right biax laminate']].edgeB[1:] +
                                                      region[rDict['bottom spar cap']].edgeB[1:] +
                                                      region[rDict['right shear web, left biax laminate']].edgeB[1:] +
                                                      region[rDict['right shear web, foam core']].edgeB[1:] +
                                                      region[rDict['right shear web, right biax laminate']].edgeB[1:])
        

        ## TOP ROOT BUILDUP ##
        ### assign the left, top, and right edges (as usual)
        (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['top root buildup'], node, number_of_nodes, 'left')
        (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['top root buildup'], node, number_of_nodes, 'top')
        (region, node, number_of_nodes) = tqg.makeEdgeNodes(region, rDict['top root buildup'], node, number_of_nodes, 'right')
        ### construct the bottom edge of the top root buildup from the top edges of the adjacent spar cap and shear webs
        region[rDict['top root buildup']].edgeB = (region[rDict['left shear web, left biax laminate']].edgeT +
                                                   region[rDict['left shear web, foam core']].edgeT[1:] +
                                                   region[rDict['left shear web, right biax laminate']].edgeT[1:] +
                                                   region[rDict['top spar cap']].edgeT[1:] +
                                                   region[rDict['right shear web, left biax laminate']].edgeT[1:] +
                                                   region[rDict['right shear web, foam core']].edgeT[1:] +
                                                   region[rDict['right shear web, right biax laminate']].edgeT[1:])
        


        # if main_debug_flag:
        #     tqg.inspectRegion(region[rDict['bottom root buildup']])
        #     tqg.inspectRegion(region[rDict['top root buildup']])



        ################################################################################################################################################
        # fill root buildup regions with interior elements
        print "STATUS: fill root buildup regions with interior elements"
        
        # fill bottom root buildup region
        (number_of_elements,element,
         number_of_nodes,node,
         coarseEdgeT) = tqg.fillBoundaryTriElements_bottomRB(rDict['bottom root buildup'],region,
                                                             number_of_elements,element,
                                                             number_of_nodes,node,debug_flag=False)

        (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['bottom root buildup'],region,
                                                               number_of_elements,element,
                                                               number_of_nodes,node,
                                                               bottom_RB_coarse_flag=True,
                                                               temp_coarseEdgeT=coarseEdgeT)
        # # assign all elements to layer 3, and set theta1 = 180.0 (bottom root buildup)
        # for i in range(start_elem, number_of_elements+1):
        #     element[i].layer = layer[3]
        #     element[i].theta1 = 180.0
        # start_elem = number_of_elements+1


        # fill top root buildup region
        (number_of_elements,element,
         number_of_nodes,node,
         coarseEdgeB) = tqg.fillBoundaryTriElements_topRB(rDict['top root buildup'],region,
                                                          number_of_elements,element,
                                                          number_of_nodes,node,debug_flag=False)

        (number_of_elements,element,number_of_nodes,node) = tqg.fillInteriorQuadElements(rDict['top root buildup'],region,
                                                               number_of_elements,element,
                                                               number_of_nodes,node,
                                                               coarse_flag=False,bottom_RB_coarse_flag=False,
                                                               top_RB_coarse_flag=True,
                                                               temp_coarseEdgeB=coarseEdgeB)
        # # assign all elements to layer 3, and set theta1 = 0.0 (top root buildup)
        # for i in range(start_elem, number_of_elements+1):
        #     element[i].layer = layer[3]
        #     element[i].theta1 = 0.0
        # start_elem = number_of_elements+1





















    # assign all elements to layer 1, and set theta1 = 0.0 (just to test if VABS runs)
    for i in range(1, number_of_elements+1):
        element[i].layer = layer[1]
        element[i].theta1 = 0.0













    




    # verify that input was saved correctly
    if main_debug_flag:
        print "REGIONS:"
        for i in range(1,number_of_regions+1):
            print ('  #' + str(region[i].region_no) + '  (' + str(region[i].cornerNode1.node_no) + ', '
                                                            + str(region[i].cornerNode2.node_no) + ', '
                                                            + str(region[i].cornerNode3.node_no) + ', '
                                                            + str(region[i].cornerNode4.node_no) + ')' )


    if plot_flag:   # plot the grid to the screen using mayavi
        ###########################################################################################################################
        print "STATUS: plot the grid to the screen using mayavi"
        # import the required plotting modules #
        from mayavi import mlab
        import autogridgen.gridViz as gv

        if gridlines_flag:  # print nodes with element lines
            ########################################################################################################################
            # write the element connectivity in a way that Mayavi can understand and plot
            print "STATUS: write the element connectivity for Mayavi"
            conn = tqg.buildConnections(element,number_of_elements)
            tqg.plotNodes(node, number_of_nodes, line_flag=True, connections=conn, circle_scale='0.0002', figure_num=spar_stn)  
        else:
            tqg.plotNodes(node, number_of_nodes, circle_scale='0.0005')  # print nodes without element lines
        
        if zoom_flag:
            tqg.nice2Dview(distance=0.183, focalpoint=np.array([-0.7736655 ,  2.34868712,  0.00626454]))  # zoomed view of shear web/spar cap interface
        else:
            tqg.nice2Dview()  # full view of cross-section
        
        if axes_flag:  # show the axes on the plot
            tqg.showAxes()



    # write to the VABS input file ###################################################################################################
    if writeVABS_flag:
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
                               'nnode': number_of_nodes,
                               'nelem': number_of_elements,
                               'nmate': number_of_materials}
                               # package all the VABS flags into one dictionary
        vu.writeVABSfile(vabs_filename, node, layer, material, element, VABSflag_dictionary)


    # calculate the time it took to run the code #####################################################################################################################
    elapsed_time_stn = time.time() - stn_start_time
    elapsed_min_stn = int(elapsed_time_stn/60)  # extract minutes elapsed
    elapsed_sec_stn = elapsed_time_stn % 60     # extract seconds elapsed
    print "spar station #" + str(spar_stn) + " completed in " + str(elapsed_min_stn) + ":" + ("%.2f" % round(elapsed_sec_stn,2)) + "  (min:sec)"

    if runVABS_flag:
        # run the input file with VABS from the Windows command line
        import os
        print ""
        print "RUNNING VABS....."
        vabs_command = r'.\VABS\VABSIII .\ '[:-1] + vabs_filename
        os.system(vabs_command)


# calculate the time it took to run the code #####################################################################################################################
elapsed_time_tot = time.time() - start_time
elapsed_min_tot = int(elapsed_time_tot/60)  # extract minutes elapsed
elapsed_sec_tot = elapsed_time_tot % 60     # extract seconds elapsed
print "program completed in " + str(elapsed_min_tot) + ":" + ("%.2f" % round(elapsed_sec_tot,2)) + "  (min:sec)"
