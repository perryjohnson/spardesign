"""Plot edgewise deflections under a torsional tip load.

Usage: Open a pylab IPython prompt and type:
|> %run plot_edgewise_deflections_under_torsional_tipload

Author: Perry Roth-Johnson
Last updated: February 12, 2014

"""


import numpy as np
import matplotlib.pyplot as plt
import os
# from matplotlib import rc


# GLOBAL FLAGS
half_height_flag = True  # if false, don't run the case for a biplane
                         # spar with a half-height shear web

# get current working directory
fig_xx_dir = os.getcwd()

# adjust font sizes
# rc('font', size=18.0)  # make fonts bigger, for readable presentation slides

monoplane_dir = fig_xx_dir + '\\monoplane_spar\\torsional_tipload\\2e05\\FIGURES'

### constants ###
C = 0.0
G = C
F = 91.9

### parameters ###
scalefactor = 1.0  # figure size scale factor
fw=8               # figure width
fh=4               # figure height

glw=1.5            # global line width
gms=7.5            # global marker size
gmew=1.5           # global marker edge width
gmfc='None'        # global marker face color (none/empty)

mec_ms='red'       # marker edge color for monoplane spars
mec_bs_hh='blue'   # marker edge color for biplane spars, half-height cross-sections
mec_bs_fh='green'  # marker edge color for biplane spars, full-height cross-sections


# spar = '24-bispar-rj452-g125'
D = 25.2
E = 41.5
full_height_biplane_dir = fig_xx_dir + '\\full-height_biplane_spar\\torsional_tipload\\2e05\\FIGURES'
if half_height_flag:
    half_height_biplane_dir = fig_xx_dir + '\\half-height_biplane_spar\\torsional_tipload\\2e05\\FIGURES'


### derived quantities ###
H = D




plt.close('all')

# only plot results at each of the spar stations (every 3rd entry, since we used 3rd-order beam elements)
skip_every = 1
# x1 coordinates of all 24 spar stations
x1_stn = np.array([0.0, 0.2, 2.3, 4.4, 6.5, 9.0, 12.2, 13.9, 15.5, 17.1, 19.8, 22.5, 25.2, 33.4, 41.5, 49.6, 57.8, 64.3, 65.9, 70.8, 74.0, 82.2, 87.0, 91.9])


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


def plot_monospar_edgewise_deflection(skip_num):
    ### monoplane spar ###
    os.chdir(monoplane_dir)
    AB = np.loadtxt('svy_disp_spar.mdt')
    B = 91.9
    AB[:,0] = AB[:,0]*B
    plt.plot(AB[::skip_num,0], AB[::skip_num,2], 'rs--', markerfacecolor=gmfc, markersize=gms, linewidth=glw, markeredgewidth=gmew, markeredgecolor=mec_ms, label='monoplane spar', zorder=2)
    mono_defl_data = np.vstack( (AB[::skip_num,0],AB[::skip_num,2]) ).T
    plt.show()

    return mono_defl_data


def load_bispar_displacement():
    CD = np.loadtxt('svy_disp_CD.mdt')
    DE = np.loadtxt('svy_disp_DE.mdt')
    EF = np.loadtxt('svy_disp_EF.mdt')
    GH = np.loadtxt('svy_disp_GH.mdt')
    HE = np.loadtxt('svy_disp_HE.mdt')

    return (CD,DE,EF,GH,HE)


def process_bispar_results(CD,DE,EF,GH,HE,C,D,E,F,G,H):
    # post-process the biplane spar results
    # convert non-dimensional eta (column 0) to dimensional span (x1-coordinate)
    CD[:,0] = CD[:,0]*(D-C) + C  # upper inboard biplane
    DE[:,0] = DE[:,0]*(E-D) + D  # upper inboard biplane-monoplane transition
    EF[:,0] = EF[:,0]*(F-E) + E  # outboard monoplane
    GH[:,0] = GH[:,0]*(H-G) + G  # lower inboard biplane
    HE[:,0] = HE[:,0]*(E-H) + H  # lower inboard biplane-monoplane transition

    # consolidate the data from multiple arrays into two arrays:
    # ... one for the upper inboard biplane element + outboard monoplane
    bispar_upper = np.vstack( (CD[0:-1],DE[0:-1],EF) )
    # ... and another for the lower biplane element + outboard monoplane
    bispar_lower = np.vstack( (GH[0:-1],HE[0:-1],EF) )

    return (bispar_upper, bispar_lower)


