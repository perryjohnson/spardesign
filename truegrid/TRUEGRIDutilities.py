## read the TrueGrid-formatted template file into memory
##    input: filestr <string>, the filename of the TrueGrid-formatted template file
##    output: tgfile <string>, a string of all characters in the TrueGrid-formatted template file
def readFile(filestr):
    f = open(filestr, 'r')  # read the file
    tgTemplate = f.readlines()  # parse all characters in file into one long string
    return tgTemplate


## make TrueGrid file on hard disk to store mesh generation script
##    input:  basefilestr <string>, base file string (spar_station_nn)
##    output: tgFile <object>, file handle to 'basefilestr'.tg
def makeTGFile(basefilestr):
    tgFile = open(basefilestr+'.tg', 'w+')  # file for node coordinates
    return tgFile


## define regular expressions to search for nodes and elements in ABAQUS-formatted file
##    input: <none>
##    output: nnPat <object>, regex pattern for 'nn'
def defineRegularExpressions():
    import re
    # nn pattern:
    nnPat = re.compile(r'.*nn.*')
    scPat = re.compile(r'para sc_ht.+')
    rbPat = re.compile(r'para rb_ht.+')
    swPat = re.compile(r'para sw_ht.+')
    swfmiPat = re.compile(r'para swfm_ielem.+')
    swfmjPat = re.compile(r'para swfm_jelem.+')
    sciPat = re.compile(r'para sc_ielem.+')
    scjPat = re.compile(r'para sc_jelem.+')
    x4Pat = re.compile(r'para x4.+')
    x3Pat = re.compile(r'para x3.+')
    x2Pat = re.compile(r'para x2.+')
    x1Pat = re.compile(r'para x1.+')
    writePat = re.compile(r'write.+')
    exitPat = re.compile(r'c exit')

    return (nnPat, scPat, rbPat, swPat, swfmiPat, swfmjPat, sciPat, scjPat, x1Pat, x2Pat, x3Pat, x4Pat, writePat, exitPat)


def replaceDefaults(tgTemplate, stn, stnData, elemData, nowrite_flag=False, silent_flag=False):
    (nnPat, scPat, rbPat, swPat, swfmiPat, swfmjPat, sciPat, scjPat, x1Pat, x2Pat, x3Pat, x4Pat, writePat, exitPat) = defineRegularExpressions()
    for i in range(len(tgTemplate)):
        nnMatch = nnPat.match(tgTemplate[i])
        scMatch = scPat.match(tgTemplate[i])
        rbMatch = rbPat.match(tgTemplate[i])
        swMatch = swPat.match(tgTemplate[i])
        swfmiMatch = swfmiPat.match(tgTemplate[i])
        swfmjMatch = swfmjPat.match(tgTemplate[i])
        sciMatch = sciPat.match(tgTemplate[i])
        scjMatch = scjPat.match(tgTemplate[i])
        x4Match = x4Pat.match(tgTemplate[i])
        x3Match = x3Pat.match(tgTemplate[i])
        x2Match = x2Pat.match(tgTemplate[i])
        x1Match = x1Pat.match(tgTemplate[i])
        exitMatch = exitPat.match(tgTemplate[i])
        if nnMatch:
            if stn < 10:
                tgTemplate[i] = tgTemplate[i].replace('nn','0'+str(stn))
            else:
                tgTemplate[i] = tgTemplate[i].replace('nn', str(stn))
        elif scMatch:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['spar cap height']))
        elif rbMatch:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['root buildup height']))
        elif swMatch:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['shear web height']))
        elif swfmiMatch:
            tgTemplate[i] = tgTemplate[i].replace('000', str(elemData['shear web foam, i-elements']))
        elif swfmjMatch:
            tgTemplate[i] = tgTemplate[i].replace('000', str(elemData['shear web foam, j-elements']))
        elif sciMatch:
            tgTemplate[i] = tgTemplate[i].replace('000', str(elemData['spar cap, i-elements']))
        elif scjMatch:
            tgTemplate[i] = tgTemplate[i].replace('000', str(elemData['spar cap, j-elements']))
        elif x4Match:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['spar cap base'] * (-0.5)))
        elif x3Match:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['spar cap base'] * (-0.5) - stnData['shear web biaxial GFRP base']))
        elif x2Match:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['spar cap base'] * (-0.5) - stnData['shear web biaxial GFRP base'] - stnData['shear web foam base']))
        elif x1Match:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['spar cap base'] * (-0.5) - stnData['shear web biaxial GFRP base'] * (2.0) - stnData['shear web foam base']))
        elif writePat and nowrite_flag:
            tgTemplate[i] = tgTemplate[i].replace('write   c write the output file to disk', 'c write   c do not write the output file to disk')
        elif exitMatch and silent_flag:
            tgTemplate[i] = tgTemplate[i].replace('c ', '')
    
    return tgTemplate


