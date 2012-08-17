## make files on hard disk to store VABS input file
##    input: filestr <string>, filename of *.dat VABS input file
##    output: VABSfile <object>, file handle to VABS input file
def openFileForVABSinput(filestr):
    VABSfile = open(filestr, 'w+')  # this file will hold our node coordinates
    return VABSfile


## write the VABS input file header (flag values)
##    input: VABSfile <object>, file handle to VABS input file
##           vd <dictionary>, package of VABS flags
##    output: <none>
def writeHeader(VABSfile, vd):
    VABSfile.write( str(vd['format_flag']) + ' ' + str(vd['nlayer']) + '\n' )
    VABSfile.write( str(vd['Timoshenko_flag']) + ' ' + str(vd['recover_flag']) + ' ' + str(vd['thermal_flag']) + "    # Timoshenko_flag  recover_flag  thermal_flag" + '\n' )
    if vd['curve_flag'] == 1:
        VABSfile.write( str(vd['curve_flag']) + ' ' + str(vd['oblique_flag']) + ' ' + str(vd['trapeze_flag']) + ' ' + str(vd['Vlasov_flag']) + "  # curve_flag  oblique_flag  trapeze_flag  Vlasov_flag" + '\n' )
        VABSfile.write( str(vd['k1']) + ' ' + str(vd['k2']) + ' ' + str(vd['k3']) + '\n\n' )
    else:
        VABSfile.write( str(vd['curve_flag']) + ' ' + str(vd['oblique_flag']) + ' ' + str(vd['trapeze_flag']) + ' ' + str(vd['Vlasov_flag']) + "  # curve_flag  oblique_flag  trapeze_flag  Vlasov_flag" + '\n\n' )
    return


## write the number of nodes, elements, and materials
##    input: VABSfile <object>, file handle to VABS input file
##           nnode <int>, number of nodes in this grid
##           nelem <int>, number of elements in this grid
##           nmate <int>, number of materials in this grid
##    output: <none>
def writeNumberOfNodesElementsAndMaterials(VABSfile, nnode, nelem, nmate):
    VABSfile.write(str(nnode) + ' ' + str(nelem) + ' ' + str(nmate) + "   # nnode  nelem  nmate   (where: nnode = total number of nodes, nelem = total number of elements, nmate = total number of material types)\n\n")
    return


## write the coordinates code block
##    input: VABSfile <object>, file handle to VABS input file
##           nnode <int>, number of nodes in this grid
##           coordinates <array>, numpy array of x&y coordinates of each node in this grid
##    output: <none>
def writeCoordinatesBlock(VABSfile, nnode, node_list):
    # create string format based on character columns in nnode
    strfmt = '%' + str(len(str(nnode))) + 'i'

    # traverse the array of node coordinates, and print each line to the VABS input file
    for i in range(1,nnode+1):
        # vary the number of spaces between printed columns
        #  so they line up neatly, even if some numbers have negative signs
        node_no = node_list[i].node_no
        x2 = node_list[i].x2
        x3 = node_list[i].x3
        if ((x2 >= 0) and (x3 >= 0)):
            VABSfile.write(str(strfmt   % node_no) + '     ' +
                           str('%10.8f' % x2)      + '     ' + 
                           str('%10.8f' % x3)      + '\n')
        elif ((x2 < 0) and (x3 >= 0)):
            VABSfile.write(str(strfmt   % node_no) + '    ' +
                           str('%10.8f' % x2)      + '     ' + 
                           str('%10.8f' % x3)      + '\n')
        elif ((x2 >= 0) and (x3 < 0)):
            VABSfile.write(str(strfmt   % node_no) + '     ' +
                           str('%10.8f' % x2)      + '    ' + 
                           str('%10.8f' % x3)      + '\n')
        elif ((x2 < 0) and (x3 < 0)):
            VABSfile.write(str(strfmt   % node_no) + '    ' +
                           str('%10.8f' % x2)      + '    ' + 
                           str('%10.8f' % x3)      + '\n')
        else:  # make sure the coordinates print, even if your pretty print rules aren't followed!
            VABSfile.write(str(strfmt   % node_no) + '     ' +
                           str('%10.8f' % x2)      + '     ' + 
                           str('%10.8f' % x3)      + '\n')

    VABSfile.write('\n')
    return