def load_full_height_bispar_nn_displacement(C,D,E,F,G,H):
    os.chdir(full_height_biplane_dir)
    (CD,DE,EF,GH,HE) = load_bispar_displacement()
    (bispar_upper, bispar_lower) = process_bispar_results(CD,DE,EF,GH,HE,C,D,E,F,G,H)

    return (bispar_upper, bispar_lower)


def load_half_height_bispar_nn_displacement(C,D,E,F,G,H):
    os.chdir(half_height_biplane_dir)
    (CD,DE,EF,GH,HE) = load_bispar_displacement()
    (bispar_upper, bispar_lower) = process_bispar_results(CD,DE,EF,GH,HE,C,D,E,F,G,H)

    return (bispar_upper, bispar_lower)


def plot_full_height_bispar_edgewise_deflection(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[::skip_num,0], bispar_upper[::skip_num,2], 'go-', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_fh, label='biplane spar, upper', zorder=3)
    plt.plot(bispar_lower[::skip_num,0], bispar_lower[::skip_num,2], 'gx-', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_fh, label='biplane spar, lower', zorder=4)
    # plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower'), loc='lower left' )
    plt.show()

    bi_upper_defl_data = np.vstack( (bispar_upper[::skip_num,0], bispar_upper[::skip_num,2]) ).T
    bi_lower_defl_data = np.vstack( (bispar_lower[::skip_num,0], bispar_lower[::skip_num,2]) ).T

    return (bi_upper_defl_data, bi_lower_defl_data)


def plot_half_height_bispar_edgewise_deflection(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[::skip_num,0], bispar_upper[::skip_num,2], 'bo-.', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_hh, label='biplane spar, upper', zorder=3)
    plt.plot(bispar_lower[::skip_num,0], bispar_lower[::skip_num,2], 'bx-.', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_hh, label='biplane spar, lower', zorder=4)
    # plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower'), loc='lower left' )
    plt.show()

    bi_upper_defl_data = np.vstack( (bispar_upper[::skip_num,0], bispar_upper[::skip_num,2]) ).T
    bi_lower_defl_data = np.vstack( (bispar_lower[::skip_num,0], bispar_lower[::skip_num,2]) ).T

    return (bi_upper_defl_data, bi_lower_defl_data)


# compare deflections
plt.figure(figsize=(fw*scalefactor,fh*scalefactor))
plt.axes().set_aspect('auto')
mono_data = plot_monospar_edgewise_deflection(skip_every)
(full_height_bispar_upper, full_height_bispar_lower) = load_full_height_bispar_nn_displacement(C,D,E,F,G,H)
if half_height_flag:
    (half_height_bispar_upper, half_height_bispar_lower) = load_half_height_bispar_nn_displacement(C,D,E,F,G,H)
(bi_upper_data, bi_lower_data) = plot_full_height_bispar_edgewise_deflection(full_height_bispar_upper, full_height_bispar_lower, skip_every)
if half_height_flag:
    (bi_upper_data2, bi_lower_data2) = plot_half_height_bispar_edgewise_deflection(half_height_bispar_upper, half_height_bispar_lower, skip_every)
plt.plot([0,100],[0,0],'k:',linewidth=2.0, label='zeroline', zorder=1)  # plot zero-line of y-axis
plt.xlabel('span [m]')
plt.ylabel('edgewise deflections [m]')
plt.subplots_adjust(right=0.93, bottom=0.16)
plt.savefig(fig_xx_dir + '\\fig_xx_edgewise_deflections_under_torsional_tipload.eps')
plt.savefig(fig_xx_dir + '\\fig_xx_edgewise_deflections_under_torsional_tipload.png')


# return to the original directory
os.chdir(fig_xx_dir)