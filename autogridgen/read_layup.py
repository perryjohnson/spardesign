import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('monoplane_spar_layup.txt')  # read in layup file

# split layup file data by columns into separate data sets
spar_stn    = data[:,0]   # spar station
x1          = data[:,1]   # spanwise length from root to tip (m)
eta         = data[:,2]   # eta coordinate along span from root to tip, 0 < eta < 1
spar_frac   = data[:,3]   # spar fraction (%)
sparcap_bse = data[:,4]   # spar cap base (m)
sparcap_ht  = data[:,5]   # spar cap height (m)
rtbldup_bse = data[:,6]   # root buildup base (m)
rtbldup_ht  = data[:,7]   # root buildup height (m)
shearwb_bse = data[:,8]   # shear web base (m)
shearwb_ht  = data[:,9]   # shear web height (m)
twist_deg   = data[:,10]  # twist angle (deg)
twist_rad   = data[:,11]  # twist angle (rad)
k1          = data[:,12]  # twist rate (rad/m)
blde_stn    = data[:,13]  # blade station
blade_frac  = data[:,14]  # blade fraction (%)

plt.close('all')

data_rows = np.shape(data)[0]

v = np.arange(0, data_rows)
for i in v:
	n = v[i]
	# n = 0  # for now, just focus on the root cross-section (we'll iterate thru the entire span later)

	### all corners are stored in the following order ###
	## 0: top left corner
	## 1: top right corner
	## 2: bottom left corner
	## 3: bottom right corner

	### find and plot the corners of the cross-section ###
	# total_bse = rtbldup_bse[n]  # this doesn't work when the root buildup disappears past 9.8% span!
	total_bse = sparcap_bse[n] + 2.0 * shearwb_bse[n]
	total_ht = shearwb_ht[n] + 2.0 * rtbldup_ht[n]
	corners = np.zeros((4,2))  # column 0 stores x-coords, column 1 stores y-coords
	# store the x-coords #
	corners[0,0] = total_bse / 2.0 * -1.0
	corners[1,0] = corners[0,0] * -1.0
	corners[2:4,0] = corners[0:2,0]
	# store the y-coords #
	corners[0,1] = total_ht / 2.0
	corners[1,1] = corners[0,1]
	corners[2:4,1] = corners[0:2,1] * -1.0

	### find and plot the corners of the root buildup ###
	rtbldup = np.zeros((8,2))  # column 0 stores x-coords, column 1 stores y-coords
	## upper root buildup ## (row entries 0-3)
	# store the x-coords #
	rtbldup[0:4,0] = corners[0:4,0]
	# store the y-coords #
	rtbldup[0:2,1] = corners[0:2,1]
	rtbldup[2:4,1] = rtbldup[0:2,1] - rtbldup_ht[n]
	## lower root buildup ## (row entries 4-8)
	# store the x-coords #
	rtbldup[4:8,0] = rtbldup[0:4,0]
	# store the y-coords #
	rtbldup[4:8,1] = rtbldup[0:4,1] * -1.0

	### find and plot the corners of the shear webs ###
	shearwb = np.zeros((8,2))  # column 0 stores x-coords, column 1 stores y-coords
	## left shear web ##
	# store coords shared with root buildup #
	shearwb[0,:] = rtbldup[2,:] # top left corner of shear web, bottom left corner of upper root buildup
	shearwb[2,:] = rtbldup[6,:] # bottom left corner of shear web, top left corner of lower root buildup
	# store coords for right boundary of left shear web #
	shearwb[1,0] = shearwb[0,0] + shearwb_bse[n]  # x-coord for upper right corner (add shear web thickness)
	shearwb[1,1] = shearwb[0,1]                   # y-coord for upper right corner
	shearwb[3,0] = shearwb[1,0]                   # x-coord for lower right corner
	shearwb[3,1] = shearwb[2,1]                   # y-coord for lower right corner
	## right shear web ##
	# store the x-coords #
	shearwb[4:8,0] = shearwb[0:4,0] * -1.0
	# store the y-coords #
	shearwb[4:8,1] = shearwb[0:4,1]

	### find and plot the corners of the spar caps ###
	sparcap = np.zeros((8,2))  # column 0 stores x-coords, column 1 stores y-coords
	## upper spar cap ##
	# store coords shared with shear webs #
	sparcap[0,:] = shearwb[1,:] # top left corner of upper spar cap, top right corner of left shear web
	sparcap[1,:] = shearwb[5,:] # top right corner of upper spar cap, top left corner of right shear web
	# store coords for lower boundary of upper spar cap #
	sparcap[2,0] = sparcap[0,0]                  # x-coord for lower left corner
	sparcap[2,1] = sparcap[0,1] - sparcap_ht[n]  # y-coord for lower left corner (subtract spar cap thickness)
	sparcap[3,0] = sparcap[1,0]                  # x-coord for lower right corner
	sparcap[3,1] = sparcap[2,1]                  # y-coord for lower right corner
	## lower spar cap ##
	# store the x-coords #
	sparcap[4:8,0] = sparcap[0:4,0]
	# store the y-coords #
	sparcap[4:8,1] = sparcap[0:4,1] * -1.0

	### plot the results ###
	plt.figure(n)
	plt.axes().set_aspect('equal')
	plt.axes().set_xlim(-2,2)
	plt.axes().set_ylim(-3,3)
	plt.plot(corners[:,0], corners[:,1], 'b+')
	plt.plot(rtbldup[:,0], rtbldup[:,1], 'ro')
	plt.plot(shearwb[:,0], shearwb[:,1], 'cs')
	plt.plot(sparcap[:,0], sparcap[:,1], 'k*')
	plt.xlabel('x [m]')
	plt.ylabel('y [m]')
	plt.title('Cross-section at eta = ' + str(eta[n]))
	plt.show()

