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


from .BusinessDay import BusinessDay

class CustomBusinessDay(BusinessDay):
    """
    DateOffset subclass representing possibly n custom business days.
    
        In CustomBusinessDay we can use custom weekmask, holidays, and calendar.
    
        Parameters
        ----------
        n : int, default 1
            The number of days represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        weekmask : str, Default 'Mon Tue Wed Thu Fri'
            Weekmask of valid business days, passed to ``numpy.busdaycalendar``.
        holidays : list
            List/array of dates to exclude from the set of valid business days,
            passed to ``numpy.busdaycalendar``.
        calendar : np.busdaycalendar
            Calendar to integrate.
        offset : timedelta, default timedelta(0)
            Time offset to apply.
    
        Examples
        --------
        In the example below the default parameters give the next business day.
    
        >>> ts = pd.Timestamp(2022, 8, 5, 16)
        >>> ts + pd.offsets.CustomBusinessDay()
        Timestamp('2022-08-08 16:00:00')
    
        Business days can be specified by ``weekmask`` parameter. To convert
        the returned datetime object to its string representation
        the function strftime() is used in the next example.
    
        >>> import datetime as dt
        >>> freq = pd.offsets.CustomBusinessDay(weekmask="Mon Wed Fri")
        >>> pd.date_range(dt.datetime(2022, 12, 10), dt.datetime(2022, 12, 21),
        ...               freq=freq).strftime('%a %d %b %Y %H:%M')
        Index(['Mon 12 Dec 2022 00:00', 'Wed 14 Dec 2022 00:00',
               'Fri 16 Dec 2022 00:00', 'Mon 19 Dec 2022 00:00',
               'Wed 21 Dec 2022 00:00'],
               dtype='object')
    
        Using NumPy business day calendar you can define custom holidays.
    
        >>> import datetime as dt
        >>> bdc = np.busdaycalendar(holidays=['2022-12-12', '2022-12-14'])
        >>> freq = pd.offsets.CustomBusinessDay(calendar=bdc)
        >>> pd.date_range(dt.datetime(2022, 12, 10), dt.datetime(2022, 12, 25), freq=freq)
        DatetimeIndex(['2022-12-13', '2022-12-15', '2022-12-16', '2022-12-19',
                       '2022-12-20', '2022-12-21', '2022-12-22', '2022-12-23'],
                       dtype='datetime64[ns]', freq='C')
    
        If you want to shift the result on n day you can use the parameter ``offset``.
    
        >>> pd.Timestamp(2022, 8, 5, 16) + pd.offsets.CustomBusinessDay(1)
        Timestamp('2022-08-08 16:00:00')
    
        >>> import datetime as dt
        >>> ts = pd.Timestamp(2022, 8, 5, 16)
        >>> ts + pd.offsets.CustomBusinessDay(1, offset=dt.timedelta(days=1))
        Timestamp('2022-08-09 16:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _period_dtype_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _attributes = (
        'n',
        'normalize',
        'weekmask',
        'holidays',
        'calendar',
        'offset',
    )
    _prefix = 'C'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023690832E80>'


