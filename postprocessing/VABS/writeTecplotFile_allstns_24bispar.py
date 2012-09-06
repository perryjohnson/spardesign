## takes VABS input and output files, and writes a Tecplot input file
#############   spar_station_24.dat     = VABS input file
#   nodes.txt               = nodes/coordinates from VABS input file
#   connectivity.txt        = element connectivity from VABS input file
#   spar_station_24.dat.ELE = VABS output file with averaged 3D strain/stress data for each element
#   spar_station_24_tp.dat  = Tecplot input file

import numpy as np
import os

# spar_stn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # generate [M] and [K] matrices for these spar stations
spar_stn_list = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # generate [M] and [K] matrices for these spar stations

os.chdir('../../VABS/input_files')
for n in range(len(spar_stn_list)):
    spar_station = spar_stn_list[n]
    if spar_station < 15:
        biplane_cx_flag = True
    else:
        biplane_cx_flag = False

    if spar_station == 14:
        curved_cx_flag = True
    else:
        curved_cx_flag = False

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

    VABS_input_file = basefilestr + '.dat'
    if biplane_cx_flag:
        VABS_input_file2 = basefilestr2 + '.dat'


    # load data from VABS input file ############################################################################
    f = open(VABS_input_file, 'r')   # read the file
    VABS_input_data = f.readlines()  # parse all characters in file into one long string
    f.close()
    if curved_cx_flag:
        nnode = int(VABS_input_data[5].split(' ')[0])  # total number of nodes     # use this line for a curved cross-section
        nelem = int(VABS_input_data[5].split(' ')[1])  # total number of elements  # use this line for a curved cross-section
    else:
        nnode = int(VABS_input_data[4].split(' ')[0])  # total number of nodes
        nelem = int(VABS_input_data[4].split(' ')[1])  # total number of elements

    nodeFile = open('nodes.txt', 'w+')  # create a temp file to store all the nodes
    if curved_cx_flag:
        node_block_start_line = 7  # use this line for a curved cross-section
    else:
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
    # reuse node_no, x2, x3, conn in VABS_input_file2 as well ... they're the same in both the upper and lower cross-sections!

    # load data from VABS recovery file #########################################################################
    VABS_recovery_file = VABS_input_file + '.ELE'
    elem_no, e11_b, e12_b, e13_b, e22_b, e23_b, e33_b, s11_b, s12_b, s13_b, s22_b, s23_b, s33_b, e11_m, e12_m, e13_m, e22_m, e23_m, e33_m, s11_m, s12_m, s13_m, s22_m, s23_m, s33_m = np.loadtxt(VABS_recovery_file, unpack=True)
    if biplane_cx_flag:
        VABS_recovery_file2 = VABS_input_file2 + '.ELE'
        elem_no2, e11_b2, e12_b2, e13_b2, e22_b2, e23_b2, e33_b2, s11_b2, s12_b2, s13_b2, s22_b2, s23_b2, s33_b2, e11_m2, e12_m2, e13_m2, e22_m2, e23_m2, e33_m2, s11_m2, s12_m2, s13_m2, s22_m2, s23_m2, s33_m2 = np.loadtxt(VABS_recovery_file2, unpack=True)

    # open a new file for the Tecplot input file
    tpFile = open(VABS_input_file + '.tp', 'w+')
    if biplane_cx_flag:
        tpFile2 = open(VABS_input_file2 + '.tp', 'w+')

    # write the header for the Tecplot input file
    tpFile.write(
    """TITLE="Avg 3D strain/stress for each element"
    VARIABLES="x2" "x3" "e11_b" "e12_b" "e13_b" "e22_b" "e23_b" "e33_b" "s11_b" "s12_b" "s13_b" "s22_b" "s23_b" "s33_b" "e11_m" "e12_m" "e13_m" "e22_m" "e23_m" "e33_m" "s11_m" "s12_m" "s13_m" "s22_m" "s23_m" "s33_m"
    ZONE T="upper element", ZONETYPE=FEQUADRILATERAL, DATAPACKING=BLOCK, VARLOCATION=([3-26]=CELLCENTERED)"""
    )
    if biplane_cx_flag:
        tpFile2.write(
        """TITLE="Avg 3D strain/stress for each element"
        VARIABLES="x2" "x3" "e11_b" "e12_b" "e13_b" "e22_b" "e23_b" "e33_b" "s11_b" "s12_b" "s13_b" "s22_b" "s23_b" "s33_b" "e11_m" "e12_m" "e13_m" "e22_m" "e23_m" "e33_m" "s11_m" "s12_m" "s13_m" "s22_m" "s23_m" "s33_m"
        ZONE T="lower element", ZONETYPE=FEQUADRILATERAL, DATAPACKING=BLOCK, VARLOCATION=([3-26]=CELLCENTERED)"""
        )
    tpFile.write(', N=' + str(nnode) + ', E=' + str(nelem) + '\n')
    if biplane_cx_flag:
        tpFile2.write(', N=' + str(nnode) + ', E=' + str(nelem) + '\n')

    ## write a column of data for one variable as a row for Tecplot
    ##      input:  fobj <file object>, the file object to write data to
    ##              varname <np.array>, array containing the variable's data
    ##              nn <int>, number of data entries in the array
    ##      output: writes the data to tpFile (file object)
    def writeVarRow(fobj, varname, nn):
        for i in range(nn):
            fobj.write(str('%19.10E' % varname[i]))
            if (i+1)%200 == 0:
                fobj.write('\ \n')
        fobj.write('\n')

    # write all the data in the Tecplot input file
    tpFile.write('# x2\n')
    writeVarRow(tpFile, x2, nnode)
    if biplane_cx_flag:
        tpFile2.write('# x2\n')
        writeVarRow(tpFile2, x2, nnode)

    tpFile.write('# x3\n')
    if biplane_cx_flag:
        writeVarRow(tpFile, (x3+4.768), nnode)  # upper element of biplane cross-section
        tpFile2.write('# x3\n')
        writeVarRow(tpFile2, (x3-4.768), nnode)  # lower element of biplane cross-section
    else:
        writeVarRow(tpFile, x3, nnode) # monoplane cross-section

    tpFile.write('# e11_b\n')
    writeVarRow(tpFile, e11_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e11_b\n')
        writeVarRow(tpFile2, e11_b2, nelem)

    tpFile.write('# e12_b\n')
    writeVarRow(tpFile, e12_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e12_b\n')
        writeVarRow(tpFile2, e12_b2, nelem)

    tpFile.write('# e13_b\n')
    writeVarRow(tpFile, e13_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e13_b\n')
        writeVarRow(tpFile2, e13_b2, nelem)

    tpFile.write('# e22_b\n')
    writeVarRow(tpFile, e22_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e22_b\n')
        writeVarRow(tpFile2, e22_b2, nelem)

    tpFile.write('# e23_b\n')
    writeVarRow(tpFile, e23_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e23_b\n')
        writeVarRow(tpFile2, e23_b2, nelem)

    tpFile.write('# e33_b\n')
    writeVarRow(tpFile, e33_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e33_b\n')
        writeVarRow(tpFile2, e33_b2, nelem)

    tpFile.write('# s11_b\n')
    writeVarRow(tpFile, s11_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s11_b\n')
        writeVarRow(tpFile2, s11_b2, nelem)

    tpFile.write('# s12_b\n')
    writeVarRow(tpFile, s12_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s12_b\n')
        writeVarRow(tpFile2, s12_b2, nelem)

    tpFile.write('# s13_b\n')
    writeVarRow(tpFile, s13_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s13_b\n')
        writeVarRow(tpFile2, s13_b2, nelem)

    tpFile.write('# s22_b\n')
    writeVarRow(tpFile, s22_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s22_b\n')
        writeVarRow(tpFile2, s22_b2, nelem)

    tpFile.write('# s23_b\n')
    writeVarRow(tpFile, s23_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s23_b\n')
        writeVarRow(tpFile2, s23_b2, nelem)

    tpFile.write('# s33_b\n')
    writeVarRow(tpFile, s33_b, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s33_b\n')
        writeVarRow(tpFile2, s33_b2, nelem)

    tpFile.write('# e11_m\n')
    writeVarRow(tpFile, e11_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e11_m\n')
        writeVarRow(tpFile2, e11_m2, nelem)

    tpFile.write('# e12_m\n')
    writeVarRow(tpFile, e12_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e12_m\n')
        writeVarRow(tpFile2, e12_m2, nelem)

    tpFile.write('# e13_m\n')
    writeVarRow(tpFile, e13_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e13_m\n')
        writeVarRow(tpFile2, e13_m2, nelem)

    tpFile.write('# e22_m\n')
    writeVarRow(tpFile, e22_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e22_m\n')
        writeVarRow(tpFile2, e22_m2, nelem)

    tpFile.write('# e23_m\n')
    writeVarRow(tpFile, e23_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e23_m\n')
        writeVarRow(tpFile2, e23_m2, nelem)

    tpFile.write('# e33_m\n')
    writeVarRow(tpFile, e33_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# e33_m\n')
        writeVarRow(tpFile2, e33_m2, nelem)

    tpFile.write('# s11_m\n')
    writeVarRow(tpFile, s11_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s11_m\n')
        writeVarRow(tpFile2, s11_m2, nelem)

    tpFile.write('# s12_m\n')
    writeVarRow(tpFile, s12_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s12_m\n')
        writeVarRow(tpFile2, s12_m2, nelem)

    tpFile.write('# s13_m\n')
    writeVarRow(tpFile, s13_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s13_m\n')
        writeVarRow(tpFile2, s13_m2, nelem)

    tpFile.write('# s22_m\n')
    writeVarRow(tpFile, s22_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s22_m\n')
        writeVarRow(tpFile2, s22_m2, nelem)

    tpFile.write('# s23_m\n')
    writeVarRow(tpFile, s23_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s23_m\n')
        writeVarRow(tpFile2, s23_m2, nelem)

    tpFile.write('# s33_m\n')
    writeVarRow(tpFile, s33_m, nelem)
    if biplane_cx_flag:
        tpFile2.write('# s33_m\n')
        writeVarRow(tpFile2, s33_m2, nelem)

    tpFile.write('\n# connectivity\n')
    for i in range(nelem):
        for j in range(4):
            tpFile.write(str('%8i' % conn[i,j]))
        tpFile.write('\n')
    if biplane_cx_flag:
        tpFile2.write('\n# connectivity\n')
        for i in range(nelem):
            for j in range(4):
                tpFile2.write(str('%8i' % conn[i,j]))
            tpFile2.write('\n')

    tpFile.close()
    if biplane_cx_flag:
        tpFile2.close()

os.chdir('../../postprocessing/VABS/')