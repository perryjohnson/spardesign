import os

print "\n**********"
print "running VABS in normal mode..."
os.chdir('../../VABS')
os.system(r'.\VABSIII .\input_files\spar_station_24.dat')

print "\n**********"
print "setting recover_flag = 1"
f = open('./input_files/spar_station_24.dat', 'r+')   # read the file
f.readline()  # skip the first line of the VABS input file
recover_flag_line_pos = f.tell() # save the position of the line containing the recover_flag
f.seek(recover_flag_line_pos)
f.write('1 1 0')  # set recover_flag = 1
f.close()

print "\n**********"
print "running VABS in recovery mode..."
os.system(r'.\VABSIII .\input_files\spar_station_24.dat')

os.chdir('D:\\Dropbox\\ucla\\research\\perry\\github\\spardesign\\postprocessing\\VABS')