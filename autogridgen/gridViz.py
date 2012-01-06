from numpy import array
from tvtk.api import tvtk
from mayavi import mlab


def generate_grid():
    r = tvtk.RectilinearGrid()
    r.dimensions = (3,4,1)  # (num_of_x_coordinates, num_of_y_coordinates, 1=<no z_coordinates>?)
    r.x_coordinates = array((0, 0.7, 1.4))
    r.y_coordinates = array((0, 1, 3, 4))
    return r


def generate_grid2():
    r = tvtk.RectilinearGrid()
    r.dimensions = (3,4,1)  # (num_of_x_coordinates, num_of_y_coordinates, 1=<no z_coordinates>?)
    r.x_coordinates = array((-1.0, -0.5, 0))
    r.y_coordinates = array((0, 0.5, 0.7, 1.0))
    return r


def generate_grid3():
    r = tvtk.RectilinearGrid()
    r.dimensions = (3,4,1)  # (num_of_x_coordinates, num_of_y_coordinates, 1=<no z_coordinates>?)
    r.x_coordinates = array((-1.0, -0.5, 0))
    r.y_coordinates = array((1.5, 2.5, 2.7, 3.0))
    return r


def view(dataset):
    mlab.view(0, 0)  # set the view to -Z (better for 2D grids)
    gp = mlab.pipeline.grid_plane(dataset)  # draw the grid plane from the dataset


@mlab.show  # the @ is a python function "decorator"... so, the call: main() = mlab.show(main()) ... its like shorthand?!?!
def main():
    fig = mlab.figure(figure='Cartesian grid', size=(600,750))  # make a new mayavie scene (figure window)
    view(generate_grid())  # plot the first grid
    view(generate_grid2()) # plot the second grid (in the same window)
    view(generate_grid3())

if __name__ == '__main__':
    main()