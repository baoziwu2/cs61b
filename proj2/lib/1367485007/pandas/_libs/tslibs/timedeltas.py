# encoding: utf-8
# module pandas._libs.tslibs.timedeltas
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslibs\timedeltas.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import collections as collections # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\collections\__init__.py
import warnings as warnings # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\warnings.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
from pandas._libs.tslibs.fields import RoundTo, round_nsint64

from pandas._libs.tslibs.np_datetime import (OutOfBoundsDatetime, 
    OutOfBoundsTimedelta)

import datetime as __datetime


# functions

def array_to_timedelta64(*args, **kwargs): # real signature unknown
    """
    Convert an ndarray to an array of timedeltas. If errors == 'coerce',
        coerce non-convertible objects to NaT. Otherwise, raise.
    
        Returns
        -------
        np.ndarray[timedelta64ns]
    """
    pass

def delta_to_nanoseconds(*args, **kwargs): # real signature unknown
    pass

def disallow_ambiguous_unit(*args, **kwargs): # real signature unknown
    pass

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

def floordiv_object_array(*args, **kwargs): # real signature unknown
    pass

def get_unit_for_round(*args, **kwargs): # real signature unknown
    pass

def ints_to_pytimedelta(*args, **kwargs): # real signature unknown
    """
    convert an i8 repr to an ndarray of timedelta or Timedelta (if box ==
        True)
    
        Parameters
        ----------
        arr : ndarray[timedelta64]
        box : bool, default False
    
        Returns
        -------
        result : ndarray[object]
            array of Timedelta or timedeltas objects
    """
    pass

