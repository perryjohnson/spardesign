import numpy as np
import matplotlib.pyplot as plt

### read in the layup file ###
###     input:  fname <string>, the name of the layup file
###     output: data <np.array, double>, 2D array of all data contained in the layup file
def readLayupFile(fname):
    data = np.loadtxt(fname)  # read layup file and store all data in one array
    return data

### load the dictionary for columns in the 2D array of data from the layup file ###
###     input:  <none>
###     output: dataDict <dictionary>, dictionary of keywords that correspond to different columns of the data from the layup file
def loadDict():
    dataDict = {'spar station'                :  0,  # station numbers for the spar (begins at 1)
                'x1'                          :  1,  # distances from root (in meters)
                'eta'                         :  2,  # distances from root (dimensionless, normalized by total spar length)
                'spar fraction'               :  3,  # percentage distances from spar root (dimensionless, normalized by total spar length and multiplied by 100)
                'spar cap base'               :  4,  # spar cap base lengths (in meters)
                'spar cap height'             :  5,  # spar cap height lengths (in meters)
                'root buildup base'           :  6,  # root buildup base lengths (in meters)
                'root buildup height'         :  7,  # root buildup height lengths (in meters)
                'shear web base'              :  8,  # shear web base lengths (in meters)
                'shear web height'            :  9,  # shear web height lengths (in meters)
                'shear web foam base'         : 10,  # shear web foam base lengths (in meters)
                'shear web biaxial GFRP base' : 11,  # shear web biaxial GFRP base lengths (in meters)
                'twist degrees'               : 12,  # twist angles (in degrees)
                'twist radians'               : 13,  # twist angles (in radians)
                'k1'                          : 14,  # twist rates (in radians/meter)
                'blade station'               : 15,  # station numbers for the blade (begins at 7)
                'blade fraction'              : 16 } # percentage distances from blade root (dimensionless, normalized by total blade length and multiplied by 100)
    return dataDict


### extract a specific column from the layup data ###
###     input:  data <np.array, double>, 2D array of all data contained in the layup file
###             colname <string>, keyword name of the column to extract from the 2D array of data
###     output: dataCol <np.array>, array of the data in the desired column
def extractDataColumn(data,colname):
    dataDict = loadDict()  # load the dictionary of column name keywords
    if (colname == 'spar station' or colname == 'blade station'): # if the data is for a spar or blade station ...
        dataCol = np.int_( data[ :,dataDict[colname] ] )          # ... convert the data to integers
    else:
        dataCol = data[ :,dataDict[colname] ]
    return dataCol


### extract a specific row from the layup data ###
###     input:  data <np.array, double>, 2D array of all data contained in the layup file
###             stn <int>, spanwise station number
###     output: stationData <np.array>, array of the data for the desired station
def extractStationData(data,stn,print_flag=False):
    raw_stationData = data[stn-1,:]
    if int(raw_stationData[0]) != stn:
        print "ERROR: wrong station data pulled!"
    else:
        if print_flag:
            print "correct station data pulled!  :)"

    dataDict = loadDict()
    stationData = { 'spar cap height':     raw_stationData[dataDict['spar cap height']],
                    'root buildup height': raw_stationData[dataDict['root buildup height']],
                    'shear web height':    raw_stationData[dataDict['shear web height']] }

    return stationData


### extract the corners of the entire cross-section (XS) ###
###     input:  data <np.array, double>, 2D array of all data contained in the layup file
###             spar_stn <int>, station number for the cross-section of interest
###     output: corners <np.array>, 4x2 array of the x&y coordinates of the corners of the entire cross-section
###                                 row index 0: top left corner
###                                 row index 1: top right corner
###                                 row index 2: bottom left corner
###                                 row index 3: bottom right corner
def extract_XS_corners(data,spar_stn):
    n = spar_stn - 1  # subtract 1 from the spar station, b/c python arrays start with index 0
    ### read in the columns for spar cap base, shear web base, shear web height, & root buildup height
    sparcap_bse = extractDataColumn(data,'spar cap base')
    shearwb_bse = extractDataColumn(data,'shear web base')
    shearwb_ht  = extractDataColumn(data,'shear web height')
    rtbldup_ht  = extractDataColumn(data,'root buildup height')
    ### find and plot the corners of the cross-section ###
    total_bse = sparcap_bse[n] + 2.0 * shearwb_bse[n]
    total_ht = shearwb_ht[n] + 2.0 * rtbldup_ht[n]
    corners = np.zeros((4,2))  # column 0 stores x-coords, column 1 stores y-coords
    # store the x-coords #
    corners[0,0] = total_bse / 2.0 * -1.0
    corners[1,0] = corners[0,0] * -1.0
    corners[2:4,0] = corners[0:2,0]
    # store the y-coords #
    corners[0,1] = total_ht / 2.0
    corners[1,1] = corners[0,1]
    corners[2:4,1] = corners[0:2,1] * -1.0
    return corners


