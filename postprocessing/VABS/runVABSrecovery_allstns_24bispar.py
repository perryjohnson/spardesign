import os
import numpy as np

VABS_normal_flag = True
VABS_recovery_flag = True

spar_stn_list = [13]  # generate [M] and [K] matrices for these spar stations
# spar_stn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # generate [M] and [K] matrices for these spar stations

# store extrapolated results from DYMORE (biplane_spar_constload/untwisted-noRootJoint/24-bispar-rj452-g125/FIGURES/svy_force_spar_new.mdt)
os.chdir('D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\biplane_spar_constload\\untwisted-noRootJoint\\24-bispar-rj452-g125\\FIGURES')
# F1, F2, F3, M1, M2, M3 = np.loadtxt('svy_force_spar_new.mdt', usecols=(2,3,4,5,6,7), unpack=True)
stn, x1, F1_upper, F2_upper, F3_upper, M1_upper, M2_upper, M3_upper, F1_lower, F2_lower, F3_lower, M1_lower, M2_lower, M3_lower = np.loadtxt('svy_force_spar_new.mdt', unpack=True)

os.chdir('D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\VABS')

for n in range(len(spar_stn_list)):
    spar_station = spar_stn_list[n]
    if spar_station < 15:
        biplane_cx_flag = True
    else:
        biplane_cx_flag = False

    if spar_station < 10:
        basefilestr = 'spar_station_0' + str(spar_station)
    else:
        basefilestr = 'spar_station_' + str(spar_station)

    if biplane_cx_flag:
        basefilestr2 = basefilestr + '_lower'
        basefilestr = basefilestr + '_upper'

    print ''
    print '***************'
    print basefilestr
    if biplane_cx_flag:
        print basefilestr2
    print '***************'

    vabs_filename = basefilestr + '.dat'
    if biplane_cx_flag:
        vabs_filename2 = basefilestr2 + '.dat'

    if VABS_normal_flag:
        print "\n**********"
        print "running VABS in normal mode..."
        # os.chdir('../../VABS')
        vabs_command = r'.\VABSIII .\input_files\ '[:-1] + vabs_filename
        os.system(vabs_command)
        if biplane_cx_flag:
            vabs_command2 = r'.\VABSIII .\input_files\ '[:-1] + vabs_filename2
            os.system(vabs_command2)

    print "\n**********"
    print "setting recover_flag = 1"
    f = open('./input_files/'+vabs_filename, 'r+')   # read the file
    f.readline()  # skip the first line of the VABS input file
    recover_flag_line_pos = f.tell() # save the position of the line containing the recover_flag
    f.seek(recover_flag_line_pos)
    f.write('1 1 0')  # set recover_flag = 1
    f.close()
    if biplane_cx_flag:
        f = open('./input_files/'+vabs_filename2, 'r+')   # read the file
        f.readline()  # skip the first line of the VABS input file
        recover_flag_line_pos = f.tell() # save the position of the line containing the recover_flag
        f.seek(recover_flag_line_pos)
        f.write('1 1 0')  # set recover_flag = 1
        f.close()

    print "\n**********"
    print "writing recovery mode inputs"
    # set default values for recovery mode inputs
    recovery_dict = {# ui: 1D beam displacements
                     'u1'  :  0.0,  # displacement along x1
                     'u2'  :  0.0,  # displacement along x2
                     'u3'  :  0.0,  # displacement along x3

                     # Cij: direction cosine matrix between undeformed triad and deformed triad on beam reference line
                     #   Bi = Ci1*b1 + Ci2*b2 + Ci3*b3  with i=1,2,3
                     #   where B1, B2, B3 are the base vectors of the deformed triad
                     #         b1, b2, b3 are the base vectors of the undeformed triad
                     'C11' :  1.0,     'C12' :  0.0,     'C13' :  0.0,
                     'C21' :  0.0,     'C22' :  1.0,     'C23' :  0.0,
                     'C31' :  0.0,     'C32' :  0.0,     'C33' :  1.0,

                     # Fi: cross-sectional forces
                     'F1'  :  0.0,  # axial force along x1 (tension/compression)
                     'F2'  :  0.0,  # transverse force along x2 (edgewise shear)
                     'F3'  :  0.0,  # transverse force along x3 (flapwise shear)

                     # Mi: cross-sectional moments
                     'M1'  :  0.0,  # moment about x1 (torque)
                     'M2'  :  0.0,  # moment about x2 (flapwise bending)
                     'M3'  :  0.0,  # moment about x3 (edgewise bending)

                     # fi and mi: applied loads
                     #   fi: distributed forces (including both applied and inertial forces)
                     #   mi: distributed moments (including both applied and inertial moments)
                     'f1'  :  0.0,  # distributed force per unit span along x1
                     'f2'  :  0.0,  # distributed force per unit span along x2
                     'f3'  : -1.0,  # distributed force per unit span along x3
                     'm1'  :  0.0,  # distributed moment per unit span about x1
                     'm2'  :  0.0,  # distributed moment per unit span about x2
                     'm3'  :  0.0,  # distributed moment per unit span about x3

                     # fi,1 and mi,1: 1st derivative of applied loads, wrt x1 (beam axis) ... d(...)/dx1
                     'f1,1':  0.0,  # d(f1)/dx1
                     'f2,1':  0.0,  # d(f2)/dx1
                     'f3,1':  0.0,  # d(f3)/dx1
                     'm1,1':  0.0,  # d(m1)/dx1
                     'm2,1':  0.0,  # d(m2)/dx1
                     'm3,1':  0.0,  # d(m3)/dx1

                     # f_i,2 and m_i,2: 2nd derivative of applied loads, wrt x1 (beam axis) ... d^2(...)/dx1^2
                     'f1,2':  0.0,  # d^2(f1)/dx1^2
                     'f2,2':  0.0,  # d^2(f2)/dx1^2
                     'f3,2':  0.0,  # d^2(f3)/dx1^2
                     'm1,2':  0.0,  # d^2(m1)/dx1^2
                     'm2,2':  0.0,  # d^2(m2)/dx1^2
                     'm3,2':  0.0   # d^2(m3)/dx1^2
                     }

    # overwrite new values for recovery mode inputs...

    # applied loads from DYMORE (biplane_spar_constload/untwisted-noRootJoint/24-bispar-rj452-g125/loadDist.dat)
    recovery_dict['f3'] = -500.0  # [N/m] constant load distribution, flapwise direction (on biplane cross-sections)
    # recovery_dict['f3'] = -1000.0  # [N/m] constant load distribution, flapwise direction (on monoplane cross-sections)

    recovery_dict['F1'] = F1_upper[spar_station-1]  # take the row for the current spar station; index 0 has data for station 1
    recovery_dict['F2'] = F2_upper[spar_station-1]
    recovery_dict['F3'] = F3_upper[spar_station-1]
    recovery_dict['M1'] = M1_upper[spar_station-1]
    recovery_dict['M2'] = M2_upper[spar_station-1]
    recovery_dict['M3'] = M3_upper[spar_station-1]
    if biplane_cx_flag:
        recovery_dict2 = recovery_dict.copy()
        recovery_dict2['F1'] = F1_lower[spar_station-1]  # take the row for the current spar station; index 0 has data for station 1
        recovery_dict2['F2'] = F2_lower[spar_station-1]
        recovery_dict2['F3'] = F3_lower[spar_station-1]
        recovery_dict2['M1'] = M1_lower[spar_station-1]
        recovery_dict2['M2'] = M2_lower[spar_station-1]
        recovery_dict2['M3'] = M3_lower[spar_station-1]

    f = open('./input_files/'+vabs_filename, 'a')   # append the file
    # write the recovery mode inputs at the end of the VABS input file
    f.write('\n' +
        # ui: 1D beam displacements
        ('%19.12e' % recovery_dict['u1']) + ('%20.12e' % recovery_dict['u2']) + ('%20.12e' % recovery_dict['u3']) + '\n' +

        # Cij: direction cosine matrix
        ('%19.12e' % recovery_dict['C11']) + ('%20.12e' % recovery_dict['C12']) + ('%20.12e' % recovery_dict['C13']) + '\n' +
        ('%19.12e' % recovery_dict['C21']) + ('%20.12e' % recovery_dict['C22']) + ('%20.12e' % recovery_dict['C23']) + '\n' +
        ('%19.12e' % recovery_dict['C31']) + ('%20.12e' % recovery_dict['C32']) + ('%20.12e' % recovery_dict['C33']) + '\n' +

        # Fi and Mi: cross-sectional forces and moments
        ('%19.12e' % recovery_dict['F1']) + ('%20.12e' % recovery_dict['M1']) + ('%20.12e' % recovery_dict['M2']) + ('%20.12e' % recovery_dict['M3']) + '\n' +
        ('%19.12e' % recovery_dict['F2']) + ('%20.12e' % recovery_dict['F3']) + '\n' +

        # fi and mi: applied loads
        ('%19.12e' % recovery_dict['f1']) + ('%20.12e' % recovery_dict['f2']) + ('%20.12e' % recovery_dict['f3']) + ('%20.12e' % recovery_dict['m1']) + ('%20.12e' % recovery_dict['m2']) + ('%20.12e' % recovery_dict['m3']) + '\n' +

        # fi,1 and mi,1: 1st derivative of applied loads
        ('%19.12e' % recovery_dict['f1,1']) + ('%20.12e' % recovery_dict['f2,1']) + ('%20.12e' % recovery_dict['f3,1']) + ('%20.12e' % recovery_dict['m1,1']) + ('%20.12e' % recovery_dict['m2,1']) + ('%20.12e' % recovery_dict['m3,1']) + '\n' +

        # fi,2 and mi,2: 2nd derivative of applied loads
        ('%19.12e' % recovery_dict['f1,2']) + ('%20.12e' % recovery_dict['f2,2']) + ('%20.12e' % recovery_dict['f3,2']) + ('%20.12e' % recovery_dict['m1,2']) + ('%20.12e' % recovery_dict['m2,2']) + ('%20.12e' % recovery_dict['m3,2']) + '\n'
        )
    f.close()
    if biplane_cx_flag:
        f = open('./input_files/'+vabs_filename2, 'a')   # append the file
        # write the recovery mode inputs at the end of the VABS input file
        f.write('\n' +
            # ui: 1D beam displacements
            ('%19.12e' % recovery_dict2['u1']) + ('%20.12e' % recovery_dict2['u2']) + ('%20.12e' % recovery_dict2['u3']) + '\n' +

            # Cij: direction cosine matrix
            ('%19.12e' % recovery_dict2['C11']) + ('%20.12e' % recovery_dict2['C12']) + ('%20.12e' % recovery_dict2['C13']) + '\n' +
            ('%19.12e' % recovery_dict2['C21']) + ('%20.12e' % recovery_dict2['C22']) + ('%20.12e' % recovery_dict2['C23']) + '\n' +
            ('%19.12e' % recovery_dict2['C31']) + ('%20.12e' % recovery_dict2['C32']) + ('%20.12e' % recovery_dict2['C33']) + '\n' +

            # Fi and Mi: cross-sectional forces and moments
            ('%19.12e' % recovery_dict2['F1']) + ('%20.12e' % recovery_dict2['M1']) + ('%20.12e' % recovery_dict2['M2']) + ('%20.12e' % recovery_dict2['M3']) + '\n' +
            ('%19.12e' % recovery_dict2['F2']) + ('%20.12e' % recovery_dict2['F3']) + '\n' +

            # fi and mi: applied loads
            ('%19.12e' % recovery_dict2['f1']) + ('%20.12e' % recovery_dict2['f2']) + ('%20.12e' % recovery_dict2['f3']) + ('%20.12e' % recovery_dict2['m1']) + ('%20.12e' % recovery_dict2['m2']) + ('%20.12e' % recovery_dict2['m3']) + '\n' +

            # fi,1 and mi,1: 1st derivative of applied loads
            ('%19.12e' % recovery_dict2['f1,1']) + ('%20.12e' % recovery_dict2['f2,1']) + ('%20.12e' % recovery_dict2['f3,1']) + ('%20.12e' % recovery_dict2['m1,1']) + ('%20.12e' % recovery_dict2['m2,1']) + ('%20.12e' % recovery_dict2['m3,1']) + '\n' +

            # fi,2 and mi,2: 2nd derivative of applied loads
            ('%19.12e' % recovery_dict2['f1,2']) + ('%20.12e' % recovery_dict2['f2,2']) + ('%20.12e' % recovery_dict2['f3,2']) + ('%20.12e' % recovery_dict2['m1,2']) + ('%20.12e' % recovery_dict2['m2,2']) + ('%20.12e' % recovery_dict2['m3,2']) + '\n'
            )
        f.close()

    if VABS_recovery_flag:
        print "\n**********"
        print "running VABS in recovery mode..."
        os.system(vabs_command)
        if biplane_cx_flag:
            os.system(vabs_command2)

# change back to the original directory
os.chdir('D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\postprocessing\\VABS')