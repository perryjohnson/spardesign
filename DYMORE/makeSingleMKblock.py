import DYMOREutilities as du
import os
os.chdir('..')
import truegrid.read_layup as rl
os.chdir('DYMORE')

# parameters #####################################################################
spar_station = 16
dymoreMKfile = du.makeFile('spar_station_16__k2_0020_MK.dat')
vabsMK = '../VABS/cs_database/biplane_full-hSW_curved/spar_station_16__k2_0020.dat.K'
##################################################################################


# write the mass and stiffness matrices as a DYMORE-formatted file
layup_data = rl.readLayupFile('../truegrid/biplane_cross-sections_layup_20120517_full-hSW.txt')
stationData = rl.extractStationData(layup_data,spar_station)
du.writeMKmatrices(dymoreMKfile, vabsMK, stationData, CoordType='ETA_COORDINATE', debug_flag=True)
dymoreMKfile.close()