import numpy as np
import read_layup as rl
import cartGrid as cg
import time
import elementMap as em
from mayavi import mlab
import gridViz as gv

### TODO ###
# remove gridpts output from all cg.storeGridPoints2 function calls?


def genRootBuildup(data,spar_stn,RB_plies=6,maxAR=1.2,plotflag=False):
    ### read in the columns for root buildup base & root buildup height
    RB_corners = rl.extract_RB_corners(data,spar_stn)
    ## top root buildup ##
    (dimH,dimV) = cg.calcCornerDims(RB_corners[0,:,:])
    (nV,nH) = cg.calcCellNums(dimV,RB_plies,maxAR,dimH)
    (nrows,ncols) = (nV,nH)
    (RB_T_gridpts,
     RB_T_nodes,
     RB_T_elements,
     RB_T_number_of_nodes,
     RB_T_number_of_elements,
     RB_T_nodeMap,
     RB_T_elementMap,
     RB_T_x,
     RB_T_y) = cg.storeGridPoints2(nrows,
                                   ncols,
                                   RB_corners[0,:,:])
    ## bottom root buildup ##
    (dimH,dimV) = cg.calcCornerDims(RB_corners[1,:,:])
    (nV,nH) = cg.calcCellNums(dimV,RB_plies,maxAR,dimH)
    (nrows,ncols) = (nV,nH)
    (RB_B_gridpts,
     RB_B_nodes,
     RB_B_elements,
     RB_B_number_of_nodes,
     RB_B_number_of_elements,
     RB_B_nodeMap,
     RB_B_elementMap,
     RB_B_x,
     RB_B_y) = cg.storeGridPoints2(nrows,
                                   ncols,
                                   RB_corners[1,:,:])
    ## plot both root buildups ##
    if (plotflag):
        gv.plotRectGrid(RB_T_x,RB_T_y)
        gv.plotRectGrid(RB_B_x,RB_B_y)

    return (RB_T_nodes, RB_T_elements, RB_T_number_of_nodes, RB_T_number_of_elements, RB_T_nodeMap, RB_T_elementMap, RB_T_x, RB_T_y,
            RB_B_nodes, RB_B_elements, RB_B_number_of_nodes, RB_B_number_of_elements, RB_B_nodeMap, RB_B_elementMap, RB_B_x, RB_B_y)


def genSparCaps(data,spar_stn,SC_plies=2,maxAR=1.2,plotflag=False):
    SC_corners = rl.extract_SC_corners(data,spar_stn)
    ## top spar cap ##
    (dimH,dimV) = cg.calcCornerDims(SC_corners[0,:,:])
    (nV,nH) = cg.calcCellNums(dimV,SC_plies,maxAR,dimH)
    (nrows,ncols) = (nV,nH)
    (SC_T_gridpts,
     SC_T_nodes,
     SC_T_elements,
     SC_T_number_of_nodes,
     SC_T_number_of_elements,
     SC_T_nodeMap,
     SC_T_elementMap,
     SC_T_x,
     SC_T_y) = cg.storeGridPoints2(nrows,
                                   ncols,
                                   SC_corners[0,:,:])
    ## bottom spar cap ##
    (dimH,dimV) = cg.calcCornerDims(SC_corners[1,:,:])
    (nV,nH) = cg.calcCellNums(dimV,SC_plies,maxAR,dimH)
    (nrows,ncols) = (nV,nH)
    (SC_B_gridpts,
     SC_B_nodes,
     SC_B_elements,
     SC_B_number_of_nodes,
     SC_B_number_of_elements,
     SC_B_nodeMap,
     SC_B_elementMap,
     SC_B_x,
     SC_B_y) = cg.storeGridPoints2(nrows,
                                   ncols,
                                   SC_corners[1,:,:])
    ## plot both spar caps ##
    if (plotflag):
        gv.plotRectGrid(SC_T_x,SC_T_y)
        gv.plotRectGrid(SC_B_x,SC_B_y)

    return (SC_T_nodes, SC_T_elements, SC_T_number_of_nodes, SC_T_number_of_elements, SC_T_nodeMap, SC_T_elementMap, SC_T_x, SC_T_y,
            SC_B_nodes, SC_B_elements, SC_B_number_of_nodes, SC_B_number_of_elements, SC_B_nodeMap, SC_B_elementMap, SC_B_x, SC_B_y)


