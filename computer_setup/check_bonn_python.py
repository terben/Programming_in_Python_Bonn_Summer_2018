""" Run this file to check your python installation.
"""
from numpy.testing import assert_array_equal

def test_python_version():
    import sys

    version_found = (int(sys.version[0]), int(sys.version[2]))
    assert version_found >= (3, 6)

def test_import_jupyter():
    import jupyter_core

def test_jupyter_version():
    import jupyter_core

    version_found = jupyter_core.__version__.split(".")
    version_found = tuple(int(num) for num in version_found)
    assert version_found >= (4, 3)

def test_import_numpy():
    import numpy

def test_numpy_version():
    import numpy
    version_found = numpy.__version__.split(".")
    version_found = tuple(int(num) for num in version_found)
    assert version_found >= (1, 11)

def test_import_matplotlib():
    from matplotlib.pyplot import plot

def test_matplotlib_version():
    import matplotlib
    version_found = matplotlib.__version__.split(".")
    version_found = tuple(int(num) for num in version_found)
    assert version_found >= (2, 0)

def test_slicing():
    from numpy import array
    x = array([[1, 2, 3], [4, 5, 6]])
    assert_array_equal(x[:, ::2], array([[1, 3], [4, 6]]))

def test_import_scipy():
    import scipy

def test_scipy_version():
    import scipy
    version_found = scipy.__version__.split(".")
    version_found = tuple(int(num) for num in version_found)
    assert version_found >= (0, 18)

def test_import_sympy():
    import sympy

def test_sympy_version():
    import sympy
    version_found = sympy.__version__.split(".")
    version_found = tuple(int(num) for num in version_found)
    assert version_found >= (1, 0)

if __name__ == "__main__":
    import nose
    nose.run(defaultTest=__name__)