### extract the corners of the root buildup (RB) ###
###     input:  data <np.array, double>, 2D array of all data contained in the layup file
###             spar_stn <int>, station number for the cross-section of interest
###     output: rtbldup <np.array>, 2x4x2 array of the x&y coordinates of the corners of the root buildup
###                                 row index 0: top left corner
###                                 row index 1: top right corner
###                                 row index 2: bottom left corner
###                                 row index 3: bottom right corner
def extract_RB_corners(data,spar_stn):
    corners = extract_XS_corners(data,spar_stn)
    n = spar_stn - 1  # subtract 1 from the spar station, b/c python arrays start with index 0
    ### read in the columns for root buildup base & root buildup height
    rtbldup_bse = extractDataColumn(data,'root buildup base')
    rtbldup_ht  = extractDataColumn(data,'root buildup height')
    ### initialize the array of root buildup corners ###
    rtbldup = np.zeros((2,4,2))  # slice 0 stores upper root buildup, slice 1 stores lower root buildup
                                 # column 0 stores x-coords, column 1 stores y-coords
    if rtbldup_bse[n] * rtbldup_ht[n] > 0.0:  # only store corners of root buildup if its cross-sectional area is non-zero
        ## upper root buildup ## (slice 0, rtbldup[0,:,:])
        # store the x-coords #
        rtbldup[0,0:4,0] = corners[0:4,0]
        # store the y-coords #
        rtbldup[0,0:2,1] = corners[0:2,1]
        rtbldup[0,2:4,1] = rtbldup[0,0:2,1] - rtbldup_ht[n]
        ## lower root buildup ## (slice 1, rtbldup[1,:,:])
        # store the x-coords #
        rtbldup[1,0:4,0] = rtbldup[0,0:4,0]
        # store the y-coords #
        rtbldup[1,0:2,1] = rtbldup[0,2:4,1] * -1.0  # top row of lower root buildup = -1 * bottom row of upper root buildup
        rtbldup[1,2:4,1] = rtbldup[0,0:2,1] * -1.0  # bottom row of lower root buildup = -1 * top row of upper root buildup
    else:
        print "\n***ERROR: cross-sectional area of the root buildup is ZERO***\n"
    return rtbldup


