import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri

node,x2,x3,U1,U2,U3 = np.loadtxt('spar_station_24.dat.U', unpack=True)
# node = int(node)

# x,y1,y2,y3,y4,stress = np.loadtxt('data.txt', skiprows=2, delimiter=',', unpack=True)

# Arrays of all the point coordinates and stresses.
n = len(x2)
# x = np.hstack((x,x,x,x))
# y = np.hstack((y1,y2,y3,y4))
# stress = np.hstack((stress,stress,stress,stress))

# Triangle connectivity.
triangles = []
for i in range(n-1):
  triangles.append([i,i+1,n+i])
  triangles.append([i+1,n+i+1,n+i])
  triangles.append([2*n+i,2*n+i+1,3*n+i])
  triangles.append([2*n+i+1,3*n+i+1,3*n+i])

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(x2, x3)

# Plot.
plt.tricontourf(triang, U1, 256)
plt.colorbar()
plt.show() 