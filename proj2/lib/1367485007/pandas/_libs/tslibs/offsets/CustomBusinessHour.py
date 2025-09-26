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


from .BusinessHour import BusinessHour

class CustomBusinessHour(BusinessHour):
    """
    DateOffset subclass representing possibly n custom business days.
    
        In CustomBusinessHour we can use custom weekmask, holidays, and calendar.
    
        Parameters
        ----------
        n : int, default 1
            The number of hours represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        weekmask : str, Default 'Mon Tue Wed Thu Fri'
            Weekmask of valid business days, passed to ``numpy.busdaycalendar``.
        holidays : list
            List/array of dates to exclude from the set of valid business days,
            passed to ``numpy.busdaycalendar``.
        calendar : np.busdaycalendar
            Calendar to integrate.
        start : str, time, or list of str/time, default "09:00"
            Start time of your custom business hour in 24h format.
        end : str, time, or list of str/time, default: "17:00"
            End time of your custom business hour in 24h format.
        offset : timedelta, default timedelta(0)
            Time offset to apply.
    
        Examples
        --------
        In the example below the default parameters give the next business hour.
    
        >>> ts = pd.Timestamp(2022, 8, 5, 16)
        >>> ts + pd.offsets.CustomBusinessHour()
        Timestamp('2022-08-08 09:00:00')
    
        We can also change the start and the end of business hours.
    
        >>> ts = pd.Timestamp(2022, 8, 5, 16)
        >>> ts + pd.offsets.CustomBusinessHour(start="11:00")
        Timestamp('2022-08-08 11:00:00')
    
        >>> from datetime import time as dt_time
        >>> ts = pd.Timestamp(2022, 8, 5, 16)
        >>> ts + pd.offsets.CustomBusinessHour(end=dt_time(19, 0))
        Timestamp('2022-08-05 17:00:00')
    
        >>> ts = pd.Timestamp(2022, 8, 5, 22)
        >>> ts + pd.offsets.CustomBusinessHour(end=dt_time(19, 0))
        Timestamp('2022-08-08 10:00:00')
    
        You can divide your business day hours into several parts.
    
        >>> import datetime as dt
        >>> freq = pd.offsets.CustomBusinessHour(start=["06:00", "10:00", "15:00"],
        ...                                      end=["08:00", "12:00", "17:00"])
        >>> pd.date_range(dt.datetime(2022, 12, 9), dt.datetime(2022, 12, 13), freq=freq)
        DatetimeIndex(['2022-12-09 06:00:00', '2022-12-09 07:00:00',
                       '2022-12-09 10:00:00', '2022-12-09 11:00:00',
                       '2022-12-09 15:00:00', '2022-12-09 16:00:00',
                       '2022-12-12 06:00:00', '2022-12-12 07:00:00',
                       '2022-12-12 10:00:00', '2022-12-12 11:00:00',
                       '2022-12-12 15:00:00', '2022-12-12 16:00:00'],
                       dtype='datetime64[ns]', freq='cbh')
    
        Business days can be specified by ``weekmask`` parameter. To convert
        the returned datetime object to its string representation
        the function strftime() is used in the next example.
    
        >>> import datetime as dt
        >>> freq = pd.offsets.CustomBusinessHour(weekmask="Mon Wed Fri",
        ...                                      start="10:00", end="13:00")
        >>> pd.date_range(dt.datetime(2022, 12, 10), dt.datetime(2022, 12, 18),
        ...               freq=freq).strftime('%a %d %b %Y %H:%M')
        Index(['Mon 12 Dec 2022 10:00', 'Mon 12 Dec 2022 11:00',
               'Mon 12 Dec 2022 12:00', 'Wed 14 Dec 2022 10:00',
               'Wed 14 Dec 2022 11:00', 'Wed 14 Dec 2022 12:00',
               'Fri 16 Dec 2022 10:00', 'Fri 16 Dec 2022 11:00',
               'Fri 16 Dec 2022 12:00'],
               dtype='object')
    
        Using NumPy business day calendar you can define custom holidays.
    
        >>> import datetime as dt
        >>> bdc = np.busdaycalendar(holidays=['2022-12-12', '2022-12-14'])
        >>> freq = pd.offsets.CustomBusinessHour(calendar=bdc, start="10:00", end="13:00")
        >>> pd.date_range(dt.datetime(2022, 12, 10), dt.datetime(2022, 12, 18), freq=freq)
        DatetimeIndex(['2022-12-13 10:00:00', '2022-12-13 11:00:00',
                       '2022-12-13 12:00:00', '2022-12-15 10:00:00',
                       '2022-12-15 11:00:00', '2022-12-15 12:00:00',
                       '2022-12-16 10:00:00', '2022-12-16 11:00:00',
                       '2022-12-16 12:00:00'],
                       dtype='datetime64[ns]', freq='cbh')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _anchor = 0
    _attributes = (
        'n',
        'normalize',
        'weekmask',
        'holidays',
        'calendar',
        'start',
        'end',
        'offset',
    )
    _prefix = 'cbh'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023690832FC0>'