### extract the corners of the shear webs (SW) ###
###     input:  data <np.array, double>, 2D array of all data contained in the layup file
###             spar_stn <int>, station number for the cross-section of interest
###     output: shearwb <np.array>, 2x3x4x2 array of the x&y coordinates of the corners of the shear webs
###                                 (array dimension 1) 2: left/right SHEAR WEB
###                                 (array dimension 2) 3: biax/foam/biax LAMINATE
###                                 (array dimension 3) 4: top left/top right/bottom left/bottom right CORNER
###                                 (array dimension 4) 2: x/y COORDINATE
###                                 row index 0: top left corner
###                                 row index 1: top right corner
###                                 row index 2: bottom left corner
###                                 row index 3: bottom right corner
def extract_SW_corners(data,spar_stn):
    corners = extract_XS_corners(data,spar_stn)
    n = spar_stn - 1  # subtract 1 from the spar station, b/c python arrays start with index 0
    ### read in the columns for spar cap base, shear web base, shear web height, & root buildup height
    rtbldup_bse = extractDataColumn(data,'root buildup base')
    rtbldup_ht  = extractDataColumn(data,'root buildup height')
    # shearwb_bse = extractDataColumn(data,'shear web base')
    shearwb_foam_bse = extractDataColumn(data,'shear web foam base')
    shearwb_biax_bse = extractDataColumn(data,'shear web biaxial GFRP base')

    ### initialize the array of shear web corners ###
    shearwb = np.zeros((2,3,4,2))  # column 0 stores x-coords, column 1 stores y-coords
    # shearwb[0,0,:,:]  is  left shear web, left biax laminate
    # shearwb[0,1,:,:]  is  left shear web, foam laminate
    # shearwb[0,2,:,:]  is  left shear web, right biax laminate
    # shearwb[1,0,:,:]  is  right shear web, left biax laminate
    # shearwb[1,1,:,:]  is  right shear web, foam laminate
    # shearwb[1,2,:,:]  is  right shear web, right biax laminate

    # shearwb[1,2,3,0]  is  right shear web, right biax laminate, bottom right corner, x-coordinate
    # shearwb[1,2,3,1]  is  right shear web, right biax laminate, bottom right corner, y-coordinate
    # etc ...

    ### left shear web ### (slice 0, shearwb[0,:,:,:])
    ## left shear web, left biax laminate ##  shearwb[0,0,:,:]
    # store coords shared with root buildup #
    if rtbldup_bse[n] * rtbldup_ht[n] > 0.0:  # only base corners of shear web off of root buildup if cross-sectional area of root buildup is non-zero
        rtbldup = extract_RB_corners(data,spar_stn)
        shearwb[0,0,0,:] = rtbldup[0,2,:] # top left corner of left shear web (left biax laminate), bottom left corner of upper root buildup
        shearwb[0,0,2,:] = rtbldup[1,0,:] # bottom left corner of left shear web (left biax laminate), top left corner of lower root buildup
    else:
        shearwb[0,0,0,:] = corners[0,:] # top left corner of left shear web, top left corner of cross-section
        shearwb[0,0,2,:] = corners[2,:] # bottom left corner of left shear web, bottom left corner of cross-section
    # store coords for right boundary of left shear web (left biax laminate) #
    shearwb[0,0,1,0] = shearwb[0,0,0,0] + shearwb_biax_bse[n]  # x-coord for top right corner (add shear web biaxial GFRP thickness)
    shearwb[0,0,1,1] = shearwb[0,0,0,1]                        # y-coord for top right corner
    shearwb[0,0,3,0] = shearwb[0,0,1,0]                        # x-coord for bottom right corner
    shearwb[0,0,3,1] = shearwb[0,0,2,1]                        # y-coord for bottom right corner
    
    ## left shear web, foam laminate ##  shearwb[0,1,:,:]
    # store coords shared with left shear web, left biax laminate #
    shearwb[0,1,0,:] = shearwb[0,0,1,:] # top left corner of left shear web (foam laminate), top right corner of left shear web (left biax laminate)
    shearwb[0,1,2,:] = shearwb[0,0,3,:] # bottom left corner of left shear web (foam laminate), bottom right corner of left shear web (left biax laminate)
    # store coords for right boundary of left shear web (foam laminate) #
    shearwb[0,1,1,0] = shearwb[0,1,0,0] + shearwb_foam_bse[n]  # x-coord for top right corner (add shear web foam thickness)
    shearwb[0,1,1,1] = shearwb[0,1,0,1]                        # y-coord for top right corner
    shearwb[0,1,3,0] = shearwb[0,1,1,0]                        # x-coord for bottom right corner
    shearwb[0,1,3,1] = shearwb[0,1,2,1]                        # y-coord for bottom right corner

    ## left shear web, right biax laminate ##  shearwb[0,2,:,:]
    # store coords shared with left shear web, left biax laminate #
    shearwb[0,2,0,:] = shearwb[0,1,1,:] # top left corner of left shear web (right biax laminate), top right corner of left shear web (foam laminate)
    shearwb[0,2,2,:] = shearwb[0,1,3,:] # bottom left corner of left shear web (right biax laminate), bottom right corner of left shear web (foam laminate)
    # store coords for right boundary of left shear web (foam laminate) #
    shearwb[0,2,1,0] = shearwb[0,2,0,0] + shearwb_biax_bse[n]  # x-coord for top right corner (add shear web biaxial GFRP thickness)
    shearwb[0,2,1,1] = shearwb[0,2,0,1]                        # y-coord for top right corner
    shearwb[0,2,3,0] = shearwb[0,2,1,0]                        # x-coord for bottom right corner
    shearwb[0,2,3,1] = shearwb[0,2,2,1]                        # y-coord for bottom right corner

    ### right shear web ### (slice 1, shearwb[1,:,:,:])
    ## right shear web, left biax laminate ##  shearwb[1,0,:,:]
    # store the x-coords #
    shearwb[1,0,0,0] = shearwb[0,2,1,0] * -1.0  # top left corner of right shear web (left biax laminate) = -1 * top right corner of left shear web (right biax laminate)
    shearwb[1,0,1,0] = shearwb[0,2,0,0] * -1.0  # top right corner of right shear web (left biax laminate) = -1 * top left corner of left shear web (right biax laminate)
    shearwb[1,0,2,0] = shearwb[0,2,3,0] * -1.0  # bottom left corner of right shear web (left biax laminate) = -1 * bottom right corner of left shear web (right biax laminate)
    shearwb[1,0,3,0] = shearwb[0,2,2,0] * -1.0  # bottom right corner of right shear web (left biax laminate) = -1 * bottom left corner of left shear web (right biax laminate)
    # store the y-coords #
    shearwb[1,0,0:4,1] = shearwb[0,2,0:4,1]

    ## right shear web, foam laminate ##  shearwb[1,1,:,:]
    # store the x-coords #
    shearwb[1,1,0,0] = shearwb[0,1,1,0] * -1.0  # top left corner of right shear web (foam laminate) = -1 * top right corner of left shear web (foam laminate)
    shearwb[1,1,1,0] = shearwb[0,1,0,0] * -1.0  # top right corner of right shear web (foam laminate) = -1 * top left corner of left shear web (foam laminate)
    shearwb[1,1,2,0] = shearwb[0,1,3,0] * -1.0  # bottom left corner of right shear web (foam laminate) = -1 * bottom right corner of left shear web (foam laminate)
    shearwb[1,1,3,0] = shearwb[0,1,2,0] * -1.0  # bottom right corner of right shear web (foam laminate) = -1 * bottom left corner of left shear web (foam laminate)
    # store the y-coords #
    shearwb[1,1,0:4,1] = shearwb[0,1,0:4,1]

    ## right shear web, right biax laminate ##  shearwb[1,2,:,:]
    # store the x-coords #
    shearwb[1,2,0,0] = shearwb[0,0,1,0] * -1.0  # top left corner of right shear web (right biax laminate) = -1 * top right corner of left shear web (left biax laminate)
    shearwb[1,2,1,0] = shearwb[0,0,0,0] * -1.0  # top right corner of right shear web (right biax laminate) = -1 * top left corner of left shear web (left biax laminate)
    shearwb[1,2,2,0] = shearwb[0,0,3,0] * -1.0  # bottom left corner of right shear web (right biax laminate) = -1 * bottom right corner of left shear web (left biax laminate)
    shearwb[1,2,3,0] = shearwb[0,0,2,0] * -1.0  # bottom right corner of right shear web (right biax laminate) = -1 * bottom left corner of left shear web (left biax laminate)
    # store the y-coords #
    shearwb[1,2,0:4,1] = shearwb[0,0,0:4,1]

    return shearwb


