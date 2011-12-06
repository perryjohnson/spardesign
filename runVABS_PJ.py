#! /bin/python
# script to run VABS from current directory,
# then move VABS output files to a subdirectory of the same name
# usage: runVABS_PJ.py FILEIN.dat

import sys, os, shutil

# copy VABS license to current directory
shutil.copy('D:\\Programs\\VABS\\VABS3.5ReleasesPC64bit-07-20-2011\\license', '.')

# execute VABS
os.system('VABSIII.exe ' + sys.argv[1])  # note: sys.argv[1] = FILEIN.dat

# remove license file from current directory
os.remove('license')