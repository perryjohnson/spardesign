import numpy as np

temp = np.loadtxt('monoplane_spar_layup.txt')

spar_stn    = temp[:,0]   # spar station
x1          = temp[:,1]   # spanwise length from root to tip (m)
eta         = temp[:,2]   # eta coordinate along span from root to tip, 0 < eta < 1
spar_frac   = temp[:,3]   # spar fraction (%)
sparcap_bse = temp[:,4]   # spar cap base (m)
sparcap_ht  = temp[:,5]   # spar cap height (m)
rtbldup_bse = temp[:,6]   # root buildup base (m)
rtbldup_ht  = temp[:,7]   # root buildup height (m)
shearwb_bse = temp[:,8]   # shear web base (m)
shearwb_ht  = temp[:,9]   # shear web height (m)
twist_deg   = temp[:,10]  # twist angle (deg)
twist_rad   = temp[:,11]  # twist angle (rad)
k1          = temp[:,12]  # twist rate (rad/m)
blde_stn    = temp[:,13]  # blade station
blade_frac  = temp[:,14]  # blade fraction (%)