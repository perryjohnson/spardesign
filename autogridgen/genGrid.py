import numpy as np
import matplotlib.pyplot as plt
import read_layup as rl
import cartGrid as cg

data = rl.readLayupFile('monoplane_spar_layup.txt')

for i in range(1,len(data)+1):
	spar_stn = i
	nrows = 5
	ncols = 10

	plt.figure(i)
	plt.axes().set_xlim(-2,2)
	plt.axes().set_ylim(-3,3)

	### read in the columns for root buildup base & root buildup height
	rtbldup_bse = rl.extractDataColumn(data,'root buildup base')
	rtbldup_ht  = rl.extractDataColumn(data,'root buildup height')
	if rtbldup_bse[i-1] * rtbldup_ht[i-1] > 0.0:  # only perform operations for root buildup if its cross-sectional area is non-zero
		RB_corners = rl.extract_RB_corners(data,spar_stn)
		RB_T_gridpts = cg.storeGridPoints(nrows,ncols,RB_corners[0,:,:])  # top root buildup
		RB_B_gridpts = cg.storeGridPoints(nrows,ncols,RB_corners[1,:,:])  # bottom root buildup
		cg.plotGridPoints(RB_T_gridpts, RB_corners[0,:,:])
		cg.plotGridPoints(RB_B_gridpts, RB_corners[1,:,:])

	SW_corners = rl.extract_SW_corners(data,spar_stn)
	SW_L_gridpts = cg.storeGridPoints(nrows,ncols,SW_corners[0,:,:])  # left shear web
	SW_R_gridpts = cg.storeGridPoints(nrows,ncols,SW_corners[1,:,:])  # right shear web
	cg.plotGridPoints(SW_L_gridpts, SW_corners[0,:,:])
	cg.plotGridPoints(SW_R_gridpts, SW_corners[1,:,:])

	SC_corners = rl.extract_SC_corners(data,spar_stn)
	SC_T_gridpts = cg.storeGridPoints(nrows,ncols,SC_corners[0,:,:])  # top spar cap
	SC_B_gridpts = cg.storeGridPoints(nrows,ncols,SC_corners[1,:,:])  # bottom spar cap
	cg.plotGridPoints(SC_T_gridpts, SC_corners[0,:,:])
	cg.plotGridPoints(SC_B_gridpts, SC_corners[1,:,:])
