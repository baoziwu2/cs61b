# encoding: utf-8
# module pandas._libs.tslibs.vectorized
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslibs\vectorized.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from pandas._libs.tslibs.dtypes import Resolution


# functions

def dt64arr_to_periodarr(*args, **kwargs): # real signature unknown
    pass

def get_resolution(*args, **kwargs): # real signature unknown
    pass

def ints_to_pydatetime(*args, **kwargs): # real signature unknown
    """
    Convert an i8 repr to an ndarray of datetimes, date, time or Timestamp.
    
        Parameters
        ----------
        stamps : array of i8
        tz : str, optional
             convert to this timezone
        box : {'datetime', 'timestamp', 'date', 'time'}, default 'datetime'
            * If datetime, convert to datetime.datetime
            * If date, convert to datetime.date
            * If time, convert to datetime.time
            * If Timestamp, convert to pandas.Timestamp
    
        reso : NPY_DATETIMEUNIT, default NPY_FR_ns
    
        Returns
        -------
        ndarray[object] of type specified by box
    """
    pass

def is_date_array_normalized(*args, **kwargs): # real signature unknown
    """
    Check if all of the given (nanosecond) timestamps are normalized to
        midnight, i.e. hour == minute == second == 0.  If the optional timezone
        `tz` is not None, then this is midnight for this timezone.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
        reso : NPY_DATETIMEUNIT
    
        Returns
        -------
        is_normalized : bool True if all stamps are normalized
    """
    pass

def normalize_i8_timestamps(*args, **kwargs): # real signature unknown
    """
    Normalize each of the (nanosecond) timezone aware timestamps in the given
        array by rounding down to the beginning of the day (i.e. midnight).
        This is midnight for timezone, `tz`.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
        reso : NPY_DATETIMEUNIT
    
        Returns
        -------
        result : int64 ndarray of converted of normalized nanosecond timestamps
    """
    pass

def tz_convert_from_utc(*args, **kwargs): # real signature unknown
    """
    Convert the values (in i8) from UTC to tz
    
        Parameters
        ----------
        stamps : ndarray[int64]
        tz : tzinfo
    
        Returns
        -------
        ndarray[int64]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002CEE6030230>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.vectorized', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002CEE6030230>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\vectorized.cp313-win_amd64.pyd')"

__test__ = {}