def parse_timedelta_unit(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        unit : str or None
    
        Returns
        -------
        str
            Canonical unit string.
    
        Raises
        ------
        ValueError : on non-parseable input
    """
    pass

def truediv_object_array(*args, **kwargs): # real signature unknown
    pass

def _binary_op_method_timedeltalike(*args, **kwargs): # real signature unknown
    pass

def _op_unary_method(*args, **kwargs): # real signature unknown
    pass

def _timedelta_unpickle(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__Timedelta(*args, **kwargs): # real signature unknown
    pass

# classes

class Components(tuple):
    """ Components(days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Components object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new Components object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds): # reliably restored by inspect
        """ Create new instance of Components(days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds) """
        pass

    def __replace__(self, **kwds): # reliably restored by inspect
        """ Return a new Components object replacing specified fields with new values """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    days = _tuplegetter(0, 'Alias for field number 0')
    hours = _tuplegetter(1, 'Alias for field number 1')
    microseconds = _tuplegetter(5, 'Alias for field number 5')
    milliseconds = _tuplegetter(4, 'Alias for field number 4')
    minutes = _tuplegetter(2, 'Alias for field number 2')
    nanoseconds = _tuplegetter(6, 'Alias for field number 6')
    seconds = _tuplegetter(3, 'Alias for field number 3')
    _fields = (
        'days',
        'hours',
        'minutes',
        'seconds',
        'milliseconds',
        'microseconds',
        'nanoseconds',
    )
    _field_defaults = {}
    __match_args__ = (
        'days',
        'hours',
        'minutes',
        'seconds',
        'milliseconds',
        'microseconds',
        'nanoseconds',
    )
    __slots__ = ()


class MinMaxReso(object):
    """
    We need to define min/max/resolution on both the Timedelta _instance_
        and Timedelta class.  On an instance, these depend on the object's _reso.
        On the class, we default to the values we would get with nanosecond _reso.
    """
    def __get__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.timedeltas\', \'__doc__\': "\\n    We need to define min/max/resolution on both the Timedelta _instance_\\n    and Timedelta class.  On an instance, these depend on the object\'s _reso.\\n    On the class, we default to the values we would get with nanosecond _reso.\\n    ", \'__init__\': <cyfunction MinMaxReso.__init__ at 0x0000019CFEFA5A80>, \'__get__\': <cyfunction MinMaxReso.__get__ at 0x0000019CFEFA5B40>, \'__set__\': <cyfunction MinMaxReso.__set__ at 0x0000019CFEFA5C00>, \'__dict__\': <attribute \'__dict__\' of \'MinMaxReso\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'MinMaxReso\' objects>})'


class _Timedelta(__datetime.timedelta):
    # no doc
    def as_unit(self, s): # real signature unknown; restored from __doc__
        """
        Convert the underlying int64 representation to the given unit.
        
                Parameters
                ----------
                unit : {"ns", "us", "ms", "s"}
                round_ok : bool, default True
                    If False and the conversion requires rounding, raise.
        
                Returns
                -------
                Timedelta
        
                Examples
                --------
                >>> td = pd.Timedelta('1001ms')
                >>> td
                Timedelta('0 days 00:00:01.001000')
                >>> td.as_unit('s')
                Timedelta('0 days 00:00:01')
        """
        pass

    def isoformat(self): # real signature unknown; restored from __doc__
        """
        Format the Timedelta as ISO 8601 Duration.
        
                ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``, where the ``[n]`` s are replaced by the
                values. See https://en.wikipedia.org/wiki/ISO_8601#Durations.
        
                Returns
                -------
                str
        
                See Also
                --------
                Timestamp.isoformat : Function is used to convert the given
                    Timestamp object into the ISO format.
        
                Notes
                -----
                The longest component is days, whose value may be larger than
                365.
                Every component is always included, even if its value is 0.
                Pandas uses nanosecond precision, so up to 9 decimal places may
                be included in the seconds component.
                Trailing 0's are removed from the seconds component after the decimal.
                We do not 0 pad components, so it's `...T5H...`, not `...T05H...`
        
                Examples
                --------
                >>> td = pd.Timedelta(days=6, minutes=50, seconds=3,
                ...                   milliseconds=10, microseconds=10, nanoseconds=12)
        
                >>> td.isoformat()
                'P6DT0H50M3.010010012S'
                >>> pd.Timedelta(hours=1, seconds=10).isoformat()
                'P0DT1H0M10S'
                >>> pd.Timedelta(days=500.5).isoformat()
                'P500DT12H0M0S'
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

    def to_numpy(self): # real signature unknown; restored from __doc__
        """
        Convert the Timedelta to a NumPy timedelta64.
        
                This is an alias method for `Timedelta.to_timedelta64()`. The dtype and
                copy parameters are available here only for compatibility. Their values
                will not affect the return value.
        
                Returns
                -------
                numpy.timedelta64
        
                See Also
                --------
                Series.to_numpy : Similar method for Series.
        
                Examples
                --------
                >>> td = pd.Timedelta('3D')
                >>> td
                Timedelta('3 days 00:00:00')
                >>> td.to_numpy()
                numpy.timedelta64(259200000000000,'ns')
        """
        pass

    def to_pytimedelta(self): # real signature unknown; restored from __doc__
        """
        Convert a pandas Timedelta object into a python ``datetime.timedelta`` object.
        
                Timedelta objects are internally saved as numpy datetime64[ns] dtype.
                Use to_pytimedelta() to convert to object dtype.
        
                Returns
                -------
                datetime.timedelta or numpy.array of datetime.timedelta
        
                See Also
                --------
                to_timedelta : Convert argument to Timedelta type.
        
                Notes
                -----
                Any nanosecond resolution will be lost.
        
                Examples
                --------
                >>> td = pd.Timedelta('3D')
                >>> td
                Timedelta('3 days 00:00:00')
                >>> td.to_pytimedelta()
                datetime.timedelta(days=3)
        """
        pass

    def to_timedelta64(self): # real signature unknown; restored from __doc__
        """
        Return a numpy.timedelta64 object with 'ns' precision.
        
                Examples
                --------
                >>> td = pd.Timedelta('3D')
                >>> td
                Timedelta('3 days 00:00:00')
                >>> td.to_timedelta64()
                numpy.timedelta64(259200000000000,'ns')
        """
        pass

    def view(self, p_int): # real signature unknown; restored from __doc__
        """
        Array view compatibility.
        
                Parameters
                ----------
                dtype : str or dtype
                    The dtype to view the underlying data as.
        
                Examples
                --------
                >>> td = pd.Timedelta('3D')
                >>> td
                Timedelta('3 days 00:00:00')
                >>> td.view(int)
                259200000000000
        """
        pass

    @classmethod
    def _from_value_and_reso(cls, *args, **kwargs): # real signature unknown
        pass

    def _maybe_cast_to_matching_resos(self, *args, **kwargs): # real signature unknown
        """ If _resos do not match, cast to the higher resolution, raising on overflow. """
        pass

    def _repr_base(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                format : None|all|sub_day|long
        
                Returns
                -------
                converted : string of a Timedelta
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a numpy timedelta64 array scalar view.

        Provides access to the array scalar view (i.e. a combination of the
        value and the units) associated with the numpy.timedelta64().view(),
        including a 64-bit integer representation of the timedelta in
        nanoseconds (Python int compatible).

        Returns
        -------
        numpy timedelta64 array scalar view
            Array scalar view of the timedelta in nanoseconds.

        Examples
        --------
        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')
        >>> td.asm8
        numpy.timedelta64(86520000003042,'ns')

        >>> td = pd.Timedelta('2 min 3 s')
        >>> td.asm8
        numpy.timedelta64(123000000000,'ns')

        >>> td = pd.Timedelta('3 ms 5 us')
        >>> td.asm8
        numpy.timedelta64(3005000,'ns')

        >>> td = pd.Timedelta(42, unit='ns')
        >>> td.asm8
        numpy.timedelta64(42,'ns')
        """

    components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a components namedtuple-like.

        Examples
        --------
        >>> td = pd.Timedelta('2 day 4 min 3 us 42 ns')
        >>> td.components
        Components(days=2, hours=0, minutes=4, seconds=0, milliseconds=0,
            microseconds=3, nanoseconds=42)
        """

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns the days of the timedelta.

        Returns
        -------
        int

        Examples
        --------
        >>> td = pd.Timedelta(1, "d")
        >>> td.days
        1

        >>> td = pd.Timedelta('4 min 3 us 42 ns')
        >>> td.days
        0
        """

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of nanoseconds (n), where 0 <= n < 1 microsecond.

        Returns
        -------
        int
            Number of nanoseconds.

        See Also
        --------
        Timedelta.components : Return all attributes with assigned values
            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,
            nanoseconds).

        Examples
        --------
        **Using string input**

        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')

        >>> td.nanoseconds
        42

        **Using integer input**

        >>> td = pd.Timedelta(42, unit='ns')
        >>> td.nanoseconds
        42
        """

    resolution_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a string representing the lowest timedelta resolution.

        Each timedelta has a defined resolution that represents the lowest OR
        most granular level of precision. Each level of resolution is
        represented by a short string as defined below:

        Resolution:     Return value

        * Days:         'D'
        * Hours:        'h'
        * Minutes:      'min'
        * Seconds:      's'
        * Milliseconds: 'ms'
        * Microseconds: 'us'
        * Nanoseconds:  'ns'

        Returns
        -------
        str
            Timedelta resolution.

        Examples
        --------
        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')
        >>> td.resolution_string
        'ns'

        >>> td = pd.Timedelta('1 days 2 min 3 us')
        >>> td.resolution_string
        'us'

        >>> td = pd.Timedelta('2 min 3 s')
        >>> td.resolution_string
        's'

        >>> td = pd.Timedelta(36, unit='us')
        >>> td.resolution_string
        'us'
        """

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the total hours, minutes, and seconds of the timedelta as seconds.

        Timedelta.seconds = hours * 3600 + minutes * 60 + seconds.

        Returns
        -------
        int
            Number of seconds.

        See Also
        --------
        Timedelta.components : Return all attributes with assigned values
            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,
            nanoseconds).
        Timedelta.total_seconds : Express the Timedelta as total number of seconds.

        Examples
        --------
        **Using string input**

        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')
        >>> td.seconds
        120

        **Using integer input**

        >>> td = pd.Timedelta(42, unit='s')
        >>> td.seconds
        42
        """

    unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _creso = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _h = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_populated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _s = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The abbreviation associated with self._creso.
        """

    _us = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = Timedelta('106751 days 23:47:16.854775807')
    min = Timedelta('-106752 days +00:12:43.145224193')
    resolution = Timedelta('0 days 00:00:00.000000001')
    __array_priority__ = 100
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000019CFEF06D40>'


