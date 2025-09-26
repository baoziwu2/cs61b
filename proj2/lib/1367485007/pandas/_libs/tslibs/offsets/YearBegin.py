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


from .YearOffset import YearOffset

class YearBegin(YearOffset):
    """
    DateOffset increments between calendar year begin dates.
    
        YearBegin goes to the next date which is the start of the year.
    
        Parameters
        ----------
        n : int, default 1
            The number of years represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        month : int, default 1
            A specific integer for the month of the year.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 12, 1)
        >>> ts + pd.offsets.YearBegin()
        Timestamp('2023-01-01 00:00:00')
    
        >>> ts = pd.Timestamp(2023, 1, 1)
        >>> ts + pd.offsets.YearBegin()
        Timestamp('2024-01-01 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.YearBegin(month=2)
        Timestamp('2022-02-01 00:00:00')
    
        If you want to get the start of the current year:
    
        >>> ts = pd.Timestamp(2023, 1, 1)
        >>> pd.offsets.YearBegin().rollback(ts)
        Timestamp('2023-01-01 00:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'start'
    _default_month = 1
    _prefix = 'YS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000236908306D0>'


