import os
import numpy as np

# read in the raw DYMORE output file
os.chdir("D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\monoplane_spar_constload\\untwisted\\grid_density_1\\FIGURES")

print "*** reading DYMORE output file ***"
eta, F1, F2, F3, M1, M2, M3 = np.loadtxt('svy_force_spar.mdt', unpack=True)

# convert eta (dimensionless parameter) to x1 (dimensional parameter)
B = 91.9  # [m]  length of spar
x1 = eta*B

### linear extrapolation and interpolation ###
from scipy.interpolate import interp1d
from scipy import array

def extrap1d(interpolator):
    # copied from http://stackoverflow.com/questions/2745329/how-to-make-scipy-interpolate-give-a-an-extrapolated-result-beyond-the-input-ran
    xs = interpolator.x
    ys = interpolator.y

    def pointwise(x):
        if x < xs[0]:
            return ys[0]+(x-xs[0])*(ys[1]-ys[0])/(xs[1]-xs[0])
        elif x > xs[-1]:
            return ys[-1]+(x-xs[-1])*(ys[-1]-ys[-2])/(xs[-1]-xs[-2])
        else:
            return interpolator(x)

    def ufunclike(xs):
        return array(map(pointwise, array(xs)))

    return ufunclike


print "*** interpolating results at each spar station ***"
f_F1 = interp1d(x1,F1)
f_F2 = interp1d(x1,F2)
f_F3 = interp1d(x1,F3)
f_M1 = interp1d(x1,M1)
f_M2 = interp1d(x1,M2)
f_M3 = interp1d(x1,M3)

f_F1_new = extrap1d(f_F1)
f_F2_new = extrap1d(f_F2)
f_F3_new = extrap1d(f_F3)
f_M1_new = extrap1d(f_M1)
f_M2_new = extrap1d(f_M2)
f_M3_new = extrap1d(f_M3)

x1_new = np.array([0.0, 0.2, 2.3, 4.4, 6.5, 9.0, 12.2, 13.9, 15.5, 17.1, 19.8, 22.5, 25.2, 33.4, 41.5, 49.6, 57.8, 64.3, 65.9, 70.8, 74.0, 82.2, 87.0, 91.9])  # x1 coordinates of all 24 spar stations

F1_new = f_F1_new(x1_new)  # use extrapolations function returned by 'extrap1d'
F2_new = f_F2_new(x1_new)
F3_new = f_F3_new(x1_new)
M1_new = f_M1_new(x1_new)
M2_new = f_M2_new(x1_new)
M3_new = f_M3_new(x1_new)

print "*** writing results for each spar station ***"

f = open('svy_force_spar_new.mdt', 'w')
f.write('# monoplane_spar_constload results, interpolated at each spar station\n')
f.write('#\n')
f.write('# stn  x1(m)  F1' + ' '*19 + 'F2' + ' '*19 + 'F3' + ' '*19 + 'M1' + ' '*19 + 'M2' + ' '*19 + 'M3\n')
f.write('# ---  -----' + '  -------------------'*6 + '\n')

for i in range(24):
    f.write(
        '%5i' % (i+1)         +  # station
        '%7.1f' % x1_new[i]   +  # x1
        '%21.12e' % F1_new[i] +  # F1
        '%21.12e' % F2_new[i] +  # F2
        '%21.12e' % F3_new[i] +  # F3
        '%21.12e' % M1_new[i] +  # M1
        '%21.12e' % M2_new[i] +  # M2
        '%21.12e' % M3_new[i] +  # M3
        '\n')

f.close()

print "*** finished ***"
# change back to the original directory
os.chdir('D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\postprocessing\\VABS')