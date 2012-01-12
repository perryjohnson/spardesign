# from numpy import array
from tvtk.api import tvtk
from mayavi import mlab


### generate a rectilinear grid with TVTK
###     input: x <np.array>, array of x-coordinates for tvtk.RectilinearGrid().x_coordinates in mayavi
###            y <np.array>, array of y-coordinates for tvtk.RectilinearGrid().y_coordinates in mayavi
###     output: r <tvtk object>, rectilinear grid object from TVTK
def genRectGrid(x,y):
    r = tvtk.RectilinearGrid()
    r.dimensions = (len(x),len(y),1)  # (num_of_x_coordinates, num_of_y_coordinates, 1=<no z_coordinates>?)
    (r.x_coordinates, r.y_coordinates) = (x,y)
    return r


### draw a GridPlane module in Mayavi
###     input: dataset <tvtk object>, rectilinear grid object from TVTK
###     output: <none>
def drawGridPlane(dataset):
    gp = mlab.pipeline.grid_plane(dataset,
                                  line_width=0.5,
                                  color=(0,0,0))  # draw the grid plane from the dataset
    return


### draw a Surface module in Mayavi
###     input: dataset <tvtk object>, rectilinear grid object from TVTK
###     output: <none>
def drawSurface(dataset,color_tuple=(0,0,0),opacity_value=0.5):
    surf = mlab.pipeline.surface(dataset,
                                 color=color_tuple,
                                 opacity=opacity_value)     # fill in the grid with a half-transparent red
    return


### draw a rectilinear grid from TVTK as a GridPlane in Mayavi
###     input: x_coords <np.array>, array of x-coordinates for tvtk.RectilinearGrid().x_coordinates in mayavi
###            y_coords <np.array>, array of y-coordinates for tvtk.RectilinearGrid().y_coordinates in mayavi
###     output: Mayavi plot of the grid (on the screen)
def plotRectGrid(x_coords,y_coords):
    grid = genRectGrid(x_coords,y_coords)
    drawGridPlane(grid)
    # drawSurface(grid,(0,0,1))
    return


###
def plotSurface(x_coords,y_coords,color_tuple=(0,0,0),opacity_value=0.5):
    grid = genRectGrid(x_coords,y_coords)
    drawSurface(grid,color_tuple,opacity_value)
    return


### TEST FUNCTIONS ###
# def generate_grid():
#     r = tvtk.RectilinearGrid()
#     r.dimensions = (3,4,1)  # (num_of_x_coordinates, num_of_y_coordinates, 1=<no z_coordinates>?)
#     r.x_coordinates = array((0, 0.7, 1.4))
#     r.y_coordinates = array((0, 1, 3, 4))
#     return r

# def generate_grid2():
#     r = tvtk.RectilinearGrid()
#     r.dimensions = (3,4,1)  # (num_of_x_coordinates, num_of_y_coordinates, 1=<no z_coordinates>?)
#     r.x_coordinates = array((-1.0, -0.5, 0))
#     r.y_coordinates = array((0, 0.5, 0.7, 1.0))
#     return r

# def generate_grid3():
#     r = tvtk.RectilinearGrid()
#     r.dimensions = (3,4,1)  # (num_of_x_coordinates, num_of_y_coordinates, 1=<no z_coordinates>?)
#     r.x_coordinates = array((-1.0, -0.5, 0))
#     r.y_coordinates = array((1.5, 2.5, 2.7, 3.0))
#     return r


# @mlab.show  # the @ is a python function "decorator"... so, the call: main() = mlab.show(main()) ... its like shorthand?!?!
# def main():
#     fig = mlab.figure(figure='Cartesian grid', size=(800,800))  # make a new mayavi scene (figure window)
#     view(generate_grid())  # plot the first grid
#     view(generate_grid2()) # plot the second grid (in the same window)
#     view(generate_grid3())
#     mlab.view(0, 0)  # set the view to -Z (better for 2D grids)
#     return
    

# @mlab.show
# def main2():    # hardcoded to display the bottom root buildup grid in mayavi
#     fig = mlab.figure(figure='bottom root buildup grid', size=(600,750))  # make a new mayavi scene (figure window)
#     x_coord1 = array([-0.836     , -0.82342857, -0.81085714, -0.79828571, -0.78571429,
#                       -0.77314286, -0.76057143, -0.748     , -0.73542857, -0.72285714,
#                       -0.71028571, -0.69771429, -0.68514286, -0.67257143, -0.66      ,
#                       -0.64742857, -0.63485714, -0.62228571, -0.60971429, -0.59714286,
#                       -0.58457143, -0.572     , -0.55942857, -0.54685714, -0.53428571,
#                       -0.52171429, -0.50914286, -0.49657143, -0.484     , -0.47142857,
#                       -0.45885714, -0.44628571, -0.43371429, -0.42114286, -0.40857143,
#                       -0.396     , -0.38342857, -0.37085714, -0.35828571, -0.34571429,
#                       -0.33314286, -0.32057143, -0.308     , -0.29542857, -0.28285714,
#                       -0.27028571, -0.25771429, -0.24514286, -0.23257143, -0.22      ,
#                       -0.20742857, -0.19485714, -0.18228571, -0.16971429, -0.15714286,
#                       -0.14457143, -0.132     , -0.11942857, -0.10685714, -0.09428571,
#                       -0.08171429, -0.06914286, -0.05657143, -0.044     , -0.03142857,
#                       -0.01885714, -0.00628571,  0.00628571,  0.01885714,  0.03142857,
#                        0.044     ,  0.05657143,  0.06914286,  0.08171429,  0.09428571,
#                        0.10685714,  0.11942857,  0.132     ,  0.14457143,  0.15714286,
#                        0.16971429,  0.18228571,  0.19485714,  0.20742857,  0.22      ,
#                        0.23257143,  0.24514286,  0.25771429,  0.27028571,  0.28285714,
#                        0.29542857,  0.308     ,  0.32057143,  0.33314286,  0.34571429,
#                        0.35828571,  0.37085714,  0.38342857,  0.396     ,  0.40857143,
#                        0.42114286,  0.43371429,  0.44628571,  0.45885714,  0.47142857,
#                        0.484     ,  0.49657143,  0.50914286,  0.52171429,  0.53428571,
#                        0.54685714,  0.55942857,  0.572     ,  0.58457143,  0.59714286,
#                        0.60971429,  0.62228571,  0.63485714,  0.64742857,  0.66      ,
#                        0.67257143,  0.68514286,  0.69771429,  0.71028571,  0.72285714,
#                        0.73542857,  0.748     ,  0.76057143,  0.77314286,  0.78571429,
#                        0.79828571,  0.81085714,  0.82342857,  0.836     ])
#     y_coord1 = array([-2.633 , -2.6435, -2.654 , -2.6645, -2.675 , -2.6855, -2.696 ])
#     view(genRectGrid(x_coord1,y_coord1))
#     mlab.view(0, 0)  # set the view to -Z (better for 2D grids)
#     return


# if __name__ == '__main__':
#     # main()
#     main2()