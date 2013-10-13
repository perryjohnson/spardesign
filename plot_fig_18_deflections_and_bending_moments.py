"""Figure 18, deflection and bending moment vs. span

Caption:
Comparison of spar deflections and bending moments under load, calculated with
the computational model (DYMORE): a monoplane spar, a biplane spar with "full-
height" biplane cross-sections, and a biplane spar with "half-height" biplane
cross-sections. Both biplane spars had design parameters of rj/R = 0.452 and
g/c = 1.25.

Usage: Open a pylab IPython prompt and type:
|> %run plot_fig_18_deflections_and_bending_moments

Alternative usage: Open a Windows command prompt and type:
> python plot_fig_18_deflections_and_bending_moments.py


Author: Perry Roth-Johnson
Last updated: July 25, 2013

"""


import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import rc


# GLOBAL FLAGS
plot_half_height_SW_flag = False  # if false, don't run the case for a biplane
                                  # spar with a half-height shear web

# get current working directory
fig_18_dir = os.getcwd()

# adjust font sizes
rc('font', size=18.0)  # make fonts bigger, for readable presentation slides

monoplane_dir = fig_18_dir + '\\monoplane_spar\\untwisted\\grid_density_1\\FIGURES'

### constants ###
C = 0.0
G = C
F = 91.9

### parameters ###
scalefactor = 1.6  # figure size scale factor
fw=7               # figure width
fh=3               # figure height

glw=3.0            # global line width
gms=10.0           # global marker size
gmew=2.0           # global marker edge width
gmfc='None'        # global marker face color (none/empty)

mec_ms='red'       # marker edge color for monoplane spars
mec_bs_hh='blue'   # marker edge color for biplane spars, half-height cross-sections
mec_bs_fh='green'  # marker edge color for biplane spars, full-height cross-sections


# spar = '24-bispar-rj452-g125'
D = 25.2
E = 41.5
biplane_dir = fig_18_dir + '\\biplane_spar\\untwisted-noRootJoint_full-hSW\\24-bispar-rj452-g125\\FIGURES'
if plot_half_height_SW_flag:
    biplane_dir2 = fig_18_dir + '\\biplane_spar\\untwisted-noRootJoint\\24-bispar-rj452-g125\\FIGURES'


### derived quantities ###
H = D




plt.close('all')

# only plot results at each of the spar stations (every 3rd entry, since we used 3rd-order beam elements)
skip_every = 3
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


def plot_monospar_deflection(skip_num):
    ### monoplane spar ###
    os.chdir(monoplane_dir)
    AB = np.loadtxt('svy_disp_spar.mdt')
    B = 91.9
    AB[:,0] = AB[:,0]*B
    plt.plot(AB[::skip_num,0], AB[::skip_num,3], 'rs--', markerfacecolor=gmfc, markersize=gms, linewidth=glw, markeredgewidth=gmew, markeredgecolor=mec_ms, label='monoplane spar', zorder=2)
    mono_defl_data = np.vstack( (AB[::skip_num,0],AB[::skip_num,3]) ).T
    plt.show()

    return mono_defl_data


def plot_monospar_axialforce(x1):
    """
Plots the axial force resultant vs. span for the monoplane spar.

Input
-----
x1 <np.array>: x1-coordinates of all 24 spar stations

    """
    ### monoplane spar ###
    os.chdir(monoplane_dir)
    # read in all forces and moments calculated by DYMORE
    AB = np.loadtxt('svy_force_spar.mdt')
    # the spar length, 91.9 meters
    B = 91.9
    # multiply column 0 (eta-coordinates) by the spar length, B
    AB[:,0] = AB[:,0]*B

    # plot the span (column 0) along the x-axis
    x = AB[:,0]
    # plot the axial (along x1) force resultant (column 1) along the y-axis
    y = AB[:,1]
    # get force results at all the spar stations, using interpolation
    # (instead of using the default results at Gaussian integration points)
    f_i = interp1d(x,y)
    f_x = extrap1d(f_i)
    y1 = f_x(x1)  # use extrapolations function returned by 'extrap1d'

    # plot the results to the screen
    plt.plot(x1, y1/1000.0, 'rs--', markerfacecolor=gmfc, markersize=gms, linewidth=glw, markeredgewidth=gmew, markeredgecolor=mec_ms,  label='monoplane spar', zorder=2)
    plt.show()

    return


