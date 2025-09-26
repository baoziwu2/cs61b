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


from ._CustomBusinessMonth import _CustomBusinessMonth

class CustomBusinessMonthEnd(_CustomBusinessMonth):
    """
    DateOffset subclass representing custom business month(s).
    
        Increments between end of month dates.
    
        Parameters
        ----------
        n : int, default 1
            The number of months represented.
        normalize : bool, default False
            Normalize end dates to midnight before generating date range.
        weekmask : str, Default 'Mon Tue Wed Thu Fri'
            Weekmask of valid business days, passed to ``numpy.busdaycalendar``.
        holidays : list
            List/array of dates to exclude from the set of valid business days,
            passed to ``numpy.busdaycalendar``.
        calendar : np.busdaycalendar
            Calendar to integrate.
        offset : timedelta, default timedelta(0)
            Time offset to apply.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        In the example below we use the default parameters.
    
        >>> ts = pd.Timestamp(2022, 8, 5)
        >>> ts + pd.offsets.CustomBusinessMonthEnd()
        Timestamp('2022-08-31 00:00:00')
    
        Custom business month end can be specified by ``weekmask`` parameter.
        To convert the returned datetime object to its string representation
        the function strftime() is used in the next example.
    
        >>> import datetime as dt
        >>> freq = pd.offsets.CustomBusinessMonthEnd(weekmask="Wed Thu")
        >>> pd.date_range(dt.datetime(2022, 7, 10), dt.datetime(2022, 12, 18),
        ...               freq=freq).strftime('%a %d %b %Y %H:%M')
        Index(['Thu 28 Jul 2022 00:00', 'Wed 31 Aug 2022 00:00',
               'Thu 29 Sep 2022 00:00', 'Thu 27 Oct 2022 00:00',
               'Wed 30 Nov 2022 00:00'],
               dtype='object')
    
        Using NumPy business day calendar you can define custom holidays.
    
        >>> import datetime as dt
        >>> bdc = np.busdaycalendar(holidays=['2022-08-01', '2022-09-30',
        ...                                   '2022-10-31', '2022-11-01'])
        >>> freq = pd.offsets.CustomBusinessMonthEnd(calendar=bdc)
        >>> pd.date_range(dt.datetime(2022, 7, 10), dt.datetime(2022, 11, 10), freq=freq)
        DatetimeIndex(['2022-07-29', '2022-08-31', '2022-09-29', '2022-10-28'],
                       dtype='datetime64[ns]', freq='CBME')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _prefix = 'CBME'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023690833380>'


