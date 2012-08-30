import os
os.chdir('D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\biplane_spar_constload\\untwisted-noRootJoint\\24-bispar-rj452-g125\\FIGURES')

from numpy import loadtxt
stn, x1, F1_upper, F2_upper, F3_upper, M1_upper, M2_upper, M3_upper, F1_lower, F2_lower, F3_lower, M1_lower, M2_lower, M3_lower = loadtxt('svy_force_spar_new.mdt', unpack=True)

import matplotlib.pyplot as plt
plt.close('all')

### F1
plt.figure()
plt.title('F1')
plt.plot(x1,F1_upper,'bo--',x1[0:14],F1_lower[0:14],'rx--')
plt.plot(x1_CD,F1_CD,'k:')
plt.plot(x1_DE,F1_DE,'k:')
plt.plot(x1_EF,F1_EF,'k:')
plt.plot(x1_GH,F1_GH,'k:')
plt.plot(x1_HE,F1_HE,'k:')

### F2
plt.figure()
plt.title('F2')
plt.plot(x1,F2_upper,'bo--',x1[0:14],F2_lower[0:14],'rx--')
plt.plot(x1_CD,F2_CD,'k:')
plt.plot(x1_DE,F2_DE,'k:')
plt.plot(x1_EF,F2_EF,'k:')
plt.plot(x1_GH,F2_GH,'k:')
plt.plot(x1_HE,F2_HE,'k:')

### F3
plt.figure()
plt.title('F3')
plt.plot(x1,F3_upper,'bo--',x1[0:14],F3_lower[0:14],'rx--')
plt.plot(x1_CD,F3_CD,'k:')
plt.plot(x1_DE,F3_DE,'k:')
plt.plot(x1_EF,F3_EF,'k:')
plt.plot(x1_GH,F3_GH,'k:')
plt.plot(x1_HE,F3_HE,'k:')

### M1
plt.figure()
plt.title('M1')
plt.plot(x1,M1_upper,'bo--',x1[0:14],M1_lower[0:14],'rx--')
plt.plot(x1_CD,M1_CD,'k:')
plt.plot(x1_DE,M1_DE,'k:')
plt.plot(x1_EF,M1_EF,'k:')
plt.plot(x1_GH,M1_GH,'k:')
plt.plot(x1_HE,M1_HE,'k:')

### M2
plt.figure()
plt.title('M2')
plt.plot(x1,M2_upper,'bo--',x1[0:14],M2_lower[0:14],'rx--')
plt.plot(x1_CD,M2_CD,'k:')
plt.plot(x1_DE,M2_DE,'k:')
plt.plot(x1_EF,M2_EF,'k:')
plt.plot(x1_GH,M2_GH,'k:')
plt.plot(x1_HE,M2_HE,'k:')

### M3
plt.figure()
plt.title('M3')
plt.plot(x1,M3_upper,'bo--',x1[0:14],M3_lower[0:14],'rx--')
plt.plot(x1_CD,M3_CD,'k:')
plt.plot(x1_DE,M3_DE,'k:')
plt.plot(x1_EF,M3_EF,'k:')
plt.plot(x1_GH,M3_GH,'k:')
plt.plot(x1_HE,M3_HE,'k:')

plt.show()

os.chdir('D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\postprocessing\\VABS')