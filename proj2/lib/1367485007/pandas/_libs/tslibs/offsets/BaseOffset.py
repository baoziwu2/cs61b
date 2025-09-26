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


from .object import object

class BaseOffset(object):
    """
    Base class for DateOffset methods that are not overridden by subclasses.
    
        Parameters
        ----------
        n : int
            Number of multiples of the frequency.
    
        normalize : bool
            Whether the frequency can align with midnight.
    
        Examples
        --------
        >>> pd.offsets.Hour(5).n
        5
        >>> pd.offsets.Hour(5).normalize
        False
    """
    def copy(self): # real signature unknown; restored from __doc__
        """
        Return a copy of the frequency.
        
                Examples
                --------
                >>> freq = pd.DateOffset(1)
                >>> freq_copy = freq.copy()
                >>> freq is freq_copy
                False
        """
        pass

    def is_anchored(self): # real signature unknown; restored from __doc__
        """
        Return boolean whether the frequency is a unit frequency (n=1).
        
                .. deprecated:: 2.2.0
                    is_anchored is deprecated and will be removed in a future version.
                    Use ``obj.n == 1`` instead.
        
                Examples
                --------
                >>> pd.DateOffset().is_anchored()
                True
                >>> pd.DateOffset(2).is_anchored()
                False
        """
        pass

    def is_month_end(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the month end.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_month_end(ts)
                False
        """
        pass

    def is_month_start(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the month start.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_month_start(ts)
                True
        """
        pass

    def is_on_offset(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp intersects with this frequency.
        
                Parameters
                ----------
                dt : datetime.datetime
                    Timestamp to check intersections with frequency.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Day(1)
                >>> freq.is_on_offset(ts)
                True
        
                >>> ts = pd.Timestamp(2022, 8, 6)
                >>> ts.day_name()
                'Saturday'
                >>> freq = pd.offsets.BusinessDay(1)
                >>> freq.is_on_offset(ts)
                False
        """
        pass

    def is_quarter_end(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the quarter end.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_quarter_end(ts)
                False
        """
        pass

    def is_quarter_start(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the quarter start.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_quarter_start(ts)
                True
        """
        pass

    def is_year_end(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the year end.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_year_end(ts)
                False
        """
        pass

    def is_year_start(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the year start.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_year_start(ts)
                True
        """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """
        Roll provided date backward to next offset only if not on offset.
        
                Returns
                -------
                TimeStamp
                    Rolled timestamp if not on offset, otherwise unchanged timestamp.
        """
        pass

    def rollforward(self, *args, **kwargs): # real signature unknown
        """
        Roll provided date forward to next offset only if not on offset.
        
                Returns
                -------
                TimeStamp
                    Rolled timestamp if not on offset, otherwise unchanged timestamp.
        """
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def _get_offset_day(self, *args, **kwargs): # real signature unknown
        pass

    def _offset_str(self, *args, **kwargs): # real signature unknown
        pass

    def _repr_attrs(self, *args, **kwargs): # real signature unknown
        pass

    def _validate_n(self, *args, **kwargs): # real signature unknown
        """
        Require that `n` be an integer.
        
                Parameters
                ----------
                n : int
        
                Returns
                -------
                nint : int
        
                Raises
                ------
                TypeError if `int(n)` raises
                ValueError if n != int(n)
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Return a pickleable state """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Reconstruct an instance from a pickled state """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns a copy of the calling offset object with n=1 and all other
        attributes equal.
        """

    kwds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a dict of extra parameters for the offset.

        Examples
        --------
        >>> pd.DateOffset(5).kwds
        {}

        >>> pd.offsets.FY5253Quarter().kwds
        {'weekday': 0,
         'startingMonth': 1,
         'qtr_with_extra_week': 1,
         'variation': 'nearest'}
        """

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a string representing the base frequency.

        Examples
        --------
        >>> pd.offsets.Hour().name
        'h'

        >>> pd.offsets.Hour(5).name
        'h'
        """

    nanos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    normalize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    freqstr = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x00000236907FF880>'
    _adjust_dst = True
    _attributes = (
        'n',
        'normalize',
    )
    _day_opt = None
    _params = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x00000236907FD7C0>'
    _use_relativedelta = False
    __array_priority__ = 1000


