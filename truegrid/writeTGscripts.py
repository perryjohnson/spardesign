import time

# record the time when the code starts
start_time = time.time()

import read_layup as rl
import TRUEGRIDutilities as tgu

main_debug_flag = True
run_TG_silent = True

# set constants
sw_foam_base = 0.080 # units: meters
sc_base = 1.5 # units: meters

# set parameters
sw_foam_ielem_init = 12 #10 #8 #4
sc_ielem_init = 120 #100 #80 #40
maxAR = 1.34

spar_stn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # generate grids for these spar stations
# spar_stn_list = [4]  # generate grids for these spar stations (subset)

# read the layup file
data = rl.readLayupFile('monoplane_spar_layup.txt')

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

    # ----------------------------------------------------------------------------------

    stationData = rl.extractStationData(data,spar_station)
    if stationData['root buildup height'] > 0.0:
        RB_flag = True
    else:
        RB_flag = False
    (sw_foam_ielem,sw_foam_jelem) = tgu.calcCellNums(sw_foam_base,sw_foam_ielem_init,maxAR,stationData['shear web height'])
    (sc_ielem,sc_jelem) = tgu.calcCellNums(sc_base,sc_ielem_init,maxAR,stationData['spar cap height'])
    if sw_foam_jelem % 2 != 0:  # if this number isn't even...
        sw_foam_jelem += 1      # add 1 to it to make it even
    if sc_jelem % 2 != 0:  # if this number isn't even...
        sc_jelem += 1      # add 1 to it to make it even
    elemData = { 'shear web foam, i-elements': sw_foam_ielem,
                 'shear web foam, j-elements': sw_foam_jelem,
                 'spar cap, i-elements': sc_ielem,
                 'spar cap, j-elements': sc_jelem }
    if main_debug_flag:
        if RB_flag:
            print 'root buildup height: ' + ('%5.3f' % stationData['root buildup height']) + ' m'
        print 'shear web height:    ' + ('%5.3f' % stationData['shear web height'])    + ' m'
        print '  sw foam i-elems:   ' + str(sw_foam_ielem)
        print '  sw foam j-elems:   ' + str(sw_foam_jelem)
        print 'spar cap height:     ' + ('%5.3f' % stationData['spar cap height'])     + ' m'
        print '  sc i-elems:        ' + str(sc_ielem)
        print '  sc j-elems:        ' + str(sc_jelem)
        if run_TG_silent:
            print 'silent flag is ON (TrueGrid will exit at end of script)'
        else:
            print 'silent flag is OFF'

    # ----------------------------------------------------------------------------------

    tgTemplate = tgu.readFile('spar_station_nn.tg')
    tgFile = tgu.makeTGFile(basefilestr)
    tgTemplate = tgu.replaceDefaults(tgTemplate, spar_station, stationData, elemData, silent_flag=run_TG_silent)
    if not RB_flag:
        tgTemplate = tgu.removeRBentries(tgTemplate)
    tgu.writeNewTGscript(tgFile, tgTemplate)
    tgFile.close()

# ----------------------------------------------------------------------------------
print ""
# print constants
print "CONSTANTS:"
print '  shear web foam base: ' + ('%5.3f' % sw_foam_base) + ' m'
print '  spar cap base:       ' + ('%5.3f' % sc_base)      + ' m'

# print parameters
print "PARAMETERS:"
print '  shear web foam, i-elements (initial guess): ' + ('%3d' % sw_foam_ielem_init)
print '  spar cap, i-elements (initial guess):       ' + ('%3d' % sc_ielem_init)
print '  maximum aspect ratio for a cell:            ' + ('%6.2f' % maxAR)

# calculate the time it took to run the code
elapsed_time_tot = time.time() - start_time
elapsed_min_tot = int(elapsed_time_tot/60)  # extract minutes elapsed
elapsed_sec_tot = elapsed_time_tot % 60     # extract seconds elapsed
print ""
print "program completed in " + str(elapsed_min_tot) + ":" + ("%.2f" % round(elapsed_sec_tot,2)) + "  (min:sec)"