def plot_monospar_bendmoment(x1):
    """
Plots the bending moment vs. span for the monoplane spar.

Input
-----
x1 <np.array>: x1-coordinates of all 24 spar stations

    """
    ### monoplane spar ###
    os.chdir(monoplane_dir)
    # read in all forces and moments calculated by DYMORE
    AB = np.loadtxt('svy_force_spar.mdt')
    # the spar length, 91.9 meters
    B = 91.9
    # multiply column 0 (eta-coordinates) by the spar length, B
    AB[:,0] = AB[:,0]*B

    # plot the span (column 0) along the x-axis
    x = AB[:,0]
    # plot the flapwise (about x2) bending moment (column 5) along the y-axis
    y = AB[:,5]
    # get bending moment results at all the spar stations, using interpolation
    # (instead of using the default results at Gaussian integration points)
    f_i = interp1d(x,y)
    f_x = extrap1d(f_i)
    y1 = f_x(x1)  # use extrapolations function returned by 'extrap1d'

    # plot the results to the screen
    plt.plot(x1, y1/1000.0, 'rs--', markerfacecolor=gmfc, markersize=gms, linewidth=glw, markeredgewidth=gmew, markeredgecolor=mec_ms,  label='monoplane spar', zorder=2)
    plt.show()

    return

def load_bispar_displacement():
    CD = np.loadtxt('svy_disp_CD.mdt')
    DE = np.loadtxt('svy_disp_DE.mdt')
    EF = np.loadtxt('svy_disp_EF.mdt')
    GH = np.loadtxt('svy_disp_GH.mdt')
    HE = np.loadtxt('svy_disp_HE.mdt')

    return (CD,DE,EF,GH,HE)


def load_bispar_force():
    CD = np.loadtxt('svy_force_CD.mdt')
    DE = np.loadtxt('svy_force_DE.mdt')
    EF = np.loadtxt('svy_force_EF.mdt')
    GH = np.loadtxt('svy_force_GH.mdt')
    HE = np.loadtxt('svy_force_HE.mdt')

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


def load_bispar_nn_displacement(C,D,E,F,G,H):
    os.chdir(biplane_dir)
    (CD,DE,EF,GH,HE) = load_bispar_displacement()
    (bispar_upper, bispar_lower) = process_bispar_results(CD,DE,EF,GH,HE,C,D,E,F,G,H)

    return (bispar_upper, bispar_lower)


def load_bispar_nn_displacement2(C,D,E,F,G,H):
    os.chdir(biplane_dir2)
    (CD,DE,EF,GH,HE) = load_bispar_displacement()
    (bispar_upper, bispar_lower) = process_bispar_results(CD,DE,EF,GH,HE,C,D,E,F,G,H)

    return (bispar_upper, bispar_lower)


def load_bispar_nn_force(C,D,E,F,G,H):
    os.chdir(biplane_dir)
    (CD,DE,EF,GH,HE) = load_bispar_force()
    (bispar_upper, bispar_lower) = process_bispar_results(CD,DE,EF,GH,HE,C,D,E,F,G,H)

    return (bispar_upper, bispar_lower)


def load_bispar_nn_force2(C,D,E,F,G,H):
    os.chdir(biplane_dir2)
    (CD,DE,EF,GH,HE) = load_bispar_force()
    (bispar_upper, bispar_lower) = process_bispar_results(CD,DE,EF,GH,HE,C,D,E,F,G,H)

    return (bispar_upper, bispar_lower)


def plot_bispar_deflection(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[::skip_num,0], bispar_upper[::skip_num,3], 'go-', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_fh, label='biplane spar, upper', zorder=3)
    plt.plot(bispar_lower[::skip_num,0], bispar_lower[::skip_num,3], 'gx-', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_fh, label='biplane spar, lower', zorder=4)
    # plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower'), loc='lower left' )
    plt.show()

    bi_upper_defl_data = np.vstack( (bispar_upper[::skip_num,0], bispar_upper[::skip_num,3]) ).T
    bi_lower_defl_data = np.vstack( (bispar_lower[::skip_num,0], bispar_lower[::skip_num,3]) ).T

    return (bi_upper_defl_data, bi_lower_defl_data)


def plot_bispar_deflection2(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[::skip_num,0], bispar_upper[::skip_num,3], 'bo-.', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_hh, label='biplane spar, upper', zorder=3)
    plt.plot(bispar_lower[::skip_num,0], bispar_lower[::skip_num,3], 'bx-.', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_hh, label='biplane spar, lower', zorder=4)
    # plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower'), loc='lower left' )
    plt.show()

    bi_upper_defl_data = np.vstack( (bispar_upper[::skip_num,0], bispar_upper[::skip_num,3]) ).T
    bi_lower_defl_data = np.vstack( (bispar_lower[::skip_num,0], bispar_lower[::skip_num,3]) ).T

    return (bi_upper_defl_data, bi_lower_defl_data)


def plot_bispar_bendmoment(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[:,0], bispar_upper[:,4]/1000.0, 'go-', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_fh, label='biplane spar, upper', zorder=3)
    plt.plot(bispar_lower[:,0], bispar_lower[:,4]/1000.0, 'gx-', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_fh, label='biplane spar, lower', zorder=4)
    # plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower') )
    plt.show()
    return


