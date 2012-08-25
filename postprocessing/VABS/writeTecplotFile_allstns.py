## takes VABS input and output files, and writes a Tecplot input file
#############   spar_station_24.dat     = VABS input file
#   nodes.txt               = nodes/coordinates from VABS input file
#   connectivity.txt        = element connectivity from VABS input file
#   spar_station_24.dat.ELE = VABS output file with averaged 3D strain/stress data for each element
#   spar_station_24_tp.dat  = Tecplot input file

import numpy as np
import os

spar_stn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # generate [M] and [K] matrices for these spar stations

os.chdir('../../VABS/input_files')
for n in range(len(spar_stn_list)):
    spar_station = spar_stn_list[n]
    if spar_station < 10:
        basefilestr = 'spar_station_0' + str(spar_station)
    else:
        basefilestr = 'spar_station_' + str(spar_station)

    print ''
    print '***************'
    print basefilestr
    print '***************'

    VABS_input_file = basefilestr + '.dat'


    # load data from VABS input file ############################################################################
    f = open(VABS_input_file, 'r')   # read the file
    VABS_input_data = f.readlines()  # parse all characters in file into one long string
    nnode = int(VABS_input_data[4].split(' ')[0])  # total number of nodes
    nelem = int(VABS_input_data[4].split(' ')[1])  # total number of elements

    nodeFile = open('nodes.txt', 'w+')  # create a temp file to store all the nodes
    node_block_start_line = 6
    node_block_end_line = node_block_start_line+nnode
    for i in range(node_block_start_line,node_block_end_line):
        nodeFile.write(VABS_input_data[i])
    nodeFile.close()
    node_no, x2, x3 = np.loadtxt('nodes.txt', unpack=True)  # store all the nodes in an array
    os.remove('nodes.txt')  # delete the temp file

    connFile = open('connectivity.txt', 'w+')  # create a temp file to store the element connectivity
    conn_block_start_line = node_block_end_line+1
    conn_block_end_line = conn_block_start_line+nelem
    for i in range(conn_block_start_line,conn_block_end_line):
        connFile.write(VABS_input_data[i])
    connFile.close()
    conn = np.loadtxt('connectivity.txt', dtype=int, usecols=(1,2,3,4))
    os.remove('connectivity.txt')  # delete the temp file


    # load data from VABS recovery file #########################################################################
    VABS_recovery_file = VABS_input_file + '.ELE'
    elem_no, e11_b, e12_b, e13_b, e22_b, e23_b, e33_b, s11_b, s12_b, s13_b, s22_b, s23_b, s33_b, e11_m, e12_m, e13_m, e22_m, e23_m, e33_m, s11_m, s12_m, s13_m, s22_m, s23_m, s33_m = np.loadtxt(VABS_recovery_file, unpack=True)

    # open a new file for the Tecplot input file
    tpFile = open(VABS_input_file + '.tp', 'w+')

    # write the header for the Tecplot input file
    tpFile.write(
    """TITLE="Avg 3D strain/stress for each element"
    VARIABLES="x2" "x3" "e11_b" "e12_b" "e13_b" "e22_b" "e23_b" "e33_b" "s11_b" "s12_b" "s13_b" "s22_b" "s23_b" "s33_b" "e11_m" "e12_m" "e13_m" "e22_m" "e23_m" "e33_m" "s11_m" "s12_m" "s13_m" "s22_m" "s23_m" "s33_m"
    ZONE T="isorect", ZONETYPE=FEQUADRILATERAL, DATAPACKING=BLOCK, VARLOCATION=([3-26]=CELLCENTERED)"""
    )
    tpFile.write(', N=' + str(nnode) + ', E=' + str(nelem) + '\n')

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

os.chdir('../../postprocessing/VABS/')