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


from .QuarterOffset import QuarterOffset

class QuarterEnd(QuarterOffset):
    """
    DateOffset increments between Quarter end dates.
    
        startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...
        startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...
        startingMonth = 3 corresponds to dates like 3/31/2007, 6/30/2007, ...
    
        Parameters
        ----------
        n : int, default 1
            The number of quarters represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        startingMonth : int, default 3
            A specific integer for the month of the year from which we start quarters.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.QuarterEnd()
        Timestamp('2022-03-31 00:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _period_dtype_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _day_opt = 'end'
    _default_starting_month = 3
    _prefix = 'QE'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023690830DB0>'


