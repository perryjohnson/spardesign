import numpy as np
import matplotlib.pyplot as plt
import os

monoplane_dir = 'D:\\data\\2012-03-05 (truegrid-VABS-DYMORE mesh refinement)\\grid_density_1\\dymore\\FIGURES'

### SET THESE PARAMETERS FOR THE BIPLANE SPAR ###########################################
# 07-bispar-rj629-g100 (with root joint)
biplane_dir = 'D:\\data\\2012-05-18 (biplane spars, with root joint, full shear web height)\\07-bispar-rj629-g100\\FIGURES'
A = 0.0
B = 0.2
C = 4.4
D = 41.5
E = 57.8
F = 91.9
G = C
H = D


#########################################################################################


os.chdir('D:\\data')

plt.close('all')

skip_every = 3  # only plot results at each of the spar stations (every 3rd entry, since we used 3rd-order beam elements)
x1_stn = np.array([0.0, 0.2, 2.3, 4.4, 6.5, 9.0, 12.2, 13.9, 15.5, 17.1, 19.8, 22.5, 25.2, 33.4, 41.5, 49.6, 57.8, 64.3, 65.9, 70.8, 74.0, 82.2, 87.0, 91.9])  # x1 coordinates of all 24 spar stations
cs_heights_mono = np.array([5.392, 5.375, 5.089, 4.791, 4.455, 4.101, 3.680, 3.480, 3.285, 3.089, 2.882, 2.696, 2.498, 2.077, 1.672, 1.360, 1.138, 0.954, 0.910, 0.832, 0.796, 0.707, 0.651, 0.508])  # cross-sectional heights of all 24 monoplane spar stations
I_mono = np.array([3.8579, 3.6622, 3.0272, 2.5015, 2.2209, 1.8770, 1.6211, 1.5493, 1.4031, 1.3126, 1.1129, 0.9500, 0.7632, 0.4710, 0.2702, 0.1574, 0.0920, 0.0526, 0.0452, 0.0300, 0.0220, 0.0111, 0.0067, 0.0028])  # second moment of area of all 24 monoplane spar stations

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
    plt.plot(AB[::skip_num,0], AB[::skip_num,3], 'bo--', label='monoplane spar')
    mono_defl_data = np.vstack( (AB[::skip_num,0],AB[::skip_num,3]) ).T
    plt.show()

    return mono_defl_data


def plot_monospar_rotation(skip_num):
    ### monoplane spar ###
    os.chdir(monoplane_dir)
    AB = np.loadtxt('svy_disp_spar.mdt')
    B = 91.9
    AB[:,0] = AB[:,0]*B
    plt.plot(AB[::skip_num,0], AB[::skip_num,5], 'bo--', label='monoplane spar')
    plt.show()

    return


def plot_monospar_shearforce(x1):
    ### monoplane spar ###
    os.chdir(monoplane_dir)
    AB = np.loadtxt('svy_force_spar.mdt')
    B = 91.9
    AB[:,0] = AB[:,0]*B

    x = AB[:,0]
    y = AB[:,3]
    f_i = interp1d(x,y)
    f_x = extrap1d(f_i)

    # x1 = np.array([0.0, 0.2, 2.3, 4.4, 6.5, 9.0, 12.2, 13.9, 15.5, 17.1, 19.8, 22.5, 25.2, 33.4, 41.5, 49.6, 57.8, 64.3, 65.9, 70.8, 74.0, 82.2, 87.0, 91.9])  # x1 coordinates of all 24 spar stations
    # y1 = f(x1)  # use interpolations function returned by 'interp1d'
    y1 = f_x(x1)  # use extrapolations function returned by 'extrap1d'

    # plt.plot(x, y, 'o', x1, y1, 'rs-')  # test that interpolation and extrapolation are working properly
    plt.plot(x1, y1, 'bo--', label='monoplane spar')
    plt.show()

    return


def plot_monospar_bendmoment(x1):
    ### monoplane spar ###
    os.chdir(monoplane_dir)
    AB = np.loadtxt('svy_force_spar.mdt')
    B = 91.9
    AB[:,0] = AB[:,0]*B

    x = AB[:,0]
    y = AB[:,5]
    f_i = interp1d(x,y)
    f_x = extrap1d(f_i)

    # x1 = np.array([0.0, 0.2, 2.3, 4.4, 6.5, 9.0, 12.2, 13.9, 15.5, 17.1, 19.8, 22.5, 25.2, 33.4, 41.5, 49.6, 57.8, 64.3, 65.9, 70.8, 74.0, 82.2, 87.0, 91.9])  # x1 coordinates of all 24 spar stations
    y1 = f_x(x1)  # use extrapolations function returned by 'extrap1d'

    # plt.plot(x, y, 'o', x1, y1, 'rs-')
    plt.plot(x1, y1, 'bo--', label='monoplane spar')
    plt.show()

    return