def plot_bispar_bendmoment2(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[:,0], bispar_upper[:,6]/1000.0, 'bo-.', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_hh, label='biplane spar, upper', zorder=3)
    plt.plot(bispar_lower[:,0], bispar_lower[:,6]/1000.0, 'bx-.', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_hh, label='biplane spar, lower', zorder=4)
    # plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower') )
    plt.show()
    return


def plot_bispar_axialforce(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[:,0], bispar_upper[:,1]/1000.0, 'go-', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_fh, label='biplane spar, upper', zorder=3)
    plt.plot(bispar_lower[:,0], bispar_lower[:,1]/1000.0, 'gx-', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_fh, label='biplane spar, lower', zorder=4)
    # plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower') )
    plt.show()
    return


def plot_bispar_axialforce2(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[:,0], bispar_upper[:,1]/1000.0, 'bo-.', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_hh, label='biplane spar, upper', zorder=3)
    plt.plot(bispar_lower[:,0], bispar_lower[:,1]/1000.0, 'bx-.', markersize=gms, linewidth=glw, markerfacecolor=gmfc, markeredgewidth=gmew, markeredgecolor=mec_bs_hh, label='biplane spar, lower', zorder=4)
    # plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower') )
    plt.show()
    return


# compare deflections
plt.figure(figsize=(fw*scalefactor,fh*scalefactor))
plt.axes().set_aspect('auto')
mono_data = plot_monospar_deflection(skip_every)
(bispar_upper, bispar_lower) = load_bispar_nn_displacement(C,D,E,F,G,H)
if plot_half_height_SW_flag:
    (bispar_upper2, bispar_lower2) = load_bispar_nn_displacement2(C,D,E,F,G,H)
(bi_upper_data, bi_lower_data) = plot_bispar_deflection(bispar_upper, bispar_lower, skip_every)
if plot_half_height_SW_flag:
    (bi_upper_data2, bi_lower_data2) = plot_bispar_deflection2(bispar_upper2, bispar_lower2, skip_every)
plt.plot([0,100],[0,0],'k:',linewidth=2.0, label='zeroline', zorder=1)  # plot zero-line of y-axis
plt.xlabel('span [m]')
plt.ylabel('twist angle [rad]')
plt.subplots_adjust(left=0.10, right=0.97, bottom=0.13, top=0.96)
plt.savefig(fig_18_dir + '\\fig_18a_deflections.pdf')
plt.savefig(fig_18_dir + '\\fig_18a_deflections.png')


# compare bending moments
plt.figure(figsize=(fw*scalefactor,fh*scalefactor))
plt.axes().set_aspect('auto')
plot_monospar_bendmoment(x1_stn)
(bispar_upper, bispar_lower) = load_bispar_nn_force(C,D,E,F,G,H)
if plot_half_height_SW_flag:
    (bispar_upper2, bispar_lower2) = load_bispar_nn_force2(C,D,E,F,G,H)
plot_bispar_bendmoment(bispar_upper, bispar_lower, skip_every)
if plot_half_height_SW_flag:
    plot_bispar_bendmoment2(bispar_upper2, bispar_lower2, skip_every)
plt.plot([0,100],[0,0],'k:',linewidth=2.0, label='zeroline', zorder=1)  # plot zero-line of y-axis
plt.xlabel('span [m]')
plt.ylabel('torsional moment [kN*m]')
plt.subplots_adjust(left=0.12, right=0.97, bottom=0.13, top=0.96)
plt.savefig(fig_18_dir + '\\fig_18b_bendmoment.pdf')
plt.savefig(fig_18_dir + '\\fig_18b_bendmoment.png')


# compare axial force resultants
plt.figure(figsize=(fw*scalefactor,fh*scalefactor))
plt.axes().set_aspect('auto')
plot_monospar_axialforce(x1_stn)
(bispar_upper, bispar_lower) = load_bispar_nn_force(C,D,E,F,G,H)
if plot_half_height_SW_flag:
    (bispar_upper2, bispar_lower2) = load_bispar_nn_force2(C,D,E,F,G,H)
plot_bispar_axialforce(bispar_upper, bispar_lower, skip_every)
if plot_half_height_SW_flag:
    plot_bispar_axialforce2(bispar_upper2, bispar_lower2, skip_every)
plt.plot([0,100],[0,0],'k:',linewidth=2.0, label='zeroline', zorder=1)  # plot zero-line of y-axis
plt.xlabel('span [m]')
plt.ylabel('axial force resultant [kN]')
plt.subplots_adjust(left=0.10, right=0.97, bottom=0.13, top=0.96)
plt.savefig(fig_18_dir + '\\fig_18c_axialforce.pdf')
plt.savefig(fig_18_dir + '\\fig_18c_axialforce.png')


# return to the original directory
os.chdir(fig_18_dir)