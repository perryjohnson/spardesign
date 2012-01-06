import numpy as np
import matplotlib.pyplot as plt
import read_layup as rl
import cartGrid as cg
import time
# import elapsed_time as et
# import VABSobjects as vo
import plotgrid as pg
import elementMap as em
from mayavi import mlab
import gridViz as gv

### TODO ###
# remove gridpts output from all cg.storeGridPoints2 function calls?




# record the time when the code starts
start_time = time.time()

fastflag = False   # set to True to speed up this script



if fastflag:
	plotflag = False   # set to False to suppress plot output and speed up this script
else:
	plotflag = True


## set the maximum aspect ratio for any given cell ##
maxAR = 1.2


# import the data from the layup file
data = rl.readLayupFile('monoplane_spar_layup.txt')

if fastflag:
	endrange = 2                   # run for the first cross-section only
else:
	endrange = len(data)+1         # run for all cross-sections

for i in range(1,endrange):
	spar_stn = i
	print "calculating grids for spar station", spar_stn, "..."

	## set number of plies for each structural component ##
	SC_plies = 2       # spar cap has 2 plies:                      [0]_2
	RB_plies = 6       # root buildup has 6 plies:                  [+/-45]_2 [0]_2
	SW_biax_plies = 8  # biaxial laminate in shear web has 8 plies: [+/-45]_4
	SW_foam_plies = 4  # set the foam part of the shear web to use 4 cells across its thickness (the foam doesn't really have plies)

	## create a new figure for each cross-section, and define the max&min plot limits in the x&y directions
	figtitle = "spar station #" + str(i)
	fig = mlab.figure(figure=figtitle, size=(600,750))  # make a new mayavi scene (figure window)
	mlab.view(0,0)  # set the view to -Z (better for 2D grids)


	### ROOT BUILDUP ###
	print "ROOT BUILDUP"
	### read in the columns for root buildup base & root buildup height
	rtbldup_bse = rl.extractDataColumn(data,'root buildup base')
	rtbldup_ht  = rl.extractDataColumn(data,'root buildup height')
	if rtbldup_bse[i-1] * rtbldup_ht[i-1] > 0.0:  # only perform operations for root buildup if its cross-sectional area is non-zero
		RB_corners = rl.extract_RB_corners(data,spar_stn)
		## top root buildup ##
		(dimH,dimV) = cg.calcCornerDims(RB_corners[0,:,:])
		(nV,nH) = cg.calcCellNums(dimV,RB_plies,maxAR,dimH)
		(nrows,ncols) = (nV,nH)
		(RB_T_gridpts,RB_T_nodes,RB_T_elements,RB_T_number_of_nodes,RB_T_number_of_elements,RB_T_elementMap,RB_T_x,RB_T_y) = cg.storeGridPoints2(nrows,ncols,RB_corners[0,:,:])
		## bottom root buildup ##
		(dimH,dimV) = cg.calcCornerDims(RB_corners[1,:,:])
		(nV,nH) = cg.calcCellNums(dimV,RB_plies,maxAR,dimH)
		(nrows,ncols) = (nV,nH)
		(RB_B_gridpts,RB_B_nodes,RB_B_elements,RB_B_number_of_nodes,RB_B_number_of_elements,RB_B_elementMap,RB_B_x,RB_B_y) = cg.storeGridPoints2(nrows,ncols,RB_corners[1,:,:])
		## plot both root buildups ##
		if (plotflag):
			gv.plotVABSgrid(RB_T_x,RB_T_y)
			gv.plotVABSgrid(RB_B_x,RB_B_y)


	### SPAR CAPS ###
	print "SPAR CAPS"
	SC_corners = rl.extract_SC_corners(data,spar_stn)
	## top spar cap ##
	(dimH,dimV) = cg.calcCornerDims(SC_corners[0,:,:])
	(nV,nH) = cg.calcCellNums(dimV,SC_plies,maxAR,dimH)
	(nrows,ncols) = (nV,nH)
	(SC_T_gridpts,SC_T_nodes,SC_T_elements,SC_T_number_of_nodes,SC_T_number_of_elements,SC_T_elementMap,SC_T_x,SC_T_y) = cg.storeGridPoints2(nrows,ncols,SC_corners[0,:,:])
	## bottom spar cap ##
	(dimH,dimV) = cg.calcCornerDims(SC_corners[1,:,:])
	(nV,nH) = cg.calcCellNums(dimV,SC_plies,maxAR,dimH)
	(nrows,ncols) = (nV,nH)
	(SC_B_gridpts,SC_B_nodes,SC_B_elements,SC_B_number_of_nodes,SC_B_number_of_elements,SC_B_elementMap,SC_B_x,SC_B_y) = cg.storeGridPoints2(nrows,ncols,SC_corners[1,:,:])
	## plot both spar caps ##
	if (plotflag):
		gv.plotVABSgrid(SC_T_x,SC_T_y)
		gv.plotVABSgrid(SC_B_x,SC_B_y)


	### SHEAR WEBS ###
	print "SHEAR WEBS"
	SW_corners = rl.extract_SW_corners(data,spar_stn)
	## left shear web ##
	# left biax laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[0,0,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	(SW_L_biaxL_gridpts,SW_L_biaxL_nodes,SW_L_biaxL_elements,SW_L_biaxL_number_of_nodes,SW_L_biaxL_number_of_elements,SW_L_biaxL_elementMap,SW_L_biaxL_x,SW_L_biaxL_y) = cg.storeGridPoints2(nrows,ncols,SW_corners[0,0,:,:])

	# foam laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[0,1,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_foam_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	(SW_L_foam_gridpts,SW_L_foam_nodes,SW_L_foam_elements,SW_L_foam_number_of_nodes,SW_L_foam_number_of_elements,SW_L_foam_elementMap,SW_L_foam_x,SW_L_foam_y) = cg.storeGridPoints2(nrows,ncols,SW_corners[0,1,:,:])

	# right biax laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[0,2,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	(SW_L_biaxR_gridpts,SW_L_biaxR_nodes,SW_L_biaxR_elements,SW_L_biaxR_number_of_nodes,SW_L_biaxR_number_of_elements,SW_L_biaxR_elementMap,SW_L_biaxR_x,SW_L_biaxR_y) = cg.storeGridPoints2(nrows,ncols,SW_corners[0,2,:,:])

	## right shear web ##
	# left biax laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[1,0,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	(SW_R_biaxL_gridpts,SW_R_biaxL_nodes,SW_R_biaxL_elements,SW_R_biaxL_number_of_nodes,SW_R_biaxL_number_of_elements,SW_R_biaxL_elementMap,SW_R_biaxL_x,SW_R_biaxL_y) = cg.storeGridPoints2(nrows,ncols,SW_corners[1,0,:,:])

	# foam laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[1,1,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_foam_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	(SW_R_foam_gridpts,SW_R_foam_nodes,SW_R_foam_elements,SW_R_foam_number_of_nodes,SW_R_foam_number_of_elements,SW_R_foam_elementMap,SW_R_foam_x,SW_R_foam_y) = cg.storeGridPoints2(nrows,ncols,SW_corners[1,1,:,:])

	# right biax laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[1,2,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	(SW_R_biaxR_gridpts,SW_R_biaxR_nodes,SW_R_biaxR_elements,SW_R_biaxR_number_of_nodes,SW_R_biaxR_number_of_elements,SW_R_biaxR_elementMap,SW_R_biaxR_x,SW_R_biaxR_y) = cg.storeGridPoints2(nrows,ncols,SW_corners[1,2,:,:])


	## plot both shear webs (all laminates) ##
	if (plotflag):
		print "* left shear web"
		print "** left biax"
		gv.plotVABSgrid(SW_L_biaxL_x,SW_L_biaxL_y)
		print "** foam"
		gv.plotVABSgrid(SW_L_foam_x,SW_L_foam_y)
		print "** right biax"
		gv.plotVABSgrid(SW_L_biaxR_x,SW_L_biaxR_y)
		print "* right shear web"
		print "** left biax"
		gv.plotVABSgrid(SW_R_biaxL_x,SW_R_biaxL_y)
		print "** foam"
		gv.plotVABSgrid(SW_R_foam_x,SW_R_foam_y)
		print "** right biax"
		gv.plotVABSgrid(SW_R_biaxR_x,SW_R_biaxR_y)


# calculate the time it took to run the code
elapsed_time_tot = time.time() - start_time

print "program completed in", ("%.2f" % round(elapsed_time_tot,2)), "seconds"
# print et.elapsed_time(elapsed_time_tot)