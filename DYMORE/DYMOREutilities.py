import numpy as np


## read a file into memory
##    input: filestr <string>, the filename of the file to be read into memory
##    output: fileLines <list of strings>, a list of strings, each of which represents one line in the file
def readFile(filestr):
    f = open(filestr, 'r')  # read the file
    fileLines = f.readlines()  # parse all characters in file into one long string
    return fileLines


## define regular expressions to search for mass and stiffness matrices in VABS-formatted output file
##    input: <none>
##    output: nnPat <object>, regex pattern for 'nn'
def defineRegularExpressions():
    import re
    cm_x2_pat = re.compile(r'\s\sXm2 =.+')
    cm_x3_pat = re.compile(r'\s\sXm3 =.+')
    mpus_pat = re.compile(r'\sMass Per Unit Span\s+=.+')
    i1_pat = re.compile(r'\sMass Moments of Intertia about x1 axis\s+=.+')
    i2_pat = re.compile(r'\sMass Moments of Intertia about x2 axis\s+=.+')
    i3_pat = re.compile(r'\sMass Moments of Intertia about x3 axis\s+=.+')
    K_head_pat = re.compile(r'\sTimoshenko Stiffness Matrix.+')
    
    return (cm_x2_pat, cm_x3_pat, mpus_pat, i1_pat, i2_pat, i3_pat, K_head_pat)


def pullMKmatrices(MKlines, print_flag=False):
    (cm_x2_pat, cm_x3_pat, mpus_pat, i1_pat, i2_pat, i3_pat, K_head_pat) = defineRegularExpressions()

    for i in range(len(MKlines)):
        cm_x2_match = cm_x2_pat.match(MKlines[i])
        cm_x3_match = cm_x3_pat.match(MKlines[i])
        mpus_match = mpus_pat.match(MKlines[i])
        i1_match = i1_pat.match(MKlines[i])
        i2_match = i2_pat.match(MKlines[i])
        i3_match = i3_pat.match(MKlines[i])
        K_head_match = K_head_pat.match(MKlines[i])

        if cm_x2_match:
            cm_x2 = float(MKlines[i].replace('Xm2 =',''))
        elif cm_x3_match:
            cm_x3 = float(MKlines[i].replace('Xm3 =',''))
        elif mpus_match:
            mpus = float(MKlines[i].replace('Mass Per Unit Span                     =',''))
        elif i1_match:
            i1 = float(MKlines[i].replace('Mass Moments of Intertia about x1 axis =',''))
        elif i2_match:
            i2 = float(MKlines[i].replace('Mass Moments of Intertia about x2 axis =',''))
        elif i3_match:
            i3 = float(MKlines[i].replace('Mass Moments of Intertia about x3 axis =',''))
        elif K_head_match:
            K_head_line = i

    K_row_1 = np.fromstring(MKlines[K_head_line+3], sep=' ')
    K_row_2 = np.fromstring(MKlines[K_head_line+4], sep=' ')
    K_row_3 = np.fromstring(MKlines[K_head_line+5], sep=' ')
    K_row_4 = np.fromstring(MKlines[K_head_line+6], sep=' ')
    K_row_5 = np.fromstring(MKlines[K_head_line+7], sep=' ')
    K_row_6 = np.fromstring(MKlines[K_head_line+8], sep=' ')
    K = np.vstack((K_row_1,K_row_2,K_row_3,K_row_4,K_row_5,K_row_6))

    if print_flag:
        print "center of mass, x2 = " + str(cm_x2)
        print "center of mass, x3 = " + str(cm_x3)
        print "mass per unit span = " + str(mpus)
        print "moment of inertia about x1 axis = " + str(i1)
        print "moment of inertia about x2 axis = " + str(i2)
        print "moment of inertia about x3 axis = " + str(i3)
        print ""
        print "Stiffness matrix:"
        print K

    return (cm_x2, cm_x3, mpus, i1, i2, i3, K)


## make temp file on hard disk to store DYMORE-formatted mass and stiffness matrices
##    input:  <none>
##    output: tempFile <object>, file handle to temp file
def makeMKfile():
    tempFile = open('dymoreMK.txt', 'w+')
    return tempFile


