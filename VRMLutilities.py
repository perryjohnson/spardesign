import re                        # import the regular expression module
import os                        # import the operating system module
import numpy as np               # import the the numpy module; rename it as np


## read the VRML-formatted file from Gridgen into memory
##    input: filestr <string>, the filename of the *.grd VRML-formatted file
##    output: VRML_readlines <string>, a string of all characters in the VRML-formatted file
def readFile(filestr):
	f = open(filestr, 'r')  # read the file
	VRML_readlines = f.readlines()    # parse all characters in file into one long string
	return VRML_readlines

## make temporary files on hard disk to store coordinates and connectivity parsed from the VRML-formatted file from Gridgen
##    input: <none>
##    output: coordinatesFile <object>, file handle to coordinates.dat
##            connectivityFile <object>, file handle to connectivity.dat
def openFilesForcoordinatesAndConnectivity():
	coordinatesFile = open('coordinates.dat', 'w+')  # this file will hold our node coordinates
	connectivityFile = open('connectivity.dat', 'w+')  # this file will hold our element connectivity
	return (coordinatesFile, connectivityFile)

## define regular expressions
##    input: <none>
##    output: nodePattern <object>, regular expression pattern for a node in the VRML-formatted file
##            connectivityPattern <object>, regular expression pattern for the connectivity of an element in the VRML-formatted file
def defineRegularExpressions():
	# (x,y,z) coordinates:
	nodePattern = re.compile(r' +-?[0-9]\.[0-9]+e[\-\+][0-9]+ +-?[0-9]\.[0-9]+e[\-\+][0-9]+ +-?[0-9]\.[0-9]+e[\-\+][0-9]+,\s*')
	# element connectivity:
	connectivityPattern = re.compile(r' +[0-9]+, +[0-9]+, +[0-9]+, +[0-9]+, +\-1,\s*')
	return (nodePattern, connectivityPattern)

## interpret readlines() string from VRML file
##    parse coordinates and connectivity into numpy arrays
##    input: VRML_readlines <string>, a string of all characters in the VRML-formatted file
##           coordinatesFile <object>, file handle to coordinates.dat
##           connectivityFile <object>, file handle to connectivity.dat
##    output: coordinates <array>, a numpy array of x&y coordinates for each node
##            connectivity <array>, a numpy array of node numbers describing the connectivity of each element
##            nnode <int>, the total number of nodes in this grid
##            nelem <int>, the total number of elements (cells) in this grid
def interpretVRML(VRML_readlines, coordinatesFile, connectivityFile):
	(nodePattern, connectivityPattern) = defineRegularExpressions()

	for i in range(len(VRML_readlines)):
		# search for (x,y,z) coordinates:
		nodeMatch = nodePattern.match(VRML_readlines[i])
		connectivityMatch = connectivityPattern.match(VRML_readlines[i])
		if nodeMatch:  # if we find
			coordinatesFile.write(VRML_readlines[i][:-20] + '\n')
			# ***IMPROVE: don't hard code this, search for the last column of zeros and delete it!
		elif connectivityMatch:
			connectivityFile.write(VRML_readlines[i][:-10] + '\n')
			# ***IMPROVE: don't hard code this, search for the last column of ',    -1' and delete it!

	# rewind cursor to beginning of file 'coordinates.dat'
	coordinatesFile.seek(0,0)
	# load coordinates into an array
	coordinates = np.loadtxt('coordinates.dat')

	# rewind cursor to beginning of file 'connectivity.dat'
	connectivityFile.seek(0,0)
	# load connectivity into an array (of integers)
	connectivity = np.loadtxt('connectivity.dat', dtype='int', delimiter=',')
	# increment all elements of connectvity array by 1 (to match VABS convention: the first node is node1, not node0)
	connectivity = connectivity + 1

	nnode = len(coordinates)  # set the number of nodes
	nelem = len(connectivity)  # set the number of elements

	return (coordinates, connectivity, nnode, nelem)

## close files on hard disk that store coordinates and connectivity
##    input: coordinatesFile <object>, file handle to coordinates.dat
##            connectivityFile <object>, file handle to connectivity.dat
##    output: <none>
def closeFilesForcoordinatesAndConnectivity(coordinatesFile, connectivityFile):
	coordinatesFile.close()
	connectivityFile.close()
	return

## delete the files on hard disk that store coordinates and connectivity
##    input: <none>
##    output: <none>
def deleteFilesForcoordinatesAndConnectivity():
	os.remove('coordinates.dat')
	os.remove('connectivity.dat')
	return

## parse the VRML file and return numpy arrays with the coordinates and connectivity
##    also return the number of nodes and the number of elements
##    input: filestr <string>, the filename of the *.grd VRML-formatted file
##    output: <none>
def parseVRML(filestr):
	VRMLfile = readFile(filestr)
	(coordinatesFile, connectivityFile) = openFilesForcoordinatesAndConnectivity()

	(coordinates, connectivity, nnode, nelem) = interpretVRML(VRMLfile, coordinatesFile, connectivityFile)

	closeFilesForcoordinatesAndConnectivity(coordinatesFile, connectivityFile)
	deleteFilesForcoordinatesAndConnectivity()

	return (coordinates, connectivity, nnode, nelem)