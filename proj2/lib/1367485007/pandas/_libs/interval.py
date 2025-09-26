# encoding: utf-8
# module pandas._libs.interval
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\interval.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numbers as numbers # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\numbers.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
from pandas._libs.algos import is_monotonic

from _operator import le, lt


# functions

def intervals_to_interval_bounds(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        intervals : ndarray
            Object array of Intervals / nulls.
    
        validate_closed: bool, default True
            Boolean indicating if all intervals must be closed on the same side.
            Mismatching closed will raise if True, else return None for closed.
    
        Returns
        -------
        tuple of
            left : ndarray
            right : ndarray
            closed: IntervalClosedType
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IntervalMixin(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IntervalTree(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uint64ClosedBothIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uint64ClosedLeftIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uint64ClosedNeitherIntervalNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uint64ClosedRightIntervalNode(*args, **kwargs): # real signature unknown
    pass

# classes

class IntervalMixin(object):
    # no doc
    def _check_closed_matches(self, *args, **kwargs): # real signature unknown
        """
        Check if the closed attribute of `other` matches.
        
                Note that 'left' and 'right' are considered different from 'both'.
        
                Parameters
                ----------
                other : Interval, IntervalIndex, IntervalArray
                name : str
                    Name to use for 'other' in the error message.
        
                Raises
                ------
                ValueError
                    When `other` is not closed exactly the same as self.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    closed_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the interval is closed on the left side.

        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.

        Returns
        -------
        bool
            True if the Interval is closed on the left-side.

        See Also
        --------
        Interval.closed_right : Check if the interval is closed on the right side.
        Interval.open_left : Boolean inverse of closed_left.

        Examples
        --------
        >>> iv = pd.Interval(0, 5, closed='left')
        >>> iv.closed_left
        True

        >>> iv = pd.Interval(0, 5, closed='right')
        >>> iv.closed_left
        False
        """

    closed_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the interval is closed on the right side.

        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.

        Returns
        -------
        bool
            True if the Interval is closed on the left-side.

        See Also
        --------
        Interval.closed_left : Check if the interval is closed on the left side.
        Interval.open_right : Boolean inverse of closed_right.

        Examples
        --------
        >>> iv = pd.Interval(0, 5, closed='both')
        >>> iv.closed_right
        True

        >>> iv = pd.Interval(0, 5, closed='left')
        >>> iv.closed_right
        False
        """

    is_empty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Indicates if an interval is empty, meaning it contains no points.

        Returns
        -------
        bool or ndarray
            A boolean indicating if a scalar :class:`Interval` is empty, or a
            boolean ``ndarray`` positionally indicating if an ``Interval`` in
            an :class:`~arrays.IntervalArray` or :class:`IntervalIndex` is
            empty.

        See Also
        --------
        Interval.length : Return the length of the Interval.

        Examples
        --------
        An :class:`Interval` that contains points is not empty:

        >>> pd.Interval(0, 1, closed='right').is_empty
        False

        An ``Interval`` that does not contain any points is empty:

        >>> pd.Interval(0, 0, closed='right').is_empty
        True
        >>> pd.Interval(0, 0, closed='left').is_empty
        True
        >>> pd.Interval(0, 0, closed='neither').is_empty
        True

        An ``Interval`` that contains a single point is not empty:

        >>> pd.Interval(0, 0, closed='both').is_empty
        False

        An :class:`~arrays.IntervalArray` or :class:`IntervalIndex` returns a
        boolean ``ndarray`` positionally indicating if an ``Interval`` is
        empty:

        >>> ivs = [pd.Interval(0, 0, closed='neither'),
        ...        pd.Interval(1, 2, closed='neither')]
        >>> pd.arrays.IntervalArray(ivs).is_empty
        array([ True, False])

        Missing values are not considered empty:

        >>> ivs = [pd.Interval(0, 0, closed='neither'), np.nan]
        >>> pd.IntervalIndex(ivs).is_empty
        array([ True, False])
        """

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the length of the Interval.

        See Also
        --------
        Interval.is_empty : Indicates if an interval contains no points.

        Examples
        --------
        >>> interval = pd.Interval(left=1, right=2, closed='left')
        >>> interval
        Interval(1, 2, closed='left')
        >>> interval.length
        1
        """

    mid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the midpoint of the Interval.

        Examples
        --------
        >>> iv = pd.Interval(0, 5)
        >>> iv.mid
        2.5
        """

    open_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the interval is open on the left side.

        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.

        Returns
        -------
        bool
            True if the Interval is not closed on the left-side.

        See Also
        --------
        Interval.open_right : Check if the interval is open on the right side.
        Interval.closed_left : Boolean inverse of open_left.

        Examples
        --------
        >>> iv = pd.Interval(0, 5, closed='neither')
        >>> iv.open_left
        True

        >>> iv = pd.Interval(0, 5, closed='both')
        >>> iv.open_left
        False
        """

    open_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the interval is open on the right side.

        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.

        Returns
        -------
        bool
            True if the Interval is not closed on the left-side.

        See Also
        --------
        Interval.open_left : Check if the interval is open on the left side.
        Interval.closed_right : Boolean inverse of open_right.

        Examples
        --------
        >>> iv = pd.Interval(0, 5, closed='left')
        >>> iv.open_right
        True

        >>> iv = pd.Interval(0, 5)
        >>> iv.open_right
        False
        """



class Interval(IntervalMixin):
    """
    Immutable object implementing an Interval, a bounded slice-like interval.
    
        Parameters
        ----------
        left : orderable scalar
            Left bound for the interval.
        right : orderable scalar
            Right bound for the interval.
        closed : {'right', 'left', 'both', 'neither'}, default 'right'
            Whether the interval is closed on the left-side, right-side, both or
            neither. See the Notes for more detailed explanation.
    
        See Also
        --------
        IntervalIndex : An Index of Interval objects that are all closed on the
            same side.
        cut : Convert continuous data into discrete bins (Categorical
            of Interval objects).
        qcut : Convert continuous data into bins (Categorical of Interval objects)
            based on quantiles.
        Period : Represents a period of time.
    
        Notes
        -----
        The parameters `left` and `right` must be from the same type, you must be
        able to compare them and they must satisfy ``left <= right``.
    
        A closed interval (in mathematics denoted by square brackets) contains
        its endpoints, i.e. the closed interval ``[0, 5]`` is characterized by the
        conditions ``0 <= x <= 5``. This is what ``closed='both'`` stands for.
        An open interval (in mathematics denoted by parentheses) does not contain
        its endpoints, i.e. the open interval ``(0, 5)`` is characterized by the
        conditions ``0 < x < 5``. This is what ``closed='neither'`` stands for.
        Intervals can also be half-open or half-closed, i.e. ``[0, 5)`` is
        described by ``0 <= x < 5`` (``closed='left'``) and ``(0, 5]`` is
        described by ``0 < x <= 5`` (``closed='right'``).
    
        Examples
        --------
        It is possible to build Intervals of different types, like numeric ones:
    
        >>> iv = pd.Interval(left=0, right=5)
        >>> iv
        Interval(0, 5, closed='right')
    
        You can check if an element belongs to it, or if it contains another interval:
    
        >>> 2.5 in iv
        True
        >>> pd.Interval(left=2, right=5, closed='both') in iv
        True
    
        You can test the bounds (``closed='right'``, so ``0 < x <= 5``):
    
        >>> 0 in iv
        False
        >>> 5 in iv
        True
        >>> 0.0001 in iv
        True
    
        Calculate its length
    
        >>> iv.length
        5
    
        You can operate with `+` and `*` over an Interval and the operation
        is applied to each of its bounds, so the result depends on the type
        of the bound elements
    
        >>> shifted_iv = iv + 3
        >>> shifted_iv
        Interval(3, 8, closed='right')
        >>> extended_iv = iv * 10.0
        >>> extended_iv
        Interval(0.0, 50.0, closed='right')
    
        To create a time interval you can use Timestamps as the bounds
    
        >>> year_2017 = pd.Interval(pd.Timestamp('2017-01-01 00:00:00'),
        ...                         pd.Timestamp('2018-01-01 00:00:00'),
        ...                         closed='left')
        >>> pd.Timestamp('2017-01-01 00:00') in year_2017
        True
        >>> year_2017.length
        Timedelta('365 days 00:00:00')
    """
    def overlaps(self, i2): # real signature unknown; restored from __doc__
        """
        Check whether two Interval objects overlap.
        
                Two intervals overlap if they share a common point, including closed
                endpoints. Intervals that only have an open endpoint in common do not
                overlap.
        
                Parameters
                ----------
                other : Interval
                    Interval to check against for an overlap.
        
                Returns
                -------
                bool
                    True if the two intervals overlap.
        
                See Also
                --------
                IntervalArray.overlaps : The corresponding method for IntervalArray.
                IntervalIndex.overlaps : The corresponding method for IntervalIndex.
        
                Examples
                --------
                >>> i1 = pd.Interval(0, 2)
                >>> i2 = pd.Interval(1, 3)
                >>> i1.overlaps(i2)
                True
                >>> i3 = pd.Interval(4, 5)
                >>> i1.overlaps(i3)
                False
        
                Intervals that share closed endpoints overlap:
        
                >>> i4 = pd.Interval(0, 1, closed='both')
                >>> i5 = pd.Interval(1, 2, closed='both')
                >>> i4.overlaps(i5)
                True
        
                Intervals that only have an open endpoint in common do not overlap:
        
                >>> i6 = pd.Interval(1, 2, closed='neither')
                >>> i4.overlaps(i6)
                False
        """
        pass

    def _validate_endpoint(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return bool(key in self). """
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

    def __init__(self, left=0, right=5): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    String describing the inclusive side the intervals.

    Either ``left``, ``right``, ``both`` or ``neither``.

    Examples
    --------
    >>> interval = pd.Interval(left=1, right=2, closed='left')
    >>> interval
    Interval(1, 2, closed='left')
    >>> interval.closed
    'left'
    """

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Left bound for the interval.

    Examples
    --------
    >>> interval = pd.Interval(left=1, right=2, closed='left')
    >>> interval
    Interval(1, 2, closed='left')
    >>> interval.left
    1
    """

    right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
    Right bound for the interval.

    Examples
    --------
    >>> interval = pd.Interval(left=1, right=2, closed='left')
    >>> interval
    Interval(1, 2, closed='left')
    >>> interval.right
    2
    """


    _typ = 'interval'
    __array_priority__ = 1000


class IntervalTree(IntervalMixin):
    """
    A centered interval tree
    
        Based off the algorithm described on Wikipedia:
        https://en.wikipedia.org/wiki/Interval_tree
    
        we are emulating the IndexEngine interface
    """
    def clear_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                left, right : np.ndarray[ndim=1]
                    Left and right bounds for each interval. Assumed to contain no
                    NaNs.
                closed : {'left', 'right', 'both', 'neither'}, optional
                    Whether the intervals are closed on the left-side, right-side, both
                    or neither. Defaults to 'right'.
                leaf_size : int, optional
                    Parameter that controls when the tree switches from creating nodes
                    to brute-force search. Tune this parameter to optimize query
                    performance.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __pyx_fuse_0get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_0get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_1get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_1get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __pyx_fuse_2get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to unique intervals that overlap
                with the given array of scalar targets.
        """
        pass

    def __pyx_fuse_2get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return the positions corresponding to intervals that overlap with
                the given array of scalar targets. Non-unique positions are repeated.
        """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_increasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if the IntervalTree is monotonic increasing (only equal or
        increasing values), else False
        """

    is_overlapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Determine if the IntervalTree contains overlapping intervals.
        Cached as self._is_overlapping.
        """

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    left_sorter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How to sort the left labels; this is used for binary search
        """

    right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    right_sorter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How to sort the right labels
        """

    root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_overlapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _left_sorter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _na_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _right_sorter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

NODE_CLASSES = {
    (
        'float64',
        'both',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Float64ClosedBothIntervalNode'>"
    ,
    (
        'float64',
        'left',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Float64ClosedLeftIntervalNode'>"
    ,
    (
        'float64',
        'neither',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Float64ClosedNeitherIntervalNode'>"
    ,
    (
        'float64',
        'right',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Float64ClosedRightIntervalNode'>"
    ,
    (
        'int64',
        'both',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Int64ClosedBothIntervalNode'>"
    ,
    (
        'int64',
        'left',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Int64ClosedLeftIntervalNode'>"
    ,
    (
        'int64',
        'neither',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Int64ClosedNeitherIntervalNode'>"
    ,
    (
        'int64',
        'right',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Int64ClosedRightIntervalNode'>"
    ,
    (
        'uint64',
        'both',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Uint64ClosedBothIntervalNode'>"
    ,
    (
        'uint64',
        'left',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Uint64ClosedLeftIntervalNode'>"
    ,
    (
        'uint64',
        'neither',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Uint64ClosedNeitherIntervalNode'>"
    ,
    (
        'uint64',
        'right',
    ): 
        None # (!) real value is "<class 'pandas._libs.interval.Uint64ClosedRightIntervalNode'>"
    ,
}

VALID_CLOSED = None # (!) real value is "frozenset({'left', 'right', 'both', 'neither'})"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C4754C8290>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.interval', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C4754C8290>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\interval.cp313-win_amd64.pyd')"

__test__ = {
    'Interval.overlaps (line 539)': "\n        Check whether two Interval objects overlap.\n\n        Two intervals overlap if they share a common point, including closed\n        endpoints. Intervals that only have an open endpoint in common do not\n        overlap.\n\n        Parameters\n        ----------\n        other : Interval\n            Interval to check against for an overlap.\n\n        Returns\n        -------\n        bool\n            True if the two intervals overlap.\n\n        See Also\n        --------\n        IntervalArray.overlaps : The corresponding method for IntervalArray.\n        IntervalIndex.overlaps : The corresponding method for IntervalIndex.\n\n        Examples\n        --------\n        >>> i1 = pd.Interval(0, 2)\n        >>> i2 = pd.Interval(1, 3)\n        >>> i1.overlaps(i2)\n        True\n        >>> i3 = pd.Interval(4, 5)\n        >>> i1.overlaps(i3)\n        False\n\n        Intervals that share closed endpoints overlap:\n\n        >>> i4 = pd.Interval(0, 1, closed='both')\n        >>> i5 = pd.Interval(1, 2, closed='both')\n        >>> i4.overlaps(i5)\n        True\n\n        Intervals that only have an open endpoint in common do not overlap:\n\n        >>> i6 = pd.Interval(1, 2, closed='neither')\n        >>> i4.overlaps(i6)\n        False\n        ",
    'IntervalMixin.closed_left.__get__ (line 49)': "\n        Check if the interval is closed on the left side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n\n        See Also\n        --------\n        Interval.closed_right : Check if the interval is closed on the right side.\n        Interval.open_left : Boolean inverse of closed_left.\n\n        Examples\n        --------\n        >>> iv = pd.Interval(0, 5, closed='left')\n        >>> iv.closed_left\n        True\n\n        >>> iv = pd.Interval(0, 5, closed='right')\n        >>> iv.closed_left\n        False\n        ",
    'IntervalMixin.closed_right.__get__ (line 78)': "\n        Check if the interval is closed on the right side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is closed on the left-side.\n\n        See Also\n        --------\n        Interval.closed_left : Check if the interval is closed on the left side.\n        Interval.open_right : Boolean inverse of closed_right.\n\n        Examples\n        --------\n        >>> iv = pd.Interval(0, 5, closed='both')\n        >>> iv.closed_right\n        True\n\n        >>> iv = pd.Interval(0, 5, closed='left')\n        >>> iv.closed_right\n        False\n        ",
    'IntervalMixin.is_empty.__get__ (line 201)': "\n        Indicates if an interval is empty, meaning it contains no points.\n\n        Returns\n        -------\n        bool or ndarray\n            A boolean indicating if a scalar :class:`Interval` is empty, or a\n            boolean ``ndarray`` positionally indicating if an ``Interval`` in\n            an :class:`~arrays.IntervalArray` or :class:`IntervalIndex` is\n            empty.\n\n        See Also\n        --------\n        Interval.length : Return the length of the Interval.\n\n        Examples\n        --------\n        An :class:`Interval` that contains points is not empty:\n\n        >>> pd.Interval(0, 1, closed='right').is_empty\n        False\n\n        An ``Interval`` that does not contain any points is empty:\n\n        >>> pd.Interval(0, 0, closed='right').is_empty\n        True\n        >>> pd.Interval(0, 0, closed='left').is_empty\n        True\n        >>> pd.Interval(0, 0, closed='neither').is_empty\n        True\n\n        An ``Interval`` that contains a single point is not empty:\n\n        >>> pd.Interval(0, 0, closed='both').is_empty\n        False\n\n        An :class:`~arrays.IntervalArray` or :class:`IntervalIndex` returns a\n        boolean ``ndarray`` positionally indicating if an ``Interval`` is\n        empty:\n\n        >>> ivs = [pd.Interval(0, 0, closed='neither'),\n        ...        pd.Interval(1, 2, closed='neither')]\n        >>> pd.arrays.IntervalArray(ivs).is_empty\n        array([ True, False])\n\n        Missing values are not considered empty:\n\n        >>> ivs = [pd.Interval(0, 0, closed='neither'), np.nan]\n        >>> pd.IntervalIndex(ivs).is_empty\n        array([ True, False])\n        ",
    'IntervalMixin.length.__get__ (line 182)': "\n        Return the length of the Interval.\n\n        See Also\n        --------\n        Interval.is_empty : Indicates if an interval contains no points.\n\n        Examples\n        --------\n        >>> interval = pd.Interval(left=1, right=2, closed='left')\n        >>> interval\n        Interval(1, 2, closed='left')\n        >>> interval.length\n        1\n        ",
    'IntervalMixin.mid.__get__ (line 165)': '\n        Return the midpoint of the Interval.\n\n        Examples\n        --------\n        >>> iv = pd.Interval(0, 5)\n        >>> iv.mid\n        2.5\n        ',
    'IntervalMixin.open_left.__get__ (line 107)': "\n        Check if the interval is open on the left side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is not closed on the left-side.\n\n        See Also\n        --------\n        Interval.open_right : Check if the interval is open on the right side.\n        Interval.closed_left : Boolean inverse of open_left.\n\n        Examples\n        --------\n        >>> iv = pd.Interval(0, 5, closed='neither')\n        >>> iv.open_left\n        True\n\n        >>> iv = pd.Interval(0, 5, closed='both')\n        >>> iv.open_left\n        False\n        ",
    'IntervalMixin.open_right.__get__ (line 136)': "\n        Check if the interval is open on the right side.\n\n        For the meaning of `closed` and `open` see :class:`~pandas.Interval`.\n\n        Returns\n        -------\n        bool\n            True if the Interval is not closed on the left-side.\n\n        See Also\n        --------\n        Interval.open_left : Check if the interval is open on the left side.\n        Interval.closed_right : Boolean inverse of open_right.\n\n        Examples\n        --------\n        >>> iv = pd.Interval(0, 5, closed='left')\n        >>> iv.open_right\n        True\n\n        >>> iv = pd.Interval(0, 5)\n        >>> iv.open_right\n        False\n        ",
}