def genShearWebs(data,spar_stn,SW_biax_plies=8,SW_foam_plies=4,maxAR=1.2,plotflag=False):
    SW_corners = rl.extract_SW_corners(data,spar_stn)
    ## left shear web ###########################################################
    # left biax laminate #
    (dimH,dimV) = cg.calcCornerDims(SW_corners[0,0,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
    (nrows,ncols) = (nV,nH)
    (SW_L_biaxL_gridpts,
     SW_L_biaxL_nodes,
     SW_L_biaxL_elements,
     SW_L_biaxL_number_of_nodes,
     SW_L_biaxL_number_of_elements,
     SW_L_biaxL_nodeMap,
     SW_L_biaxL_elementMap,
     SW_L_biaxL_x,
     SW_L_biaxL_y) = cg.storeGridPoints2(nrows,
                                         ncols,
                                         SW_corners[0,0,:,:])

    # foam laminate #
    (dimH,dimV) = cg.calcCornerDims(SW_corners[0,1,:,:])
    ## (nH,nV) = cg.calcCellNums(dimH,SW_foam_plies,maxAR,dimV)
    ## (nrows,ncols) = (nV,nH)
    (nrows,ncols) = (nV,SW_foam_plies)   # changed PJ, 2012-01-17
    ### nV_biax = nV
    ### (SW_foam_plies,nV_foam) = cg.calcCellNums(dimV,nV_biax,maxAR,dimH)
    ### (nrows,ncols) = (nV_biax,SW_foam_plies)  # changed PJ, 2012-01-17 (2)
    (SW_L_foam_gridpts,
     SW_L_foam_nodes,
     SW_L_foam_elements,
     SW_L_foam_number_of_nodes,
     SW_L_foam_number_of_elements,
     SW_L_foam_nodeMap,
     SW_L_foam_elementMap,
     SW_L_foam_x,
     SW_L_foam_y) = cg.storeGridPoints2(nrows,
                                        ncols,
                                        SW_corners[0,1,:,:])

    # right biax laminate #
    (dimH,dimV) = cg.calcCornerDims(SW_corners[0,2,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
    (nrows,ncols) = (nV,nH)
    (SW_L_biaxR_gridpts,
     SW_L_biaxR_nodes,
     SW_L_biaxR_elements,
     SW_L_biaxR_number_of_nodes,
     SW_L_biaxR_number_of_elements,
     SW_L_biaxR_nodeMap,
     SW_L_biaxR_elementMap,
     SW_L_biaxR_x,
     SW_L_biaxR_y) = cg.storeGridPoints2(nrows,
                                         ncols,
                                         SW_corners[0,2,:,:])

    ## right shear web ###########################################################
    # left biax laminate #
    (dimH,dimV) = cg.calcCornerDims(SW_corners[1,0,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
    (nrows,ncols) = (nV,nH)
    (SW_R_biaxL_gridpts,
     SW_R_biaxL_nodes,
     SW_R_biaxL_elements,
     SW_R_biaxL_number_of_nodes,
     SW_R_biaxL_number_of_elements,
     SW_R_biaxL_nodeMap,
     SW_R_biaxL_elementMap,
     SW_R_biaxL_x,
     SW_R_biaxL_y) = cg.storeGridPoints2(nrows,
                                         ncols,
                                         SW_corners[1,0,:,:])

    # foam laminate #
    (dimH,dimV) = cg.calcCornerDims(SW_corners[1,1,:,:])
    # (nH,nV) = cg.calcCellNums(dimH,SW_foam_plies,maxAR,dimV)
    # (nrows,ncols) = (nV,nH)
    (nrows,ncols) = (nV,SW_foam_plies)   # changed PJ, 2012-01-17
    (SW_R_foam_gridpts,
     SW_R_foam_nodes,
     SW_R_foam_elements,
     SW_R_foam_number_of_nodes,
     SW_R_foam_number_of_elements,
     SW_R_foam_nodeMap,
     SW_R_foam_elementMap,
     SW_R_foam_x,
     SW_R_foam_y) = cg.storeGridPoints2(nrows,
                                        ncols,
                                        SW_corners[1,1,:,:])

    # right biax laminate #
    (dimH,dimV) = cg.calcCornerDims(SW_corners[1,2,:,:])
    (nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
    (nrows,ncols) = (nV,nH)
    (SW_R_biaxR_gridpts,
     SW_R_biaxR_nodes,
     SW_R_biaxR_elements,
     SW_R_biaxR_number_of_nodes,
     SW_R_biaxR_number_of_elements,
     SW_R_biaxR_nodeMap,
     SW_R_biaxR_elementMap,
     SW_R_biaxR_x,
     SW_R_biaxR_y) = cg.storeGridPoints2(nrows,
                                         ncols,
                                         SW_corners[1,2,:,:])


    ## if plotflag==True, plot both shear webs (all laminates) ##
    if (plotflag):
        ## left shear web ##
        gv.plotRectGrid(SW_L_biaxL_x,SW_L_biaxL_y)  # left biax
        gv.plotRectGrid(SW_L_foam_x,SW_L_foam_y)    # foam
        gv.plotRectGrid(SW_L_biaxR_x,SW_L_biaxR_y)  # right biax
        ## right shear web ##
        gv.plotRectGrid(SW_R_biaxL_x,SW_R_biaxL_y)  # left biax
        gv.plotRectGrid(SW_R_foam_x,SW_R_foam_y)    # foam
        gv.plotRectGrid(SW_R_biaxR_x,SW_R_biaxR_y)  # right biax


    return (SW_L_biaxL_nodes, SW_L_biaxL_elements, SW_L_biaxL_number_of_nodes, SW_L_biaxL_number_of_elements, SW_L_biaxL_nodeMap, SW_L_biaxL_elementMap, SW_L_biaxL_x, SW_L_biaxL_y,
            SW_L_foam_nodes,  SW_L_foam_elements,  SW_L_foam_number_of_nodes,  SW_L_foam_number_of_elements,  SW_L_foam_nodeMap,  SW_L_foam_elementMap,  SW_L_foam_x,  SW_L_foam_y,
            SW_L_biaxR_nodes, SW_L_biaxR_elements, SW_L_biaxR_number_of_nodes, SW_L_biaxR_number_of_elements, SW_L_biaxR_nodeMap, SW_L_biaxR_elementMap, SW_L_biaxR_x, SW_L_biaxR_y,
            SW_R_biaxL_nodes, SW_R_biaxL_elements, SW_R_biaxL_number_of_nodes, SW_R_biaxL_number_of_elements, SW_R_biaxL_nodeMap, SW_R_biaxL_elementMap, SW_R_biaxL_x, SW_R_biaxL_y,
            SW_R_foam_nodes,  SW_R_foam_elements,  SW_R_foam_number_of_nodes,  SW_R_foam_number_of_elements,  SW_R_foam_nodeMap,  SW_R_foam_elementMap,  SW_R_foam_x,  SW_R_foam_y,
            SW_R_biaxR_nodes, SW_R_biaxR_elements, SW_R_biaxR_number_of_nodes, SW_R_biaxR_number_of_elements, SW_R_biaxR_nodeMap, SW_R_biaxR_elementMap, SW_R_biaxR_x, SW_R_biaxR_y)


if __name__ == '__main__':
    # record the time when the code starts
    start_time = time.time()

    fastflag = True   # set to True to speed up this script (run for the first cross-section only)
    plotflag = True   # set to False to disable plotting

    maxAR = 1.2  ## set the maximum aspect ratio for any given cell ##
    data = rl.readLayupFile('monoplane_spar_layup.txt')  # import the data from the layup file

    ## set number of plies for each structural component ##
    SC_plies = 2       # spar cap has 2 plies:                      [0]_2
    RB_plies = 6       # root buildup has 6 plies:                  [+/-45]_2 [0]_2
    SW_biax_plies = 8  # biaxial laminate in shear web has 8 plies: [+/-45]_4
    SW_foam_plies = 4  # set the foam part of the shear web to use 4 cells across its thickness (the foam doesn't really have plies)

    if fastflag:
        endrange = 2                   # run for the first cross-section only
    else:
        endrange = len(data)+1         # run for all cross-sections

    for spar_stn in range(1,endrange):
        print "calculating grids for spar station", spar_stn, "..."

        ## create a new figure for each cross-section
        if (plotflag):
            figtitle = "spar station #" + str(spar_stn)
            fig = mlab.figure(figure=figtitle, size=(800,800))  # make a new mayavi scene (figure window)
            mlab.view(0,180)  # set the view to be along the +Z axis (better for 2D grids)

        ### ROOT BUILDUP ###
        rtbldup_bse = rl.extractDataColumn(data,'root buildup base')
        rtbldup_ht  = rl.extractDataColumn(data,'root buildup height')
        plotRBflag = (rtbldup_bse[spar_stn-1] * rtbldup_ht[spar_stn-1] > 0.0)
        if plotRBflag:  # only perform operations for root buildup if its cross-sectional area is non-zero
            genRootBuildup(data,spar_stn,RB_plies,maxAR,plotflag)

        ### SPAR CAPS ###
        genSparCaps(data,spar_stn,SC_plies,maxAR,plotflag)

        ### SHEAR WEBS ###
        genShearWebs(data,spar_stn,SW_biax_plies,SW_foam_plies,maxAR,plotflag)
        
        if ((plotflag == True) and (fastflag == False)):  # wait for the user to approve plotting the next grid (temp workaround bc lots of mayavi grids sometimes will crash python)
            print "Press Enter to plot the next grid..."
            raw_input()
        
    # calculate the time it took to run the code
    elapsed_time_tot = time.time() - start_time

    print "program completed in", ("%.2f" % round(elapsed_time_tot,2)), "seconds"
