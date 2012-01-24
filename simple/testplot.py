import numpy as np
import autogridgen.cartGrid as cg
from mayavi import mlab

(x1,y1) = (0,0)
(x2,y2) = (2,0)
(x3,y3) = (2,2)
(x4,y4) = (0,2)

nrows = 2
ncols = 2
corners = np.array([[x4,y4],
                    [x3,y3],
                    [x1,y1],
                    [x2,y2]])

(node, element, number_of_nodes, number_of_elements) = cg.storeGridPoints3(nrows, ncols, corners)


# extract coordinates
x = [np.nan]
y = [np.nan]
z = [np.nan]
for i in range(1,number_of_nodes+1):
    x.append(node[i].x2)
    y.append(node[i].x3)
    z.append(0)

# extract connectivity
conn = np.array([])
i = 1
for i in range(1,number_of_elements+1):
    if (i == 1):
        conn = np.array([[element[i].node1.node_no, element[i].node2.node_no],
                         [element[i].node2.node_no, element[i].node3.node_no],
                         [element[i].node3.node_no, element[i].node4.node_no],
                         [element[i].node4.node_no, element[i].node1.node_no]])
    else:
        conn = np.vstack( (conn, np.array([[element[i].node1.node_no, element[i].node2.node_no],
                                           [element[i].node2.node_no, element[i].node3.node_no],
                                           [element[i].node3.node_no, element[i].node4.node_no],
                                           [element[i].node4.node_no, element[i].node1.node_no]]) ) )

# create the plot
mlab.figure(1, size=(400, 400), bgcolor=(1, 1, 1))
mlab.clf()

# Create the points
src = mlab.pipeline.scalar_scatter(x, y, z)

# Connect them
src.mlab_source.dataset.lines = conn

# Finally, display the set of lines
mlab.pipeline.surface(src, line_width=1, opacity=1.0)

# And choose a nice view
mlab.view(0, 0)
mlab.show()


