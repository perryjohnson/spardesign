import time

# record the time when the code starts
start_time = time.time()

import autogridgen.genGrid as gg
import autogridgen.VABSobjects as vo
import autogridgen.read_layup as rl

fastflag = True
plot_grid_flag = True
plot_layer_flag = False
plot_material_flag = False
startrange = 23   # run the 23rd spar station
maxAR = 1.2
vabs_filename = 'test_input_file_SC.dat'


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


# create VABS objects for nodes and elements for each structural component #########################################################################################
print "STATUS: read input file..."

data = rl.readLayupFile('autogridgen/monoplane_spar_layup.txt')  # import the data from the layup file

## set number of plies for each structural component ##
SC_plies = 2       # spar cap has 2 plies:                      [0]_2
RB_plies = 6       # root buildup has 6 plies:                  [+/-45]_2 [0]_2
SW_biax_plies = 8  # biaxial laminate in shear web has 8 plies: [+/-45]_4
SW_foam_plies = 4  # set the foam part of the shear web to use 4 cells across its thickness (the foam doesn't really have plies)

if fastflag:
    endrange = startrange+1          # run for one cross-section only
else:
    endrange = len(data)+1         # run for all cross-sections

for spar_stn in range(startrange,endrange):
    # generate the grids ###########################################################################################################################################
    print ""
    print "STATUS: create VABS nodes and elements for COMPONENTS of spar station #" + str(spar_stn) + "..."
    print "        - maximum aspect ratio =", maxAR

    rtbldup_bse = rl.extractDataColumn(data,'root buildup base')
    rtbldup_ht  = rl.extractDataColumn(data,'root buildup height')
    plotRBflag = (rtbldup_bse[spar_stn-1] * rtbldup_ht[spar_stn-1] > 0.0)

    if plotRBflag:  # only perform operations for root buildup if its cross-sectional area is non-zero
        (RB_T_nodes, RB_T_elements, RB_T_number_of_nodes, RB_T_number_of_elements, RB_T_nodeMap, RB_T_elementMap, RB_T_x, RB_T_y,
         RB_B_nodes, RB_B_elements, RB_B_number_of_nodes, RB_B_number_of_elements, RB_B_nodeMap, RB_B_elementMap, RB_B_x, RB_B_y) = gg.genRootBuildup(data,spar_stn,RB_plies,maxAR)
    
    (SC_T_nodes, SC_T_elements, SC_T_number_of_nodes, SC_T_number_of_elements, SC_T_nodeMap, SC_T_elementMap, SC_T_x, SC_T_y,
     SC_B_nodes, SC_B_elements, SC_B_number_of_nodes, SC_B_number_of_elements, SC_B_nodeMap, SC_B_elementMap, SC_B_x, SC_B_y) = gg.genSparCaps(data,spar_stn,SC_plies,maxAR)
    
    (SW_L_biaxL_nodes, SW_L_biaxL_elements, SW_L_biaxL_number_of_nodes, SW_L_biaxL_number_of_elements, SW_L_biaxL_nodeMap, SW_L_biaxL_elementMap, SW_L_biaxL_x, SW_L_biaxL_y,
     SW_L_foam_nodes,  SW_L_foam_elements,  SW_L_foam_number_of_nodes,  SW_L_foam_number_of_elements,  SW_L_foam_nodeMap,  SW_L_foam_elementMap,  SW_L_foam_x,  SW_L_foam_y,
     SW_L_biaxR_nodes, SW_L_biaxR_elements, SW_L_biaxR_number_of_nodes, SW_L_biaxR_number_of_elements, SW_L_biaxR_nodeMap, SW_L_biaxR_elementMap, SW_L_biaxR_x, SW_L_biaxR_y,
     SW_R_biaxL_nodes, SW_R_biaxL_elements, SW_R_biaxL_number_of_nodes, SW_R_biaxL_number_of_elements, SW_R_biaxL_nodeMap, SW_R_biaxL_elementMap, SW_R_biaxL_x, SW_R_biaxL_y,
     SW_R_foam_nodes,  SW_R_foam_elements,  SW_R_foam_number_of_nodes,  SW_R_foam_number_of_elements,  SW_R_foam_nodeMap,  SW_R_foam_elementMap,  SW_R_foam_x,  SW_R_foam_y,
     SW_R_biaxR_nodes, SW_R_biaxR_elements, SW_R_biaxR_number_of_nodes, SW_R_biaxR_number_of_elements, SW_R_biaxR_nodeMap, SW_R_biaxR_elementMap, SW_R_biaxR_x, SW_R_biaxR_y) = gg.genShearWebs(data,spar_stn,SW_biax_plies,SW_foam_plies,maxAR)


    # define the layer (and material) for each element ###################################################################################################################
    print "STATUS: define the layer (and material) for each element"

    if plotRBflag:  # only perform operations for root buildup if its cross-sectional area is non-zero
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


    # create VABS objects for nodes and elements for the entire cross-section ############################################################################################
    print "STATUS: create VABS nodes and elements for the ENTIRE CROSS-SECTION..."

    ### CREATE NODES ###
    unique_node = []  # create an empty list of node objects
    # sum all the nodes for each structual component together
    if not plotRBflag:  # set number of nodes in root buildup to zero if it doesn't exist
        RB_T_number_of_nodes = 0
        RB_B_number_of_nodes = 0
    total_number_of_nodes = SC_T_number_of_nodes
    # total_number_of_nodes = (RB_T_number_of_nodes + RB_B_number_of_nodes +
    #                          SC_T_number_of_nodes + SC_B_number_of_nodes + 
    #                          SW_L_biaxL_number_of_nodes + SW_L_foam_number_of_nodes + SW_L_biaxR_number_of_nodes +
    #                          SW_R_biaxL_number_of_nodes + SW_R_foam_number_of_nodes + SW_R_biaxR_number_of_nodes)
    vo.fillNodeObjects(total_number_of_nodes, unique_node)


    ### CREATE ELEMENTS ###
    element = []      # create an empty list of element objects
    # sum all the elements for each structual component together
    if not plotRBflag:  # set number of elements in root buildup to zero if it doesn't exist
        RB_T_number_of_elements = 0
        RB_B_number_of_elements = 0
    total_number_of_elements = SC_T_number_of_elements
    # total_number_of_elements = (RB_T_number_of_elements + RB_B_number_of_elements +
    #                             SC_T_number_of_elements + SC_B_number_of_elements +
    #                             SW_L_biaxL_number_of_elements + SW_L_foam_number_of_elements + SW_L_biaxR_number_of_elements +
    #                             SW_R_biaxL_number_of_elements + SW_R_foam_number_of_elements + SW_R_biaxR_number_of_elements)
    vo.fillElementObjects(total_number_of_elements, element)


    # assign nodes and elements from each structural component to the entire cross-section ##########################################################################
    ### ASSIGN NODES ###
    i = 1                                            # initialize counter for the node number
    # if plotRBflag:  # only perform operations for root buildup if its cross-sectional area is non-zero
    #     for j in range(1,RB_T_number_of_nodes+1):
    #         unique_node[i] = RB_T_nodes[j]               # assign coordinates for top root buildup
    #         unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND RB_T_nodes[j] (b/c the previous line performs a shallow copy, not a deep copy)
    #         i = i+1                                      # increment counter for the node number
    #     for j in range(1,RB_B_number_of_nodes+1):
    #         unique_node[i] = RB_B_nodes[j]               # assign coordinatess for bottom root buildup
    #         unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND RB_B_nodes[j]
    #         i = i+1
    for j in range(1,SC_T_number_of_nodes+1):
        unique_node[i] = SC_T_nodes[j]               # assign coordinates for top spar cap
        unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SC_T_nodes[j]
        i = i+1
    # for j in range(1,SC_B_number_of_nodes+1):
    #     unique_node[i] = SC_B_nodes[j]               # assign coordinates for bottom spar cap
    #     unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SC_B_nodes[j]
    #     i = i+1
    # for j in range(1,SW_L_biaxL_number_of_nodes+1):
    #     unique_node[i] = SW_L_biaxL_nodes[j]         # assign coordinates for left shear web, left biax laminate
    #     unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_L_biaxL_nodes[j]
    #     i = i+1
    # for j in range(1,SW_L_foam_number_of_nodes+1):
    #     unique_node[i] = SW_L_foam_nodes[j]          # assign coordinates for left shear web, foam laminate
    #     unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_L_foam_nodes[j]
    #     i = i+1
    # for j in range(1,SW_L_biaxR_number_of_nodes+1):
    #     unique_node[i] = SW_L_biaxR_nodes[j]         # assign coordinates for left shear web, right biax laminate
    #     unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_L_biaxR_nodes[j]
    #     i = i+1
    # for j in range(1,SW_R_biaxL_number_of_nodes+1):
    #     unique_node[i] = SW_R_biaxL_nodes[j]         # assign coordinates for right shear web, left biax laminate
    #     unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_R_biaxL_nodes[j]
    #     i = i+1
    # for j in range(1,SW_R_foam_number_of_nodes+1):
    #     unique_node[i] = SW_R_foam_nodes[j]          # assign coordinates for right shear web, foam laminate
    #     unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_R_foam_nodes[j]
    #     i = i+1
    # for j in range(1,SW_R_biaxR_number_of_nodes+1):
    #     unique_node[i] = SW_R_biaxR_nodes[j]         # assign coordinates for right shear web, right biax laminate
    #     unique_node[i].node_no = i                   # overwrite node_no for unique_node[i] AND SW_R_biaxR_nodes[j]
    #     i = i+1


    ### ASSIGN ELEMENTS ###
    i = 1                                     # initialize counter for the element number
    # if plotRBflag:  # only perform operations for root buildup if its cross-sectional area is non-zero
    #     for j in range(1,RB_T_number_of_elements+1):
    #         element[i] = RB_T_elements[j]         # assign elements for top root buildup
    #         element[i].elem_no = i                # overwrite the element number
    #         i = i+1                               # increment counter for the element number
    #     for j in range(1,RB_B_number_of_elements+1):
    #         element[i] = RB_B_elements[j]         # assign elements for bottom root buildup
    #         element[i].elem_no = i                # overwrite the element number
    #         i = i+1
    for j in range(1,SC_T_number_of_elements+1):
        element[i] = SC_T_elements[j]         # assign elements for top spar cap
        element[i].elem_no = i                # overwrite the element number
        i = i+1
    # for j in range(1,SC_B_number_of_elements+1):
    #     element[i] = SC_B_elements[j]         # assign elements for bottom spar cap
    #     element[i].elem_no = i                # overwrite the element number
    #     i = i+1
    # for j in range(1,SW_L_biaxL_number_of_elements+1):
    #     element[i] = SW_L_biaxL_elements[j]   # assign elements for left shear web, left biax laminate
    #     element[i].elem_no = i                # overwrite the element number
    #     i = i+1
    # for j in range(1,SW_L_foam_number_of_elements+1):
    #     element[i] = SW_L_foam_elements[j]    # assign elements for left shear web, foam laminate
    #     element[i].elem_no = i                # overwrite the element number
    #     i = i+1
    # for j in range(1,SW_L_biaxR_number_of_elements+1):
    #     element[i] = SW_L_biaxR_elements[j]   # assign elements for left shear web, right biax laminate
    #     element[i].elem_no = i                # overwrite the element number
    #     i = i+1
    # for j in range(1,SW_R_biaxL_number_of_elements+1):
    #     element[i] = SW_R_biaxL_elements[j]   # assign elements for right shear web, left biax laminate
    #     element[i].elem_no = i                # overwrite the element number
    #     i = i+1
    # for j in range(1,SW_R_foam_number_of_elements+1):
    #     element[i] = SW_R_foam_elements[j]    # assign elements for right shear web, foam laminate
    #     element[i].elem_no = i                # overwrite the element number
    #     i = i+1
    # for j in range(1,SW_R_biaxR_number_of_elements+1):
    #     element[i] = SW_R_biaxR_elements[j]   # assign elements for right shear web, right biax laminate
    #     element[i].elem_no = i                # overwrite the element number
    #     i = i+1


    if plot_grid_flag:   # plot the grid to the screen using mayavi
        # import the required plotting modules ######################################################################################################
        from mayavi import mlab
        import autogridgen.gridViz as gv


        # plot the grid #############################################################################################################################
        print "        - plotting the grid"
        ## create a new figure for each cross-section
        figtitle = 'spar station #' + str(spar_stn) + ', grid'
        mlab.figure(figure=figtitle, size=(800,800))
        mlab.view(0,180)  # set the view to be along the +Z axis (better for 2D grids)

        # ### ROOT BUILDUP ###
        # if plotRBflag:  # only perform operations for root buildup if its cross-sectional area is non-zero
        #     gv.plotRectGrid(RB_T_x,RB_T_y)
        #     gv.plotRectGrid(RB_B_x,RB_B_y)

        ### SPAR CAPS ###
        gv.plotRectGrid(SC_T_x,SC_T_y)
        # gv.plotRectGrid(SC_B_x,SC_B_y)

        # ### SHEAR WEBS ###
        # ## left shear web ##
        # gv.plotRectGrid(SW_L_biaxL_x,SW_L_biaxL_y)  # left biax
        # gv.plotRectGrid(SW_L_foam_x,SW_L_foam_y)    # foam
        # gv.plotRectGrid(SW_L_biaxR_x,SW_L_biaxR_y)  # right biax
        # ## right shear web ##
        # gv.plotRectGrid(SW_R_biaxL_x,SW_R_biaxL_y)  # left biax
        # gv.plotRectGrid(SW_R_foam_x,SW_R_foam_y)    # foam
        # gv.plotRectGrid(SW_R_biaxR_x,SW_R_biaxR_y)  # right biax
        
        if ((plot_grid_flag == True) and (fastflag == False)):  # wait for the user to approve plotting the next grid (temp workaround bc lots of mayavi grids sometimes will crash python)
            print "Press Enter to plot the next grid..."
            raw_input()

    # if plot_layer_flag:   # plot the layers to the screen using mayavi
    #     # plot the elements by layer #############################################################################################################################
    #     print "        - coloring the elements by layer"
    #     figtitle = 'spar station #' + str(spar_stn) + ', layer'
    #     mlab.figure(figure=figtitle, size=(800,800))
    #     mlab.view(0,180)

    #     if plotRBflag:  # only perform operations for root buildup if its cross-sectional area is non-zero
    #         ### root buildup (top) ###     ###############################################################
    #         for i in range(RB_plies):
    #             a = RB_T_elementMap[i,0]
    #             b = RB_T_elementMap[i,-1]
    #             x_coords = [RB_T_elements[a].node4.x2, RB_T_elements[b].node2.x2]
    #             y_coords = [RB_T_elements[a].node4.x3, RB_T_elements[b].node2.x3]
    #             gv.plotSurface(x_coords,y_coords,RB_T_elements[a].layer.rgb,1.0)

    #         ### root buildup (bottom) ###
    #         for i in range(RB_plies):
    #             a = RB_B_elementMap[i,0]
    #             b = RB_B_elementMap[i,-1]
    #             x_coords = [RB_B_elements[a].node4.x2, RB_B_elements[b].node2.x2]
    #             y_coords = [RB_B_elements[a].node4.x3, RB_B_elements[b].node2.x3]
    #             gv.plotSurface(x_coords,y_coords,RB_B_elements[a].layer.rgb,1.0)

    #     ### spar cap (top) ###     ###################################################################
    #     for i in range(SC_plies):
    #         a = SC_T_elementMap[i,0]
    #         b = SC_T_elementMap[i,-1]
    #         x_coords = [SC_T_elements[a].node4.x2, SC_T_elements[b].node2.x2]
    #         y_coords = [SC_T_elements[a].node4.x3, SC_T_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SC_T_elements[a].layer.rgb,1.0)

    #     ### spar cap (bottom) ###
    #     for i in range(SC_plies):
    #         a = SC_B_elementMap[i,0]
    #         b = SC_B_elementMap[i,-1]
    #         x_coords = [SC_B_elements[a].node4.x2, SC_B_elements[b].node2.x2]
    #         y_coords = [SC_B_elements[a].node4.x3, SC_B_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SC_B_elements[a].layer.rgb,1.0)

    #     ### shear web (left, left biax) ###     ######################################################
    #     for i in range(SW_biax_plies):
    #         a = SW_L_biaxL_elementMap[0,i]
    #         b = SW_L_biaxL_elementMap[-1,i]
    #         x_coords = [SW_L_biaxL_elements[a].node4.x2, SW_L_biaxL_elements[b].node2.x2]
    #         y_coords = [SW_L_biaxL_elements[a].node4.x3, SW_L_biaxL_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_L_biaxL_elements[a].layer.rgb,1.0)

    #     ### shear web (left, foam) ###
    #     for i in range(SW_foam_plies):
    #         a = SW_L_foam_elementMap[0,i]
    #         b = SW_L_foam_elementMap[-1,i]
    #         x_coords = [SW_L_foam_elements[a].node4.x2, SW_L_foam_elements[b].node2.x2]
    #         y_coords = [SW_L_foam_elements[a].node4.x3, SW_L_foam_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_L_foam_elements[a].layer.rgb,1.0)

    #     ### shear web (left, right biax) ###
    #     for i in range(SW_biax_plies):
    #         a = SW_L_biaxR_elementMap[0,i]
    #         b = SW_L_biaxR_elementMap[-1,i]
    #         x_coords = [SW_L_biaxR_elements[a].node4.x2, SW_L_biaxR_elements[b].node2.x2]
    #         y_coords = [SW_L_biaxR_elements[a].node4.x3, SW_L_biaxR_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_L_biaxR_elements[a].layer.rgb,1.0)

    #     ### shear web (right, left biax) ###
    #     for i in range(SW_biax_plies):
    #         a = SW_R_biaxL_elementMap[0,i]
    #         b = SW_R_biaxL_elementMap[-1,i]
    #         x_coords = [SW_R_biaxL_elements[a].node4.x2, SW_R_biaxL_elements[b].node2.x2]
    #         y_coords = [SW_R_biaxL_elements[a].node4.x3, SW_R_biaxL_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_R_biaxL_elements[a].layer.rgb,1.0)

    #     ### shear web (right, foam) ###
    #     for i in range(SW_foam_plies):
    #         a = SW_R_foam_elementMap[0,i]
    #         b = SW_R_foam_elementMap[-1,i]
    #         x_coords = [SW_R_foam_elements[a].node4.x2, SW_R_foam_elements[b].node2.x2]
    #         y_coords = [SW_R_foam_elements[a].node4.x3, SW_R_foam_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_R_foam_elements[a].layer.rgb,1.0)

    #     ### shear web (right, right biax) ###
    #     for i in range(SW_biax_plies):
    #         a = SW_R_biaxR_elementMap[0,i]
    #         b = SW_R_biaxR_elementMap[-1,i]
    #         x_coords = [SW_R_biaxR_elements[a].node4.x2, SW_R_biaxR_elements[b].node2.x2]
    #         y_coords = [SW_R_biaxR_elements[a].node4.x3, SW_R_biaxR_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_R_biaxR_elements[a].layer.rgb,1.0)


    # if plot_material_flag:   # plot the materials to the screen using mayavi
    #     # plot the elements by material ##################################################################################################################################
    #     print "        - coloring the elements by material"
    #     figtitle = 'spar station #' + str(spar_stn) + ', material'
    #     mlab.figure(figure=figtitle, size=(800,800))
    #     mlab.view(0,180)

    #     if plotRBflag:  # only perform operations for root buildup if its cross-sectional area is non-zero
    #         ### root buildup (top) ###     ###############################################################
    #         for i in range(RB_plies):
    #             a = RB_T_elementMap[i,0]
    #             b = RB_T_elementMap[i,-1]
    #             x_coords = [RB_T_elements[a].node4.x2, RB_T_elements[b].node2.x2]
    #             y_coords = [RB_T_elements[a].node4.x3, RB_T_elements[b].node2.x3]
    #             gv.plotSurface(x_coords,y_coords,RB_T_elements[a].layer.material.rgb,1.0)

    #         ### root buildup (bottom) ###
    #         for i in range(RB_plies):
    #             a = RB_B_elementMap[i,0]
    #             b = RB_B_elementMap[i,-1]
    #             x_coords = [RB_B_elements[a].node4.x2, RB_B_elements[b].node2.x2]
    #             y_coords = [RB_B_elements[a].node4.x3, RB_B_elements[b].node2.x3]
    #             gv.plotSurface(x_coords,y_coords,RB_B_elements[a].layer.material.rgb,1.0)

    #     ### spar cap (top) ###     ###################################################################
    #     for i in range(SC_plies):
    #         a = SC_T_elementMap[i,0]
    #         b = SC_T_elementMap[i,-1]
    #         x_coords = [SC_T_elements[a].node4.x2, SC_T_elements[b].node2.x2]
    #         y_coords = [SC_T_elements[a].node4.x3, SC_T_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SC_T_elements[a].layer.material.rgb,1.0)

    #     ### spar cap (bottom) ###
    #     for i in range(SC_plies):
    #         a = SC_B_elementMap[i,0]
    #         b = SC_B_elementMap[i,-1]
    #         x_coords = [SC_B_elements[a].node4.x2, SC_B_elements[b].node2.x2]
    #         y_coords = [SC_B_elements[a].node4.x3, SC_B_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SC_B_elements[a].layer.material.rgb,1.0)

    #     ### shear web (left, left biax) ###     ######################################################
    #     for i in range(SW_biax_plies):
    #         a = SW_L_biaxL_elementMap[0,i]
    #         b = SW_L_biaxL_elementMap[-1,i]
    #         x_coords = [SW_L_biaxL_elements[a].node4.x2, SW_L_biaxL_elements[b].node2.x2]
    #         y_coords = [SW_L_biaxL_elements[a].node4.x3, SW_L_biaxL_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_L_biaxL_elements[a].layer.material.rgb,1.0)

    #     ### shear web (left, foam) ###
    #     for i in range(SW_foam_plies):
    #         a = SW_L_foam_elementMap[0,i]
    #         b = SW_L_foam_elementMap[-1,i]
    #         x_coords = [SW_L_foam_elements[a].node4.x2, SW_L_foam_elements[b].node2.x2]
    #         y_coords = [SW_L_foam_elements[a].node4.x3, SW_L_foam_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_L_foam_elements[a].layer.material.rgb,1.0)

    #     ### shear web (left, right biax) ###
    #     for i in range(SW_biax_plies):
    #         a = SW_L_biaxR_elementMap[0,i]
    #         b = SW_L_biaxR_elementMap[-1,i]
    #         x_coords = [SW_L_biaxR_elements[a].node4.x2, SW_L_biaxR_elements[b].node2.x2]
    #         y_coords = [SW_L_biaxR_elements[a].node4.x3, SW_L_biaxR_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_L_biaxR_elements[a].layer.material.rgb,1.0)

    #     ### shear web (right, left biax) ###
    #     for i in range(SW_biax_plies):
    #         a = SW_R_biaxL_elementMap[0,i]
    #         b = SW_R_biaxL_elementMap[-1,i]
    #         x_coords = [SW_R_biaxL_elements[a].node4.x2, SW_R_biaxL_elements[b].node2.x2]
    #         y_coords = [SW_R_biaxL_elements[a].node4.x3, SW_R_biaxL_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_R_biaxL_elements[a].layer.material.rgb,1.0)

    #     ### shear web (right, foam) ###
    #     for i in range(SW_foam_plies):
    #         a = SW_R_foam_elementMap[0,i]
    #         b = SW_R_foam_elementMap[-1,i]
    #         x_coords = [SW_R_foam_elements[a].node4.x2, SW_R_foam_elements[b].node2.x2]
    #         y_coords = [SW_R_foam_elements[a].node4.x3, SW_R_foam_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_R_foam_elements[a].layer.material.rgb,1.0)

    #     ### shear web (right, right biax) ###
    #     for i in range(SW_biax_plies):
    #         a = SW_R_biaxR_elementMap[0,i]
    #         b = SW_R_biaxR_elementMap[-1,i]
    #         x_coords = [SW_R_biaxR_elements[a].node4.x2, SW_R_biaxR_elements[b].node2.x2]
    #         y_coords = [SW_R_biaxR_elements[a].node4.x3, SW_R_biaxR_elements[b].node2.x3]
    #         gv.plotSurface(x_coords,y_coords,SW_R_biaxR_elements[a].layer.material.rgb,1.0)


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


# calculate the time it took to run the code #####################################################################################################################
elapsed_time_tot = time.time() - start_time

print "program completed in", ("%.2f" % round(elapsed_time_tot,2)), "seconds"