# ### extract the corners of the shear webs (SW) ###
# ###       input:  data <np.array, double>, 2D array of all data contained in the layup file
# ###               spar_stn <int>, station number for the cross-section of interest
# ###       output: shearwb <np.array>, 2x4x2 array of the x&y coordinates of the corners of the shear webs
# ###                                   row index 0: top left corner
# ###                                   row index 1: top right corner
# ###                                   row index 2: bottom left corner
# ###                                   row index 3: bottom right corner
# def extract_SW_corners(data,spar_stn):
#   corners = extract_XS_corners(data,spar_stn)
#   n = spar_stn - 1  # subtract 1 from the spar station, b/c python arrays start with index 0
#   ### read in the columns for spar cap base, shear web base, shear web height, & root buildup height
#   rtbldup_bse = extractDataColumn(data,'root buildup base')
#   rtbldup_ht  = extractDataColumn(data,'root buildup height')
#   shearwb_bse = extractDataColumn(data,'shear web base')
#   ### initialize the array of shear web corners ###
#   shearwb = np.zeros((2,4,2))  # slice 0 stores left shear web, slice 1 stores right shear web
#                                # column 0 stores x-coords, column 1 stores y-coords
#   ## left shear web ## (slice 0, shearwb[0,:,:])
#   # store coords shared with root buildup #
#   if rtbldup_bse[n] * rtbldup_ht[n] > 0.0:  # only base corners of shear web off of root buildup if cross-sectional area of root buildup is non-zero
#       rtbldup = extract_RB_corners(data,spar_stn)
#       shearwb[0,0,:] = rtbldup[0,2,:] # top left corner of left shear web, bottom left corner of upper root buildup
#       shearwb[0,2,:] = rtbldup[1,0,:] # bottom left corner of left shear web, top left corner of lower root buildup
#   else:
#       shearwb[0,0,:] = corners[0,:] # top left corner of left shear web, top left corner of cross-section
#       shearwb[0,2,:] = corners[2,:] # bottom left corner of left shear web, bottom left corner of cross-section
#   # store coords for right boundary of left shear web #
#   shearwb[0,1,0] = shearwb[0,0,0] + shearwb_bse[n]  # x-coord for top right corner (add shear web thickness)
#   shearwb[0,1,1] = shearwb[0,0,1]                   # y-coord for top right corner
#   shearwb[0,3,0] = shearwb[0,1,0]                   # x-coord for bottom right corner
#   shearwb[0,3,1] = shearwb[0,2,1]                   # y-coord for bottom right corner
#   ## right shear web ## (slice 1, shearwb[1,:,:])
#   # store the x-coords #
#   shearwb[1,0,0] = shearwb[0,1,0] * -1.0  # top left corner of right shear web = -1 * top right corner of left shear web
#   shearwb[1,1,0] = shearwb[0,0,0] * -1.0  # top right corner of right shear web = -1 * top left corner of left shear web
#   shearwb[1,2,0] = shearwb[0,3,0] * -1.0  # bottom left corner of right shear web = -1 * bottom right corner of left shear web
#   shearwb[1,3,0] = shearwb[0,2,0] * -1.0  # bottom right corner of right shear web = -1 * bottom left corner of left shear web
#   # store the y-coords #
#   shearwb[1,0:4,1] = shearwb[0,0:4,1]
#   return shearwb


