# encoding: utf-8
# module pandas._libs.hashtable
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\hashtable.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py

# Variables with simple values

SIZE_HINT_LIMIT = 1048583

# functions

def duplicated(*args, **kwargs): # real signature unknown
    pass

def get_hashtable_trace_domain(*args, **kwargs): # real signature unknown
    pass

def ismember(*args, **kwargs): # real signature unknown
    pass

def mode(*args, **kwargs): # real signature unknown
    pass

def objects_are_equal(*args, **kwargs): # real signature unknown
    pass

def object_hash(*args, **kwargs): # real signature unknown
    pass

def unique_label_indices(*args, **kwargs): # real signature unknown
    """
    Indices of the first occurrences of the unique labels
        *excluding* -1. equivalent to:
            np.unique(labels, return_index=True)[1]
    """
    pass

def value_count(*args, **kwargs): # real signature unknown
    pass

def _unique_label_indices_int32(*args, **kwargs): # real signature unknown
    """
    Indices of the first occurrences of the unique labels
        *excluding* -1. equivalent to:
            np.unique(labels, return_index=True)[1]
    """
    pass

def _unique_label_indices_int64(*args, **kwargs): # real signature unknown
    """
    Indices of the first occurrences of the unique labels
        *excluding* -1. equivalent to:
            np.unique(labels, return_index=True)[1]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_HashTable(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

from .Factorizer import Factorizer
from .Complex128Factorizer import Complex128Factorizer
from .HashTable import HashTable
from .Complex128HashTable import Complex128HashTable
from .Vector import Vector
from .Complex128Vector import Complex128Vector
from .Complex64Factorizer import Complex64Factorizer
from .Complex64HashTable import Complex64HashTable
from .Complex64Vector import Complex64Vector
from .Float32Factorizer import Float32Factorizer
from .Float32HashTable import Float32HashTable
from .Float32Vector import Float32Vector
from .Float64Factorizer import Float64Factorizer
from .Float64HashTable import Float64HashTable
from .Float64Vector import Float64Vector
from .Int16Factorizer import Int16Factorizer
from .Int16HashTable import Int16HashTable
from .Int16Vector import Int16Vector
from .Int32Factorizer import Int32Factorizer
from .Int32HashTable import Int32HashTable
from .Int32Vector import Int32Vector
from .Int64Factorizer import Int64Factorizer
from .IntpHashTable import IntpHashTable
from .Int64HashTable import Int64HashTable
from .Int64Vector import Int64Vector
from .Int8Factorizer import Int8Factorizer
from .Int8HashTable import Int8HashTable
from .Int8Vector import Int8Vector
from .ObjectFactorizer import ObjectFactorizer
from .ObjectVector import ObjectVector
from .PyObjectHashTable import PyObjectHashTable
from .StringHashTable import StringHashTable
from .StringVector import StringVector
from .UInt16Factorizer import UInt16Factorizer
from .UInt16HashTable import UInt16HashTable
from .UInt16Vector import UInt16Vector
from .UInt32Factorizer import UInt32Factorizer
from .UInt32HashTable import UInt32HashTable
from .UInt32Vector import UInt32Vector
from .UInt64Factorizer import UInt64Factorizer
from .UInt64HashTable import UInt64HashTable
from .UInt64Vector import UInt64Vector
from .UInt8Factorizer import UInt8Factorizer
from .UInt8HashTable import UInt8HashTable
from .UInt8Vector import UInt8Vector
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A3D0D4FED0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.hashtable', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A3D0D4FED0>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\hashtable.cp313-win_amd64.pyd')"

__test__ = {
    'Complex128Factorizer.factorize (line 1621)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = Complex128Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="complex128"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'Complex64Factorizer.factorize (line 3499)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = Complex64Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="complex64"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'Float32Factorizer.factorize (line 3953)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = Float32Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="float32"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'Float64Factorizer.factorize (line 2075)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = Float64Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="float64"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'Int16Factorizer.factorize (line 5769)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = Int16Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="int16"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'Int32Factorizer.factorize (line 4861)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = Int32Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="int32"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'Int64Factorizer.factorize (line 3045)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = Int64Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="int64"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'Int8Factorizer.factorize (line 6677)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = Int8Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="int8"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'ObjectFactorizer.factorize (line 98)': "\n\n        Returns\n        -------\n        np.ndarray[np.intp]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = ObjectFactorizer(3)\n        >>> fac.factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)\n        array([ 0,  1, 20])\n        ",
    'UInt16Factorizer.factorize (line 5315)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = UInt16Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="uint16"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'UInt32Factorizer.factorize (line 4407)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = UInt32Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="uint32"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'UInt64Factorizer.factorize (line 2529)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = UInt64Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="uint64"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'UInt8Factorizer.factorize (line 6223)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = UInt8Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3], dtype="uint8"), na_sentinel=20)\n        array([0, 1, 2])\n        ',
}

