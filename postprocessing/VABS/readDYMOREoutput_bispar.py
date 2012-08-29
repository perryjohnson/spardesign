import os
import numpy as np

# read in the raw DYMORE output file
os.chdir("D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\biplane_spar_constload\\untwisted-noRootJoint\\24-bispar-rj452-g125\\FIGURES")

### parameters ###
scalefactor = 1.6  # figure size scale factor
fw=5               # figure width
fh=6               # figure height

glw=3.0            # global line width
gms=10.0           # global marker size
gmew=2.0           # global marker edge width
gmfc='None'        # global marker face color (none/empty)

mec_ms='red'       # marker edge color for monoplane spars
mec_bs_hh='blue'   # marker edge color for biplane spars, half-height cross-sections
mec_bs_fh='green'  # marker edge color for biplane spars, full-height cross-sections


print "*** reading DYMORE output files ***"
eta_CD, F1_CD, F2_CD, F3_CD, M1_CD, M2_CD, M3_CD = np.loadtxt('svy_force_CD.mdt', unpack=True)
eta_DE, F1_DE, F2_DE, F3_DE, M1_DE, M2_DE, M3_DE = np.loadtxt('svy_force_DE.mdt', unpack=True)
eta_EF, F1_EF, F2_EF, F3_EF, M1_EF, M2_EF, M3_EF = np.loadtxt('svy_force_EF.mdt', unpack=True)
eta_GH, F1_GH, F2_GH, F3_GH, M1_GH, M2_GH, M3_GH = np.loadtxt('svy_force_GH.mdt', unpack=True)
eta_HE, F1_HE, F2_HE, F3_HE, M1_HE, M2_HE, M3_HE = np.loadtxt('svy_force_HE.mdt', unpack=True)

# convert eta (dimensionless parameter) to x1 (dimensional parameter)
### constants ###
C = 0.0   # [m]  upper root of spar
G = C     # [m]  lower root of spar
F = 91.9  # [m]  tip of spar
### dimensions specific to spar station #24 ###
D = 25.2  # [m]  upper part of joint transition
E = 41.5  # [m]  joint
### derived quantities ###
H = D     # [m]  lower part of joint transition
### conversions ###
x1_CD = eta_CD*(D-C) + C
x1_DE = eta_DE*(E-D) + D
x1_EF = eta_EF*(F-E) + E
x1_GH = eta_GH*(H-G) + G
x1_HE = eta_HE*(E-H) + H

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
#
# C    D
# x----x-
#        \ E    F
#         -x----x     (--> x1)
#        /
# x----x-
# G    H
#
# ---------------------------------
### CD
f_F1_CD = interp1d(x1_CD,F1_CD)
f_F2_CD = interp1d(x1_CD,F2_CD)
f_F3_CD = interp1d(x1_CD,F3_CD)
f_M1_CD = interp1d(x1_CD,M1_CD)
f_M2_CD = interp1d(x1_CD,M2_CD)
f_M3_CD = interp1d(x1_CD,M3_CD)
### DE
f_F1_DE = interp1d(x1_DE,F1_DE)
f_F2_DE = interp1d(x1_DE,F2_DE)
f_F3_DE = interp1d(x1_DE,F3_DE)
f_M1_DE = interp1d(x1_DE,M1_DE)
f_M2_DE = interp1d(x1_DE,M2_DE)
f_M3_DE = interp1d(x1_DE,M3_DE)
### EF
f_F1_EF = interp1d(x1_EF,F1_EF)
f_F2_EF = interp1d(x1_EF,F2_EF)
f_F3_EF = interp1d(x1_EF,F3_EF)
f_M1_EF = interp1d(x1_EF,M1_EF)
f_M2_EF = interp1d(x1_EF,M2_EF)
f_M3_EF = interp1d(x1_EF,M3_EF)
### GH
f_F1_GH = interp1d(x1_GH,F1_GH)
f_F2_GH = interp1d(x1_GH,F2_GH)
f_F3_GH = interp1d(x1_GH,F3_GH)
f_M1_GH = interp1d(x1_GH,M1_GH)
f_M2_GH = interp1d(x1_GH,M2_GH)
f_M3_GH = interp1d(x1_GH,M3_GH)
### HE
f_F1_HE = interp1d(x1_HE,F1_HE)
f_F2_HE = interp1d(x1_HE,F2_HE)
f_F3_HE = interp1d(x1_HE,F3_HE)
f_M1_HE = interp1d(x1_HE,M1_HE)
f_M2_HE = interp1d(x1_HE,M2_HE)
f_M3_HE = interp1d(x1_HE,M3_HE)
# ---------------------------------
# CD
f_F1_CD_new = extrap1d(f_F1_CD)
f_F2_CD_new = extrap1d(f_F2_CD)
f_F3_CD_new = extrap1d(f_F3_CD)
f_M1_CD_new = extrap1d(f_M1_CD)
f_M2_CD_new = extrap1d(f_M2_CD)
f_M3_CD_new = extrap1d(f_M3_CD)
# DE
f_F1_DE_new = extrap1d(f_F1_DE)
f_F2_DE_new = extrap1d(f_F2_DE)
f_F3_DE_new = extrap1d(f_F3_DE)
f_M1_DE_new = extrap1d(f_M1_DE)
f_M2_DE_new = extrap1d(f_M2_DE)
f_M3_DE_new = extrap1d(f_M3_DE)
# EF
f_F1_EF_new = extrap1d(f_F1_EF)
f_F2_EF_new = extrap1d(f_F2_EF)
f_F3_EF_new = extrap1d(f_F3_EF)
f_M1_EF_new = extrap1d(f_M1_EF)
f_M2_EF_new = extrap1d(f_M2_EF)
f_M3_EF_new = extrap1d(f_M3_EF)
# GH
f_F1_GH_new = extrap1d(f_F1_GH)
f_F2_GH_new = extrap1d(f_F2_GH)
f_F3_GH_new = extrap1d(f_F3_GH)
f_M1_GH_new = extrap1d(f_M1_GH)
f_M2_GH_new = extrap1d(f_M2_GH)
f_M3_GH_new = extrap1d(f_M3_GH)
# HE
f_F1_HE_new = extrap1d(f_F1_HE)
f_F2_HE_new = extrap1d(f_F2_HE)
f_F3_HE_new = extrap1d(f_F3_HE)
f_M1_HE_new = extrap1d(f_M1_HE)
f_M2_HE_new = extrap1d(f_M2_HE)
f_M3_HE_new = extrap1d(f_M3_HE)


