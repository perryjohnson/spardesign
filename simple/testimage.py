import numpy
from mayavi.mlab import *

def test_imshow():
    """ Use imshow to visualize a 2D 10x10 random array.
    """
    # s = numpy.random.random((3,3))
    s = numpy.array([[1, 2, 3],
                     [1, 2, 3],
                     [1, 2, 3]])
    print s
    return imshow(s, colormap='gist_earth')

if __name__ == '__main__':
    test_imshow()