## write the element connectivity code block
##    input: VABSfile <object>, file handle to VABS input file
##           nelem <int>, number of elements in this grid
##           connectivity <array>, a numpy array of node numbers describing the connectivity of each element
##    output: <none>
def writeConnectivityBlock(VABSfile, nelem, elem):
    # create string format based on character columns in nelem
    strfmt = '%' + str( len(str(nelem)) ) + 'i'
    # create another string format that's a little wider than strfmt, for better readability of the VABS input file
    strfmt2 = '%' + str( len(str(nelem))+2 ) + 'i'

    # traverse the array of node coordinates, and print each line to the VABS input file
    for i in range(1,nelem+1):
        node_1 = elem[i].node1.node_no
        node_2 = elem[i].node2.node_no
        node_3 = elem[i].node3.node_no
        node_4 = elem[i].node4.node_no
        node_5 = elem[i].node5.node_no
        node_6 = elem[i].node6.node_no
        node_7 = elem[i].node7.node_no
        node_8 = elem[i].node8.node_no
        node_9 = elem[i].node9.node_no
        VABSfile.write(str(strfmt % elem[i].elem_no) + '  ' +
                       str(strfmt2 % node_1) +
                       str(strfmt2 % node_2) +
                       str(strfmt2 % node_3) +
                       str(strfmt2 % node_4) +
                       str(strfmt2 % node_5) +
                       str(strfmt2 % node_6) +
                       str(strfmt2 % node_7) +
                       str(strfmt2 % node_8) +
                       str(strfmt2 % node_9) + '\n')

    VABSfile.write('\n')
    return


## write the element material code block
##    input: VABSfile <object>, file handle to VABS input file
##           nelem <int>, number of elements in this grid
##           elem <object>, list of element objects
##    output: <none>
def writeElementMaterialBlock(VABSfile, nelem, elem):
    # create string format based on character columns in nelem
    strfmt = '%' + str( len(str(nelem)) ) + 'i'

    # traverse the array of elements, and print each line to the VABS input file
    for i in range (1,nelem+1):
        VABSfile.write(str(strfmt % elem[i].elem_no) + '   ' +
                       str(elem[i].layer.layer_no) +
                       str('%8.2f' % elem[i].theta1) + '\n')
    
    VABSfile.write('\n')
    return


## write the layer code block
##    input: VABSfile <object>, file handle to VABS input file
##           nlayer <int>, number of layers in this grid
##           layer_list <object>, list of layer objects
##    output: <none>
def writeLayerBlock(VABSfile, nlayer, layer_list):
    # create string format based on character columns in nlayer
    strfmt = '%' + str( len(str(nlayer)) ) + 'i'
    strfmt2 = '%' + str( len(str(nlayer))+4 ) + 'i'

    # traverse the array of layers, and print each line to the VABS input file
    for i in range (1,nlayer+1):
        VABSfile.write(str(strfmt % layer_list[i].layer_no) +
                       str(strfmt2 % layer_list[i].material.material_no) +
                       str('%9.2f' % layer_list[i].theta3) + '\n')
    VABSfile.write('\n')
    return


## write the material definition code block
##    input: VABSfile <object>, file handle to VABS input file
##           nmate <int>, number_of_materials
##           matl <object>, list of material objects
##    output: <none>
def writeMaterialDefinitionBlock(VABSfile, nmate, matl):
    strfmt = '%11.5e'
    strfmt2 = '%14.5e'
    for i in range(1,nmate+1):
        VABSfile.write( str(matl[i].material_no) + '   ' + str(matl[i].orth_flag) + '   # ' + matl[i].material_name + '\n' )
        if matl[i].orth_flag == 0:
            VABSfile.write( str(strfmt % matl[i].E) + str(strfmt2 % matl[i].nu) + '\n' )
        elif matl[i].orth_flag == 1:
            VABSfile.write( str(strfmt % matl[i].E1) + str(strfmt2 % matl[i].E2) + str(strfmt2 % matl[i].E3) + '\n' )
            VABSfile.write( str(strfmt % matl[i].G12) + str(strfmt2 % matl[i].G13) + str(strfmt2 % matl[i].G23) + '\n' )
            VABSfile.write( str(strfmt % matl[i].nu12) + str(strfmt2 % matl[i].nu13) + str(strfmt2 % matl[i].nu23) + '\n' )
        else:
            print "ERROR: no material constants available for material #" + str(matl[i].material_no)
        VABSfile.write( str(strfmt % matl[i].rho) + '\n\n' )
    return


## write blank line at the end of the file on hard disk that stores VABS input file
##    input: VABSfile <object>, file handle to VABS input file
##    output: <none>
def writeBlankLineAtEndOfFile(VABSfile):
    VABSfile.write('\n')
    return


## close file on hard disk that stores VABS input file
##    input: VABSfile <object>, file handle to VABS input file
##    output: <none>
def closeFileForVABSinput(VABSfile):
    VABSfile.close()
    return


