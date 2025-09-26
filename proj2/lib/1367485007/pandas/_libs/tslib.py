# encoding: utf-8
# module pandas._libs.tslib
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslib.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\warnings.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
from pandas._libs.tslibs.dtypes import Resolution

from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.timestamps import Timestamp

from pandas._libs.tslibs.vectorized import get_resolution

import datetime as __datetime


# functions

def array_to_datetime(*args, **kwargs): # real signature unknown
    """
    Converts a 1D array of date-like values to a numpy array of either:
            1) datetime64[ns] data
            2) datetime.datetime objects, if OutOfBoundsDatetime or TypeError
               is encountered
    
        Also returns a fixed-offset tzinfo object if an array of strings with the same
        timezone offset is passed and utc=True is not passed. Otherwise, None
        is returned
    
        Handles datetime.date, datetime.datetime, np.datetime64 objects, numeric,
        strings
    
        Parameters
        ----------
        values : ndarray of object
            date-like objects to convert
        errors : str, default 'raise'
            error behavior when parsing
        dayfirst : bool, default False
            dayfirst parsing behavior when encountering datetime strings
        yearfirst : bool, default False
            yearfirst parsing behavior when encountering datetime strings
        utc : bool, default False
            indicator whether the dates should be UTC
        creso : NPY_DATETIMEUNIT, default NPY_FR_ns
            Set to NPY_FR_GENERIC to infer a resolution.
    
        Returns
        -------
        np.ndarray
            May be datetime64[creso_unit] or object dtype
        tzinfo or None
    """
    pass

def array_to_datetime_with_tz(*args, **kwargs): # real signature unknown
    """
    Vectorized analogue to pd.Timestamp(value, tz=tz)
    
        values has object-dtype, unrestricted ndim.
    
        Major differences between this and array_to_datetime with utc=True
            - np.datetime64 objects are treated as _wall_ times.
            - tznaive datetimes are treated as _wall_ times.
    """
    pass

def array_with_unit_to_datetime(*args, **kwargs): # real signature unknown
    """
    Convert the ndarray to datetime according to the time unit.
    
        This function converts an array of objects into a numpy array of
        datetime64[ns]. It returns the converted array
        and also returns the timezone offset
    
        if errors:
          - raise: return converted values or raise OutOfBoundsDatetime
              if out of range on the conversion or
              ValueError for other conversions (e.g. a string)
          - ignore: return non-convertible values as the same unit
          - coerce: NaT for non-convertibles
    
        Parameters
        ----------
        values : ndarray
             Date-like objects to convert.
        unit : str
             Time unit to use during conversion.
        errors : str, default 'raise'
             Error behavior when parsing.
    
        Returns
        -------
        result : ndarray of m8 values
        tz : parsed timezone offset or None
    """
    pass

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

def first_non_null(*args, **kwargs): # real signature unknown
    """ Find position of first non-null value, return -1 if there isn't one. """
    pass

def format_array_from_datetime(*args, **kwargs): # real signature unknown
    """
    return a np object array of the string formatted values
    
        Parameters
        ----------
        values : ndarray[int64_t], arbitrary ndim
        tz : tzinfo or None, default None
        format : str or None, default None
              a strftime capable string
        na_rep : optional, default is None
              a nat format
        reso : NPY_DATETIMEUNIT, default NPY_FR_ns
    
        Returns
        -------
        np.ndarray[object]
    """
    pass

def _test_parse_iso8601(*args, **kwargs): # real signature unknown
    """
    TESTING ONLY: Parse string into Timestamp using iso8601 parser. Used
        only for testing, actual construction uses `convert_str_to_tsobject`
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class timezone(__datetime.tzinfo):
    """ Fixed offset from UTC implementation of tzinfo. """
    def dst(self, *args, **kwargs): # real signature unknown
        """ Return None. """
        pass

    def fromutc(self, *args, **kwargs): # real signature unknown
        """ datetime in UTC -> datetime in local time. """
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        """ If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+|-)HH:MM'. """
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        """ Return fixed offset. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getinitargs__(self, *args, **kwargs): # real signature unknown
        """ pickle support """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    max = datetime.timezone(datetime.timedelta(seconds=86340))
    min = datetime.timezone(datetime.timedelta(days=-1, seconds=60))
    utc = datetime.timezone.utc


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EBFBB7F9B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EBFBB7F9B0>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslib.cp313-win_amd64.pyd')"

__test__ = {}