# x1 coordinates of all 24 spar stations
x1_CD_new = np.array([0.0, 0.2, 2.3, 4.4, 6.5, 9.0, 12.2, 13.9, 15.5, 17.1, 19.8, 22.5, 25.2])
x1_GH_new = x1_CD_new
x1_DE_new = np.array([25.2, 33.4, 41.5])
x1_HE_new = x1_DE_new
x1_EF_new = np.array([41.5, 49.6, 57.8, 64.3, 65.9, 70.8, 74.0, 82.2, 87.0, 91.9])


# use extrapolations function returned by 'extrap1d'
### CD
F1_CD_new = f_F1_CD_new(x1_CD_new)
F2_CD_new = f_F2_CD_new(x1_CD_new)
F3_CD_new = f_F3_CD_new(x1_CD_new)
M1_CD_new = f_M1_CD_new(x1_CD_new)
M2_CD_new = f_M2_CD_new(x1_CD_new)
M3_CD_new = f_M3_CD_new(x1_CD_new)
### DE
F1_DE_new = f_F1_DE_new(x1_DE_new)
F2_DE_new = f_F2_DE_new(x1_DE_new)
F3_DE_new = f_F3_DE_new(x1_DE_new)
M1_DE_new = f_M1_DE_new(x1_DE_new)
M2_DE_new = f_M2_DE_new(x1_DE_new)
M3_DE_new = f_M3_DE_new(x1_DE_new)
### EF
F1_EF_new = f_F1_EF_new(x1_EF_new)
F2_EF_new = f_F2_EF_new(x1_EF_new)
F3_EF_new = f_F3_EF_new(x1_EF_new)
M1_EF_new = f_M1_EF_new(x1_EF_new)
M2_EF_new = f_M2_EF_new(x1_EF_new)
M3_EF_new = f_M3_EF_new(x1_EF_new)
### GH
F1_GH_new = f_F1_GH_new(x1_GH_new)
F2_GH_new = f_F2_GH_new(x1_GH_new)
F3_GH_new = f_F3_GH_new(x1_GH_new)
M1_GH_new = f_M1_GH_new(x1_GH_new)
M2_GH_new = f_M2_GH_new(x1_GH_new)
M3_GH_new = f_M3_GH_new(x1_GH_new)
### HE
F1_HE_new = f_F1_HE_new(x1_HE_new)
F2_HE_new = f_F2_HE_new(x1_HE_new)
F3_HE_new = f_F3_HE_new(x1_HE_new)
M1_HE_new = f_M1_HE_new(x1_HE_new)
M2_HE_new = f_M2_HE_new(x1_HE_new)
M3_HE_new = f_M3_HE_new(x1_HE_new)