## write the entire VABS input file
##    input: filestr <string>, filename of *.dat VABS input file
##           node_list <object>, list of nodes in this grid
##           elem <object>, list of elements in this grid
##           VABSflag_dict <dictionary>, package of all the VABS flags
##    output: <none>
def writeVABSfile(filestr, node_list, layer_list, matl, elem, VABSflag_dict):
    VABSfile = openFileForVABSinput(filestr)
    writeHeader(VABSfile, VABSflag_dict)
    writeNumberOfNodesElementsAndMaterials(VABSfile, VABSflag_dict['nnode'], VABSflag_dict['nelem'], VABSflag_dict['nmate'])
    writeCoordinatesBlock(VABSfile, VABSflag_dict['nnode'], node_list)
    writeConnectivityBlock(VABSfile, VABSflag_dict['nelem'], elem)
    writeElementMaterialBlock(VABSfile, VABSflag_dict['nelem'], elem)
    writeLayerBlock(VABSfile, VABSflag_dict['nlayer'], layer_list)
    writeMaterialDefinitionBlock(VABSfile, VABSflag_dict['nmate'], matl)
    # writeBlankLineAtEndOfFile(VABSfile)
    closeFileForVABSinput(VABSfile)
    return


## define regular expressions to search for errors in the VABS input file
##    input: <none>
##    output: nanPat <object>, regex pattern for a "not a number" entry
def defineRegularExpressions():
    import re

    # general 'not a number' pattern:
    nanPat = re.compile(r'.*nan.*')
    #  this regex pattern explained:
    #  -----------------------------
    #  .*nan.*  :  find if 'nan' is located anywhere in a row of the VABS input file

    # theta1=nan pattern:
    nanTheta1Pat = re.compile(r'\s*[0-9]+\s+[0-9]+\s+nan')
    #  this regex pattern explained:
    #  -----------------------------
    #  \s*        :  [optional whitespace]
    #  [0-9]+\s+  :  element number [whitespace]
    #  [0-9]+\s+  :  layer number [whitespace]
    #  nan        :  find if theta1 is set to 'nan'

    return (nanPat, nanTheta1Pat)


## find any errors in the VABS input file, and return their line numbers
def findErrors(nanPat, VABSfile):
    errorLineNums = []
    for i in range(len(VABSfile)):
        nanMatch = nanPat.match(VABSfile[i])
        if nanMatch:
            errorLineNums.append(i)
    
    return errorLineNums


## find any theta1 assignment errors in the VABS input file, and return their element numbers
def findTheta1Errors(nanTheta1Pat, VABSfile):
    import numpy as np
    errorElemNums = []
    for i in range(len(VABSfile)):
        nanTheta1Match = nanTheta1Pat.match(VABSfile[i])
        if nanTheta1Match:
            errorElemNums.append(np.fromstring(VABSfile[i], dtype=int, sep=' ')[0])
    
    return errorElemNums


def checkVABSfileForErrors(filestr):
    ok_flag = False
    f = open(filestr, 'r')  # read the file
    VABSfile = f.readlines()    # parse all characters in file into one long string
    (nanPat, nanTheta1Pat) = defineRegularExpressions()
    errorLines = findErrors(nanPat, VABSfile)
    print str(len(errorLines)) + ' errors found in the VABS input file'
    errorElemNums = findTheta1Errors(nanTheta1Pat, VABSfile)
    print str(len(errorElemNums)) + ' theta1 errors found in the VABS input file'
    if len(errorLines) == 0 and len(errorElemNums) == 0:
        ok_flag = True

    return ok_flag


if __name__ == '__main__':
    f = open('../spar_station_04.dat', 'r')  # read the file
    VABSfile = f.readlines()    # parse all characters in file into one long string
    (nanPat, nanTheta1Pat) = defineRegularExpressions()
    errorLines = findErrors(nanPat, VABSfile)
    print 'found ' + str(len(errorLines)) + ' errors in the VABS input file'
    errorElemNums = findTheta1Errors(nanTheta1Pat, VABSfile)
    print 'found ' + str(len(errorElemNums)) + ' theta1 errors in the VABS input file'

    # for i in range(len(errorElemNums)):
    #     (x2,x3) = element[errorElemNums[i]].middle()
    #     if x2 > -0.836 and x2 < -0.75 and x3 > -2.3705 and x3 < 2.3705:  # left shear web
    #         element[errorElemNums[i]].theta1 = 90.0
    #     elif x2 > 0.75 and x2 < 0.836 and x3 > -2.3705 and x3 < 2.3705:  # right shear web
    #         element[errorElemNums[i]].theta1 = 270.0
    #     elif x2 > -0.836 and x2 < 0.836 and x3 > 2.3705 and x3 < 2.3955: # top root buildup
    #         element[errorElemNums[i]].theta1 = 0.0
    #     elif x2 > -0.836 and x2 < 0.836 and x3 > -2.3955 and x3 < -2.3705: # bottom root buildup
    #         element[errorElemNums[i]].theta1 = 180.0
    #     elif x2 > -0.75 and x2 < 0.75 and x3 > 2.3405 and x3 < 2.3705: # top spar cap
    #         element[errorElemNums[i]].theta1 = 0.0
    #     elif x2 > -0.75 and x2 < 0.75 and x3 > -2.3705 and x3 < -2.3405: # bottom spar cap
    #         element[errorElemNums[i]].theta1 = 180.0