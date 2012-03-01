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
    exitPat = re.compile(r'c exit')
    
    return (nnPat, scPat, rbPat, swPat, exitPat)


def replaceDefaults(tgTemplate, stn, stnData, silent_flag=False):
    (nnPat, scPat, rbPat, swPat, exitPat) = defineRegularExpressions()
    for i in range(len(tgTemplate)):
        nnMatch = nnPat.match(tgTemplate[i])
        scMatch = scPat.match(tgTemplate[i])
        rbMatch = rbPat.match(tgTemplate[i])
        swMatch = swPat.match(tgTemplate[i])
        exitMatch = exitPat.match(tgTemplate[i])
        if nnMatch:
            if stn < 10:
                tgTemplate[i] = tgTemplate[i].replace('nn','0'+str(stn))
            else:
                tgTemplate[i] = tgTemplate[i].replace('nn',str(stn))
        elif scMatch:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['spar cap height']))
        elif rbMatch:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['root buildup height']))
        elif swMatch:
            tgTemplate[i] = tgTemplate[i].replace('0.000', str(stnData['shear web height']))
        elif exitMatch and silent_flag:
            tgTemplate[i] = tgTemplate[i].replace('c ', '')
    
    return tgTemplate


def writeNewTGscript(tgFile, tgTemplate):
    for i in range(len(tgTemplate)):
        tgFile.write( tgTemplate[i] )
    return



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