print "*** writing results for each spar station ***"

f = open('svy_force_spar_new.mdt', 'w')
f.write('# biplane_spar_constload results, interpolated at each spar station\n')
f.write('#\n')
f.write('# biplane spar configuration: 24-bispar-rj452-g125 (untwisted, no root joint, half-height cross-sections)\n')
f.write('#\n')
f.write("""# C    D
# x----x-
#        \ E    F
#         -x----x     (--> x1)
#        /
# x----x-
# G    H
""")
f.write('#\n')
f.write("""# point C and G: (x1= 0.0)
# point D and H: (x1=25.2)
# point E:       (x1=41.5)
# point F:       (x1=91.9)
""")
f.write('#\n')
f.write('# stn  x1(m)  F1_upper' + ' '*13 + 'F2_upper' + ' '*13 + 'F3_upper' + ' '*13 + 'M1_upper' + ' '*13 + 'M2_upper' + ' '*13 + 'M3_upper' + ' '*13)
f.write('F1_lower' + ' '*13 + 'F2_lower' + ' '*13 + 'F3_lower' + ' '*13 + 'M1_lower' + ' '*13 + 'M2_lower' + ' '*13 + 'M3_lower\n')
f.write('# ---  -----' + '  -------------------'*12 + '\n')

C_stn = 1  # station  1: points C and G
D_stn = 13 # station 13: points D and H
E_stn = 15 # station 15: point  E
F_stn = 24 # station 24: point  F

