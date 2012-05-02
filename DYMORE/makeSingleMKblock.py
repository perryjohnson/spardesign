import DYMOREutilities as du

dymoreMKfile = du.makeFile('spar_station_16__k2_0019_MK.dat')

vabsMK = '../VABS/cs_database/biplane_curved/spar_station_16__k2_0019.dat.K'

import truegrid.read_layup as rl

layup_data = rl.readLayupFile('../truegrid/biplane_cross-sections_layup.txt')

spar_station = 16

stationData = rl.extractStationData(layup_data,spar_station)

du.writeMKmatrices(dymoreMKfile, vabsMK, stationData, CoordType='ETA_COORDINATE', debug_flag=True)

dymoreMKfile.close()