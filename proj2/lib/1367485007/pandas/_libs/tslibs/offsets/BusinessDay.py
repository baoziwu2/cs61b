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


from .BusinessMixin import BusinessMixin

class BusinessDay(BusinessMixin):
    """
    DateOffset subclass representing possibly n business days.
    
        Parameters
        ----------
        n : int, default 1
            The number of days represented.
        normalize : bool, default False
            Normalize start/end dates to midnight.
        offset : timedelta, default timedelta(0)
            Time offset to apply.
    
        Examples
        --------
        You can use the parameter ``n`` to represent a shift of n business days.
    
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts.strftime('%a %d %b %Y %H:%M')
        'Fri 09 Dec 2022 15:00'
        >>> (ts + pd.offsets.BusinessDay(n=5)).strftime('%a %d %b %Y %H:%M')
        'Fri 16 Dec 2022 15:00'
    
        Passing the parameter ``normalize`` equal to True, you shift the start
        of the next business day to midnight.
    
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts + pd.offsets.BusinessDay(normalize=True)
        Timestamp('2022-12-12 00:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def _offset_str(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, n=5): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _attributes = (
        'n',
        'normalize',
        'offset',
    )
    _period_dtype_code = 5000
    _prefix = 'B'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002369081B7E0>'


