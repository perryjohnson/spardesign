import time

# record the time when the code starts
start_time = time.time()

import read_layup as rl
import TRUEGRIDutilities as tgu

main_debug_flag = True
run_TG_silent = False

sw_foam_base = 0.080 # units: meters
sw_foam_ielem = 8
maxAR = 1.3


for i in range(1,6+1):
    spar_station = i
    if spar_station < 10:
        basefilestr = 'spar_station_0' + str(spar_station)
    else:
        basefilestr = 'spar_station_' + str(spar_station)

    print ''
    print '***************'
    print basefilestr
    print '***************'

    # ----------------------------------------------------------------------------------

    data = rl.readLayupFile('monoplane_spar_layup.txt')
    stationData = rl.extractStationData(data,spar_station)
    (sw_foam_ielem,sw_foam_jelem) = tgu.calcCellNums(sw_foam_base,sw_foam_ielem,maxAR,stationData['shear web height'])
    if sw_foam_jelem % 2 != 0:  # if this number isn't even...
        sw_foam_jelem += 1      # add 1 to it to make it even
    if main_debug_flag:
        print 'spar cap height:     ' + ('%5.3f' % stationData['spar cap height'])     + ' m'
        print 'root buildup height: ' + ('%5.3f' % stationData['root buildup height']) + ' m'
        print 'shear web height:    ' + ('%5.3f' % stationData['shear web height'])    + ' m'
        print 'sw foam j-elems:     ' + str(sw_foam_jelem)
        if run_TG_silent:
            print 'silent flag is ON (TrueGrid will exit at end of script)'
        else:
            print 'silent flag is OFF'

    # ----------------------------------------------------------------------------------

    tgTemplate = tgu.readFile('spar_station_nn.tg')
    tgFile = tgu.makeTGFile(basefilestr)
    tgTemplate = tgu.replaceDefaults(tgTemplate, spar_station, stationData, sw_foam_jelem, silent_flag=run_TG_silent)
    tgu.writeNewTGscript(tgFile, tgTemplate)
    tgFile.close()



# ----------------------------------------------------------------------------------
# calculate the time it took to run the code
elapsed_time_tot = time.time() - start_time
elapsed_min_tot = int(elapsed_time_tot/60)  # extract minutes elapsed
elapsed_sec_tot = elapsed_time_tot % 60     # extract seconds elapsed
print ""
print "program completed in " + str(elapsed_min_tot) + ":" + ("%.2f" % round(elapsed_sec_tot,2)) + "  (min:sec)"