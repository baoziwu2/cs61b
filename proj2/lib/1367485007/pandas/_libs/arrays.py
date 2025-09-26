# encoding: utf-8
# module pandas._libs.arrays
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\arrays.cp313-win_amd64.pyd
# by generator 1.147
""" Cython implementations for internal ExtensionArrays. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py

# functions

def __pyx_unpickle_NDArrayBacked(*args, **kwargs): # real signature unknown
    pass

# classes

class NDArrayBacked(object):
    """
    Implementing these methods in cython improves performance quite a bit.
    
        import pandas as pd
    
        from pandas._libs.arrays import NDArrayBacked as cls
    
        dti = pd.date_range("2016-01-01", periods=3)
        dta = dti._data
        arr = dta._ndarray
    
        obj = cls._simple_new(arr, arr.dtype)
    
        # for foo in [arr, dta, obj]: ...
    
        %timeit foo.copy()
        299 ns ± 30 ns per loop     # <-- arr underlying ndarray (for reference)
        530 ns ± 9.24 ns per loop   # <-- dta with cython NDArrayBacked
        1.66 µs ± 46.3 ns per loop  # <-- dta without cython NDArrayBacked
        328 ns ± 5.29 ns per loop   # <-- obj with NDArrayBacked.__cinit__
        371 ns ± 6.97 ns per loop   # <-- obj with NDArrayBacked._simple_new
    
        %timeit foo.T
        125 ns ± 6.27 ns per loop   # <-- arr underlying ndarray (for reference)
        226 ns ± 7.66 ns per loop   # <-- dta with cython NDArrayBacked
        911 ns ± 16.6 ns per loop   # <-- dta without cython NDArrayBacked
        215 ns ± 4.54 ns per loop   # <-- obj with NDArrayBacked._simple_new
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def ravel(self, *args, **kwargs): # real signature unknown
        pass

    def repeat(self, *args, **kwargs): # real signature unknown
        pass

    def reshape(self, *args, **kwargs): # real signature unknown
        pass

    def swapaxes(self, *args, **kwargs): # real signature unknown
        pass

    def transpose(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _concat_same_type(cls, *args, **kwargs): # real signature unknown
        pass

    def _from_backing_data(self, self__ndarray): # real signature unknown; restored from __doc__
        """
        Construct a new ExtensionArray `new_array` with `arr` as its _ndarray.
        
                The returned array has the same dtype as self.
        
                Caller is responsible for ensuring `values.dtype == self._ndarray.dtype`.
        
                This should round-trip:
                    self == self._from_backing_data(self._ndarray)
        """
        pass

    @classmethod
    def _simple_new(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    T = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ndarray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023E961A1DF0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023E96172A50>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.arrays', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023E96172A50>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\arrays.cp313-win_amd64.pyd')"

__test__ = {}

