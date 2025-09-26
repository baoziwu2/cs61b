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


# Variables with simple values

INVALID_FREQ_ERR_MSG = 'Invalid frequency: {0}'

# functions

def apply_wraps(*args, **kwargs): # real signature unknown
    pass

def delta_to_tick(*args, **kwargs): # real signature unknown
    pass

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

def roll_convention(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : int, generally the day component of a datetime
        n : number of periods to increment, before adjusting for rolling
        compare : int, generally the day component of a datetime, in the same
                  month as the datetime form which `other` was taken.
    
        Returns
        -------
        n : int number of periods to increment
    """
    pass

def roll_qtrday(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : datetime or Timestamp
        n : number of periods to increment, before adjusting for rolling
        month : int reference month giving the first month of the year
        day_opt : {'start', 'end', 'business_start', 'business_end'}
            The convention to use in finding the day in a given month against
            which to compare for rollforward/rollbackward decisions.
        modby : int 3 for quarters, 12 for years
    
        Returns
        -------
        n : int number of periods to increment
    
        See Also
        --------
        get_day_of_month : Find the day in a month provided an offset.
    """
    pass

def shift_month(*args, **kwargs): # real signature unknown
    """
    Given a datetime (or Timestamp) `stamp`, an integer `months` and an
        option `day_opt`, return a new datetimelike that many months later,
        with day determined by `day_opt` using relativedelta semantics.
    
        Scalar analogue of shift_months.
    
        Parameters
        ----------
        stamp : datetime or Timestamp
        months : int
        day_opt : None, 'start', 'end', 'business_start', 'business_end', or int
            None: returned datetimelike has the same day as the input, or the
                  last day of the month if the new month is too short
            'start': returned datetimelike has day=1
            'end': returned datetimelike has day on the last day of the month
            'business_start': returned datetimelike has day on the first
                business day of the month
            'business_end': returned datetimelike has day on the last
                business day of the month
            int: returned datetimelike has day equal to day_opt
    
        Returns
        -------
        shifted : datetime or Timestamp (same as input `stamp`)
    """
    pass

def shift_months(*args, **kwargs): # real signature unknown
    """
    Given an int64-based datetime index, shift all elements
        specified number of months using DateOffset semantics
    
        day_opt: {None, 'start', 'end', 'business_start', 'business_end'}
           * None: day of month
           * 'start' 1st day of month
           * 'end' last day of month
    """
    pass

def to_offset(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return DateOffset object from string or datetime.timedelta object.
    
        Parameters
        ----------
        freq : str, datetime.timedelta, BaseOffset or None
    
        Returns
        -------
        BaseOffset subclass or None
    
        Raises
        ------
        ValueError
            If freq is an invalid frequency
    
        See Also
        --------
        BaseOffset : Standard kind of date increment used for a date range.
    
        Examples
        --------
        >>> from pandas.tseries.frequencies import to_offset
        >>> to_offset("5min")
        <5 * Minutes>
    
        >>> to_offset("1D1h")
        <25 * Hours>
    
        >>> to_offset("2W")
        <2 * Weeks: weekday=6>
    
        >>> to_offset("2B")
        <2 * BusinessDays>
    
        >>> to_offset(pd.Timedelta(days=1))
        <Day>
    
        >>> to_offset(pd.offsets.Hour())
        <Hour>
    """
    pass

def _get_offset(EOM): # real signature unknown; restored from __doc__
    """
    Return DateOffset object associated with rule name.
    
        Examples
        --------
        _get_offset('EOM') --> BMonthEnd(1)
    """
    pass

def __pyx_unpickle_BaseOffset(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_RelativeDeltaOffset(*args, **kwargs): # real signature unknown
    pass

# classes

from .ApplyTypeError import ApplyTypeError
from .BaseOffset import BaseOffset
from .SingleConstructorOffset import SingleConstructorOffset
from .BusinessMixin import BusinessMixin
from .BusinessDay import BusinessDay
from .BDay import BDay
from .MonthOffset import MonthOffset
from .BusinessMonthBegin import BusinessMonthBegin
from .BMonthBegin import BMonthBegin
from .BusinessMonthEnd import BusinessMonthEnd
from .BMonthEnd import BMonthEnd
from .QuarterOffset import QuarterOffset
from .BQuarterBegin import BQuarterBegin
from .BQuarterEnd import BQuarterEnd
from .BusinessHour import BusinessHour
from .YearOffset import YearOffset
from .BYearBegin import BYearBegin
from .BYearEnd import BYearEnd
from ._CustomBusinessMonth import _CustomBusinessMonth
from .CustomBusinessMonthBegin import CustomBusinessMonthBegin
from .CBMonthBegin import CBMonthBegin
from .CustomBusinessMonthEnd import CustomBusinessMonthEnd
from .CBMonthEnd import CBMonthEnd
from .CustomBusinessDay import CustomBusinessDay
from .CDay import CDay
from .CustomBusinessHour import CustomBusinessHour
from .RelativeDeltaOffset import RelativeDeltaOffset
from .DateOffset import DateOffset
from .Tick import Tick
from .Day import Day
from .Easter import Easter
from .FY5253Mixin import FY5253Mixin
from .FY5253 import FY5253
from .FY5253Quarter import FY5253Quarter
from .Hour import Hour
from .WeekOfMonthMixin import WeekOfMonthMixin
from .LastWeekOfMonth import LastWeekOfMonth
from .Micro import Micro
from .Milli import Milli
from .Minute import Minute
from .MonthBegin import MonthBegin
from .MonthEnd import MonthEnd
from .Nano import Nano
from .OffsetMeta import OffsetMeta
from .QuarterBegin import QuarterBegin
from .QuarterEnd import QuarterEnd
from .Second import Second
from .SemiMonthOffset import SemiMonthOffset
from .SemiMonthBegin import SemiMonthBegin
from .SemiMonthEnd import SemiMonthEnd
from .Week import Week
from .WeekOfMonth import WeekOfMonth
from .YearBegin import YearBegin
from .YearEnd import YearEnd
# variables with complex values

int_to_weekday = {
    0: 'MON',
    1: 'TUE',
    2: 'WED',
    3: 'THU',
    4: 'FRI',
    5: 'SAT',
    6: 'SUN',
}

MONTH_ALIASES = {
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUN',
    7: 'JUL',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC',
}

opattern = None # (!) real value is "re.compile('([+\\\\-]?\\\\d*|[+\\\\-]?\\\\d*\\\\.\\\\d*)\\\\s*([A-Za-z]+([\\\\-][\\\\dA-Za-z\\\\-]+)?)')"

prefix_mapping = {
    'B': BusinessDay,
    'BME': BusinessMonthEnd,
    'BMS': BusinessMonthBegin,
    'BQE': BQuarterEnd,
    'BQS': BQuarterBegin,
    'BYE': BYearEnd,
    'BYS': BYearBegin,
    'C': CustomBusinessDay,
    'CBME': CustomBusinessMonthEnd,
    'CBMS': CustomBusinessMonthBegin,
    'D': Day,
    'ME': MonthEnd,
    'MS': MonthBegin,
    'QE': QuarterEnd,
    'QS': QuarterBegin,
    'RE': FY5253,
    'REQ': FY5253Quarter,
    'SME': SemiMonthEnd,
    'SMS': SemiMonthBegin,
    'W': Week,
    'WOM': WeekOfMonth,
    'YE': YearEnd,
    'YS': YearBegin,
    'bh': BusinessHour,
    'cbh': CustomBusinessHour,
    'h': Hour,
    'min': Minute,
    'ms': Milli,
    'ns': Nano,
    's': Second,
    'us': Micro,
}

weekday_to_int = {
    'FRI': 4,
    'MON': 0,
    'SAT': 5,
    'SUN': 6,
    'THU': 3,
    'TUE': 1,
    'WED': 2,
}

_dont_uppercase = None # (!) real value is "{'MS', 'bh', 'ms', 'h', 's', 'cbh'}"

_lite_rule_alias = {
    'BYE': 'BYE-DEC',
    'BYS': 'BYS-JAN',
    'Min': 'min',
    'QE': 'QE-DEC',
    'W': 'W-SUN',
    'YE': 'YE-DEC',
    'YS': 'YS-JAN',
    'min': 'min',
    'ms': 'ms',
    'ns': 'ns',
    'us': 'us',
}

_offset_map = {}

_relativedelta_kwds = None # (!) real value is "{'weekday', 'minute', 'hours', 'hour', 'milliseconds', 'microsecond', 'month', 'days', 'months', 'seconds', 'years', 'second', 'minutes', 'millisecond', 'nanosecond', 'microseconds', 'weeks', 'day', 'year', 'nanoseconds'}"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000236907CE030>'

__pyx_capi__ = {
    'is_offset_object': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000023690819490>'
    'is_tick_object': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x00000236908194E0>'
    'to_offset': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_7offsets_to_offset *__pyx_optional_args)" at 0x0000023690819440>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.offsets', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000236907CE030>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\offsets.cp313-win_amd64.pyd')"

__test__ = {
    'BaseOffset.copy (line 499)': '\n        Return a copy of the frequency.\n\n        Examples\n        --------\n        >>> freq = pd.DateOffset(1)\n        >>> freq_copy = freq.copy()\n        >>> freq is freq_copy\n        False\n        ',
    'BaseOffset.freqstr (line 574)': "\n        Return a string representing the frequency.\n\n        Examples\n        --------\n        >>> pd.DateOffset(5).freqstr\n        '<5 * DateOffsets>'\n\n        >>> pd.offsets.BusinessHour(2).freqstr\n        '2bh'\n\n        >>> pd.offsets.Nano().freqstr\n        'ns'\n\n        >>> pd.offsets.Nano(-3).freqstr\n        '-3ns'\n        ",
    'BaseOffset.is_anchored (line 758)': '\n        Return boolean whether the frequency is a unit frequency (n=1).\n\n        .. deprecated:: 2.2.0\n            is_anchored is deprecated and will be removed in a future version.\n            Use ``obj.n == 1`` instead.\n\n        Examples\n        --------\n        >>> pd.DateOffset().is_anchored()\n        True\n        >>> pd.DateOffset(2).is_anchored()\n        False\n        ',
    'BaseOffset.is_month_end (line 797)': '\n        Return boolean whether a timestamp occurs on the month end.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_month_end(ts)\n        False\n        ',
    'BaseOffset.is_month_start (line 784)': '\n        Return boolean whether a timestamp occurs on the month start.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_month_start(ts)\n        True\n        ',
    'BaseOffset.is_on_offset (line 664)': "\n        Return boolean whether a timestamp intersects with this frequency.\n\n        Parameters\n        ----------\n        dt : datetime.datetime\n            Timestamp to check intersections with frequency.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Day(1)\n        >>> freq.is_on_offset(ts)\n        True\n\n        >>> ts = pd.Timestamp(2022, 8, 6)\n        >>> ts.day_name()\n        'Saturday'\n        >>> freq = pd.offsets.BusinessDay(1)\n        >>> freq.is_on_offset(ts)\n        False\n        ",
    'BaseOffset.is_quarter_end (line 823)': '\n        Return boolean whether a timestamp occurs on the quarter end.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_quarter_end(ts)\n        False\n        ',
    'BaseOffset.is_quarter_start (line 810)': '\n        Return boolean whether a timestamp occurs on the quarter start.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_quarter_start(ts)\n        True\n        ',
    'BaseOffset.is_year_end (line 849)': '\n        Return boolean whether a timestamp occurs on the year end.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_year_end(ts)\n        False\n        ',
    'BaseOffset.is_year_start (line 836)': '\n        Return boolean whether a timestamp occurs on the year start.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_year_start(ts)\n        True\n        ',
    'BaseOffset.kwds.__get__ (line 429)': "\n        Return a dict of extra parameters for the offset.\n\n        Examples\n        --------\n        >>> pd.DateOffset(5).kwds\n        {}\n\n        >>> pd.offsets.FY5253Quarter().kwds\n        {'weekday': 0,\n         'startingMonth': 1,\n         'qtr_with_extra_week': 1,\n         'variation': 'nearest'}\n        ",
    'BaseOffset.name.__get__ (line 551)': "\n        Return a string representing the base frequency.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour().name\n        'h'\n\n        >>> pd.offsets.Hour(5).name\n        'h'\n        ",
    'Tick.is_anchored (line 965)': '\n        Return False.\n\n        .. deprecated:: 2.2.0\n            is_anchored is deprecated and will be removed in a future version.\n            Use ``False`` instead.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour().is_anchored()\n        False\n        >>> pd.offsets.Hour(2).is_anchored()\n        False\n        ',
    'Tick.nanos.__get__ (line 945)': '\n        Return an integer of the total number of nanoseconds.\n\n        Raises\n        ------\n        ValueError\n            If the frequency is non-fixed.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour(5).nanos\n        18000000000000\n        ',
    'to_offset (line 4791)': '\n    Return DateOffset object from string or datetime.timedelta object.\n\n    Parameters\n    ----------\n    freq : str, datetime.timedelta, BaseOffset or None\n\n    Returns\n    -------\n    BaseOffset subclass or None\n\n    Raises\n    ------\n    ValueError\n        If freq is an invalid frequency\n\n    See Also\n    --------\n    BaseOffset : Standard kind of date increment used for a date range.\n\n    Examples\n    --------\n    >>> from pandas.tseries.frequencies import to_offset\n    >>> to_offset("5min")\n    <5 * Minutes>\n\n    >>> to_offset("1D1h")\n    <25 * Hours>\n\n    >>> to_offset("2W")\n    <2 * Weeks: weekday=6>\n\n    >>> to_offset("2B")\n    <2 * BusinessDays>\n\n    >>> to_offset(pd.Timedelta(days=1))\n    <Day>\n\n    >>> to_offset(pd.offsets.Hour())\n    <Hour>\n    ',
}

