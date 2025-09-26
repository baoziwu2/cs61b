# encoding: utf-8
# module numpy._core._umath_tests
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\_core\_umath_tests.cp313-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__version__ = '0.1'

# functions

def always_error(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    always_error(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])
    
    simply, broken, ufunc that sets an error (but releases the GIL).
    """
    pass

def always_error_gufunc(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    always_error_gufunc(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    simply, broken, gufunc that sets an error (but releases the GIL).
    """
    pass

def conv1d_full(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    conv1d_full(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    convolution of x and y ('full' mode)
    """
    pass

def cross1d(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cross1d(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    cross product on the last dimension and broadcast on the rest 
         "(3),(3)->(3)"
    """
    pass

def cumsum(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cumsum(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    Cumulative sum of the input (n)->(n)
    """
    pass

def euclidean_pdist(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    euclidean_pdist(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    pairwise euclidean distance on last two dimensions 
         "(n,d)->(p)"
    """
    pass

def indexed_negative(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ indexed_negative(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature]) """
    pass

def inner1d(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    inner1d(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    inner on the last dimension and broadcast on the rest 
         "(i),(i)->()"
    """
    pass

def inner1d_no_doc(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ inner1d_no_doc(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis]) """
    pass

def innerwt(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    innerwt(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    inner1d with a weight argument 
         "(i),(i),(i)->()"
    """
    pass

def matmul(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    matmul(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    matmul on last two dimensions, with some being optional
         "(m?,n),(n,p?)->(m?,p?)"
    """
    pass

def matrix_multiply(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    matrix_multiply(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    matrix multiplication on last two dimensions 
         "(m,n),(n,p)->(m,p)"
    """
    pass

def test_dispatch(*args, **kwargs): # real signature unknown
    pass

def test_signature(*args, **kwargs): # real signature unknown
    """
    Test signature parsing of ufunc. 
    Arguments: nin nout signature 
    If fails, it returns NULL. Otherwise it returns a tuple of ufunc internals.
    """
    pass

def _pickleable_module_global_ufunc(*args, **kwargs): # real signature unknown
    """
    _pickleable_module_global.ufunc(, /, out=(), *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])
    
    A dotted name for pickle testing, does nothing.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D05698B890>'

__spec__ = None # (!) real value is "ModuleSpec(name='numpy._core._umath_tests', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D05698B890>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\numpy\\\\_core\\\\_umath_tests.cp313-win_amd64.pyd')"