def writeDymoreMK(f, eta, cm_x2, cm_x3, mpus, i1, i2, i3, K):
    # example output:
    #
    # @ETA_COORDINATE {0.00000e+00} {
    #   @STIFFNESS_MATRIX { 7.6443255182E+09,   -3.5444961981E-04,   -1.5092432335E-03,    3.3599749794E+06,    2.7710007447E-01,    4.1602501550E-02,
    #                                            2.8284702841E+08,   -2.8863166160E+01,   -4.5930836014E-01,   -3.3517886643E+05,    3.4162114776E-03,
    #                                                                 3.5606703330E+08,   -4.0749872012E-01,    3.6079611429E-02,   -4.2577508629E+04,
    #                                                                                      8.8773955810E+08,    1.8897378940E-03,    8.3869473951E-04,
    #                                                                                                           4.5282893600E+10,   -5.7686739280E-02,
    #                                                                                                                                2.2625281359E+09}
    #   @MASS_PER_UNIT_SPAN {7.1224712000E+02}
    #   @MOMENTS_OF_INERTIA {3.9569408290E+03,
    #                        3.6961203640E+03,
    #                        2.6082046495E+02}
    #   @CENTRE_OF_MASS_LOCATION {-1.6834618673E-17,
    #                             -1.1472480873E-16}
    # }

    tab = '  '
    f.write(tab*2 + '@ETA_COORDINATE {' + ('%11.5e' % eta) + '} {\n')
    f.write(tab*3 +   '@STIFFNESS_MATRIX {' + ('%17.10e' % K[0,0]) + ',' + ('%20.10e' % K[0,1]) + ',' + ('%20.10e' % K[0,2]) + ',' + ('%20.10e' % K[0,3]) + ',' + ('%20.10e' % K[0,4]) + ',' + ('%20.10e' % K[0,5]) + ',' + '\n')
    f.write(tab*3 + ' '*37 +                                               ('%20.10e' % K[1,1]) + ',' + ('%20.10e' % K[1,2]) + ',' + ('%20.10e' % K[1,3]) + ',' + ('%20.10e' % K[1,4]) + ',' + ('%20.10e' % K[1,5]) + ',' + '\n')
    f.write(tab*3 + ' '*(37+21*1) +                                                                     ('%20.10e' % K[2,2]) + ',' + ('%20.10e' % K[2,3]) + ',' + ('%20.10e' % K[2,4]) + ',' + ('%20.10e' % K[2,5]) + ',' + '\n')
    f.write(tab*3 + ' '*(37+21*2) +                                                                                                  ('%20.10e' % K[3,3]) + ',' + ('%20.10e' % K[3,4]) + ',' + ('%20.10e' % K[3,5]) + ',' + '\n')
    f.write(tab*3 + ' '*(37+21*3) +                                                                                                                               ('%20.10e' % K[4,4]) + ',' + ('%20.10e' % K[4,5]) + ',' + '\n')
    f.write(tab*3 + ' '*(37+21*4) +                                                                                                                                                            ('%20.10e' % K[5,5]) + '}' + '\n')
    f.write(tab*3 +   '@MASS_PER_UNIT_SPAN {' + ('%17.10e' % mpus) + '}\n')
    f.write(tab*3 +   '@MOMENTS_OF_INERTIA {' + ('%17.10e' % i1) + ',\n')
    f.write(tab*3 + ' '*21 +                    ('%17.10e' % i2) + ',\n')
    f.write(tab*3 + ' '*21 +                    ('%17.10e' % i3) + '}\n')
    f.write(tab*3 +   '@CENTRE_OF_MASS_LOCATION {' + ('%17.10e' % cm_x2) + ',\n')
    f.write(tab*3 + ' '*26 +                         ('%17.10e' % cm_x3) + '}\n')

    return


def writeMKmatrices(sparstn, debug_flag=False):
    if sparstn < 10:
        sparstnstr = '0' + str(sparstn)
    else:
        sparstnstr = str(sparstn)
    vabsMK = '../VABS/M_and_K_matrices/spar_station_' + sparstnstr + '.dat.K'
    eta = 0.0
    print "eta =", eta
    MKlines = readFile(vabsMK)
    (cm_x2, cm_x3, mpus, i1, i2, i3, K) = pullMKmatrices(MKlines, print_flag=debug_flag)
    dymoreMKfile = makeMKfile()
    writeDymoreMK(dymoreMKfile, eta, cm_x2, cm_x3, mpus, i1, i2, i3, K)
    dymoreMKfile.close()

    return


if __name__ == '__main__':
    spar_station = 24
    print "****************"
    print "spar station #" + str(spar_station)
    print "****************"
    writeMKmatrices(spar_station, debug_flag=True)