def removeRBentries(tgTemplate):
    import re
    para_rbPat = re.compile(r'para rb.+')
    y1_or_y6Pat = re.compile(r'para y[16].+')
    RBtitlePat = re.compile(r'c  ROOT BUILDUP.*')
    include_rbPat = re.compile(r'include rb.+')
    eset_rbPat = re.compile(r'eset 0 0 1 0 0 1 = rb.+')

    for i in range(len(tgTemplate)):
        para_rbMatch = para_rbPat.match(tgTemplate[i])
        y1_or_y6Match = y1_or_y6Pat.match(tgTemplate[i])
        RBtitleMatch = RBtitlePat.match(tgTemplate[i])
        include_rbMatch = include_rbPat.match(tgTemplate[i])
        eset_rbMatch = eset_rbPat.match(tgTemplate[i])
        if para_rbMatch or y1_or_y6Match or RBtitleMatch or include_rbMatch or eset_rbMatch:
            tgTemplate[i] = ''

    return tgTemplate


def writeNewTGscript(tgFile, tgTemplate):
    for i in range(len(tgTemplate)):
        tgFile.write( tgTemplate[i] )
    return


### determine the number of cells needed for a Cartesian grid with low aspect ratio cells ###
###     input:  dim1 <double>, 1st dimension of grid area (e.g. length)
###             n1 <int>, desired number of cells to be distributed along dim1
###             maxAR <double>, desired maximum aspect ratio for any cell in the grid
###             dim2 <double>, 2nd dimension of grid area (e.g. width)
###     output: n1 <int>, number of cells to be distributed along dim1 (may be updated from input n1)
###             n2 <int>, number of cells to be distributed along dim2
def calcCellNums(dim1,n1,maxAR,dim2):
    if type(n1) != type(1):                 # check if input value for n1 is an integer
        print "ERROR: input value for n1 must be an INTEGER!"
        n1 = 0
        n2 = 0
    else:
        flag = True
        while (flag):
            # print 'n1        =', n1
            cell_dim1 = dim1/float(n1)      # calculate the cell dimension in the dim1 direction
            # print 'cell_dim1 =', cell_dim1
            # print 'maxAR     =', maxAR
            cell_dim2 = cell_dim1 * maxAR   # calculate the cell dimension in the dim2 direction
            # print 'cell_dim2 =', cell_dim2
            n2 = dim2/cell_dim2             # see how many cells of size cell_dim2 will fit in the dim2 direction
            n2 = int(n2) + 1                # round the result up to the next integer
            # print 'n2        =', n2
            cell_dim2 = dim2/float(n2)      # recalculate the cell dimension in the dim2 direction
            # print 'cell_dim2 =', cell_dim2
            AR = cell_dim1/cell_dim2        # calculate the current cell aspect ratio
            if AR < 1.0:                    # if aspect ratio is less than 1...
                AR = 1.0/AR                 # ...take its reciprocal (aspect ratio is defined as > 1)
            # print 'AR        =', AR
            # print 'maxAR     =', maxAR
            if AR < maxAR:                  # if the aspect ratio is less than the specified max aspect ratio...
                flag = False                # ...exit this loop
            else:
                n1 = n1 * 2                 # otherwise, double the number of cells in the dim1 direction and reiterate this loop
    ### optional print statements for debugging ###
    # print 'dim1      =', dim1
    # print 'dim2      =', dim2
    # print 'cell_dim1 =', cell_dim1
    # print 'cell_dim2 =', cell_dim2
    # print 'n1        =', n1
    # print 'n2        =', n2
    # print 'AR        =', AR
    # print 'maxAR     =', maxAR
    return (n1,n2)


if __name__ == '__main__':
    spar_station = 1
    if spar_station < 10:
        basefilestr = 'spar_station_0' + str(spar_station)
    else:
        basefilestr = 'spar_station_' + str(spar_station)
    print '***************'
    print basefilestr
    print '***************'
    tgTemplate = readFile('spar_station_nn.tg')
    tgFile = makeTGFile(basefilestr)
    (nnPat, scPat, rbPat, swPat) = defineRegularExpressions()
    tgTemplate = replaceDefaults(nnPat, scPat, rbPat, swPat, tgTemplate, spar_station, stationData)
    writeNewTGscript(tgFile, tgTemplate)
    tgFile.close()