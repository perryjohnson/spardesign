import truegrid.read_layup as rl
import DYMORE.DYMOREutilities as du
data = rl.readLayupFile('truegrid/monoplane_spar_layup.txt')

spar_stn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # generate grids for these spar stations

dymoreMKfile = du.makeMKfile()

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
    if stationData['spar station'] < 10:
        sparstnstr = '0' + str(stationData['spar station'])
    else:
        sparstnstr = str(stationData['spar station'])
    vabsMK = 'VABS/M_and_K_matrices/spar_station_' + sparstnstr + '.dat.K'
    du.writeMKmatrices(dymoreMKfile, vabsMK, stationData, debug_flag=True)

dymoreMKfile.close()