class Timedelta(_Timedelta):
    """
    Represents a duration, the difference between two dates or times.
    
        Timedelta is the pandas equivalent of python's ``datetime.timedelta``
        and is interchangeable with it in most cases.
    
        Parameters
        ----------
        value : Timedelta, timedelta, np.timedelta64, str, or int
        unit : str, default 'ns'
            Denote the unit of the input, if input is an integer.
    
            Possible values:
    
            * 'W', or 'D'
            * 'days', or 'day'
            * 'hours', 'hour', 'hr', or 'h'
            * 'minutes', 'minute', 'min', or 'm'
            * 'seconds', 'second', 'sec', or 's'
            * 'milliseconds', 'millisecond', 'millis', 'milli', or 'ms'
            * 'microseconds', 'microsecond', 'micros', 'micro', or 'us'
            * 'nanoseconds', 'nanosecond', 'nanos', 'nano', or 'ns'.
    
            .. deprecated:: 2.2.0
    
                Values `H`, `T`, `S`, `L`, `U`, and `N` are deprecated in favour
                of the values `h`, `min`, `s`, `ms`, `us`, and `ns`.
    
        **kwargs
            Available kwargs: {days, seconds, microseconds,
            milliseconds, minutes, hours, weeks}.
            Values for construction in compat with datetime.timedelta.
            Numpy ints and floats will be coerced to python ints and floats.
    
        Notes
        -----
        The constructor may take in either both values of value and unit or
        kwargs as above. Either one of them must be used during initialization
    
        The ``.value`` attribute is always in ns.
    
        If the precision is higher than nanoseconds, the precision of the duration is
        truncated to nanoseconds.
    
        Examples
        --------
        Here we initialize Timedelta object with both value and unit
    
        >>> td = pd.Timedelta(1, "d")
        >>> td
        Timedelta('1 days 00:00:00')
    
        Here we initialize the Timedelta object with kwargs
    
        >>> td2 = pd.Timedelta(days=1)
        >>> td2
        Timedelta('1 days 00:00:00')
    
        We see that either way we get the same result
    """
    def ceil(self, s): # real signature unknown; restored from __doc__
        """
        Return a new Timedelta ceiled to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the ceiling resolution.
                    It uses the same units as class constructor :class:`~pandas.Timedelta`.
        
                Examples
                --------
                >>> td = pd.Timedelta('1001ms')
                >>> td
                Timedelta('0 days 00:00:01.001000')
                >>> td.ceil('s')
                Timedelta('0 days 00:00:02')
        """
        pass

    def floor(self, s): # real signature unknown; restored from __doc__
        """
        Return a new Timedelta floored to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the flooring resolution.
                    It uses the same units as class constructor :class:`~pandas.Timedelta`.
        
                Examples
                --------
                >>> td = pd.Timedelta('1001ms')
                >>> td
                Timedelta('0 days 00:00:01.001000')
                >>> td.floor('s')
                Timedelta('0 days 00:00:01')
        """
        pass

    def round(self, s): # real signature unknown; restored from __doc__
        """
        Round the Timedelta to the specified resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the rounding resolution.
                    It uses the same units as class constructor :class:`~pandas.Timedelta`.
        
                Returns
                -------
                a new Timedelta rounded to the given resolution of `freq`
        
                Raises
                ------
                ValueError if the freq cannot be converted
        
                Examples
                --------
                >>> td = pd.Timedelta('1001ms')
                >>> td
                Timedelta('0 days 00:00:01.001000')
                >>> td.round('s')
                Timedelta('0 days 00:00:01')
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _req_any_kwargs_new = None # (!) real value is "{'hours', 'seconds', 'microseconds', 'weeks', 'milliseconds', 'days', 'nanoseconds', 'minutes'}"
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.timedeltas\', \'__doc__\': \'\\n    Represents a duration, the difference between two dates or times.\\n\\n    Timedelta is the pandas equivalent of python\\\'s ``datetime.timedelta``\\n    and is interchangeable with it in most cases.\\n\\n    Parameters\\n    ----------\\n    value : Timedelta, timedelta, np.timedelta64, str, or int\\n    unit : str, default \\\'ns\\\'\\n        Denote the unit of the input, if input is an integer.\\n\\n        Possible values:\\n\\n        * \\\'W\\\', or \\\'D\\\'\\n        * \\\'days\\\', or \\\'day\\\'\\n        * \\\'hours\\\', \\\'hour\\\', \\\'hr\\\', or \\\'h\\\'\\n        * \\\'minutes\\\', \\\'minute\\\', \\\'min\\\', or \\\'m\\\'\\n        * \\\'seconds\\\', \\\'second\\\', \\\'sec\\\', or \\\'s\\\'\\n        * \\\'milliseconds\\\', \\\'millisecond\\\', \\\'millis\\\', \\\'milli\\\', or \\\'ms\\\'\\n        * \\\'microseconds\\\', \\\'microsecond\\\', \\\'micros\\\', \\\'micro\\\', or \\\'us\\\'\\n        * \\\'nanoseconds\\\', \\\'nanosecond\\\', \\\'nanos\\\', \\\'nano\\\', or \\\'ns\\\'.\\n\\n        .. deprecated:: 2.2.0\\n\\n            Values `H`, `T`, `S`, `L`, `U`, and `N` are deprecated in favour\\n            of the values `h`, `min`, `s`, `ms`, `us`, and `ns`.\\n\\n    **kwargs\\n        Available kwargs: {days, seconds, microseconds,\\n        milliseconds, minutes, hours, weeks}.\\n        Values for construction in compat with datetime.timedelta.\\n        Numpy ints and floats will be coerced to python ints and floats.\\n\\n    Notes\\n    -----\\n    The constructor may take in either both values of value and unit or\\n    kwargs as above. Either one of them must be used during initialization\\n\\n    The ``.value`` attribute is always in ns.\\n\\n    If the precision is higher than nanoseconds, the precision of the duration is\\n    truncated to nanoseconds.\\n\\n    Examples\\n    --------\\n    Here we initialize Timedelta object with both value and unit\\n\\n    >>> td = pd.Timedelta(1, "d")\\n    >>> td\\n    Timedelta(\\\'1 days 00:00:00\\\')\\n\\n    Here we initialize the Timedelta object with kwargs\\n\\n    >>> td2 = pd.Timedelta(days=1)\\n    >>> td2\\n    Timedelta(\\\'1 days 00:00:00\\\')\\n\\n    We see that either way we get the same result\\n    \', \'_req_any_kwargs_new\': {\'hours\', \'seconds\', \'microseconds\', \'weeks\', \'milliseconds\', \'days\', \'nanoseconds\', \'minutes\'}, \'__new__\': <staticmethod(<cyfunction Timedelta.__new__ at 0x0000019CFEFA65C0>)>, \'__setstate__\': <cyfunction Timedelta.__setstate__ at 0x0000019CFEFA6680>, \'__reduce__\': <cyfunction Timedelta.__reduce__ at 0x0000019CFEFA6740>, \'_round\': <cyfunction Timedelta._round at 0x0000019CFEFA6800>, \'round\': <cyfunction Timedelta.round at 0x0000019CFEFA68C0>, \'floor\': <cyfunction Timedelta.floor at 0x0000019CFEFA6980>, \'ceil\': <cyfunction Timedelta.ceil at 0x0000019CFEFA6A40>, \'__neg__\': <cyfunction _op_unary_method.<locals>.f at 0x0000019CFEFA6BC0>, \'__pos__\': <cyfunction _op_unary_method.<locals>.f at 0x0000019CFEFA6D40>, \'__abs__\': <cyfunction _op_unary_method.<locals>.f at 0x0000019CFEFA6EC0>, \'__add__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x0000019CFEFA7040>, \'__radd__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x0000019CFEFA71C0>, \'__sub__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x0000019CFEFA7340>, \'__rsub__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x0000019CFEFA74C0>, \'__mul__\': <cyfunction Timedelta.__mul__ at 0x0000019CFEFA7580>, \'__rmul__\': <cyfunction Timedelta.__mul__ at 0x0000019CFEFA7580>, \'__truediv__\': <cyfunction Timedelta.__truediv__ at 0x0000019CFEFA7640>, \'__rtruediv__\': <cyfunction Timedelta.__rtruediv__ at 0x0000019CFEFA7700>, \'__floordiv__\': <cyfunction Timedelta.__floordiv__ at 0x0000019CFEFA77C0>, \'__rfloordiv__\': <cyfunction Timedelta.__rfloordiv__ at 0x0000019CFEFA7880>, \'__mod__\': <cyfunction Timedelta.__mod__ at 0x0000019CFEFA7940>, \'__rmod__\': <cyfunction Timedelta.__rmod__ at 0x0000019CFEFA7A00>, \'__divmod__\': <cyfunction Timedelta.__divmod__ at 0x0000019CFEFA7AC0>, \'__rdivmod__\': <cyfunction Timedelta.__rdivmod__ at 0x0000019CFEFA7B80>, \'__dict__\': <attribute \'__dict__\' of \'Timedelta\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Timedelta\' objects>})'


# variables with complex values

_no_input = None # (!) real value is '<object object at 0x0000019CF7EE2E70>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019CFEEE82F0>'

__pyx_capi__ = {
    'convert_to_timedelta64': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x0000019CFEF065C0>'
    'delta_to_nanoseconds': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10timedeltas_delta_to_nanoseconds *__pyx_optional_args)" at 0x0000019CFEF06570>'
    'get_unit_for_round': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, NPY_DATETIMEUNIT, int __pyx_skip_dispatch)" at 0x0000019CFEF06520>'
    'is_any_td_scalar': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000019CFEF06610>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.timedeltas', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019CFEEE82F0>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\timedeltas.cp313-win_amd64.pyd')"

__test__ = {
    'Timedelta.ceil (line 1993)': "\n        Return a new Timedelta ceiled to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the ceiling resolution.\n            It uses the same units as class constructor :class:`~pandas.Timedelta`.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1001ms')\n        >>> td\n        Timedelta('0 days 00:00:01.001000')\n        >>> td.ceil('s')\n        Timedelta('0 days 00:00:02')\n        ",
    'Timedelta.floor (line 1973)': "\n        Return a new Timedelta floored to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the flooring resolution.\n            It uses the same units as class constructor :class:`~pandas.Timedelta`.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1001ms')\n        >>> td\n        Timedelta('0 days 00:00:01.001000')\n        >>> td.floor('s')\n        Timedelta('0 days 00:00:01')\n        ",
    'Timedelta.round (line 1945)': "\n        Round the Timedelta to the specified resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the rounding resolution.\n            It uses the same units as class constructor :class:`~pandas.Timedelta`.\n\n        Returns\n        -------\n        a new Timedelta rounded to the given resolution of `freq`\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1001ms')\n        >>> td\n        Timedelta('0 days 00:00:01.001000')\n        >>> td.round('s')\n        Timedelta('0 days 00:00:01')\n        ",
    '_Timedelta.as_unit (line 1647)': '\n        Convert the underlying int64 representation to the given unit.\n\n        Parameters\n        ----------\n        unit : {"ns", "us", "ms", "s"}\n        round_ok : bool, default True\n            If False and the conversion requires rounding, raise.\n\n        Returns\n        -------\n        Timedelta\n\n        Examples\n        --------\n        >>> td = pd.Timedelta(\'1001ms\')\n        >>> td\n        Timedelta(\'0 days 00:00:01.001000\')\n        >>> td.as_unit(\'s\')\n        Timedelta(\'0 days 00:00:01\')\n        ',
    '_Timedelta.asm8.__get__ (line 1401)': "\n        Return a numpy timedelta64 array scalar view.\n\n        Provides access to the array scalar view (i.e. a combination of the\n        value and the units) associated with the numpy.timedelta64().view(),\n        including a 64-bit integer representation of the timedelta in\n        nanoseconds (Python int compatible).\n\n        Returns\n        -------\n        numpy timedelta64 array scalar view\n            Array scalar view of the timedelta in nanoseconds.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.asm8\n        numpy.timedelta64(86520000003042,'ns')\n\n        >>> td = pd.Timedelta('2 min 3 s')\n        >>> td.asm8\n        numpy.timedelta64(123000000000,'ns')\n\n        >>> td = pd.Timedelta('3 ms 5 us')\n        >>> td.asm8\n        numpy.timedelta64(3005000,'ns')\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.asm8\n        numpy.timedelta64(42,'ns')\n        ",
    '_Timedelta.components.__get__ (line 1384)': "\n        Return a components namedtuple-like.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('2 day 4 min 3 us 42 ns')\n        >>> td.components\n        Components(days=2, hours=0, minutes=4, seconds=0, milliseconds=0,\n            microseconds=3, nanoseconds=42)\n        ",
    '_Timedelta.days.__get__ (line 1057)': '\n        Returns the days of the timedelta.\n\n        Returns\n        -------\n        int\n\n        Examples\n        --------\n        >>> td = pd.Timedelta(1, "d")\n        >>> td.days\n        1\n\n        >>> td = pd.Timedelta(\'4 min 3 us 42 ns\')\n        >>> td.days\n        0\n        ',
    '_Timedelta.isoformat (line 1590)': "\n        Format the Timedelta as ISO 8601 Duration.\n\n        ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``, where the ``[n]`` s are replaced by the\n        values. See https://en.wikipedia.org/wiki/ISO_8601#Durations.\n\n        Returns\n        -------\n        str\n\n        See Also\n        --------\n        Timestamp.isoformat : Function is used to convert the given\n            Timestamp object into the ISO format.\n\n        Notes\n        -----\n        The longest component is days, whose value may be larger than\n        365.\n        Every component is always included, even if its value is 0.\n        Pandas uses nanosecond precision, so up to 9 decimal places may\n        be included in the seconds component.\n        Trailing 0's are removed from the seconds component after the decimal.\n        We do not 0 pad components, so it's `...T5H...`, not `...T05H...`\n\n        Examples\n        --------\n        >>> td = pd.Timedelta(days=6, minutes=50, seconds=3,\n        ...                   milliseconds=10, microseconds=10, nanoseconds=12)\n\n        >>> td.isoformat()\n        'P6DT0H50M3.010010012S'\n        >>> pd.Timedelta(hours=1, seconds=10).isoformat()\n        'P0DT1H0M10S'\n        >>> pd.Timedelta(days=500.5).isoformat()\n        'P500DT12H0M0S'\n        ",
    '_Timedelta.nanoseconds.__get__ (line 1494)': "\n        Return the number of nanoseconds (n), where 0 <= n < 1 microsecond.\n\n        Returns\n        -------\n        int\n            Number of nanoseconds.\n\n        See Also\n        --------\n        Timedelta.components : Return all attributes with assigned values\n            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,\n            nanoseconds).\n\n        Examples\n        --------\n        **Using string input**\n\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n\n        >>> td.nanoseconds\n        42\n\n        **Using integer input**\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.nanoseconds\n        42\n        ",
    '_Timedelta.resolution_string.__get__ (line 1436)': "\n        Return a string representing the lowest timedelta resolution.\n\n        Each timedelta has a defined resolution that represents the lowest OR\n        most granular level of precision. Each level of resolution is\n        represented by a short string as defined below:\n\n        Resolution:     Return value\n\n        * Days:         'D'\n        * Hours:        'h'\n        * Minutes:      'min'\n        * Seconds:      's'\n        * Milliseconds: 'ms'\n        * Microseconds: 'us'\n        * Nanoseconds:  'ns'\n\n        Returns\n        -------\n        str\n            Timedelta resolution.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.resolution_string\n        'ns'\n\n        >>> td = pd.Timedelta('1 days 2 min 3 us')\n        >>> td.resolution_string\n        'us'\n\n        >>> td = pd.Timedelta('2 min 3 s')\n        >>> td.resolution_string\n        's'\n\n        >>> td = pd.Timedelta(36, unit='us')\n        >>> td.resolution_string\n        'us'\n        ",
    '_Timedelta.seconds.__get__ (line 1081)': "\n        Return the total hours, minutes, and seconds of the timedelta as seconds.\n\n        Timedelta.seconds = hours * 3600 + minutes * 60 + seconds.\n\n        Returns\n        -------\n        int\n            Number of seconds.\n\n        See Also\n        --------\n        Timedelta.components : Return all attributes with assigned values\n            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,\n            nanoseconds).\n        Timedelta.total_seconds : Express the Timedelta as total number of seconds.\n\n        Examples\n        --------\n        **Using string input**\n\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.seconds\n        120\n\n        **Using integer input**\n\n        >>> td = pd.Timedelta(42, unit='s')\n        >>> td.seconds\n        42\n        ",
    '_Timedelta.to_numpy (line 1335)': "\n        Convert the Timedelta to a NumPy timedelta64.\n\n        This is an alias method for `Timedelta.to_timedelta64()`. The dtype and\n        copy parameters are available here only for compatibility. Their values\n        will not affect the return value.\n\n        Returns\n        -------\n        numpy.timedelta64\n\n        See Also\n        --------\n        Series.to_numpy : Similar method for Series.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('3D')\n        >>> td\n        Timedelta('3 days 00:00:00')\n        >>> td.to_numpy()\n        numpy.timedelta64(259200000000000,'ns')\n        ",
    '_Timedelta.to_pytimedelta (line 1281)': "\n        Convert a pandas Timedelta object into a python ``datetime.timedelta`` object.\n\n        Timedelta objects are internally saved as numpy datetime64[ns] dtype.\n        Use to_pytimedelta() to convert to object dtype.\n\n        Returns\n        -------\n        datetime.timedelta or numpy.array of datetime.timedelta\n\n        See Also\n        --------\n        to_timedelta : Convert argument to Timedelta type.\n\n        Notes\n        -----\n        Any nanosecond resolution will be lost.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('3D')\n        >>> td\n        Timedelta('3 days 00:00:00')\n        >>> td.to_pytimedelta()\n        datetime.timedelta(days=3)\n        ",
    '_Timedelta.to_timedelta64 (line 1317)': "\n        Return a numpy.timedelta64 object with 'ns' precision.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('3D')\n        >>> td\n        Timedelta('3 days 00:00:00')\n        >>> td.to_timedelta64()\n        numpy.timedelta64(259200000000000,'ns')\n        ",
    '_Timedelta.total_seconds (line 1126)': "\n        Total seconds in the duration.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1min')\n        >>> td\n        Timedelta('0 days 00:01:00')\n        >>> td.total_seconds()\n        60.0\n        ",
    '_Timedelta.view (line 1365)': "\n        Array view compatibility.\n\n        Parameters\n        ----------\n        dtype : str or dtype\n            The dtype to view the underlying data as.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('3D')\n        >>> td\n        Timedelta('3 days 00:00:00')\n        >>> td.view(int)\n        259200000000000\n        ",
}

