# encoding: utf-8
# module pandas._libs.tslibs.np_datetime
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslibs\np_datetime.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\operator.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py

# functions

def add_overflowsafe(*args, **kwargs): # real signature unknown
    """
    Overflow-safe addition for datetime64/timedelta64 dtypes.
    
        `right` may either be zero-dim or of the same shape as `left`.
    """
    pass

def astype_overflowsafe(*args, **kwargs): # real signature unknown
    """
    Convert an ndarray with datetime64[X] to datetime64[Y]
        or timedelta64[X] to timedelta64[Y],
        raising on overflow.
    """
    pass

def compare_mismatched_resolutions(*args, **kwargs): # real signature unknown
    """
    Overflow-safe comparison of timedelta64/datetime64 with mismatched resolutions.
    
        >>> left = np.array([500], dtype="M8[Y]")
        >>> right = np.array([0], dtype="M8[ns]")
        >>> left < right  # <- wrong!
        array([ True])
    """
    pass

def get_supported_dtype(*args, **kwargs): # real signature unknown
    pass

def is_supported_dtype(*args, **kwargs): # real signature unknown
    pass

def is_unitless(*args, **kwargs): # real signature unknown
    """ Check if a datetime64 or timedelta64 dtype has no attached unit. """
    pass

def operator(*args, **kwargs): # real signature unknown
    """
    Operator interface.
    
    This module exports a set of functions implemented in C corresponding
    to the intrinsic operators of Python.  For example, operator.add(x, y)
    is equivalent to the expression x+y.  The function names are those
    used for special methods; variants without leading and trailing
    '__' are also provided for convenience.
    """
    pass

def py_get_unit_from_dtype(*args, **kwargs): # real signature unknown
    pass

def py_td64_to_tdstruct(*args, **kwargs): # real signature unknown
    pass

# classes

class OutOfBoundsDatetime(ValueError):
    """
    Raised when the datetime is outside the range that can be represented.
    
        Examples
        --------
        >>> pd.to_datetime("08335394550")
        Traceback (most recent call last):
        OutOfBoundsDatetime: Parsing "08335394550" to datetime overflows,
        at position 0
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class OutOfBoundsTimedelta(ValueError):
    """
    Raised when encountering a timedelta value that cannot be represented.
    
        Representation should be within a timedelta64[ns].
    
        Examples
        --------
        >>> pd.date_range(start="1/1/1700", freq="B", periods=100000)
        Traceback (most recent call last):
        OutOfBoundsTimedelta: Cannot cast 139999 days 00:00:00
        to unit='ns' without overflow.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002427E50DA30>'

__pyx_capi__ = {
    'add_overflowsafe': None, # (!) real value is '<capsule object "PyArrayObject *(PyArrayObject *, PyArrayObject *, int __pyx_skip_dispatch)" at 0x000002427E537AB0>'
    'astype_overflowsafe': None, # (!) real value is '<capsule object "PyArrayObject *(PyArrayObject *, PyArray_Descr *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_astype_overflowsafe *__pyx_optional_args)" at 0x000002427E5378D0>'
    'check_dts_bounds': None, # (!) real value is '<capsule object "PyObject *(npy_datetimestruct *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_check_dts_bounds *__pyx_optional_args)" at 0x000002427E537650>'
    'cmp_dtstructs': None, # (!) real value is '<capsule object "int (npy_datetimestruct *, npy_datetimestruct *, int)" at 0x000002427E537970>'
    'cmp_scalar': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_int64_t, __pyx_t_5numpy_int64_t, int)" at 0x000002427E5375B0>'
    'convert_reso': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, NPY_DATETIMEUNIT, NPY_DATETIMEUNIT, int)" at 0x000002427E537A60>'
    'dts_to_iso_string': None, # (!) real value is '<capsule object "PyObject *(npy_datetimestruct *)" at 0x000002427E537600>'
    'get_conversion_factor': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (NPY_DATETIMEUNIT, NPY_DATETIMEUNIT)" at 0x000002427E537920>'
    'get_datetime64_unit': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (PyObject *)" at 0x000002427E5377E0>'
    'get_implementation_bounds': None, # (!) real value is '<capsule object "PyObject *(NPY_DATETIMEUNIT, npy_datetimestruct *, npy_datetimestruct *)" at 0x000002427E5379C0>'
    'get_unit_from_dtype': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (PyArray_Descr *)" at 0x000002427E537880>'
    'pydate_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_Date *, npy_datetimestruct *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_pydate_to_dt64 *__pyx_optional_args)" at 0x000002427E537740>'
    'pydate_to_dtstruct': None, # (!) real value is '<capsule object "void (PyDateTime_Date *, npy_datetimestruct *)" at 0x000002427E537790>'
    'pydatetime_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_DateTime *, npy_datetimestruct *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_pydatetime_to_dt64 *__pyx_optional_args)" at 0x000002427E5376A0>'
    'pydatetime_to_dtstruct': None, # (!) real value is '<capsule object "void (PyDateTime_DateTime *, npy_datetimestruct *)" at 0x000002427E5376F0>'
    'string_to_dts': None, # (!) real value is '<capsule object "int (PyObject *, npy_datetimestruct *, NPY_DATETIMEUNIT *, int *, int *, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_string_to_dts *__pyx_optional_args)" at 0x000002427E537830>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.np_datetime', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002427E50DA30>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\np_datetime.cp313-win_amd64.pyd')"

__test__ = {
    'compare_mismatched_resolutions (line 462)': '\n    Overflow-safe comparison of timedelta64/datetime64 with mismatched resolutions.\n\n    >>> left = np.array([500], dtype="M8[Y]")\n    >>> right = np.array([0], dtype="M8[ns]")\n    >>> left < right  # <- wrong!\n    array([ True])\n    ',
}