def plot_monospar_stress(x1, h, I):
    ### monoplane spar ###
    os.chdir(monoplane_dir)
    AB = np.loadtxt('svy_force_spar.mdt')
    B = 91.9
    AB[:,0] = AB[:,0]*B

    x = AB[:,0]
    y = AB[:,5]
    f_i = interp1d(x,y)
    f_x = extrap1d(f_i)

    M = f_x(x1)  # use extrapolations function returned by 'extrap1d'

    # how to calculate bending stress...
    #   sigma = (M*h)/I,  where
    #     sigma = bending stress [N/m^2]
    #     M     = bending moment [N*m]
    #     h     = the perpendicular distance to the neutral axis (cs_heights[i]/2)
    #     I     = second moment of area about the neutral axis

    sigma = (M*h)/I

    # plt.plot(AB[::skip_num,0], cs_heights*AB[::skip_num,5], 'b--', label='monoplane spar')

    plt.plot(x1, sigma, 'bo--', label='monoplane spar')
    plt.show()

    return


def load_bispar_displacement():
    AB = np.loadtxt('svy_disp_AB.mdt')
    BC = np.loadtxt('svy_disp_BC.mdt')
    BG = np.loadtxt('svy_disp_BG.mdt')
    CD = np.loadtxt('svy_disp_CD.mdt')
    DE = np.loadtxt('svy_disp_DE.mdt')
    EF = np.loadtxt('svy_disp_EF.mdt')
    GH = np.loadtxt('svy_disp_GH.mdt')
    HE = np.loadtxt('svy_disp_HE.mdt')

    return (AB,BC,CD,DE,EF,BG,GH,HE)


def load_bispar_force():
    AB = np.loadtxt('svy_force_AB.mdt')
    BC = np.loadtxt('svy_force_BC.mdt')
    BG = np.loadtxt('svy_force_BG.mdt')
    CD = np.loadtxt('svy_force_CD.mdt')
    DE = np.loadtxt('svy_force_DE.mdt')
    EF = np.loadtxt('svy_force_EF.mdt')
    GH = np.loadtxt('svy_force_GH.mdt')
    HE = np.loadtxt('svy_force_HE.mdt')

    return (AB,BC,CD,DE,EF,BG,GH,HE)


def load_bispar_strain():
    AB = np.loadtxt('svy_strain_AB.mdt')
    BC = np.loadtxt('svy_strain_BC.mdt')
    BG = np.loadtxt('svy_strain_BG.mdt')
    CD = np.loadtxt('svy_strain_CD.mdt')
    DE = np.loadtxt('svy_strain_DE.mdt')
    EF = np.loadtxt('svy_strain_EF.mdt')
    GH = np.loadtxt('svy_strain_GH.mdt')
    HE = np.loadtxt('svy_strain_HE.mdt')

    return (AB,BC,CD,DE,EF,BG,GH,HE)


def process_bispar_results(AB,BC,CD,DE,EF,BG,GH,HE,A,B,C,D,E,F,G,H):
    # post-process the biplane spar results
    AB[:,0] = AB[:,0]*(B-A) + A
    BC[:,0] = BC[:,0]*(C-B) + B
    CD[:,0] = CD[:,0]*(D-C) + C
    DE[:,0] = DE[:,0]*(E-D) + D
    EF[:,0] = EF[:,0]*(F-E) + E
    BG[:,0] = BG[:,0]*(G-B) + B
    GH[:,0] = GH[:,0]*(H-G) + G
    HE[:,0] = HE[:,0]*(E-H) + H

    bispar_upper = np.vstack( (AB[0:-1],BC[0:-1],CD[0:-1],DE[0:-1],EF) )
    bispar_lower = np.vstack( (AB[0:-1],BG[0:-1],GH[0:-1],HE[0:-1],EF) )

    return (bispar_upper, bispar_lower)


def load_bispar_nn_displacement(A,B,C,D,E,F,G,H):
    os.chdir(biplane_dir)

    (AB,BC,CD,DE,EF,BG,GH,HE) = load_bispar_displacement()

    (bispar_upper, bispar_lower) = process_bispar_results(AB,BC,CD,DE,EF,BG,GH,HE,A,B,C,D,E,F,G,H)

    return (bispar_upper, bispar_lower)


def load_bispar_nn_force(A,B,C,D,E,F,G,H):
    os.chdir(biplane_dir)

    (AB,BC,CD,DE,EF,BG,GH,HE) = load_bispar_force()

    (bispar_upper, bispar_lower) = process_bispar_results(AB,BC,CD,DE,EF,BG,GH,HE,A,B,C,D,E,F,G,H)

    return (bispar_upper, bispar_lower)


def plot_bispar_deflection(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[::skip_num,0], bispar_upper[::skip_num,3], 'rs-', label='biplane spar, upper')
    plt.plot(bispar_lower[::skip_num,0], bispar_lower[::skip_num,3], 'g^-', label='biplane spar, lower')
    plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower') )
    plt.show()

    bi_upper_defl_data = np.vstack( (bispar_upper[::skip_num,0], bispar_upper[::skip_num,3]) ).T
    bi_lower_defl_data = np.vstack( (bispar_lower[::skip_num,0], bispar_lower[::skip_num,3]) ).T

    return (bi_upper_defl_data, bi_lower_defl_data)


