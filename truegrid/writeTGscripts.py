import time

# record the time when the code starts
start_time = time.time()

import read_layup as rl
import TRUEGRIDutilities as tgu

main_debug_flag = True
run_TG_silent = True

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
    if main_debug_flag:
        print 'spar cap height:     ' + ('%5.3f' % stationData['spar cap height'])     + ' m'
        print 'root buildup height: ' + ('%5.3f' % stationData['root buildup height']) + ' m'
        print 'shear web height:    ' + ('%5.3f' % stationData['shear web height'])    + ' m'
        if run_TG_silent:
            print 'silent flag is ON (TrueGrid will exit at end of script)'
        else:
            print 'silent flag is OFF'

    # ----------------------------------------------------------------------------------

    tgTemplate = tgu.readFile('spar_station_nn.tg')
    tgFile = tgu.makeTGFile(basefilestr)
    tgTemplate = tgu.replaceDefaults(tgTemplate, spar_station, stationData, silent_flag=run_TG_silent)
    tgu.writeNewTGscript(tgFile, tgTemplate)
    tgFile.close()



# ----------------------------------------------------------------------------------
# calculate the time it took to run the code
elapsed_time_tot = time.time() - start_time
elapsed_min_tot = int(elapsed_time_tot/60)  # extract minutes elapsed
elapsed_sec_tot = elapsed_time_tot % 60     # extract seconds elapsed
print ""
print "program completed in " + str(elapsed_min_tot) + ":" + ("%.2f" % round(elapsed_sec_tot,2)) + "  (min:sec)"