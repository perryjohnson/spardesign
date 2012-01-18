import numpy as np

connectivity = np.loadtxt('connectivity_4.txt', dtype='int')
conn = connectivity[:,1:5]  # throw out the zero entries for nodes 5-9
c = np.sort(conn, axis=None)
d = np.diff(c)
err = np.nonzero(d > 1)

# print err

filestr = 'output_connectivity_4.txt'
outfile = open(filestr, 'w+')

outfile.write( str(c[0]) + '\n' )

for i in range(1,len(c)):
	outfile.write( str(c[i]) + '\t' + str(d[i-1]) + '\n' )