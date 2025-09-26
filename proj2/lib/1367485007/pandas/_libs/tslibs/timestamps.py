# encoding: utf-8
# module pandas._libs.tslibs.timestamps
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslibs\timestamps.cp313-win_amd64.pyd
# by generator 1.147
"""
_Timestamp is a c-defined subclass of datetime.datetime

_Timestamp is PITA. Because we inherit from datetime, which has very specific
construction requirements, we need to do object instantiation in python
(see Timestamp class below). This will serve as a C extension type that
shadows the python class, where we do any heavy lifting.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\warnings.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
import datetime as dt # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\datetime.py
from pandas._libs.tslibs.fields import (RoundTo, get_date_name_field, 
    get_start_end_field, round_nsint64)

from pandas._libs.tslibs.np_datetime import (OutOfBoundsDatetime, 
    OutOfBoundsTimedelta)

from pandas._libs.tslibs.timedeltas import Timedelta

import pandas._libs.tslibs.base as __pandas__libs_tslibs_base


# functions

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

def integer_op_not_supported(*args, **kwargs): # real signature unknown
    pass

def _unpickle_timestamp(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class MinMaxReso(object):
    """
    We need to define min/max/resolution on both the Timestamp _instance_
        and Timestamp class.  On an instance, these depend on the object's _reso.
        On the class, we default to the values we would get with nanosecond _reso.
    
        See also: timedeltas.MinMaxReso
    """
    def __get__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.timestamps\', \'__doc__\': "\\n    We need to define min/max/resolution on both the Timestamp _instance_\\n    and Timestamp class.  On an instance, these depend on the object\'s _reso.\\n    On the class, we default to the values we would get with nanosecond _reso.\\n\\n    See also: timedeltas.MinMaxReso\\n    ", \'__init__\': <cyfunction MinMaxReso.__init__ at 0x0000017CEDBA4400>, \'__get__\': <cyfunction MinMaxReso.__get__ at 0x0000017CEDBA44C0>, \'__set__\': <cyfunction MinMaxReso.__set__ at 0x0000017CEDBA4580>, \'__dict__\': <attribute \'__dict__\' of \'MinMaxReso\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'MinMaxReso\' objects>})'


class _Timestamp(__pandas__libs_tslibs_base.ABCTimestamp):
    # no doc
    def as_unit(self, s): # real signature unknown; restored from __doc__
        """
        Convert the underlying int64 representaton to the given unit.
        
                Parameters
                ----------
                unit : {"ns", "us", "ms", "s"}
                round_ok : bool, default True
                    If False and the conversion requires rounding, raise.
        
                Returns
                -------
                Timestamp
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 00:00:00.01')
                >>> ts
                Timestamp('2023-01-01 00:00:00.010000')
                >>> ts.unit
                'ms'
                >>> ts = ts.as_unit('s')
                >>> ts
                Timestamp('2023-01-01 00:00:00')
                >>> ts.unit
                's'
        """
        pass

    def day_name(self): # real signature unknown; restored from __doc__
        """
        Return the day name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : str, default None (English locale)
                    Locale determining the language in which to return the day name.
        
                Returns
                -------
                str
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.day_name()
                'Saturday'
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.day_name()
                nan
        """
        pass

    def isoformat(self): # real signature unknown; restored from __doc__
        """
        Return the time formatted according to ISO 8601.
        
                The full format looks like 'YYYY-MM-DD HH:MM:SS.mmmmmmnnn'.
                By default, the fractional part is omitted if self.microsecond == 0
                and self.nanosecond == 0.
        
                If self.tzinfo is not None, the UTC offset is also attached, giving
                giving a full format of 'YYYY-MM-DD HH:MM:SS.mmmmmmnnn+HH:MM'.
        
                Parameters
                ----------
                sep : str, default 'T'
                    String used as the separator between the date and time.
        
                timespec : str, default 'auto'
                    Specifies the number of additional terms of the time to include.
                    The valid values are 'auto', 'hours', 'minutes', 'seconds',
                    'milliseconds', 'microseconds', and 'nanoseconds'.
        
                Returns
                -------
                str
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.isoformat()
                '2020-03-14T15:32:52.192548651'
                >>> ts.isoformat(timespec='microseconds')
                '2020-03-14T15:32:52.192548'
        """
        pass

    def month_name(self): # real signature unknown; restored from __doc__
        """
        Return the month name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : str, default None (English locale)
                    Locale determining the language in which to return the month name.
        
                Returns
                -------
                str
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.month_name()
                'March'
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.month_name()
                nan
        """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """
        Normalize Timestamp to midnight, preserving tz information.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2020, 3, 14, 15, 30)
                >>> ts.normalize()
                Timestamp('2020-03-14 00:00:00')
        """
        pass

    def timestamp(self): # real signature unknown; restored from __doc__
        """
        Return POSIX timestamp as float.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')
                >>> ts.timestamp()
                1584199972.192548
        """
        pass

    def to_datetime64(self): # real signature unknown; restored from __doc__
        """
        Return a numpy.datetime64 object with same precision.
        
                Examples
                --------
                >>> ts = pd.Timestamp(year=2023, month=1, day=1,
                ...                   hour=10, second=15)
                >>> ts
                Timestamp('2023-01-01 10:00:15')
                >>> ts.to_datetime64()
                numpy.datetime64('2023-01-01T10:00:15.000000')
        """
        pass

    def to_numpy(self): # real signature unknown; restored from __doc__
        """
        Convert the Timestamp to a NumPy datetime64.
        
                This is an alias method for `Timestamp.to_datetime64()`. The dtype and
                copy parameters are available here only for compatibility. Their values
                will not affect the return value.
        
                Returns
                -------
                numpy.datetime64
        
                See Also
                --------
                DatetimeIndex.to_numpy : Similar method for DatetimeIndex.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.to_numpy()
                numpy.datetime64('2020-03-14T15:32:52.192548651')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.to_numpy()
                numpy.datetime64('NaT')
        """
        pass

    def to_period(self, freq='Y'): # real signature unknown; restored from __doc__
        """
        Return an period of which this timestamp is an observation.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> # Year end frequency
                >>> ts.to_period(freq='Y')
                Period('2020', 'Y-DEC')
        
                >>> # Month end frequency
                >>> ts.to_period(freq='M')
                Period('2020-03', 'M')
        
                >>> # Weekly frequency
                >>> ts.to_period(freq='W')
                Period('2020-03-09/2020-03-15', 'W-SUN')
        
                >>> # Quarter end frequency
                >>> ts.to_period(freq='Q')
                Period('2020Q1', 'Q-DEC')
        """
        pass

    def to_pydatetime(self): # real signature unknown; restored from __doc__
        """
        Convert a Timestamp object to a native Python datetime object.
        
                If warn=True, issue a warning if nanoseconds is nonzero.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')
                >>> ts.to_pydatetime()
                datetime.datetime(2020, 3, 14, 15, 32, 52, 192548)
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.to_pydatetime()
                NaT
        """
        pass

    @classmethod
    def _from_dt64(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_value_and_reso(cls, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return numpy datetime64 format in nanoseconds.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14, 15)
        >>> ts.asm8
        numpy.datetime64('2020-03-14T15:00:00.000000')
        """

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return day of the week.

        Returns
        -------
        int

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.day_of_week
        5
        """

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the year.

        Returns
        -------
        int

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.day_of_year
        74
        """

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of days in the month.

        Returns
        -------
        int

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.days_in_month
        31
        """

    day_of_week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return day of the week.

        Returns
        -------
        int

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.day_of_week
        5
        """

    day_of_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the year.

        Returns
        -------
        int

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.day_of_year
        74
        """

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if year is a leap year.

        Returns
        -------
        bool

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_leap_year
        True
        """

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the date is the last day of the month.

        Returns
        -------
        bool
            True if the date is the last day of the month.

        See Also
        --------
        Timestamp.is_month_start : Similar property indicating month start.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_month_end
        False

        >>> ts = pd.Timestamp(2020, 12, 31)
        >>> ts.is_month_end
        True
        """

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the date is the first day of the month.

        Returns
        -------
        bool
            True if the date is the first day of the month.

        See Also
        --------
        Timestamp.is_month_end : Similar property indicating the last day of the month.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_month_start
        False

        >>> ts = pd.Timestamp(2020, 1, 1)
        >>> ts.is_month_start
        True
        """

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if date is last day of the quarter.

        Returns
        -------
        bool
            True if date is last day of the quarter.

        See Also
        --------
        Timestamp.is_quarter_start : Similar property indicating the quarter start.
        Timestamp.quarter : Return the quarter of the date.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_quarter_end
        False

        >>> ts = pd.Timestamp(2020, 3, 31)
        >>> ts.is_quarter_end
        True
        """

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the date is the first day of the quarter.

        Returns
        -------
        bool
            True if date is first day of the quarter.

        See Also
        --------
        Timestamp.is_quarter_end : Similar property indicating the quarter end.
        Timestamp.quarter : Return the quarter of the date.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_quarter_start
        False

        >>> ts = pd.Timestamp(2020, 4, 1)
        >>> ts.is_quarter_start
        True
        """

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is last day of the year.

        Returns
        -------
        bool

        See Also
        --------
        Timestamp.is_year_start : Similar property indicating the start of the year.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_year_end
        False

        >>> ts = pd.Timestamp(2020, 12, 31)
        >>> ts.is_year_end
        True
        """

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is first day of the year.

        Returns
        -------
        bool

        See Also
        --------
        Timestamp.is_year_end : Similar property indicating the end of the year.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_year_start
        False

        >>> ts = pd.Timestamp(2020, 1, 1)
        >>> ts.is_year_start
        True
        """

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the quarter of the year.

        Returns
        -------
        int

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.quarter
        1
        """

    unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The abbreviation associated with self._creso.

        Examples
        --------
        >>> pd.Timestamp("2020-01-01 12:34:56").unit
        's'

        >>> pd.Timestamp("2020-01-01 12:34:56.123").unit
        'ms'

        >>> pd.Timestamp("2020-01-01 12:34:56.123456").unit
        'us'

        >>> pd.Timestamp("2020-01-01 12:34:56.123456789").unit
        'ns'
        """

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the week number of the year.

        Returns
        -------
        int

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.week
        11
        """

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _creso = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _date_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _repr_base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _time_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = Timestamp('2262-04-11 23:47:16.854775807')
    min = Timestamp('1677-09-21 00:12:43.145224193')
    resolution = Timedelta('0 days 00:00:00.000000001')
    __array_priority__ = 100
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000017CEDB1E660>'


class Timestamp(_Timestamp):
    """
    Pandas replacement for python datetime.datetime object.
    
        Timestamp is the pandas equivalent of python's Datetime
        and is interchangeable with it in most cases. It's the type used
        for the entries that make up a DatetimeIndex, and other timeseries
        oriented data structures in pandas.
    
        Parameters
        ----------
        ts_input : datetime-like, str, int, float
            Value to be converted to Timestamp.
        year, month, day : int
        hour, minute, second, microsecond : int, optional, default 0
        tzinfo : datetime.tzinfo, optional, default None
        nanosecond : int, optional, default 0
        tz : str, pytz.timezone, dateutil.tz.tzfile or None
            Time zone for time which Timestamp will have.
        unit : str
            Unit used for conversion if ts_input is of type int or float. The
            valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For
            example, 's' means seconds and 'ms' means milliseconds.
    
            For float inputs, the result will be stored in nanoseconds, and
            the unit attribute will be set as ``'ns'``.
        fold : {0, 1}, default None, keyword-only
            Due to daylight saving time, one wall clock time can occur twice
            when shifting from summer to winter time; fold describes whether the
            datetime-like corresponds  to the first (0) or the second time (1)
            the wall clock hits the ambiguous time.
    
        Notes
        -----
        There are essentially three calling conventions for the constructor. The
        primary form accepts four parameters. They can be passed by position or
        keyword.
    
        The other two forms mimic the parameters from ``datetime.datetime``. They
        can be passed by either position or keyword, but not both mixed together.
    
        Examples
        --------
        Using the primary calling convention:
    
        This converts a datetime-like string
    
        >>> pd.Timestamp('2017-01-01T12')
        Timestamp('2017-01-01 12:00:00')
    
        This converts a float representing a Unix epoch in units of seconds
    
        >>> pd.Timestamp(1513393355.5, unit='s')
        Timestamp('2017-12-16 03:02:35.500000')
    
        This converts an int representing a Unix-epoch in units of seconds
        and for a particular timezone
    
        >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')
        Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')
    
        Using the other two forms that mimic the API for ``datetime.datetime``:
    
        >>> pd.Timestamp(2017, 1, 1, 12)
        Timestamp('2017-01-01 12:00:00')
    
        >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)
        Timestamp('2017-01-01 12:00:00')
    """
    def astimezone(self, tz=None): # real signature unknown; restored from __doc__
        """
        Convert timezone-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        
                Examples
                --------
                Create a timestamp object with UTC timezone:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
        
                Change to Tokyo timezone:
        
                >>> ts.tz_convert(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Can also use ``astimezone``:
        
                >>> ts.astimezone(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.tz_convert(tz='Asia/Tokyo')
                NaT
        """
        pass

    def ceil(self, freq='h'): # real signature unknown; restored from __doc__
        """
        Return a new Timestamp ceiled to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the ceiling resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                Raises
                ------
                ValueError if the freq cannot be converted.
        
                Notes
                -----
                If the Timestamp has a timezone, ceiling will take place relative to the
                local ("wall") time and re-localized to the same timezone. When ceiling
                near daylight savings time, use ``nonexistent`` and ``ambiguous`` to
                control the re-localization behavior.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
        
                A timestamp can be ceiled using multiple frequency units:
        
                >>> ts.ceil(freq='h') # hour
                Timestamp('2020-03-14 16:00:00')
        
                >>> ts.ceil(freq='min') # minute
                Timestamp('2020-03-14 15:33:00')
        
                >>> ts.ceil(freq='s') # seconds
                Timestamp('2020-03-14 15:32:53')
        
                >>> ts.ceil(freq='us') # microseconds
                Timestamp('2020-03-14 15:32:52.192549')
        
                ``freq`` can also be a multiple of a single unit, like '5min' (i.e.  5 minutes):
        
                >>> ts.ceil(freq='5min')
                Timestamp('2020-03-14 15:35:00')
        
                or a combination of multiple units, like '1h30min' (i.e. 1 hour and 30 minutes):
        
                >>> ts.ceil(freq='1h30min')
                Timestamp('2020-03-14 16:30:00')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.ceil()
                NaT
        
                When rounding near a daylight savings time transition, use ``ambiguous`` or
                ``nonexistent`` to control how the timestamp should be re-localized.
        
                >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")
        
                >>> ts_tz.ceil("h", ambiguous=False)
                Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')
        
                >>> ts_tz.ceil("h", ambiguous=True)
                Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')
        """
        pass

    @classmethod
    def combine(cls, date, time): # real signature unknown; restored from __doc__
        """
        Timestamp.combine(date, time)
        
                Combine date, time into datetime with same date and time fields.
        
                Examples
                --------
                >>> from datetime import date, time
                >>> pd.Timestamp.combine(date(2020, 3, 14), time(15, 30, 15))
                Timestamp('2020-03-14 15:30:15')
        """
        pass

    def ctime(self): # real signature unknown; restored from __doc__
        """
        Return ctime() style string.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00.00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.ctime()
                'Sun Jan  1 10:00:00 2023'
        """
        pass

    def date(self): # real signature unknown; restored from __doc__
        """
        Return date object with same year, month and day.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00.00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.date()
                datetime.date(2023, 1, 1)
        """
        pass

    def dst(self): # real signature unknown; restored from __doc__
        """
        Return the daylight saving time (DST) adjustment.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2000-06-01 00:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2000-06-01 00:00:00+0200', tz='Europe/Brussels')
                >>> ts.dst()
                datetime.timedelta(seconds=3600)
        """
        pass

    def floor(self, freq='h'): # real signature unknown; restored from __doc__
        """
        Return a new Timestamp floored to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the flooring resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                Raises
                ------
                ValueError if the freq cannot be converted.
        
                Notes
                -----
                If the Timestamp has a timezone, flooring will take place relative to the
                local ("wall") time and re-localized to the same timezone. When flooring
                near daylight savings time, use ``nonexistent`` and ``ambiguous`` to
                control the re-localization behavior.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
        
                A timestamp can be floored using multiple frequency units:
        
                >>> ts.floor(freq='h') # hour
                Timestamp('2020-03-14 15:00:00')
        
                >>> ts.floor(freq='min') # minute
                Timestamp('2020-03-14 15:32:00')
        
                >>> ts.floor(freq='s') # seconds
                Timestamp('2020-03-14 15:32:52')
        
                >>> ts.floor(freq='ns') # nanoseconds
                Timestamp('2020-03-14 15:32:52.192548651')
        
                ``freq`` can also be a multiple of a single unit, like '5min' (i.e.  5 minutes):
        
                >>> ts.floor(freq='5min')
                Timestamp('2020-03-14 15:30:00')
        
                or a combination of multiple units, like '1h30min' (i.e. 1 hour and 30 minutes):
        
                >>> ts.floor(freq='1h30min')
                Timestamp('2020-03-14 15:00:00')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.floor()
                NaT
        
                When rounding near a daylight savings time transition, use ``ambiguous`` or
                ``nonexistent`` to control how the timestamp should be re-localized.
        
                >>> ts_tz = pd.Timestamp("2021-10-31 03:30:00").tz_localize("Europe/Amsterdam")
        
                >>> ts_tz.floor("2h", ambiguous=False)
                Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')
        
                >>> ts_tz.floor("2h", ambiguous=True)
                Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')
        """
        pass

    @classmethod
    def fromordinal(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Construct a timestamp from a a proleptic Gregorian ordinal.
        
                Parameters
                ----------
                ordinal : int
                    Date corresponding to a proleptic Gregorian ordinal.
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for the Timestamp.
        
                Notes
                -----
                By definition there cannot be any tz info on the ordinal itself.
        
                Examples
                --------
                >>> pd.Timestamp.fromordinal(737425)
                Timestamp('2020-01-01 00:00:00')
        """
        pass

    @classmethod
    def fromtimestamp(cls, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.fromtimestamp(ts)
        
                Transform timestamp[, tz] to tz's local time from POSIX timestamp.
        
                Examples
                --------
                >>> pd.Timestamp.fromtimestamp(1584199972)  # doctest: +SKIP
                Timestamp('2020-03-14 15:32:52')
        
                Note that the output may change depending on your local time.
        """
        pass

    def isocalendar(self): # real signature unknown; restored from __doc__
        """
        Return a named tuple containing ISO year, week number, and weekday.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.isocalendar()
                datetime.IsoCalendarDate(year=2022, week=52, weekday=7)
        """
        pass

    def isoweekday(self): # real signature unknown; restored from __doc__
        """
        Return the day of the week represented by the date.
        
                Monday == 1 ... Sunday == 7.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.isoweekday()
                7
        """
        pass

    @classmethod
    def now(cls): # real signature unknown; restored from __doc__
        """
        Return new Timestamp object representing current time local to tz.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to.
        
                Examples
                --------
                >>> pd.Timestamp.now()  # doctest: +SKIP
                Timestamp('2020-11-16 22:06:16.378782')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.now()
                NaT
        """
        pass

    def replace(self, year=1999, hour=10): # real signature unknown; restored from __doc__
        """
        Implements datetime.replace, handles nanoseconds.
        
                Parameters
                ----------
                year : int, optional
                month : int, optional
                day : int, optional
                hour : int, optional
                minute : int, optional
                second : int, optional
                microsecond : int, optional
                nanosecond : int, optional
                tzinfo : tz-convertible, optional
                fold : int, optional
        
                Returns
                -------
                Timestamp with fields replaced
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
        
                Replace year and the hour:
        
                >>> ts.replace(year=1999, hour=10)
                Timestamp('1999-03-14 10:32:52.192548651+0000', tz='UTC')
        
                Replace timezone (not a conversion):
        
                >>> import pytz
                >>> ts.replace(tzinfo=pytz.timezone('US/Pacific'))
                Timestamp('2020-03-14 15:32:52.192548651-0700', tz='US/Pacific')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.replace(tzinfo=pytz.timezone('US/Pacific'))
                NaT
        """
        pass

    def round(self, freq='h'): # real signature unknown; restored from __doc__
        """
        Round the Timestamp to the specified resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the rounding resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                Returns
                -------
                a new Timestamp rounded to the given resolution of `freq`
        
                Raises
                ------
                ValueError if the freq cannot be converted
        
                Notes
                -----
                If the Timestamp has a timezone, rounding will take place relative to the
                local ("wall") time and re-localized to the same timezone. When rounding
                near daylight savings time, use ``nonexistent`` and ``ambiguous`` to
                control the re-localization behavior.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
        
                A timestamp can be rounded using multiple frequency units:
        
                >>> ts.round(freq='h') # hour
                Timestamp('2020-03-14 16:00:00')
        
                >>> ts.round(freq='min') # minute
                Timestamp('2020-03-14 15:33:00')
        
                >>> ts.round(freq='s') # seconds
                Timestamp('2020-03-14 15:32:52')
        
                >>> ts.round(freq='ms') # milliseconds
                Timestamp('2020-03-14 15:32:52.193000')
        
                ``freq`` can also be a multiple of a single unit, like '5min' (i.e.  5 minutes):
        
                >>> ts.round(freq='5min')
                Timestamp('2020-03-14 15:35:00')
        
                or a combination of multiple units, like '1h30min' (i.e. 1 hour and 30 minutes):
        
                >>> ts.round(freq='1h30min')
                Timestamp('2020-03-14 15:00:00')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.round()
                NaT
        
                When rounding near a daylight savings time transition, use ``ambiguous`` or
                ``nonexistent`` to control how the timestamp should be re-localized.
        
                >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")
        
                >>> ts_tz.round("h", ambiguous=False)
                Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')
        
                >>> ts_tz.round("h", ambiguous=True)
                Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')
        """
        pass

    def strftime(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a formatted string of the Timestamp.
        
                Parameters
                ----------
                format : str
                    Format string to convert Timestamp to string.
                    See strftime documentation for more information on the format string:
                    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.strftime('%Y-%m-%d %X')
                '2020-03-14 15:32:52'
        """
        pass

    @classmethod
    def strptime(cls, string, format): # real signature unknown; restored from __doc__
        """
        Timestamp.strptime(string, format)
        
                Function is not implemented. Use pd.to_datetime().
        
                Examples
                --------
                >>> pd.Timestamp.strptime("2023-01-01", "%d/%m/%y")
                Traceback (most recent call last):
                NotImplementedError
        """
        pass

    def time(self): # real signature unknown; restored from __doc__
        """
        Return time object with same time but with tzinfo=None.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.time()
                datetime.time(10, 0)
        """
        pass

    def timetuple(self): # real signature unknown; restored from __doc__
        """
        Return time tuple, compatible with time.localtime().
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.timetuple()
                time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1,
                tm_hour=10, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=-1)
        """
        pass

    def timetz(self): # real signature unknown; restored from __doc__
        """
        Return time object with same time and tzinfo.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
                >>> ts.timetz()
                datetime.time(10, 0, tzinfo=<DstTzInfo 'Europe/Brussels' CET+1:00:00 STD>)
        """
        pass

    @classmethod
    def today(cls): # real signature unknown; restored from __doc__
        """
        Return the current time in the local timezone.
        
                This differs from datetime.today() in that it can be localized to a
                passed timezone.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to.
        
                Examples
                --------
                >>> pd.Timestamp.today()    # doctest: +SKIP
                Timestamp('2020-11-16 22:37:39.969883')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.today()
                NaT
        """
        pass

    def toordinal(self): # real signature unknown; restored from __doc__
        """
        Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:50')
                >>> ts
                Timestamp('2023-01-01 10:00:50')
                >>> ts.toordinal()
                738521
        """
        pass

    def to_julian_date(self): # real signature unknown; restored from __doc__
        """
        Convert TimeStamp to a Julian Date.
        
                0 Julian date is noon January 1, 4713 BC.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52')
                >>> ts.to_julian_date()
                2458923.147824074
        """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """
        Return time zone name.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
                >>> ts.tzname()
                'CET'
        """
        pass

    def tz_convert(self, tz=None): # real signature unknown; restored from __doc__
        """
        Convert timezone-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        
                Examples
                --------
                Create a timestamp object with UTC timezone:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
        
                Change to Tokyo timezone:
        
                >>> ts.tz_convert(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Can also use ``astimezone``:
        
                >>> ts.astimezone(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.tz_convert(tz='Asia/Tokyo')
                NaT
        """
        pass

    def tz_localize(self, tz=None): # real signature unknown; restored from __doc__
        """
        Localize the Timestamp to a timezone.
        
                Convert naive Timestamp to local time zone or remove
                timezone from timezone-aware Timestamp.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding local time.
        
                ambiguous : bool, 'NaT', default 'raise'
                    When clocks moved backward due to DST, ambiguous times may arise.
                    For example in Central European Time (UTC+01), when going from
                    03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at
                    00:30:00 UTC and at 01:30:00 UTC. In such a situation, the
                    `ambiguous` parameter dictates how ambiguous times should be
                    handled.
        
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    The behavior is as follows:
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                Returns
                -------
                localized : Timestamp
        
                Raises
                ------
                TypeError
                    If the Timestamp is tz-aware and tz is not None.
        
                Examples
                --------
                Create a naive timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651')
        
                Add 'Europe/Stockholm' as timezone:
        
                >>> ts.tz_localize(tz='Europe/Stockholm')
                Timestamp('2020-03-14 15:32:52.192548651+0100', tz='Europe/Stockholm')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.tz_localize()
                NaT
        """
        pass

    @classmethod
    def utcfromtimestamp(cls, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.utcfromtimestamp(ts)
        
                Construct a timezone-aware UTC datetime from a POSIX timestamp.
        
                Notes
                -----
                Timestamp.utcfromtimestamp behavior differs from datetime.utcfromtimestamp
                in returning a timezone-aware object.
        
                Examples
                --------
                >>> pd.Timestamp.utcfromtimestamp(1584199972)
                Timestamp('2020-03-14 15:32:52+0000', tz='UTC')
        """
        pass

    @classmethod
    def utcnow(cls): # real signature unknown; restored from __doc__
        """
        Timestamp.utcnow()
        
                Return a new Timestamp representing UTC day and time.
        
                Examples
                --------
                >>> pd.Timestamp.utcnow()   # doctest: +SKIP
                Timestamp('2020-11-16 22:50:18.092888+0000', tz='UTC')
        """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """
        Return utc offset.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
                >>> ts.utcoffset()
                datetime.timedelta(seconds=3600)
        """
        pass

    def utctimetuple(self): # real signature unknown; restored from __doc__
        """
        Return UTC time tuple, compatible with time.localtime().
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
                >>> ts.utctimetuple()
                time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1, tm_hour=9,
                tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=0)
        """
        pass

    def weekday(self): # real signature unknown; restored from __doc__
        """
        Return the day of the week represented by the date.
        
                Monday == 0 ... Sunday == 6.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01')
                >>> ts
                Timestamp('2023-01-01  00:00:00')
                >>> ts.weekday()
                6
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of days in the month.

        Returns
        -------
        int

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.days_in_month
        31
        """

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Alias for tzinfo.

        Examples
        --------
        >>> ts = pd.Timestamp(1584226800, unit='s', tz='Europe/Stockholm')
        >>> ts.tz
        <DstTzInfo 'Europe/Stockholm' CET+1:00:00 STD>
        """

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the week number of the year.

        Returns
        -------
        int

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.week
        11
        """

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.timestamps\', \'__doc__\': "\\n    Pandas replacement for python datetime.datetime object.\\n\\n    Timestamp is the pandas equivalent of python\'s Datetime\\n    and is interchangeable with it in most cases. It\'s the type used\\n    for the entries that make up a DatetimeIndex, and other timeseries\\n    oriented data structures in pandas.\\n\\n    Parameters\\n    ----------\\n    ts_input : datetime-like, str, int, float\\n        Value to be converted to Timestamp.\\n    year, month, day : int\\n    hour, minute, second, microsecond : int, optional, default 0\\n    tzinfo : datetime.tzinfo, optional, default None\\n    nanosecond : int, optional, default 0\\n    tz : str, pytz.timezone, dateutil.tz.tzfile or None\\n        Time zone for time which Timestamp will have.\\n    unit : str\\n        Unit used for conversion if ts_input is of type int or float. The\\n        valid values are \'D\', \'h\', \'m\', \'s\', \'ms\', \'us\', and \'ns\'. For\\n        example, \'s\' means seconds and \'ms\' means milliseconds.\\n\\n        For float inputs, the result will be stored in nanoseconds, and\\n        the unit attribute will be set as ``\'ns\'``.\\n    fold : {0, 1}, default None, keyword-only\\n        Due to daylight saving time, one wall clock time can occur twice\\n        when shifting from summer to winter time; fold describes whether the\\n        datetime-like corresponds  to the first (0) or the second time (1)\\n        the wall clock hits the ambiguous time.\\n\\n    Notes\\n    -----\\n    There are essentially three calling conventions for the constructor. The\\n    primary form accepts four parameters. They can be passed by position or\\n    keyword.\\n\\n    The other two forms mimic the parameters from ``datetime.datetime``. They\\n    can be passed by either position or keyword, but not both mixed together.\\n\\n    Examples\\n    --------\\n    Using the primary calling convention:\\n\\n    This converts a datetime-like string\\n\\n    >>> pd.Timestamp(\'2017-01-01T12\')\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    This converts a float representing a Unix epoch in units of seconds\\n\\n    >>> pd.Timestamp(1513393355.5, unit=\'s\')\\n    Timestamp(\'2017-12-16 03:02:35.500000\')\\n\\n    This converts an int representing a Unix-epoch in units of seconds\\n    and for a particular timezone\\n\\n    >>> pd.Timestamp(1513393355, unit=\'s\', tz=\'US/Pacific\')\\n    Timestamp(\'2017-12-15 19:02:35-0800\', tz=\'US/Pacific\')\\n\\n    Using the other two forms that mimic the API for ``datetime.datetime``:\\n\\n    >>> pd.Timestamp(2017, 1, 1, 12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n    ", \'fromordinal\': <classmethod(<cyfunction Timestamp.fromordinal at 0x0000017CEDBA5180>)>, \'now\': <classmethod(<cyfunction Timestamp.now at 0x0000017CEDBA5240>)>, \'today\': <classmethod(<cyfunction Timestamp.today at 0x0000017CEDBA5300>)>, \'utcnow\': <classmethod(<cyfunction Timestamp.utcnow at 0x0000017CEDBA53C0>)>, \'utcfromtimestamp\': <classmethod(<cyfunction Timestamp.utcfromtimestamp at 0x0000017CEDBA5480>)>, \'fromtimestamp\': <classmethod(<cyfunction Timestamp.fromtimestamp at 0x0000017CEDBA5540>)>, \'strftime\': <cyfunction Timestamp.strftime at 0x0000017CEDBA5600>, \'ctime\': <cyfunction Timestamp.ctime at 0x0000017CEDBA56C0>, \'date\': <cyfunction Timestamp.date at 0x0000017CEDBA5780>, \'dst\': <cyfunction Timestamp.dst at 0x0000017CEDBA5840>, \'isocalendar\': <cyfunction Timestamp.isocalendar at 0x0000017CEDBA5900>, \'tzname\': <cyfunction Timestamp.tzname at 0x0000017CEDBA59C0>, \'utcoffset\': <cyfunction Timestamp.utcoffset at 0x0000017CEDBA5A80>, \'utctimetuple\': <cyfunction Timestamp.utctimetuple at 0x0000017CEDBA5B40>, \'time\': <cyfunction Timestamp.time at 0x0000017CEDBA5C00>, \'timetuple\': <cyfunction Timestamp.timetuple at 0x0000017CEDBA5CC0>, \'timetz\': <cyfunction Timestamp.timetz at 0x0000017CEDBA5D80>, \'toordinal\': <cyfunction Timestamp.toordinal at 0x0000017CEDBA5E40>, \'strptime\': <classmethod(<cyfunction Timestamp.strptime at 0x0000017CEDBA5F00>)>, \'combine\': <classmethod(<cyfunction Timestamp.combine at 0x0000017CEDBA5FC0>)>, \'__new__\': <staticmethod(<cyfunction Timestamp.__new__ at 0x0000017CEDBA6080>)>, \'_round\': <cyfunction Timestamp._round at 0x0000017CEDBA6140>, \'round\': <cyfunction Timestamp.round at 0x0000017CEDBA6200>, \'floor\': <cyfunction Timestamp.floor at 0x0000017CEDBA62C0>, \'ceil\': <cyfunction Timestamp.ceil at 0x0000017CEDBA6380>, \'tz\': <property object at 0x0000017CEDB1E4D0>, \'tz_localize\': <cyfunction Timestamp.tz_localize at 0x0000017CEDBA65C0>, \'tz_convert\': <cyfunction Timestamp.tz_convert at 0x0000017CEDBA6680>, \'astimezone\': <cyfunction Timestamp.tz_convert at 0x0000017CEDBA6680>, \'replace\': <cyfunction Timestamp.replace at 0x0000017CEDBA6740>, \'to_julian_date\': <cyfunction Timestamp.to_julian_date at 0x0000017CEDBA6800>, \'isoweekday\': <cyfunction Timestamp.isoweekday at 0x0000017CEDBA68C0>, \'weekday\': <cyfunction Timestamp.weekday at 0x0000017CEDBA6980>, \'__dict__\': <attribute \'__dict__\' of \'Timestamp\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Timestamp\' objects>, \'weekofyear\': <attribute \'week\' of \'pandas._libs.tslibs.timestamps._Timestamp\' objects>, \'daysinmonth\': <attribute \'days_in_month\' of \'pandas._libs.tslibs.timestamps._Timestamp\' objects>})'


# variables with complex values

_no_input = None # (!) real value is '<object object at 0x0000017CDCB12E80>'

_zero_time = None # (!) real value is 'datetime.time(0, 0)'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017CEDAAF7D0>'

__pyx_capi__ = {
    'create_timestamp_from_ts': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10timestamps__Timestamp *(__pyx_t_5numpy_int64_t, npy_datetimestruct, PyDateTime_TZInfo *, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10timestamps_create_timestamp_from_ts *__pyx_optional_args)" at 0x0000017CEDB1DD50>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.timestamps', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017CEDAAF7D0>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\timestamps.cp313-win_amd64.pyd')"

__test__ = {
    'Timestamp.ceil (line 2091)': '\n        Return a new Timestamp ceiled to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the ceiling resolution.\n        ambiguous : bool or {\'raise\', \'NaT\'}, default \'raise\'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * \'NaT\' will return NaT for an ambiguous time.\n            * \'raise\' will raise an AmbiguousTimeError for an ambiguous time.\n\n        nonexistent : {\'raise\', \'shift_forward\', \'shift_backward, \'NaT\', timedelta}, default \'raise\'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * \'shift_forward\' will shift the nonexistent time forward to the\n              closest existing time.\n            * \'shift_backward\' will shift the nonexistent time backward to the\n              closest existing time.\n            * \'NaT\' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * \'raise\' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n\n        Notes\n        -----\n        If the Timestamp has a timezone, ceiling will take place relative to the\n        local ("wall") time and re-localized to the same timezone. When ceiling\n        near daylight savings time, use ``nonexistent`` and ``ambiguous`` to\n        control the re-localization behavior.\n\n        Examples\n        --------\n        Create a timestamp object:\n\n        >>> ts = pd.Timestamp(\'2020-03-14T15:32:52.192548651\')\n\n        A timestamp can be ceiled using multiple frequency units:\n\n        >>> ts.ceil(freq=\'h\') # hour\n        Timestamp(\'2020-03-14 16:00:00\')\n\n        >>> ts.ceil(freq=\'min\') # minute\n        Timestamp(\'2020-03-14 15:33:00\')\n\n        >>> ts.ceil(freq=\'s\') # seconds\n        Timestamp(\'2020-03-14 15:32:53\')\n\n        >>> ts.ceil(freq=\'us\') # microseconds\n        Timestamp(\'2020-03-14 15:32:52.192549\')\n\n        ``freq`` can also be a multiple of a single unit, like \'5min\' (i.e.  5 minutes):\n\n        >>> ts.ceil(freq=\'5min\')\n        Timestamp(\'2020-03-14 15:35:00\')\n\n        or a combination of multiple units, like \'1h30min\' (i.e. 1 hour and 30 minutes):\n\n        >>> ts.ceil(freq=\'1h30min\')\n        Timestamp(\'2020-03-14 16:30:00\')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.ceil()\n        NaT\n\n        When rounding near a daylight savings time transition, use ``ambiguous`` or\n        ``nonexistent`` to control how the timestamp should be re-localized.\n\n        >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")\n\n        >>> ts_tz.ceil("h", ambiguous=False)\n        Timestamp(\'2021-10-31 02:00:00+0100\', tz=\'Europe/Amsterdam\')\n\n        >>> ts_tz.ceil("h", ambiguous=True)\n        Timestamp(\'2021-10-31 02:00:00+0200\', tz=\'Europe/Amsterdam\')\n        ',
    'Timestamp.combine (line 1710)': "\n        Timestamp.combine(date, time)\n\n        Combine date, time into datetime with same date and time fields.\n\n        Examples\n        --------\n        >>> from datetime import date, time\n        >>> pd.Timestamp.combine(date(2020, 3, 14), time(15, 30, 15))\n        Timestamp('2020-03-14 15:30:15')\n        ",
    'Timestamp.ctime (line 1490)': "\n        Return ctime() style string.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00.00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.ctime()\n        'Sun Jan  1 10:00:00 2023'\n        ",
    'Timestamp.date (line 1515)': "\n        Return date object with same year, month and day.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00.00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.date()\n        datetime.date(2023, 1, 1)\n        ",
    'Timestamp.dst (line 1536)': "\n        Return the daylight saving time (DST) adjustment.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2000-06-01 00:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2000-06-01 00:00:00+0200', tz='Europe/Brussels')\n        >>> ts.dst()\n        datetime.timedelta(seconds=3600)\n        ",
    'Timestamp.floor (line 2002)': '\n        Return a new Timestamp floored to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the flooring resolution.\n        ambiguous : bool or {\'raise\', \'NaT\'}, default \'raise\'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * \'NaT\' will return NaT for an ambiguous time.\n            * \'raise\' will raise an AmbiguousTimeError for an ambiguous time.\n\n        nonexistent : {\'raise\', \'shift_forward\', \'shift_backward, \'NaT\', timedelta}, default \'raise\'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * \'shift_forward\' will shift the nonexistent time forward to the\n              closest existing time.\n            * \'shift_backward\' will shift the nonexistent time backward to the\n              closest existing time.\n            * \'NaT\' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * \'raise\' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n\n        Notes\n        -----\n        If the Timestamp has a timezone, flooring will take place relative to the\n        local ("wall") time and re-localized to the same timezone. When flooring\n        near daylight savings time, use ``nonexistent`` and ``ambiguous`` to\n        control the re-localization behavior.\n\n        Examples\n        --------\n        Create a timestamp object:\n\n        >>> ts = pd.Timestamp(\'2020-03-14T15:32:52.192548651\')\n\n        A timestamp can be floored using multiple frequency units:\n\n        >>> ts.floor(freq=\'h\') # hour\n        Timestamp(\'2020-03-14 15:00:00\')\n\n        >>> ts.floor(freq=\'min\') # minute\n        Timestamp(\'2020-03-14 15:32:00\')\n\n        >>> ts.floor(freq=\'s\') # seconds\n        Timestamp(\'2020-03-14 15:32:52\')\n\n        >>> ts.floor(freq=\'ns\') # nanoseconds\n        Timestamp(\'2020-03-14 15:32:52.192548651\')\n\n        ``freq`` can also be a multiple of a single unit, like \'5min\' (i.e.  5 minutes):\n\n        >>> ts.floor(freq=\'5min\')\n        Timestamp(\'2020-03-14 15:30:00\')\n\n        or a combination of multiple units, like \'1h30min\' (i.e. 1 hour and 30 minutes):\n\n        >>> ts.floor(freq=\'1h30min\')\n        Timestamp(\'2020-03-14 15:00:00\')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.floor()\n        NaT\n\n        When rounding near a daylight savings time transition, use ``ambiguous`` or\n        ``nonexistent`` to control how the timestamp should be re-localized.\n\n        >>> ts_tz = pd.Timestamp("2021-10-31 03:30:00").tz_localize("Europe/Amsterdam")\n\n        >>> ts_tz.floor("2h", ambiguous=False)\n        Timestamp(\'2021-10-31 02:00:00+0100\', tz=\'Europe/Amsterdam\')\n\n        >>> ts_tz.floor("2h", ambiguous=True)\n        Timestamp(\'2021-10-31 02:00:00+0200\', tz=\'Europe/Amsterdam\')\n        ',
    'Timestamp.fromordinal (line 1337)': "\n        Construct a timestamp from a a proleptic Gregorian ordinal.\n\n        Parameters\n        ----------\n        ordinal : int\n            Date corresponding to a proleptic Gregorian ordinal.\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for the Timestamp.\n\n        Notes\n        -----\n        By definition there cannot be any tz info on the ordinal itself.\n\n        Examples\n        --------\n        >>> pd.Timestamp.fromordinal(737425)\n        Timestamp('2020-01-01 00:00:00')\n        ",
    'Timestamp.fromtimestamp (line 1443)': "\n        Timestamp.fromtimestamp(ts)\n\n        Transform timestamp[, tz] to tz's local time from POSIX timestamp.\n\n        Examples\n        --------\n        >>> pd.Timestamp.fromtimestamp(1584199972)  # doctest: +SKIP\n        Timestamp('2020-03-14 15:32:52')\n\n        Note that the output may change depending on your local time.\n        ",
    'Timestamp.isocalendar (line 1550)': "\n        Return a named tuple containing ISO year, week number, and weekday.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.isocalendar()\n        datetime.IsoCalendarDate(year=2022, week=52, weekday=7)\n        ",
    'Timestamp.isoweekday (line 2543)': "\n        Return the day of the week represented by the date.\n\n        Monday == 1 ... Sunday == 7.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.isoweekday()\n        7\n        ",
    'Timestamp.now (line 1360)': "\n        Return new Timestamp object representing current time local to tz.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n\n        Examples\n        --------\n        >>> pd.Timestamp.now()  # doctest: +SKIP\n        Timestamp('2020-11-16 22:06:16.378782')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.now()\n        NaT\n        ",
    'Timestamp.replace (line 2361)': "\n        Implements datetime.replace, handles nanoseconds.\n\n        Parameters\n        ----------\n        year : int, optional\n        month : int, optional\n        day : int, optional\n        hour : int, optional\n        minute : int, optional\n        second : int, optional\n        microsecond : int, optional\n        nanosecond : int, optional\n        tzinfo : tz-convertible, optional\n        fold : int, optional\n\n        Returns\n        -------\n        Timestamp with fields replaced\n\n        Examples\n        --------\n        Create a timestamp object:\n\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')\n        >>> ts\n        Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')\n\n        Replace year and the hour:\n\n        >>> ts.replace(year=1999, hour=10)\n        Timestamp('1999-03-14 10:32:52.192548651+0000', tz='UTC')\n\n        Replace timezone (not a conversion):\n\n        >>> import pytz\n        >>> ts.replace(tzinfo=pytz.timezone('US/Pacific'))\n        Timestamp('2020-03-14 15:32:52.192548651-0700', tz='US/Pacific')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.replace(tzinfo=pytz.timezone('US/Pacific'))\n        NaT\n        ",
    'Timestamp.round (line 1907)': '\n        Round the Timestamp to the specified resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the rounding resolution.\n        ambiguous : bool or {\'raise\', \'NaT\'}, default \'raise\'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * \'NaT\' will return NaT for an ambiguous time.\n            * \'raise\' will raise an AmbiguousTimeError for an ambiguous time.\n\n        nonexistent : {\'raise\', \'shift_forward\', \'shift_backward, \'NaT\', timedelta}, default \'raise\'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * \'shift_forward\' will shift the nonexistent time forward to the\n              closest existing time.\n            * \'shift_backward\' will shift the nonexistent time backward to the\n              closest existing time.\n            * \'NaT\' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * \'raise\' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n        Returns\n        -------\n        a new Timestamp rounded to the given resolution of `freq`\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n\n        Notes\n        -----\n        If the Timestamp has a timezone, rounding will take place relative to the\n        local ("wall") time and re-localized to the same timezone. When rounding\n        near daylight savings time, use ``nonexistent`` and ``ambiguous`` to\n        control the re-localization behavior.\n\n        Examples\n        --------\n        Create a timestamp object:\n\n        >>> ts = pd.Timestamp(\'2020-03-14T15:32:52.192548651\')\n\n        A timestamp can be rounded using multiple frequency units:\n\n        >>> ts.round(freq=\'h\') # hour\n        Timestamp(\'2020-03-14 16:00:00\')\n\n        >>> ts.round(freq=\'min\') # minute\n        Timestamp(\'2020-03-14 15:33:00\')\n\n        >>> ts.round(freq=\'s\') # seconds\n        Timestamp(\'2020-03-14 15:32:52\')\n\n        >>> ts.round(freq=\'ms\') # milliseconds\n        Timestamp(\'2020-03-14 15:32:52.193000\')\n\n        ``freq`` can also be a multiple of a single unit, like \'5min\' (i.e.  5 minutes):\n\n        >>> ts.round(freq=\'5min\')\n        Timestamp(\'2020-03-14 15:35:00\')\n\n        or a combination of multiple units, like \'1h30min\' (i.e. 1 hour and 30 minutes):\n\n        >>> ts.round(freq=\'1h30min\')\n        Timestamp(\'2020-03-14 15:00:00\')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.round()\n        NaT\n\n        When rounding near a daylight savings time transition, use ``ambiguous`` or\n        ``nonexistent`` to control how the timestamp should be re-localized.\n\n        >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")\n\n        >>> ts_tz.round("h", ambiguous=False)\n        Timestamp(\'2021-10-31 02:00:00+0100\', tz=\'Europe/Amsterdam\')\n\n        >>> ts_tz.round("h", ambiguous=True)\n        Timestamp(\'2021-10-31 02:00:00+0200\', tz=\'Europe/Amsterdam\')\n        ',
    'Timestamp.strftime (line 1460)': "\n        Return a formatted string of the Timestamp.\n\n        Parameters\n        ----------\n        format : str\n            Format string to convert Timestamp to string.\n            See strftime documentation for more information on the format string:\n            https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.strftime('%Y-%m-%d %X')\n        '2020-03-14 15:32:52'\n        ",
    'Timestamp.strptime (line 1692)': '\n        Timestamp.strptime(string, format)\n\n        Function is not implemented. Use pd.to_datetime().\n\n        Examples\n        --------\n        >>> pd.Timestamp.strptime("2023-01-01", "%d/%m/%y")\n        Traceback (most recent call last):\n        NotImplementedError\n        ',
    'Timestamp.time (line 1616)': "\n        Return time object with same time but with tzinfo=None.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.time()\n        datetime.time(10, 0)\n        ",
    'Timestamp.timetuple (line 1630)': "\n        Return time tuple, compatible with time.localtime().\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.timetuple()\n        time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1,\n        tm_hour=10, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=-1)\n        ",
    'Timestamp.timetz (line 1654)': "\n        Return time object with same time and tzinfo.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')\n        >>> ts.timetz()\n        datetime.time(10, 0, tzinfo=<DstTzInfo 'Europe/Brussels' CET+1:00:00 STD>)\n        ",
    'Timestamp.to_julian_date (line 2511)': "\n        Convert TimeStamp to a Julian Date.\n\n        0 Julian date is noon January 1, 4713 BC.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52')\n        >>> ts.to_julian_date()\n        2458923.147824074\n        ",
    'Timestamp.today (line 1384)': "\n        Return the current time in the local timezone.\n\n        This differs from datetime.today() in that it can be localized to a\n        passed timezone.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n\n        Examples\n        --------\n        >>> pd.Timestamp.today()    # doctest: +SKIP\n        Timestamp('2020-11-16 22:37:39.969883')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.today()\n        NaT\n        ",
    'Timestamp.toordinal (line 1668)': "\n        Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:50')\n        >>> ts\n        Timestamp('2023-01-01 10:00:50')\n        >>> ts.toordinal()\n        738521\n        ",
    'Timestamp.tz (line 2180)': "\n        Alias for tzinfo.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(1584226800, unit='s', tz='Europe/Stockholm')\n        >>> ts.tz\n        <DstTzInfo 'Europe/Stockholm' CET+1:00:00 STD>\n        ",
    'Timestamp.tz_convert (line 2306)': "\n        Convert timezone-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n\n        Examples\n        --------\n        Create a timestamp object with UTC timezone:\n\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')\n        >>> ts\n        Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')\n\n        Change to Tokyo timezone:\n\n        >>> ts.tz_convert(tz='Asia/Tokyo')\n        Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')\n\n        Can also use ``astimezone``:\n\n        >>> ts.astimezone(tz='Asia/Tokyo')\n        Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.tz_convert(tz='Asia/Tokyo')\n        NaT\n        ",
    'Timestamp.tz_localize (line 2201)': "\n        Localize the Timestamp to a timezone.\n\n        Convert naive Timestamp to local time zone or remove\n        timezone from timezone-aware Timestamp.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding local time.\n\n        ambiguous : bool, 'NaT', default 'raise'\n            When clocks moved backward due to DST, ambiguous times may arise.\n            For example in Central European Time (UTC+01), when going from\n            03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at\n            00:30:00 UTC and at 01:30:00 UTC. In such a situation, the\n            `ambiguous` parameter dictates how ambiguous times should be\n            handled.\n\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise an AmbiguousTimeError for an ambiguous time.\n\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            The behavior is as follows:\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times.\n\n        Returns\n        -------\n        localized : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If the Timestamp is tz-aware and tz is not None.\n\n        Examples\n        --------\n        Create a naive timestamp object:\n\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts\n        Timestamp('2020-03-14 15:32:52.192548651')\n\n        Add 'Europe/Stockholm' as timezone:\n\n        >>> ts.tz_localize(tz='Europe/Stockholm')\n        Timestamp('2020-03-14 15:32:52.192548651+0100', tz='Europe/Stockholm')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.tz_localize()\n        NaT\n        ",
    'Timestamp.tzname (line 1573)': "\n        Return time zone name.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')\n        >>> ts.tzname()\n        'CET'\n        ",
    'Timestamp.utcfromtimestamp (line 1423)': "\n        Timestamp.utcfromtimestamp(ts)\n\n        Construct a timezone-aware UTC datetime from a POSIX timestamp.\n\n        Notes\n        -----\n        Timestamp.utcfromtimestamp behavior differs from datetime.utcfromtimestamp\n        in returning a timezone-aware object.\n\n        Examples\n        --------\n        >>> pd.Timestamp.utcfromtimestamp(1584199972)\n        Timestamp('2020-03-14 15:32:52+0000', tz='UTC')\n        ",
    'Timestamp.utcnow (line 1409)': "\n        Timestamp.utcnow()\n\n        Return a new Timestamp representing UTC day and time.\n\n        Examples\n        --------\n        >>> pd.Timestamp.utcnow()   # doctest: +SKIP\n        Timestamp('2020-11-16 22:50:18.092888+0000', tz='UTC')\n        ",
    'Timestamp.utcoffset (line 1587)': "\n        Return utc offset.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')\n        >>> ts.utcoffset()\n        datetime.timedelta(seconds=3600)\n        ",
    'Timestamp.utctimetuple (line 1601)': "\n        Return UTC time tuple, compatible with time.localtime().\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')\n        >>> ts.utctimetuple()\n        time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1, tm_hour=9,\n        tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=0)\n        ",
    'Timestamp.weekday (line 2562)': "\n        Return the day of the week represented by the date.\n\n        Monday == 0 ... Sunday == 6.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01')\n        >>> ts\n        Timestamp('2023-01-01  00:00:00')\n        >>> ts.weekday()\n        6\n        ",
    '_Timestamp.as_unit (line 1084)': '\n        Convert the underlying int64 representaton to the given unit.\n\n        Parameters\n        ----------\n        unit : {"ns", "us", "ms", "s"}\n        round_ok : bool, default True\n            If False and the conversion requires rounding, raise.\n\n        Returns\n        -------\n        Timestamp\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(\'2023-01-01 00:00:00.01\')\n        >>> ts\n        Timestamp(\'2023-01-01 00:00:00.010000\')\n        >>> ts.unit\n        \'ms\'\n        >>> ts = ts.as_unit(\'s\')\n        >>> ts\n        Timestamp(\'2023-01-01 00:00:00\')\n        >>> ts.unit\n        \'s\'\n        ',
    '_Timestamp.asm8.__get__ (line 1120)': "\n        Return numpy datetime64 format in nanoseconds.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14, 15)\n        >>> ts.asm8\n        numpy.datetime64('2020-03-14T15:00:00.000000')\n        ",
    '_Timestamp.day_name (line 761)': "\n        Return the day name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the day name.\n\n        Returns\n        -------\n        str\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.day_name()\n        'Saturday'\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.day_name()\n        nan\n        ",
    '_Timestamp.day_of_week.__get__ (line 830)': '\n        Return day of the week.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.day_of_week\n        5\n        ',
    '_Timestamp.day_of_year.__get__ (line 847)': '\n        Return the day of the year.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.day_of_year\n        74\n        ',
    '_Timestamp.days_in_month.__get__ (line 898)': '\n        Return the number of days in the month.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.days_in_month\n        31\n        ',
    '_Timestamp.is_leap_year.__get__ (line 813)': '\n        Return True if year is a leap year.\n\n        Returns\n        -------\n        bool\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_leap_year\n        True\n        ',
    '_Timestamp.is_month_end.__get__ (line 619)': '\n        Check if the date is the last day of the month.\n\n        Returns\n        -------\n        bool\n            True if the date is the last day of the month.\n\n        See Also\n        --------\n        Timestamp.is_month_start : Similar property indicating month start.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_month_end\n        False\n\n        >>> ts = pd.Timestamp(2020, 12, 31)\n        >>> ts.is_month_end\n        True\n        ',
    '_Timestamp.is_month_start.__get__ (line 593)': '\n        Check if the date is the first day of the month.\n\n        Returns\n        -------\n        bool\n            True if the date is the first day of the month.\n\n        See Also\n        --------\n        Timestamp.is_month_end : Similar property indicating the last day of the month.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_month_start\n        False\n\n        >>> ts = pd.Timestamp(2020, 1, 1)\n        >>> ts.is_month_start\n        True\n        ',
    '_Timestamp.is_quarter_end.__get__ (line 672)': '\n        Check if date is last day of the quarter.\n\n        Returns\n        -------\n        bool\n            True if date is last day of the quarter.\n\n        See Also\n        --------\n        Timestamp.is_quarter_start : Similar property indicating the quarter start.\n        Timestamp.quarter : Return the quarter of the date.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_quarter_end\n        False\n\n        >>> ts = pd.Timestamp(2020, 3, 31)\n        >>> ts.is_quarter_end\n        True\n        ',
    '_Timestamp.is_quarter_start.__get__ (line 645)': '\n        Check if the date is the first day of the quarter.\n\n        Returns\n        -------\n        bool\n            True if date is first day of the quarter.\n\n        See Also\n        --------\n        Timestamp.is_quarter_end : Similar property indicating the quarter end.\n        Timestamp.quarter : Return the quarter of the date.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_quarter_start\n        False\n\n        >>> ts = pd.Timestamp(2020, 4, 1)\n        >>> ts.is_quarter_start\n        True\n        ',
    '_Timestamp.is_year_end.__get__ (line 724)': '\n        Return True if date is last day of the year.\n\n        Returns\n        -------\n        bool\n\n        See Also\n        --------\n        Timestamp.is_year_start : Similar property indicating the start of the year.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_year_end\n        False\n\n        >>> ts = pd.Timestamp(2020, 12, 31)\n        >>> ts.is_year_end\n        True\n        ',
    '_Timestamp.is_year_start.__get__ (line 699)': '\n        Return True if date is first day of the year.\n\n        Returns\n        -------\n        bool\n\n        See Also\n        --------\n        Timestamp.is_year_end : Similar property indicating the end of the year.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_year_start\n        False\n\n        >>> ts = pd.Timestamp(2020, 1, 1)\n        >>> ts.is_year_start\n        True\n        ',
    '_Timestamp.isoformat (line 966)': "\n        Return the time formatted according to ISO 8601.\n\n        The full format looks like 'YYYY-MM-DD HH:MM:SS.mmmmmmnnn'.\n        By default, the fractional part is omitted if self.microsecond == 0\n        and self.nanosecond == 0.\n\n        If self.tzinfo is not None, the UTC offset is also attached, giving\n        giving a full format of 'YYYY-MM-DD HH:MM:SS.mmmmmmnnn+HH:MM'.\n\n        Parameters\n        ----------\n        sep : str, default 'T'\n            String used as the separator between the date and time.\n\n        timespec : str, default 'auto'\n            Specifies the number of additional terms of the time to include.\n            The valid values are 'auto', 'hours', 'minutes', 'seconds',\n            'milliseconds', 'microseconds', and 'nanoseconds'.\n\n        Returns\n        -------\n        str\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.isoformat()\n        '2020-03-14T15:32:52.192548651'\n        >>> ts.isoformat(timespec='microseconds')\n        '2020-03-14T15:32:52.192548'\n        ",
    '_Timestamp.month_name (line 787)': "\n        Return the month name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the month name.\n\n        Returns\n        -------\n        str\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.month_name()\n        'March'\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.month_name()\n        nan\n        ",
    '_Timestamp.normalize (line 918)': "\n        Normalize Timestamp to midnight, preserving tz information.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14, 15, 30)\n        >>> ts.normalize()\n        Timestamp('2020-03-14 00:00:00')\n        ",
    '_Timestamp.quarter.__get__ (line 864)': '\n        Return the quarter of the year.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.quarter\n        1\n        ',
    '_Timestamp.timestamp (line 1133)': "\n        Return POSIX timestamp as float.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')\n        >>> ts.timestamp()\n        1584199972.192548\n        ",
    '_Timestamp.to_datetime64 (line 1175)': "\n        Return a numpy.datetime64 object with same precision.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(year=2023, month=1, day=1,\n        ...                   hour=10, second=15)\n        >>> ts\n        Timestamp('2023-01-01 10:00:15')\n        >>> ts.to_datetime64()\n        numpy.datetime64('2023-01-01T10:00:15.000000')\n        ",
    '_Timestamp.to_numpy (line 1192)': "\n        Convert the Timestamp to a NumPy datetime64.\n\n        This is an alias method for `Timestamp.to_datetime64()`. The dtype and\n        copy parameters are available here only for compatibility. Their values\n        will not affect the return value.\n\n        Returns\n        -------\n        numpy.datetime64\n\n        See Also\n        --------\n        DatetimeIndex.to_numpy : Similar method for DatetimeIndex.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.to_numpy()\n        numpy.datetime64('2020-03-14T15:32:52.192548651')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.to_numpy()\n        numpy.datetime64('NaT')\n        ",
    '_Timestamp.to_period (line 1225)': "\n        Return an period of which this timestamp is an observation.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> # Year end frequency\n        >>> ts.to_period(freq='Y')\n        Period('2020', 'Y-DEC')\n\n        >>> # Month end frequency\n        >>> ts.to_period(freq='M')\n        Period('2020-03', 'M')\n\n        >>> # Weekly frequency\n        >>> ts.to_period(freq='W')\n        Period('2020-03-09/2020-03-15', 'W-SUN')\n\n        >>> # Quarter end frequency\n        >>> ts.to_period(freq='Q')\n        Period('2020Q1', 'Q-DEC')\n        ",
    '_Timestamp.to_pydatetime (line 1150)': "\n        Convert a Timestamp object to a native Python datetime object.\n\n        If warn=True, issue a warning if nanoseconds is nonzero.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')\n        >>> ts.to_pydatetime()\n        datetime.datetime(2020, 3, 14, 15, 32, 52, 192548)\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.to_pydatetime()\n        NaT\n        ",
    '_Timestamp.unit.__get__ (line 252)': '\n        The abbreviation associated with self._creso.\n\n        Examples\n        --------\n        >>> pd.Timestamp("2020-01-01 12:34:56").unit\n        \'s\'\n\n        >>> pd.Timestamp("2020-01-01 12:34:56.123").unit\n        \'ms\'\n\n        >>> pd.Timestamp("2020-01-01 12:34:56.123456").unit\n        \'us\'\n\n        >>> pd.Timestamp("2020-01-01 12:34:56.123456789").unit\n        \'ns\'\n        ',
    '_Timestamp.week.__get__ (line 881)': '\n        Return the week number of the year.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.week\n        11\n        ',
}

