"""Generate a file that contains: spar station, x1, max stress, min stress

Procedure:
1. Read the *.ELE file for a spar station.
2. Find the maximum value of the stress component you are interested in.
3. Write 3 values to a file: spar station, x1, max stress component.
4. Repeat steps 1-3 for all spar stations.

"""

import numpy as np
import os
import glob  # Unix style pathname pattern expansion

# PARAMETERS #
ref_coords = 'b'
component = '2e_13'
recovery_dir = "D:\\data\\2012-10-05 (VABS recovery output for 24-bispar-rj425-g125, no root joint, full height SW)"
fname = component + "-v-span_24-bispar-fullSW.txt"

# print the parameters to screen
print "Reference coordinates: " + ref_coords
print "Strain/stress component: " + component
print "Directory with *.ELE files: \n\t" + recovery_dir
print "Results will be saved in: " + fname

# save the starting directory
starting_dir = os.getcwd()

# initialize spar stations
stns = range(1,25)
# initialize spanwise location [m] of each spar station
x1 = [0.0, 0.2, 2.3, 4.4, 6.5, 9.0, 12.2, 13.9, 15.5, 17.1, 19.8, 22.5, 25.2,
      33.4, 41.5, 49.6, 57.8, 64.3, 65.9, 70.8, 74.0, 82.2, 87.0, 91.9]
# initialize array of max stresses
max_stress = []
min_stress = []

# dictionary of 3D strain/stress variables to column numbers in *.ELE file
d = {'b': {  # beam coordinates
         'e_11': 1,
         '2e_12': 2,
         '2e_13': 3,
         'e_22': 4,
         '2e_23': 5,
         'e_33': 6,
         's_11': 7,
         's_12': 8,
         's_13': 9,
         's_22': 10,
         's_23': 11,
         's_33': 12
     },
     'm': {  # material coordinates
         'e_11': 13,
         '2e_12': 14,
         '2e_13': 15,
         'e_22': 16,
         '2e_23': 17,
         'e_33': 18,
         's_11': 19,
         's_12': 20,
         's_13': 21,
         's_22': 22,
         's_23': 23,
         's_33': 24
     }
    }
# usage: d['beam coords']['s_11']
# (returns 7)

os.chdir(recovery_dir)
# ELE_files = glob.glob('*.ELE')  # this only works for monoplane spars
ELE_lower = glob.glob('spar_station_??_lower.dat.ELE')
ELE_upper = glob.glob('spar_station_??_upper.dat.ELE')
ELE_mono = glob.glob('spar_station_??.dat.ELE')
ELE_files = []
for k in range(len(ELE_lower)):
    ELE_files.append([ELE_lower[k], ELE_upper[k]])
ELE_files += ELE_mono
if len(ELE_lower) == 0: k = -1

# read the max stress component for each spar station
for j,g in enumerate(ELE_files):
    print "reading station #" + str(stns[j]) + "..."
    if j > k:
        recovery_data = np.loadtxt(g)  # load mono data from recovery file
        col = d[ref_coords][component]
        max_stress.append(max(recovery_data[col]))
        min_stress.append(min(recovery_data[col]))
    else:
        recovery_data = np.loadtxt(g[0])
        col = d[ref_coords][component]
        max_stress_lower = max(recovery_data[col])
        min_stress_lower = min(recovery_data[col])
        recovery_data = np.loadtxt(g[1])
        col = d[ref_coords][component]
        max_stress_upper = max(recovery_data[col])
        min_stress_upper = min(recovery_data[col])
        max_stress.append([max_stress_lower, max_stress_upper])
        min_stress.append([min_stress_lower, min_stress_upper])

# construct the header
tab = " "*4
# head_vars = ["max(s_11,b)", "min(s_11,b)"]
head_vars = []
if k == -1:
    head_vars.append("max(" + component + "," + ref_coords + ")")
    head_vars.append("min(" + component + "," + ref_coords + ")")
else:
    head_vars.append("max(" + component + "," + ref_coords + "),l")
    head_vars.append("min(" + component + "," + ref_coords + "),l")
    head_vars.append("max(" + component + "," + ref_coords + "),u")
    head_vars.append("min(" + component + "," + ref_coords + "),u")
head = "# " + "spar_stn" + tab + " x1" + tab*2
for entry in head_vars:
    head += '{:<20}'.format(entry)
head += "\n"
hline = "# " + "-"*23 + "-"*20*len(head_vars) + "\n"

# open the file and write the header
os.chdir(starting_dir)
f = open(fname, 'w')
f.write(head)
f.write(hline)

# write the results to a file
for i,stn in enumerate(stns):
    station = str(stn)
    span = str(x1[i])
    if len(station) < 2: station = " " + station
    if len(span) < 4: span = " " + span
    if i <= k:  # biplane inboard region
        f.write(tab + station + tab*2 + span + tab 
                + ('%20.10e' % max_stress[i][0])
                + ('%20.10e' % min_stress[i][0])
                + ('%20.10e' % max_stress[i][1])
                + ('%20.10e' % min_stress[i][1]) + "\n")
    elif i == k+1:  # joint
        f.write(tab + station + tab*2 + span + tab
                + ('%20.10e' % max_stress[i])
                + ('%20.10e' % min_stress[i])
                + ('%20.10e' % max_stress[i])
                + ('%20.10e' % min_stress[i]) + "\n")
    else:  # monoplane outboard region
        f.write(tab + station + tab*2 + span + tab 
                + ('%20.10e' % max_stress[i])
                + ('%20.10e' % min_stress[i])
                + '{:<20}'.format('    NaN')
                + '{:<20}'.format('    NaN') + "\n")

f.close()

