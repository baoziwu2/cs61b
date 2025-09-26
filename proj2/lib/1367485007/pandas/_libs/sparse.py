# encoding: utf-8
# module pandas._libs.sparse
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\sparse.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py

# functions

def get_blocks(*args, **kwargs): # real signature unknown
    pass

def make_mask_object_ndarray(*args, **kwargs): # real signature unknown
    pass

def sparse_add_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_add_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_and_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_and_uint8(*args, **kwargs): # real signature unknown
    pass

def sparse_div_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_div_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_eq_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_eq_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_floordiv_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_floordiv_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_ge_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_ge_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_gt_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_gt_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_le_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_le_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_lt_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_lt_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_mod_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_mod_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_mul_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_mul_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_ne_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_ne_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_or_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_or_uint8(*args, **kwargs): # real signature unknown
    pass

def sparse_pow_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_pow_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_sub_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_sub_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_truediv_float64(*args, **kwargs): # real signature unknown
    pass

def sparse_truediv_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_xor_int64(*args, **kwargs): # real signature unknown
    pass

def sparse_xor_uint8(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_BlockMerge(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_BlockUnion(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SparseIndex(*args, **kwargs): # real signature unknown
    pass

# classes

class SparseIndex(object):
    """ Abstract superclass for sparse index types. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class BlockIndex(SparseIndex):
    """
    Object for holding block-based sparse indexing information
    
        Parameters
        ----------
    """
    def equals(self, *args, **kwargs): # real signature unknown
        pass

    def intersect(self, *args, **kwargs): # real signature unknown
        """
        Intersect two BlockIndex objects
        
                Returns
                -------
                BlockIndex
        """
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        """
        Return the internal location if value exists on given index.
                Return -1 otherwise.
        """
        pass

    def lookup_array(self, *args, **kwargs): # real signature unknown
        """ Vectorized lookup, returns ndarray[int32_t] """
        pass

    def make_union(self, *args, **kwargs): # real signature unknown
        """
        Combine together two BlockIndex objects, accepting indices if contained
                in one or the other
        
                Parameters
                ----------
                other : SparseIndex
        
                Notes
                -----
                union is a protected keyword in Cython, hence make_union
        
                Returns
                -------
                BlockIndex
        """
        pass

    def to_block_index(self, *args, **kwargs): # real signature unknown
        pass

    def to_int_index(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    blengths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blocs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nblocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ngaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    npoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001DAE2B80220>'


class IntIndex(SparseIndex):
    """
    Object for holding exact integer sparse indexing information
    
        Parameters
        ----------
        length : integer
        indices : array-like
            Contains integers corresponding to the indices.
        check_integrity : bool, default=True
            Check integrity of the input.
    """
    def equals(self, *args, **kwargs): # real signature unknown
        pass

    def intersect(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        """
        Return the internal location if value exists on given index.
                Return -1 otherwise.
        """
        pass

    def lookup_array(self, *args, **kwargs): # real signature unknown
        """ Vectorized lookup, returns ndarray[int32_t] """
        pass

    def make_union(self, *args, **kwargs): # real signature unknown
        pass

    def to_block_index(self, *args, **kwargs): # real signature unknown
        pass

    def to_int_index(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ngaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    npoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001DAE2B63F60>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DAE2B33050>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.sparse', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DAE2B33050>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\sparse.cp313-win_amd64.pyd')"

__test__ = {}

