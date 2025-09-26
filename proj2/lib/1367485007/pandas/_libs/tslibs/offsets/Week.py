# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslibs\offsets.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\re\__init__.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\warnings.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
from pandas._libs.properties import cache_readonly

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp


from .SingleConstructorOffset import SingleConstructorOffset

class Week(SingleConstructorOffset):
    """
    Weekly offset.
    
        Parameters
        ----------
        n : int, default 1
            The number of weeks represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        weekday : int or None, default None
            Always generate specific day of week.
            0 for Monday and 6 for Sunday.
    
        See Also
        --------
        pd.tseries.offsets.WeekOfMonth :
         Describes monthly dates like, the Tuesday of the
         2nd week of each month.
    
        Examples
        --------
    
        >>> date_object = pd.Timestamp("2023-01-13")
        >>> date_object
        Timestamp('2023-01-13 00:00:00')
    
        >>> date_plus_one_week = date_object + pd.tseries.offsets.Week(n=1)
        >>> date_plus_one_week
        Timestamp('2023-01-20 00:00:00')
    
        >>> date_next_monday = date_object + pd.tseries.offsets.Week(weekday=0)
        >>> date_next_monday
        Timestamp('2023-01-16 00:00:00')
    
        >>> date_next_sunday = date_object + pd.tseries.offsets.Week(weekday=6)
        >>> date_next_sunday
        Timestamp('2023-01-15 00:00:00')
    """
    def is_anchored(self, *args, **kwargs): # real signature unknown
        pass

    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_name(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, n=1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _period_dtype_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _attributes = (
        'n',
        'normalize',
        'weekday',
    )
    _inc = datetime.timedelta(days=7)
    _prefix = 'W'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023690831DF0>'


