# encoding: utf-8
# module pandas._libs.tslibs.tzconversion
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslibs\tzconversion.cp313-win_amd64.pyd
# by generator 1.147
""" timezone conversion """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
import pytz as pytz # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pytz\__init__.py

# functions

def tz_convert_from_utc_single(*args, **kwargs): # real signature unknown
    """
    Convert the val (in i8) from UTC to tz
    
        This is a single value version of tz_convert_from_utc.
    
        Parameters
        ----------
        utc_val : int64
        tz : tzinfo
        creso : NPY_DATETIMEUNIT, default NPY_FR_ns
    
        Returns
        -------
        converted: int64
    """
    pass

def tz_localize_to_utc(*args, **kwargs): # real signature unknown
    """
    Localize tzinfo-naive i8 to given time zone (using pytz). If
        there are ambiguities in the values, raise AmbiguousTimeError.
    
        Parameters
        ----------
        vals : ndarray[int64_t]
        tz : tzinfo or None
        ambiguous : str, bool, or arraylike
            When clocks moved backward due to DST, ambiguous times may arise.
            For example in Central European Time (UTC+01), when going from 03:00
            DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC
            and at 01:30:00 UTC. In such a situation, the `ambiguous` parameter
            dictates how ambiguous times should be handled.
    
            - 'infer' will attempt to infer fall dst-transition hours based on
              order
            - bool-ndarray where True signifies a DST time, False signifies a
              non-DST time (note that this flag is only applicable for ambiguous
              times, but the array must have the same length as vals)
            - bool if True, treat all vals as DST. If False, treat them as non-DST
            - 'NaT' will return NaT where there are ambiguous times
    
        nonexistent : {None, "NaT", "shift_forward", "shift_backward", "raise", timedelta-like}
            How to handle non-existent times when converting wall times to UTC
        creso : NPY_DATETIMEUNIT, default NPY_FR_ns
    
        Returns
        -------
        localized : ndarray[int64_t]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Localizer(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002A9D1198720>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A9D11AC170>'

__pyx_capi__ = {
    'tz_convert_from_utc_single': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, PyDateTime_TZInfo *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_12tzconversion_tz_convert_from_utc_single *__pyx_optional_args)" at 0x000002A9D11984F0>'
    'tz_localize_to_utc_single': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, PyDateTime_TZInfo *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_12tzconversion_tz_localize_to_utc_single *__pyx_optional_args)" at 0x000002A9D1198540>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.tzconversion', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A9D11AC170>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\tzconversion.cp313-win_amd64.pyd')"

__test__ = {}