def plot_bispar_rotation(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[::skip_num,0], bispar_upper[::skip_num,5], 'rs-', label='biplane spar, upper')
    plt.plot(bispar_lower[::skip_num,0], bispar_lower[::skip_num,5], 'g^-', label='biplane spar, lower')
    plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower'), loc='upper left' )
    plt.show()
    return


def plot_bispar_shearforce(bispar_upper, bispar_lower, x1):
    x_upper = bispar_upper[:,0]
    y_upper = bispar_upper[:,3]
    f_i_upper = interp1d(x_upper, y_upper)
    f_x_upper = extrap1d(f_i_upper)

    y1_upper = f_x_upper(x1)  # use extrapolations function returned by 'extrap1d'

    # plt.plot(x_upper, y_upper, 'g^', x1, y1_upper, 'rs-')  # test plot to make sure extrapolation is working

    plt.plot(bispar_upper[:,0], bispar_upper[:,3], 'rs-', label='biplane spar, upper')
    plt.plot(bispar_lower[:,0], bispar_lower[:,3], 'g^-', label='biplane spar, lower')
    plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower'), loc='lower right')
    plt.show()
    return


def plot_bispar_bendmoment(bispar_upper, bispar_lower, skip_num):
    plt.plot(bispar_upper[:,0], bispar_upper[:,5], 'rs-', label='biplane spar, upper')
    plt.plot(bispar_lower[:,0], bispar_lower[:,5], 'g^-', label='biplane spar, lower')
    plt.legend( ('monoplane spar', 'biplane spar, upper', 'biplane spar, lower') )
    plt.show()
    return


# compare deflections
plt.figure()
plt.title('deflections')
plt.axes().set_aspect('auto')
mono_data = plot_monospar_deflection(skip_every)
(bispar_upper, bispar_lower) = load_bispar_nn_displacement(A,B,C,D,E,F,G,H)
(bi_upper_data, bi_lower_data) = plot_bispar_deflection(bispar_upper, bispar_lower, skip_every)
plt.xlabel('span [m]')
plt.ylabel('deflection in x3-direction [m]')


# # plot deflection reductions
# plt.figure()
# plt.title('deflection reductions')
# ax = plt.subplot(111)
# from matplotlib.ticker import MultipleLocator, FormatStrFormatter
# majorFormatter = FormatStrFormatter('%d%%')  # double the percent sign, so that it shows up as a character in the formatted string
# minorLocator = MultipleLocator(5)
# ax.yaxis.set_major_formatter(majorFormatter)
# ax.yaxis.set_minor_locator(minorLocator)
# upper_percent = np.divide(abs(bi_upper_data[1:,1]), abs(mono_data[1:,1]))*100.0
# lower_percent = np.divide(abs(bi_lower_data[1:,1]), abs(mono_data[1:,1]))*100.0
# print 'monoplane', mono_data[1,1]
# print 'biplane (upper)', bi_upper_data[1,1]
# print 'biplane (lower)', bi_lower_data[1,1]
# a = np.array([0,91.9])
# b = np.array([100.0,100.0])
# plt.plot(a, b, 'b--', label='monoplane (baseline)')
# plt.plot(mono_data[1:,0], upper_percent, 'rs-', label='biplane spar, upper')
# plt.plot(mono_data[1:,0], lower_percent, 'g^-', label='biplane spar, lower')
# plt.legend( ('monoplane (baseline)', 'biplane spar, upper', 'biplane spar, lower'), loc='lower right' )
# plt.xlabel('span [m]')
# plt.ylabel('ratio of biplane-to-monoplane deflection in x3-direction [-]')
# plt.ylim(0,120)
# plt.show()


# compare rotations
plt.figure()
plt.title('rotations')
plt.axes().set_aspect('auto')
plot_monospar_rotation(skip_every)
plot_bispar_rotation(bispar_upper, bispar_lower, skip_every)
plt.xlabel('span [m]')
plt.ylabel('rotation about x2-axis [rad]')


# compare shear forces
plt.figure()
plt.title('shear forces')
plt.axes().set_aspect('auto')
plot_monospar_shearforce(x1_stn)
(bispar_upper, bispar_lower) = load_bispar_nn_force(A,B,C,D,E,F,G,H)
plot_bispar_shearforce(bispar_upper, bispar_lower, x1_stn)
plt.xlabel('span [m]')
plt.ylabel('shear force in x3-direction [N]')


# compare bending moments
plt.figure()
plt.title('bending moments')
plt.axes().set_aspect('auto')
plot_monospar_bendmoment(x1_stn)
(bispar_upper, bispar_lower) = load_bispar_nn_force(A,B,C,D,E,F,G,H)
plot_bispar_bendmoment(bispar_upper, bispar_lower, skip_every)
plt.xlabel('span [m]')
plt.ylabel('bending moment about x2-axis [N*m]')


# # compare stresses
# plt.figure()
# plt.title('stresses')
# plt.axes().set_aspect('auto')
# plot_monospar_stress(x1_stn, cs_heights_mono/2.0, I_mono)
# plt.xlabel('span [m]')
# plt.ylabel('stresses in x1-direction [N*m]')


# return to the original directory
os.chdir('D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\postprocessing')