for i in range(24):
    current_station = i+1
    if current_station < D_stn:  # inboard straight biplane (CD and GH)
        f.write(
            '%5i'     % current_station +  # station
            '%7.1f'   % x1_CD_new[i]    +  # x1
            '%21.12e' % F1_CD_new[i]    +  # F1_upper
            '%21.12e' % F2_CD_new[i]    +  # F2_upper
            '%21.12e' % F3_CD_new[i]    +  # F3_upper
            '%21.12e' % M1_CD_new[i]    +  # M1_upper
            '%21.12e' % M2_CD_new[i]    +  # M2_upper
            '%21.12e' % M3_CD_new[i]    +  # M3_upper
            '%21.12e' % F1_GH_new[i]    +  # F1_lower
            '%21.12e' % F2_GH_new[i]    +  # F2_lower
            '%21.12e' % F3_GH_new[i]    +  # F3_lower
            '%21.12e' % M1_GH_new[i]    +  # M1_lower
            '%21.12e' % M2_GH_new[i]    +  # M2_lower
            '%21.12e' % M3_GH_new[i]    +  # M3_lower
            '\n')
    elif current_station == D_stn:  # between inboard straight biplane and inboard joint transition (points D and H)
        # average data between CD and DE, and between GH and HE
        f.write(
            '%5i'     % current_station +  # station
            '%7.1f'   % x1_CD_new[-1]   +  # x1
            '%21.12e' % ((F1_CD_new[-1] + x1_DE_new[0])/2.0)    +  # F1_upper
            '%21.12e' % ((F2_CD_new[-1] + x1_DE_new[0])/2.0)    +  # F2_upper
            '%21.12e' % ((F3_CD_new[-1] + x1_DE_new[0])/2.0)    +  # F3_upper
            '%21.12e' % ((M1_CD_new[-1] + x1_DE_new[0])/2.0)    +  # M1_upper
            '%21.12e' % ((M2_CD_new[-1] + x1_DE_new[0])/2.0)    +  # M2_upper
            '%21.12e' % ((M3_CD_new[-1] + x1_DE_new[0])/2.0)    +  # M3_upper
            '%21.12e' % ((F1_GH_new[-1] + x1_HE_new[0])/2.0)    +  # F1_lower
            '%21.12e' % ((F2_GH_new[-1] + x1_HE_new[0])/2.0)    +  # F2_lower
            '%21.12e' % ((F3_GH_new[-1] + x1_HE_new[0])/2.0)    +  # F3_lower
            '%21.12e' % ((M1_GH_new[-1] + x1_HE_new[0])/2.0)    +  # M1_lower
            '%21.12e' % ((M2_GH_new[-1] + x1_HE_new[0])/2.0)    +  # M2_lower
            '%21.12e' % ((M3_GH_new[-1] + x1_HE_new[0])/2.0)    +  # M3_lower
            '\n')
    elif current_station > D_stn and current_station < E_stn:  # inboard joint transition (DE and HE)
        f.write(
            '%5i'     % current_station +  # station
            '%7.1f'   % x1_DE_new[i-(D_stn-1)]    +  # x1
            '%21.12e' % F1_DE_new[i-(D_stn-1)]    +  # F1_upper
            '%21.12e' % F2_DE_new[i-(D_stn-1)]    +  # F2_upper
            '%21.12e' % F3_DE_new[i-(D_stn-1)]    +  # F3_upper
            '%21.12e' % M1_DE_new[i-(D_stn-1)]    +  # M1_upper
            '%21.12e' % M2_DE_new[i-(D_stn-1)]    +  # M2_upper
            '%21.12e' % M3_DE_new[i-(D_stn-1)]    +  # M3_upper
            '%21.12e' % F1_HE_new[i-(D_stn-1)]    +  # F1_lower
            '%21.12e' % F2_HE_new[i-(D_stn-1)]    +  # F2_lower
            '%21.12e' % F3_HE_new[i-(D_stn-1)]    +  # F3_lower
            '%21.12e' % M1_HE_new[i-(D_stn-1)]    +  # M1_lower
            '%21.12e' % M2_HE_new[i-(D_stn-1)]    +  # M2_lower
            '%21.12e' % M3_HE_new[i-(D_stn-1)]    +  # M3_lower
            '\n')
    elif current_station == E_stn:  # between inboard joint transition and outboard monoplane (point E)
        # average data between DE, HE and EF
        f.write(
            '%5i'     % current_station +  # station
            '%7.1f'   % x1_DE_new[-1]    +  # x1
            '%21.12e' % ((F1_DE_new[-1] + x1_HE_new[-1] + x1_EF_new[0])/3.0)    +  # F1_EF ("upper")  # although this is data for the outbord monoplane, store it in the "upper" column
            '%21.12e' % ((F2_DE_new[-1] + x1_HE_new[-1] + x1_EF_new[0])/3.0)    +  # F2_EF ("upper")
            '%21.12e' % ((F3_DE_new[-1] + x1_HE_new[-1] + x1_EF_new[0])/3.0)    +  # F3_EF ("upper")
            '%21.12e' % ((M1_DE_new[-1] + x1_HE_new[-1] + x1_EF_new[0])/3.0)    +  # M1_EF ("upper")
            '%21.12e' % ((M2_DE_new[-1] + x1_HE_new[-1] + x1_EF_new[0])/3.0)    +  # M2_EF ("upper")
            '%21.12e' % ((M3_DE_new[-1] + x1_HE_new[-1] + x1_EF_new[0])/3.0)    +  # M3_EF ("upper")
            '\n')
    elif current_station > E_stn:  # outboard monoplane (EF)
        f.write(
            '%5i'     % current_station +  # station
            '%7.1f'   % x1_EF_new[i-(E_stn-1)]    +  # x1
            '%21.12e' % F1_EF_new[i-(E_stn-1)]    +  # F1_EF ("upper")  # although this is data for the outbord monoplane, store it in the "upper" column
            '%21.12e' % F2_EF_new[i-(E_stn-1)]    +  # F2_EF ("upper")
            '%21.12e' % F3_EF_new[i-(E_stn-1)]    +  # F3_EF ("upper")
            '%21.12e' % M1_EF_new[i-(E_stn-1)]    +  # M1_EF ("upper")
            '%21.12e' % M2_EF_new[i-(E_stn-1)]    +  # M2_EF ("upper")
            '%21.12e' % M3_EF_new[i-(E_stn-1)]    +  # M3_EF ("upper")
            '\n')

f.close()

print "*** finished ***"
# change back to the original directory
os.chdir('D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\postprocessing\\VABS')