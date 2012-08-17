## takes VABS input and output files, and writes a Tecplot input file
#   spar_station_24.dat     = VABS input file
#   nodes.txt               = nodes/coordinates from VABS input file
#   connectivity.txt        = element connectivity from VABS input file
#   spar_station_24.dat.ELE = VABS output file with averaged 3D strain/stress data for each element
#   spar_station_24_tp.dat  = Tecplot input file

import numpy as np

# load data from VABS input file
node_no, x2, x3 = np.loadtxt('nodes.txt', unpack=True)
conn = np.loadtxt('connectivity.txt', dtype=int, usecols=(1,2,3,4))
elem_no, e11_b, e12_b, e13_b, e22_b, e23_b, e33_b, s11_b, s12_b, s13_b, s22_b, s23_b, s33_b, e11_m, e12_m, e13_m, e22_m, e23_m, e33_m, s11_m, s12_m, s13_m, s22_m, s23_m, s33_m = np.loadtxt('spar_station_24.dat.ELE', unpack=True)

# store number of nodes (nnode) and number of elements (nelem)
nnode = int(node_no[-1])
nelem = int(elem_no[-1])

# open a new file for the Tecplot input file
tpFile = open('spar_station_24_tp.dat', 'w+')

# write the header for the Tecplot input file
tpFile.write(
"""TITLE="Avg 3D strain/stress for each element"
VARIABLES="x2" "x3" "e11_b" "e12_b" "e13_b" "e22_b" "e23_b" "e33_b" "s11_b" "s12_b" "s13_b" "s22_b" "s23_b" "s33_b" "e11_m" "e12_m" "e13_m" "e22_m" "e23_m" "e33_m" "s11_m" "s12_m" "s13_m" "s22_m" "s23_m" "s33_m"
ZONE T="isorect", N=10192, E=2896, ZONETYPE=FEQUADRILATERAL, DATAPACKING=BLOCK, VARLOCATION=([3-26]=CELLCENTERED)
"""
)

## write a column of data for one variable as a row for Tecplot
##      input:  varname <np.array>, array containing the variable's data
##              nn <int>, number of data entries in the array
##      output: writes the data to tpFile (file object)
def writeVarRow(varname, nn):
    for i in range(nn):
        tpFile.write(str('%19.10E' % varname[i]))
        if (i+1)%200 == 0:
            tpFile.write('\ \n')
    tpFile.write('\n')

# write all the data in the Tecplot input file
tpFile.write('# x2\n')
writeVarRow(x2, nnode)

tpFile.write('# x3\n')
writeVarRow(x3, nnode)

tpFile.write('# e11_b\n')
writeVarRow(e11_b, nelem)

tpFile.write('# e12_b\n')
writeVarRow(e12_b, nelem)

tpFile.write('# e13_b\n')
writeVarRow(e13_b, nelem)

tpFile.write('# e22_b\n')
writeVarRow(e22_b, nelem)

tpFile.write('# e23_b\n')
writeVarRow(e23_b, nelem)

tpFile.write('# e33_b\n')
writeVarRow(e33_b, nelem)

tpFile.write('# s11_b\n')
writeVarRow(s11_b, nelem)

tpFile.write('# s12_b\n')
writeVarRow(s12_b, nelem)

tpFile.write('# s13_b\n')
writeVarRow(s13_b, nelem)

tpFile.write('# s22_b\n')
writeVarRow(s22_b, nelem)

tpFile.write('# s23_b\n')
writeVarRow(s23_b, nelem)

tpFile.write('# s33_b\n')
writeVarRow(s33_b, nelem)

tpFile.write('# e11_m\n')
writeVarRow(e11_m, nelem)

tpFile.write('# e12_m\n')
writeVarRow(e12_m, nelem)

tpFile.write('# e13_m\n')
writeVarRow(e13_m, nelem)

tpFile.write('# e22_m\n')
writeVarRow(e22_m, nelem)

tpFile.write('# e23_m\n')
writeVarRow(e23_m, nelem)

tpFile.write('# e33_m\n')
writeVarRow(e33_m, nelem)

tpFile.write('# s11_m\n')
writeVarRow(s11_m, nelem)

tpFile.write('# s12_m\n')
writeVarRow(s12_m, nelem)

tpFile.write('# s13_m\n')
writeVarRow(s13_m, nelem)

tpFile.write('# s22_m\n')
writeVarRow(s22_m, nelem)

tpFile.write('# s23_m\n')
writeVarRow(s23_m, nelem)

tpFile.write('# s33_m\n')
writeVarRow(s33_m, nelem)

tpFile.write('\n# connectivity\n')
for i in range(nelem):
    for j in range(4):
        tpFile.write(str('%8i' % conn[i,j]))
    tpFile.write('\n')

tpFile.close()