import numpy as np
import matplotlib.pyplot as plt
import read_layup as rl
import cartGrid as cg
import time

# record the time when the code starts
start_time = time.time()

plotflag = True   # set to false to suppress plot output and speed up this script

# import the data from the layup file
data = rl.readLayupFile('monoplane_spar_layup.txt')

for i in range(1,len(data)+1):   # run for all cross-sections
# for i in range(1,2):               # run for the first cross-section only
	spar_stn = i
	print "calculating grids for spar station", spar_stn, "..."
	# nrows = 5
	# ncols = 10
	maxAR = 1.2   # set the maximum aspect ratio for any given cell

	## set number of plies for each structural component ##
	SC_plies = 2       # spar cap has 2 plies:                      [0]_2
	RB_plies = 6       # root buildup has 6 plies:                  [+/-45]_2[0]_2
	SW_biax_plies = 8  # biaxial laminate in shear web has 8 plies: [+/-45]_4
	SW_foam_plies = 4  # set the foam part of the shear web to use 4 cells across its thickness (the foam doesn't really have plies)

	plt.figure(i)
	plt.axes().set_xlim(-2,2)
	plt.axes().set_ylim(-3,3)

	### ROOT BUILDUP ###
	### read in the columns for root buildup base & root buildup height
	rtbldup_bse = rl.extractDataColumn(data,'root buildup base')
	rtbldup_ht  = rl.extractDataColumn(data,'root buildup height')
	if rtbldup_bse[i-1] * rtbldup_ht[i-1] > 0.0:  # only perform operations for root buildup if its cross-sectional area is non-zero
		RB_corners = rl.extract_RB_corners(data,spar_stn)
		## top root buildup ##
		(dimH,dimV) = cg.calcCornerDims(RB_corners[0,:,:])
		(nV,nH) = cg.calcCellNums(dimV,RB_plies,maxAR,dimH)
		(nrows,ncols) = (nV,nH)
		RB_T_gridpts = cg.storeGridPoints(nrows,ncols,RB_corners[0,:,:])
		## bottom root buildup ##
		(dimH,dimV) = cg.calcCornerDims(RB_corners[1,:,:])
		(nV,nH) = cg.calcCellNums(dimV,RB_plies,maxAR,dimH)
		(nrows,ncols) = (nV,nH)
		RB_B_gridpts = cg.storeGridPoints(nrows,ncols,RB_corners[1,:,:])
		## plot both root buildups ##
		if (plotflag):
			cg.plotGridPoints(RB_T_gridpts, RB_corners[0,:,:])
			cg.plotGridPoints(RB_B_gridpts, RB_corners[1,:,:])

	### SPAR CAPS ###
	SC_corners = rl.extract_SC_corners(data,spar_stn)
	## top spar cap ##
	(dimH,dimV) = cg.calcCornerDims(SC_corners[0,:,:])
	(nV,nH) = cg.calcCellNums(dimV,SC_plies,maxAR,dimH)
	(nrows,ncols) = (nV,nH)
	SC_T_gridpts = cg.storeGridPoints(nrows,ncols,SC_corners[0,:,:])
	## bottom spar cap ##
	(dimH,dimV) = cg.calcCornerDims(SC_corners[1,:,:])
	(nV,nH) = cg.calcCellNums(dimV,SC_plies,maxAR,dimH)
	(nrows,ncols) = (nV,nH)
	SC_B_gridpts = cg.storeGridPoints(nrows,ncols,SC_corners[1,:,:])
	## plot both spar caps ##
	if (plotflag):
		cg.plotGridPoints(SC_T_gridpts, SC_corners[0,:,:])
		cg.plotGridPoints(SC_B_gridpts, SC_corners[1,:,:])

	### SHEAR WEBS ###
	SW_corners = rl.extract_SW_corners(data,spar_stn)
	## left shear web ##
	# left biax laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[0,0,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	SW_L_biaxL_gridpts = cg.storeGridPoints(nrows,ncols,SW_corners[0,0,:,:])
	# foam laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[0,1,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_foam_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	SW_L_foam_gridpts = cg.storeGridPoints(nrows,ncols,SW_corners[0,1,:,:])
	# right biax laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[0,2,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	SW_L_biaxR_gridpts = cg.storeGridPoints(nrows,ncols,SW_corners[0,2,:,:])
	## right shear web ##
	# left biax laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[1,0,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	SW_R_biaxL_gridpts = cg.storeGridPoints(nrows,ncols,SW_corners[1,0,:,:])
	# foam laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[1,1,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_foam_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	SW_R_foam_gridpts = cg.storeGridPoints(nrows,ncols,SW_corners[1,1,:,:])
	# right biax laminate #
	(dimH,dimV) = cg.calcCornerDims(SW_corners[1,2,:,:])
	(nH,nV) = cg.calcCellNums(dimH,SW_biax_plies,maxAR,dimV)
	(nrows,ncols) = (nV,nH)
	SW_R_biaxR_gridpts = cg.storeGridPoints(nrows,ncols,SW_corners[1,2,:,:])
	## plot both shear webs (all laminates) ##
	if (plotflag):
		cg.plotGridPoints(SW_L_biaxL_gridpts, SW_corners[0,0,:,:])
		cg.plotGridPoints(SW_L_foam_gridpts, SW_corners[0,1,:,:])
		cg.plotGridPoints(SW_L_biaxR_gridpts, SW_corners[0,2,:,:])
		cg.plotGridPoints(SW_R_biaxL_gridpts, SW_corners[1,0,:,:])
		cg.plotGridPoints(SW_R_foam_gridpts, SW_corners[1,1,:,:])
		cg.plotGridPoints(SW_R_biaxR_gridpts, SW_corners[1,2,:,:])

# calculate the time it took to run the code
elapsed_time = time.time() - start_time
print "program completed in", elapsed_time, "seconds"