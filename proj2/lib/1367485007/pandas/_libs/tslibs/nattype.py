# encoding: utf-8
# module pandas._libs.tslibs.nattype
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslibs\nattype.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
import datetime as __datetime


# Variables with simple values

iNaT = -9223372036854775808

# functions

def _make_error_func(*args, **kwargs): # real signature unknown
    pass

def _make_nan_func(*args, **kwargs): # real signature unknown
    pass

def _make_nat_func(*args, **kwargs): # real signature unknown
    pass

def __nat_unpickle(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__NaT(*args, **kwargs): # real signature unknown
    pass

# classes

class _NaT(__datetime.datetime):
    # no doc
    def isoformat(self, *args, **kwargs): # real signature unknown
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
        Convert the Timestamp to a NumPy datetime64 or timedelta64.
        
                With the default 'dtype', this is an alias method for `NaT.to_datetime64()`.
        
                The copy parameter is available here only for compatibility. Its value
                will not affect the return value.
        
                Returns
                -------
                numpy.datetime64 or numpy.timedelta64
        
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
        
                >>> pd.NaT.to_numpy("m8[ns]")
                numpy.timedelta64('NaT','ns')
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
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

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __array_priority__ = 100


class NaTType(_NaT):
    """
    (N)ot-(A)-(T)ime, the time equivalent of NaN.
    
        Examples
        --------
        >>> pd.DataFrame([pd.Timestamp("2023"), np.nan], columns=["col_1"])
                col_1
        0  2023-01-01
        1         NaT
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

    def combine(self, date, time): # real signature unknown; restored from __doc__
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

    def fromisocalendar(self, *args, **kwargs): # real signature unknown
        """
        int, int, int -> Construct a date from the ISO year, week number and weekday.
        
        This is the inverse of the date.isocalendar() function
        """
        pass

    def fromordinal(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def fromtimestamp(self, ts): # real signature unknown; restored from __doc__
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

    def now(self): # real signature unknown; restored from __doc__
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

    def strptime(self, string, format): # real signature unknown; restored from __doc__
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

    def today(self): # real signature unknown; restored from __doc__
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

    def total_seconds(self): # real signature unknown; restored from __doc__
        """
        Total seconds in the duration.
        
                Examples
                --------
                >>> td = pd.Timedelta('1min')
                >>> td
                Timedelta('0 days 00:01:00')
                >>> td.total_seconds()
                60.0
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

    def utcfromtimestamp(self, ts): # real signature unknown; restored from __doc__
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

    def utcnow(self): # real signature unknown; restored from __doc__
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    day_of_week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    day_of_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    millisecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.nattype\', \'__doc__\': \'\\n    (N)ot-(A)-(T)ime, the time equivalent of NaN.\\n\\n    Examples\\n    --------\\n    >>> pd.DataFrame([pd.Timestamp("2023"), np.nan], columns=["col_1"])\\n            col_1\\n    0  2023-01-01\\n    1         NaT\\n    \', \'__new__\': <staticmethod(<cyfunction NaTType.__new__ at 0x000001D4D7E4FAC0>)>, \'value\': <property object at 0x000001D4D90304A0>, \'__reduce_ex__\': <cyfunction NaTType.__reduce_ex__ at 0x000001D4D7E4FC40>, \'__reduce__\': <cyfunction NaTType.__reduce__ at 0x000001D4D7E4FD00>, \'__rtruediv__\': <cyfunction NaTType.__rtruediv__ at 0x000001D4D7E4FDC0>, \'__rfloordiv__\': <cyfunction NaTType.__rfloordiv__ at 0x000001D4D7E4FE80>, \'__rmul__\': <cyfunction NaTType.__rmul__ at 0x000001D4D7E4FF40>, \'year\': <property object at 0x000001D4D9030450>, \'quarter\': <property object at 0x000001D4D9030400>, \'month\': <property object at 0x000001D4D90303B0>, \'day\': <property object at 0x000001D4D90300E0>, \'hour\': <property object at 0x000001D4D90305E0>, \'minute\': <property object at 0x000001D4D9030630>, \'second\': <property object at 0x000001D4D9030680>, \'millisecond\': <property object at 0x000001D4D90306D0>, \'microsecond\': <property object at 0x000001D4D9030720>, \'nanosecond\': <property object at 0x000001D4D9030770>, \'week\': <property object at 0x000001D4D90307C0>, \'dayofyear\': <property object at 0x000001D4D9030810>, \'day_of_year\': <property object at 0x000001D4D9030860>, \'weekofyear\': <property object at 0x000001D4D90308B0>, \'days_in_month\': <property object at 0x000001D4D9030900>, \'daysinmonth\': <property object at 0x000001D4D9030950>, \'dayofweek\': <property object at 0x000001D4D90309A0>, \'day_of_week\': <property object at 0x000001D4D90309F0>, \'days\': <property object at 0x000001D4D9030A40>, \'seconds\': <property object at 0x000001D4D9030A90>, \'microseconds\': <property object at 0x000001D4D9030AE0>, \'nanoseconds\': <property object at 0x000001D4D9030B30>, \'qyear\': <property object at 0x000001D4D9030B80>, \'weekday\': <cyfunction _make_nan_func.<locals>.f at 0x000001D4D9035180>, \'isoweekday\': <cyfunction _make_nan_func.<locals>.f at 0x000001D4D9035240>, \'total_seconds\': <cyfunction _make_nan_func.<locals>.f at 0x000001D4D9035300>, \'month_name\': <cyfunction _make_nan_func.<locals>.f at 0x000001D4D90353C0>, \'day_name\': <cyfunction _make_nan_func.<locals>.f at 0x000001D4D9035480>, \'fromisocalendar\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035540>, \'isocalendar\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035600>, \'dst\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D90356C0>, \'date\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D9035780>, \'utctimetuple\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035840>, \'utcoffset\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035900>, \'tzname\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D90359C0>, \'time\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035A80>, \'timetuple\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035B40>, \'timetz\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035C00>, \'toordinal\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035CC0>, \'ctime\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035D80>, \'strftime\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035E40>, \'strptime\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035F00>, \'utcfromtimestamp\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9035FC0>, \'fromtimestamp\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9036080>, \'combine\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9036140>, \'utcnow\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9036200>, \'timestamp\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D90362C0>, \'astimezone\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9036380>, \'fromordinal\': <cyfunction _make_error_func.<locals>.f at 0x000001D4D9036440>, \'to_pydatetime\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D9036500>, \'now\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D90365C0>, \'today\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D9036680>, \'round\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D9036740>, \'floor\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D9036800>, \'ceil\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D90368C0>, \'tz_convert\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D9036980>, \'tz_localize\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D9036A40>, \'replace\': <cyfunction _make_nat_func.<locals>.f at 0x000001D4D9036B00>, \'tz\': <property object at 0x000001D4D9030BD0>, \'tzinfo\': <property object at 0x000001D4D9030C20>, \'as_unit\': <cyfunction NaTType.as_unit at 0x000001D4D9036D40>, \'__dict__\': <attribute \'__dict__\' of \'NaTType\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'NaTType\' objects>})'


# variables with complex values

NaT = None # (!) real value is 'NaT'

nat_strings = None # (!) real value is "{'NAN', 'nat', 'nan', 'NaT', 'NaN', 'NAT'}"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D4D9018110>'

__pyx_capi__ = {
    'NPY_NAT': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t" at 0x000001D4D900FA60>'
    'c_NaT': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_7nattype__NaT *" at 0x000001D4D900FB00>'
    'c_nat_strings': None, # (!) real value is '<capsule object "PyObject *" at 0x000001D4D900FAB0>'
    'checknull_with_nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001D4D900FB50>'
    'is_dt64nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001D4D900FBA0>'
    'is_td64nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001D4D900FBF0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.nattype', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D4D9018110>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\nattype.cp313-win_amd64.pyd')"

__test__ = {
    'NaTType.as_unit (line 1367)': '\n        Convert the underlying int64 representaton to the given unit.\n\n        Parameters\n        ----------\n        unit : {"ns", "us", "ms", "s"}\n        round_ok : bool, default True\n            If False and the conversion requires rounding, raise.\n\n        Returns\n        -------\n        Timestamp\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(\'2023-01-01 00:00:00.01\')\n        >>> ts\n        Timestamp(\'2023-01-01 00:00:00.010000\')\n        >>> ts.unit\n        \'ms\'\n        >>> ts = ts.as_unit(\'s\')\n        >>> ts\n        Timestamp(\'2023-01-01 00:00:00\')\n        >>> ts.unit\n        \'s\'\n        ',
    '_NaT.to_datetime64 (line 230)': "\n        Return a numpy.datetime64 object with same precision.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(year=2023, month=1, day=1,\n        ...                   hour=10, second=15)\n        >>> ts\n        Timestamp('2023-01-01 10:00:15')\n        >>> ts.to_datetime64()\n        numpy.datetime64('2023-01-01T10:00:15.000000')\n        ",
    '_NaT.to_numpy (line 245)': '\n        Convert the Timestamp to a NumPy datetime64 or timedelta64.\n\n        With the default \'dtype\', this is an alias method for `NaT.to_datetime64()`.\n\n        The copy parameter is available here only for compatibility. Its value\n        will not affect the return value.\n\n        Returns\n        -------\n        numpy.datetime64 or numpy.timedelta64\n\n        See Also\n        --------\n        DatetimeIndex.to_numpy : Similar method for DatetimeIndex.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(\'2020-03-14T15:32:52.192548651\')\n        >>> ts.to_numpy()\n        numpy.datetime64(\'2020-03-14T15:32:52.192548651\')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.to_numpy()\n        numpy.datetime64(\'NaT\')\n\n        >>> pd.NaT.to_numpy("m8[ns]")\n        numpy.timedelta64(\'NaT\',\'ns\')\n        ',
}

