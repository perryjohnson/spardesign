import numpy
from mayavi.mlab import *

def test_triangular_mesh():
    """An example of a cone, ie a non-regular mesh defined by its
        triangles.
    """
    n = 4
    t = numpy.linspace(0.0, numpy.pi, n)
    z = numpy.exp(1j*t)
    x = z.real.copy()
    y = z.imag.copy()
    z = numpy.zeros_like(x)

    triangles = [(0, i, i+1) for i in range(1, n)]
    x = numpy.r_[0, x]
    y = numpy.r_[0, y]
    z = numpy.r_[0, z]
    t = numpy.r_[0, t]
    print "x =", x
    print "y =", y
    print "z =", z
    print "triangles =", triangles

    return triangular_mesh(x, y, z, triangles, scalars=t)

if __name__ == '__main__':
    test_triangular_mesh()