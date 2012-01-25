import numpy as np

from mayavi import mlab
mlab.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
mlab.clf()

# We create a list of positions and connections, each describing a line.
x = np.array([np.nan, 0, 2, 2, 0, 4])
y = np.array([np.nan, 0, 0, 2, 2, 1])
z = np.array([np.nan, 0, 0, 0, 0, 0])
connections = np.array([[1, 2],
                        [2, 3],
                        [3, 4],
                        [4, 1],
                        [2, 5],
                        [5, 3],
                        [3, 2]])


# Create the points
src = mlab.pipeline.scalar_scatter(x, y, z)

# Connect them
src.mlab_source.dataset.lines = connections

# Finally, display the set of lines
mlab.pipeline.surface(src, line_width=1, opacity=1.0, color=(0,0,0))

# also, plot the nodes
mlab.pipeline.glyph(src, color=(0,0,0), mode='2dcircle', scale_factor='0.1')

# And choose a nice view
mlab.view(0, 0)
mlab.show()


