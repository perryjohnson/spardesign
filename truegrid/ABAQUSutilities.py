import re                        # import the regular expression module
import os                        # import the operating system module
import numpy as np               # import the the numpy module; rename it as np


## read the ABAQUS-formatted file from TrueGrid into memory
##    input: filestr <string>, the filename of the ABAQUS-formatted file
##    output: abqfile <string>, a string of all characters in the ABAQUS-formatted file
def readFile(filestr):
    f = open(filestr, 'r')  # read the file
    abqfile = f.readlines()    # parse all characters in file into one long string
    return abqfile


## make temporary files on hard disk to store nodes and element connectivity parsed from the ABAQUS-formatted file from TrueGrid
##    input: <none>
##    output: nodeFile <object>, file handle to node.txt
##            elemFile <object>, file handle to elem.txt
def makeNodeAndElemFiles():
    nodeFile = open('node.txt', 'w+')  # file for node coordinates
    elemFile = open('elem.txt', 'w+')  # file for element connectivity
    return (nodeFile, elemFile)


## define regular expressions to search for nodes and elements in ABAQUS-formatted file
##    input: <none>
##    output: nodePat <object>, regex pattern for a node
##            elemPat <object>, regex pattern for an element connectivity
def defineRegularExpressions():
    # node pattern:
    # nodePat = re.compile(r'[0-9]+,-*[0-9]+\.[0-9]+,-*[0-9]+\.[0-9]+,.+')
    nodePat = re.compile(r'[0-9]+,-*[0-9]+\.[0-9]*E*[+-]*[0-9]*,-*[0-9]+\.[0-9]*E*[+-]*[0-9]*,-*[0-9]+\.[0-9]*E*[+-]*[0-9]*')
    # node header pattern:
    nodeHeadPat = re.compile(r'\*NODE.+')
    
    # shell header pattern:
    shellHeadPat = re.compile(r'\*SHELL.+')

    # element connectivity pattern:
    elemPat = re.compile(r'[0-9]+,[0-9]+,[0-9]+,[0-9]+,[0-9]+,[0-9]+,[0-9]+,[0-9]+,[0-9]+')

    # material header pattern: (located inside the element connectivity header)
    matlHeadPat = re.compile(r'\*MATERIAL,NAME=M[0-9]+')

    # element connectivity header pattern:
    elemHeadPat = re.compile(r'\*MATERIAL.+\n\*DENSITY\n[0-9].+\n\*ELASTIC.+\n[0-9].+\n\*ELEMENT.+')
    
    return (nodePat, nodeHeadPat, shellHeadPat, elemPat, matlHeadPat, elemHeadPat)


## interpret readlines() string from ABAQUS file
##    parse nodes and element connectivity into numpy arrays
##    input: abqfile <string>, a string of all characters in the ABAQUS-formatted file
##           nodeFile <object>, file handle to node.txt
##           elemFile <object>, file handle to elem.txt
##    output: coordinates <array>, a numpy array of x&y coordinates for each node
##            connectivity <array>, a numpy array of node numbers describing the connectivity of each element
##            nnode <int>, the total number of nodes in this grid
##            nelem <int>, the total number of elements (cells) in this grid
def interpretABAQUS(abqfile, nodeFile, elemFile, debug_flag=False):
    (nodePat, nodeHeadPat, shellHeadPat, elemPat, matlHeadPat, elemHeadPat) = defineRegularExpressions()

    for i in range(len(abqfile)):
        # search for (x,y,z) coordinates:
        nodeMatch = nodePat.match(abqfile[i])
        elemMatch = elemPat.match(abqfile[i])
        matlHeadMatch = matlHeadPat.match(abqfile[i])
        if nodeMatch:  # if we find a node, write it to node.txt
            nodeFile.write(abqfile[i])
        elif matlHeadMatch:
            layer_no = int(abqfile[i][-2])
            if debug_flag:
                print 'element header found at line ' + str(i)
                print 'layer #' + str(layer_no)
                print 'first element: #' + str(np.fromstring(abqfile[i+6], dtype=int, sep=',')[0]) + '\n'
        elif elemMatch:  # if we find an element connectivity, write it to elem.txt
            elemFile.write(str(layer_no) + ',' + abqfile[i]) # store the layer number of each element at the beginning of each line in elem.txt

    # rewind cursor to beginning of file 'node.txt'
    nodeFile.seek(0,0)
    # load nodes into an array
    nodeArray = np.loadtxt('node.txt', delimiter=',', usecols=(0,1,2))
    #   usecols kwarg discards the last column, which only contains zeros (z-coords)

    # rewind cursor to beginning of file 'elem.txt'
    elemFile.seek(0,0)
    # load element connectivity into an array (of integers)
    elemArray = np.loadtxt('elem.txt', dtype='int', delimiter=',')

    nnode = len(nodeArray)  # set the number of nodes
    nelem = len(elemArray)  # set the number of elements

    checkABAQUSparsing(nodeArray, nnode)

    return (nodeArray, elemArray, nnode, nelem)



def checkABAQUSparsing(nodeArray, nnode):
    lastnodeno = int(nodeArray[-1,0])
    if lastnodeno != nnode:
        print '***ERROR: number of nodes does not equal the last node number in the list***'
        print '     number_of_nodes = ' + str(nnode)
        print '     last node number: ' + str(lastnodeno)

    return


## close files on hard disk that store nodes and element connectivity
##    input: nodeFile <object>, file handle to node.txt
##           elemFile <object>, file handle to elem.txt
##    output: <none>
def closeNodeAndElemFiles(nodeFile, elemFile):
    nodeFile.close()
    elemFile.close()
    return


## delete the files on hard disk that store coordinates and connectivity
##    input: <none>
##    output: <none>
def deleteNodeAndElemFiles():
    os.remove('node.txt')
    os.remove('elem.txt')
    return


## parse the ABAQUS file and return numpy arrays with the nodes and element connectivity
##    also return the number of nodes and the number of elements
##    input: filestr <string>, the filename of the ABAQUS-formatted file
##    output: nodeArray <np.array>, array of nodes and coordinates
##            elemArray <np.array>, array of elements and connectivity
##            nnode <int>, number of nodes
##            nelem <int>, number of elements
def parseABAQUS(filestr, debug_flag=False):
    if debug_flag:
        print 'ABAQUS file: ' + filestr
    abqfile = readFile(filestr)
    (nodeFile, elemFile) = makeNodeAndElemFiles()
    if debug_flag:
        print 'STATUS: interpreting the ABAQUS file...'
    (nodeArray, elemArray, nnode, nelem) = interpretABAQUS(abqfile, nodeFile, elemFile, debug_flag=debug_flag)
    closeNodeAndElemFiles(nodeFile, elemFile)
    # deleteNodeAndElemFiles()
    if debug_flag:
        print nodeArray[0:5,:]
        print elemArray[0:5,:]
        print 'number of nodes: ' + str(nnode)
        print 'number of elements: ' + str(nelem)

    return (nodeArray, elemArray, nnode, nelem)





if __name__ == '__main__':
    outputfile = 'spar_station_04_output.txt'
    (nodeArray, elemArray, nnode, nelem) = parseABAQUS(outputfile, debug_flag=True)