### extract the corners of the spar caps (SC) ###
###     input:  data <np.array, double>, 2D array of all data contained in the layup file
###             spar_stn <int>, station number for the cross-section of interest
###     output: sparcap <np.array>, 2x4x2 array of the x&y coordinates of the corners of the spar caps
###                                 row index 0: top left corner
###                                 row index 1: top right corner
###                                 row index 2: bottom left corner
###                                 row index 3: bottom right corner
def extract_SC_corners(data,spar_stn):
    shearwb = extract_SW_corners(data,spar_stn)
    n = spar_stn - 1  # subtract 1 from the spar station, b/c python arrays start with index 0
    ### read in the columns for spar cap base, shear web base, shear web height, & root buildup height
    sparcap_ht  = extractDataColumn(data,'spar cap height')
    ### initialize the array of shear web corners ###
    sparcap = np.zeros((2,4,2))  # slice 0 stores upper spar cap, slice 1 stores lower spar cap
                                 # column 0 stores x-coords, column 1 stores y-coords
    ## upper spar cap ## (slice 0, sparcap[0,:,:])
    # store coords shared with shear webs #
    sparcap[0,0,:] = shearwb[0,2,1,:] # top left corner of upper spar cap, top right corner of left shear web (right biax laminate)
    sparcap[0,1,:] = shearwb[1,0,0,:] # top right corner of upper spar cap, top left corner of right shear web (left biax laminate)
    # store coords for lower boundary of upper spar cap #
    sparcap[0,2,0] = sparcap[0,0,0]                  # x-coord for bottom left corner
    sparcap[0,2,1] = sparcap[0,0,1] - sparcap_ht[n]  # y-coord for bottom left corner (subtract spar cap thickness)
    sparcap[0,3,0] = sparcap[0,1,0]                  # x-coord for bottom right corner
    sparcap[0,3,1] = sparcap[0,2,1]                  # y-coord for bottom right corner
    ## lower spar cap ## (slice 1, sparcap[1,:,:])
    # store the x-coords #
    sparcap[1,0:4,0] = sparcap[0,0:4,0]
    # store the y-coords #
    sparcap[1,0:2,1] = sparcap[0,2:4,1] * -1.0  # top row of lower spar cap = -1 * bottom row of upper spar cap
    sparcap[1,2:4,1] = sparcap[0,0:2,1] * -1.0  # bottom row of lower spar cap = -1 * top row of upper spar cap
    return sparcap

if __name__ == '__main__':  # only run this block of code if this file is called directly from the command line
    # import the data from the layup file
    spar_file = '../monoplane_spar_layup.txt'
    print 'STATUS: importing spar layup file: ' + spar_file + '  ...'
    data = readLayupFile(spar_file)
    stationData = extractStationData(data,14,print_flag=True)
    extractDataColumn(stationData,'spar cap base')