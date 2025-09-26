# encoding: utf-8
# module pandas._libs.lib
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\lib.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import collections.abc as abc # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\_collections_abc.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
from pandas._libs.interval import Interval

from pandas._libs.missing import check_na_tuples_nonequal

from pandas._libs.tslibs.np_datetime import (OutOfBoundsDatetime, 
    OutOfBoundsTimedelta)

from pandas._libs.tslibs.period import Period

from sys import getsizeof

import enum as __enum
import typing as __typing


# Variables with simple values

i8max = 9223372036854775807

pa = None

u8max = 18446744073709551615

# functions

def array_equivalent_object(*args, **kwargs): # real signature unknown
    """
    Perform an element by element comparison on N-d object arrays
        taking into account nan positions.
    """
    pass

def convert_nans_to_NA(*args, **kwargs): # real signature unknown
    """
    Helper for StringArray that converts null values that
        are not pd.NA(e.g. np.nan, None) to pd.NA. Assumes elements
        have already been validated as null.
    """
    pass

def count_level_2d(*args, **kwargs): # real signature unknown
    pass

def dicts_to_array(*args, **kwargs): # real signature unknown
    pass

def dtypes_all_equal(*args, **kwargs): # real signature unknown
    """
    Faster version for:
    
        first = types[0]
        all(is_dtype_equal(first, t) for t in types[1:])
    
        And assuming all elements in the list are np.dtype/ExtensionDtype objects
    
        See timings at https://github.com/pandas-dev/pandas/pull/44594
    """
    pass

def ensure_string_array(*args, **kwargs): # real signature unknown
    """
    Returns a new numpy array with object dtype and only strings and na values.
    
        Parameters
        ----------
        arr : array-like
            The values to be converted to str, if needed.
        na_value : Any, default np.nan
            The value to use for na. For example, np.nan or pd.NA.
        convert_na_value : bool, default True
            If False, existing na values will be used unchanged in the new array.
        copy : bool, default True
            Whether to ensure that a new array is returned. When True, a new array
            is always returned. When False, a new array is only returned when needed
            to avoid mutating the input array.
        skipna : bool, default True
            Whether or not to coerce nulls to their stringified form
            (e.g. if False, NaN becomes 'nan').
    
        Returns
        -------
        np.ndarray[object]
            An array with the input array's elements casted to str or nan-like.
    """
    pass

def eq_NA_compat(*args, **kwargs): # real signature unknown
    """
    Check for `arr == key`, treating all values as not-equal to pd.NA.
    
        key is assumed to have `not isna(key)`
    """
    pass

def fast_multiget(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple_list(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple_list_gen(*args, **kwargs): # real signature unknown
    """
    Generate a list of unique values from a generator of lists.
    
        Parameters
        ----------
        gen : generator object
            Generator of lists from which the unique list is created.
        sort : bool
            Whether or not to sort the resulting unique list.
    
        Returns
        -------
        list of unique values
    """
    pass

def fast_zip(*args, **kwargs): # real signature unknown
    """ For zipping multiple ndarrays into an ndarray of tuples. """
    pass

def generate_bins_dt64(*args, **kwargs): # real signature unknown
    """ Int64 (datetime64) version of generic python version in ``groupby.py``. """
    pass

def generate_slices(*args, **kwargs): # real signature unknown
    pass

def get_level_sorter(*args, **kwargs): # real signature unknown
    """
    Argsort for a single level of a multi-index, keeping the order of higher
        levels unchanged. `starts` points to starts of same-key indices w.r.t
        to leading levels; equivalent to:
            np.hstack([codes[starts[i]:starts[i+1]].argsort(kind='mergesort')
                + starts[i] for i in range(len(starts) - 1)])
    
        Parameters
        ----------
        codes : np.ndarray[int64_t, ndim=1]
        starts : np.ndarray[intp, ndim=1]
    
        Returns
        -------
        np.ndarray[np.int, ndim=1]
    """
    pass

def get_reverse_indexer(*args, **kwargs): # real signature unknown
    """
    Reverse indexing operation.
    
        Given `indexer`, make `indexer_inv` of it, such that::
    
            indexer_inv[indexer[x]] = x
    
        Parameters
        ----------
        indexer : np.ndarray[np.intp]
        length : int
    
        Returns
        -------
        np.ndarray[np.intp]
    
        Notes
        -----
        If indexer is not unique, only first occurrence is accounted.
    """
    pass

def has_infs(*args, **kwargs): # real signature unknown
    pass

def has_only_ints_or_nan(*args, **kwargs): # real signature unknown
    pass

def indices_fast(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        index : ndarray[intp]
        labels : ndarray[int64]
        keys : list
        sorted_labels : list[ndarray[int64]]
    """
    pass

def infer_dtype(foo=None, bar=None): # real signature unknown; restored from __doc__
    """
    Return a string label of the type of a scalar or list-like of values.
    
        Parameters
        ----------
        value : scalar, list, ndarray, or pandas type
        skipna : bool, default True
            Ignore NaN values when inferring the type.
    
        Returns
        -------
        str
            Describing the common type of the input data.
        Results can include:
    
        - string
        - bytes
        - floating
        - integer
        - mixed-integer
        - mixed-integer-float
        - decimal
        - complex
        - categorical
        - boolean
        - datetime64
        - datetime
        - date
        - timedelta64
        - timedelta
        - time
        - period
        - mixed
        - unknown-array
    
        Raises
        ------
        TypeError
            If ndarray-like but cannot infer the dtype
    
        Notes
        -----
        - 'mixed' is the catchall for anything that is not otherwise
          specialized
        - 'mixed-integer-float' are floats and integers
        - 'mixed-integer' are integers mixed with non-integers
        - 'unknown-array' is the catchall for something that *is* an array (has
          a dtype attribute), but has a dtype unknown to pandas (e.g. external
          extension array)
    
        Examples
        --------
        >>> from pandas.api.types import infer_dtype
        >>> infer_dtype(['foo', 'bar'])
        'string'
    
        >>> infer_dtype(['a', np.nan, 'b'], skipna=True)
        'string'
    
        >>> infer_dtype(['a', np.nan, 'b'], skipna=False)
        'mixed'
    
        >>> infer_dtype([b'foo', b'bar'])
        'bytes'
    
        >>> infer_dtype([1, 2, 3])
        'integer'
    
        >>> infer_dtype([1, 2, 3.5])
        'mixed-integer-float'
    
        >>> infer_dtype([1.0, 2.0, 3.5])
        'floating'
    
        >>> infer_dtype(['a', 1])
        'mixed-integer'
    
        >>> from decimal import Decimal
        >>> infer_dtype([Decimal(1), Decimal(2.0)])
        'decimal'
    
        >>> infer_dtype([True, False])
        'boolean'
    
        >>> infer_dtype([True, False, np.nan])
        'boolean'
    
        >>> infer_dtype([pd.Timestamp('20130101')])
        'datetime'
    
        >>> import datetime
        >>> infer_dtype([datetime.date(2013, 1, 1)])
        'date'
    
        >>> infer_dtype([np.datetime64('2013-01-01')])
        'datetime64'
    
        >>> infer_dtype([datetime.timedelta(0, 1, 1)])
        'timedelta'
    
        >>> infer_dtype(pd.Series(list('aabc')).astype('category'))
        'categorical'
    """
    pass

def is_all_arraylike(*args, **kwargs): # real signature unknown
    """ Should we treat these as levels of a MultiIndex, as opposed to Index items? """
    pass

def is_bool(True_): # real signature unknown; restored from __doc__
    """
    Return True if given object is boolean.
    
        Returns
        -------
        bool
    
        Examples
        --------
        >>> pd.api.types.is_bool(True)
        True
    
        >>> pd.api.types.is_bool(1)
        False
    """
    pass

def is_bool_array(*args, **kwargs): # real signature unknown
    pass

def is_bool_list(obj): # real signature unknown; restored from __doc__
    """
    Check if this list contains only bool or np.bool_ objects.
    
        This is appreciably faster than checking `np.array(obj).dtype == bool`
    
        obj1 = [True, False] * 100
        obj2 = obj1 * 100
        obj3 = obj2 * 100
        obj4 = [True, None] + obj1
    
        for obj in [obj1, obj2, obj3, obj4]:
            %timeit is_bool_list(obj)
            %timeit np.array(obj).dtype.kind == "b"
    
        340 ns ± 8.22 ns
        8.78 µs ± 253 ns
    
        28.8 µs ± 704 ns
        813 µs ± 17.8 µs
    
        3.4 ms ± 168 µs
        78.4 ms ± 1.05 ms
    
        48.1 ns ± 1.26 ns
        8.1 µs ± 198 ns
    """
    pass

def is_complex(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return True if given object is complex.
    
        Returns
        -------
        bool
    
        Examples
        --------
        >>> pd.api.types.is_complex(1 + 1j)
        True
    
        >>> pd.api.types.is_complex(1)
        False
    """
    pass

def is_datetime64_array(*args, **kwargs): # real signature unknown
    pass

def is_datetime_array(*args, **kwargs): # real signature unknown
    pass

def is_datetime_with_singletz_array(*args, **kwargs): # real signature unknown
    """
    Check values have the same tzinfo attribute.
        Doesn't check values are datetime-like types.
    """
    pass

def is_date_array(*args, **kwargs): # real signature unknown
    pass

def is_decimal(*args, **kwargs): # real signature unknown
    pass

def is_float(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return True if given object is float.
    
        Returns
        -------
        bool
    
        Examples
        --------
        >>> pd.api.types.is_float(1.0)
        True
    
        >>> pd.api.types.is_float(1)
        False
    """
    pass

def is_float_array(*args, **kwargs): # real signature unknown
    pass

def is_integer(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return True if given object is integer.
    
        Returns
        -------
        bool
    
        Examples
        --------
        >>> pd.api.types.is_integer(1)
        True
    
        >>> pd.api.types.is_integer(1.0)
        False
    """
    pass

def is_integer_array(*args, **kwargs): # real signature unknown
    pass

def is_interval(*args, **kwargs): # real signature unknown
    pass

def is_interval_array(*args, **kwargs): # real signature unknown
    """ Is this an ndarray of Interval (or np.nan) with a single dtype? """
    pass

def is_int_or_none(*args, **kwargs): # real signature unknown
    """
    Return True if given object is integer or None.
    
        Returns
        -------
        bool
    """
    pass

def is_iterator(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Check if the object is an iterator.
    
        This is intended for generators, not list-like objects.
    
        Parameters
        ----------
        obj : The object to check
    
        Returns
        -------
        is_iter : bool
            Whether `obj` is an iterator.
    
        Examples
        --------
        >>> import datetime
        >>> from pandas.api.types import is_iterator
        >>> is_iterator((x for x in []))
        True
        >>> is_iterator([1, 2, 3])
        False
        >>> is_iterator(datetime.datetime(2017, 1, 1))
        False
        >>> is_iterator("foo")
        False
        >>> is_iterator(1)
        False
    """
    pass

def is_list_like(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Check if the object is list-like.
    
        Objects that are considered list-like are for example Python
        lists, tuples, sets, NumPy arrays, and Pandas Series.
    
        Strings and datetime objects, however, are not considered list-like.
    
        Parameters
        ----------
        obj : object
            Object to check.
        allow_sets : bool, default True
            If this parameter is False, sets will not be considered list-like.
    
        Returns
        -------
        bool
            Whether `obj` has list-like properties.
    
        Examples
        --------
        >>> import datetime
        >>> from pandas.api.types import is_list_like
        >>> is_list_like([1, 2, 3])
        True
        >>> is_list_like({1, 2, 3})
        True
        >>> is_list_like(datetime.datetime(2017, 1, 1))
        False
        >>> is_list_like("foo")
        False
        >>> is_list_like(1)
        False
        >>> is_list_like(np.array([2]))
        True
        >>> is_list_like(np.array(2))
        False
    """
    pass

def is_np_dtype(dtype): # real signature unknown; restored from __doc__
    """
    Optimized check for `isinstance(dtype, np.dtype)` with
        optional `and dtype.kind in kinds`.
    
        dtype = np.dtype("m8[ns]")
    
        In [7]: %timeit isinstance(dtype, np.dtype)
        117 ns ± 1.91 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
    
        In [8]: %timeit is_np_dtype(dtype)
        64 ns ± 1.51 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
    
        In [9]: %timeit is_timedelta64_dtype(dtype)
        209 ns ± 6.96 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
    
        In [10]: %timeit is_np_dtype(dtype, "m")
        93.4 ns ± 1.11 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
    """
    pass

def is_period(*args, **kwargs): # real signature unknown
    """
    Return True if given object is Period.
    
        Returns
        -------
        bool
    """
    pass

def is_pyarrow_array(*args, **kwargs): # real signature unknown
    """
    Return True if given object is a pyarrow Array or ChunkedArray.
    
        Returns
        -------
        bool
    """
    pass

def is_range_indexer(*args, **kwargs): # real signature unknown
    """
    Perform an element by element comparison on 1-d integer arrays, meant for indexer
        comparisons
    """
    pass

def is_scalar(dt): # real signature unknown; restored from __doc__
    """
    Return True if given object is scalar.
    
        Parameters
        ----------
        val : object
            This includes:
    
            - numpy array scalar (e.g. np.int64)
            - Python builtin numerics
            - Python builtin byte arrays and strings
            - None
            - datetime.datetime
            - datetime.timedelta
            - Period
            - decimal.Decimal
            - Interval
            - DateOffset
            - Fraction
            - Number.
    
        Returns
        -------
        bool
            Return True if given object is scalar.
    
        Examples
        --------
        >>> import datetime
        >>> dt = datetime.datetime(2018, 10, 3)
        >>> pd.api.types.is_scalar(dt)
        True
    
        >>> pd.api.types.is_scalar([2, 3])
        False
    
        >>> pd.api.types.is_scalar({0: 1, 2: 3})
        False
    
        >>> pd.api.types.is_scalar((0, 2))
        False
    
        pandas supports PEP 3141 numbers:
    
        >>> from fractions import Fraction
        >>> pd.api.types.is_scalar(Fraction(3, 5))
        True
    """
    pass

def is_string_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta_or_timedelta64_array(*args, **kwargs): # real signature unknown
    """ Infer with timedeltas and/or nat/none. """
    pass

def is_time_array(*args, **kwargs): # real signature unknown
    pass

def item_from_zerodim(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    If the value is a zerodim array, return the item it contains.
    
        Parameters
        ----------
        val : object
    
        Returns
        -------
        object
    
        Examples
        --------
        >>> item_from_zerodim(1)
        1
        >>> item_from_zerodim('foobar')
        'foobar'
        >>> item_from_zerodim(np.array(1))
        1
        >>> item_from_zerodim(np.array([1]))
        array([1])
    """
    pass

def Literal(*args, **kwargs): # real signature unknown
    """
    Special typing form to define literal types (a.k.a. value types).
    
    This form can be used to indicate to type checkers that the corresponding
    variable or function parameter has a value equivalent to the provided
    literal (or one of several literals)::
    
        def validate_simple(data: Any) -> Literal[True]:  # always returns True
            ...
    
        MODE = Literal['r', 'rb', 'w', 'wb']
        def open_helper(file: str, mode: MODE) -> str:
            ...
    
        open_helper('/some/path', 'r')  # Passes type check
        open_helper('/other/path', 'typo')  # Error in type checker
    
    Literal[...] cannot be subclassed. At runtime, an arbitrary value
    is allowed as type argument to Literal[...], but type checkers may
    impose restrictions.
    """
    pass

def map_infer(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference.
    
        Parameters
        ----------
        arr : ndarray
        f : function
        convert : bint
        ignore_na : bint
            If True, NA values will not have f applied
    
        Returns
        -------
        np.ndarray
    """
    pass

def map_infer_mask(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference.
    
        Parameters
        ----------
        arr : ndarray
        f : function
        mask : ndarray
            uint8 dtype ndarray indicating values not to apply `f` to.
        convert : bool, default True
            Whether to call `maybe_convert_objects` on the resulting ndarray.
        na_value : Any, optional
            The result value to use for masked values. By default, the
            input value is used.
        dtype : numpy.dtype
            The numpy dtype to use for the result ndarray.
    
        Returns
        -------
        np.ndarray
    """
    pass

def maybe_booleans_to_slice(*args, **kwargs): # real signature unknown
    pass

def maybe_convert_numeric(*args, **kwargs): # real signature unknown
    """
    Convert object array to a numeric array if possible.
    
        Parameters
        ----------
        values : ndarray[object]
            Array of object elements to convert.
        na_values : set
            Set of values that should be interpreted as NaN.
        convert_empty : bool, default True
            If an empty array-like object is encountered, whether to interpret
            that element as NaN or not. If set to False, a ValueError will be
            raised if such an element is encountered and 'coerce_numeric' is False.
        coerce_numeric : bool, default False
            If initial attempts to convert to numeric have failed, whether to
            force conversion to numeric via alternative methods or by setting the
            element to NaN. Otherwise, an Exception will be raised when such an
            element is encountered.
    
            This boolean also has an impact on how conversion behaves when a
            numeric array has no suitable numerical dtype to return (i.e. uint64,
            int32, uint8). If set to False, the original object array will be
            returned. Otherwise, a ValueError will be raised.
        convert_to_masked_nullable : bool, default False
            Whether to return a mask for the converted values. This also disables
            upcasting for ints with nulls to float64.
        Returns
        -------
        np.ndarray
            Array of converted object values to numerical ones.
    
        Optional[np.ndarray]
            If convert_to_masked_nullable is True,
            returns a boolean mask for the converted values, otherwise returns None.
    """
    pass

def maybe_convert_objects(*args, **kwargs): # real signature unknown
    """
    Type inference function-- convert object array to proper dtype
    
        Parameters
        ----------
        objects : ndarray[object]
            Array of object elements to convert.
        try_float : bool, default False
            If an array-like object contains only float or NaN values is
            encountered, whether to convert and return an array of float dtype.
        safe : bool, default False
            Whether to upcast numeric type (e.g. int cast to float). If set to
            True, no upcasting will be performed.
        convert_numeric : bool, default True
            Whether to convert numeric entries.
        convert_to_nullable_dtype : bool, default False
            If an array-like object contains only integer or boolean values (and NaN) is
            encountered, whether to convert and return an Boolean/IntegerArray.
        convert_non_numeric : bool, default False
            Whether to convert datetime, timedelta, period, interval types.
        dtype_if_all_nat : np.dtype, ExtensionDtype, or None, default None
            Dtype to cast to if we have all-NaT.
    
        Returns
        -------
        np.ndarray or ExtensionArray
            Array of converted object values to more specific dtypes if applicable.
    """
    pass

def maybe_indices_to_slice(*args, **kwargs): # real signature unknown
    pass

def memory_usage_of_objects(*args, **kwargs): # real signature unknown
    """
    Return the memory usage of an object array in bytes.
    
        Does not include the actual bytes of the pointers
    """
    pass

def NoDefault(*args, **kwargs): # real signature unknown
    pass

def to_object_array(*args, **kwargs): # real signature unknown
    """
    Convert a list of lists into an object array.
    
        Parameters
        ----------
        rows : 2-d array (N, K)
            List of lists to be converted into an array.
        min_width : int
            Minimum width of the object array. If a list
            in `rows` contains fewer than `width` elements,
            the remaining elements in the corresponding row
            will all be `NaN`.
    
        Returns
        -------
        np.ndarray[object, ndim=2]
    """
    pass

def to_object_array_tuples(*args, **kwargs): # real signature unknown
    """
    Convert a list of tuples into an object array. Any subclass of
        tuple in `rows` will be casted to tuple.
    
        Parameters
        ----------
        rows : 2-d array (N, K)
            List of tuples to be converted into an array.
    
        Returns
        -------
        np.ndarray[object, ndim=2]
    """
    pass

def tuples_to_object_array(*args, **kwargs): # real signature unknown
    pass

def using_string_dtype(): # reliably restored by inspect
    # no doc
    pass

def _map_infer_mask(*args, **kwargs): # real signature unknown
    """ Helper for map_infer_mask, split off to use fused types based on the result. """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Decimal(object):
    """
    Construct a new Decimal object. 'value' can be an integer, string, tuple,
    or another Decimal object. If no value is given, return Decimal('0'). The
    context does not affect the conversion and is only passed to determine if
    the InvalidOperation trap is active.
    """
    def adjusted(self, *args, **kwargs): # real signature unknown
        """ Return the adjusted exponent of the number.  Defined as exp + digits - 1. """
        pass

    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Decimal.as_integer_ratio() -> (int, int)
        
        Return a pair of integers, whose ratio is exactly equal to the original
        Decimal and with a positive denominator. The ratio is in lowest terms.
        Raise OverflowError on infinities and a ValueError on NaNs.
        """
        pass

    def as_tuple(self, *args, **kwargs): # real signature unknown
        """ Return a tuple representation of the number. """
        pass

    def canonical(self, *args, **kwargs): # real signature unknown
        """
        Return the canonical encoding of the argument.  Currently, the encoding
        of a Decimal instance is always canonical, so this operation returns its
        argument unchanged.
        """
        pass

    def compare(self, *args, **kwargs): # real signature unknown
        """
        Compare self to other.  Return a decimal value:
        
            a or b is a NaN ==> Decimal('NaN')
            a < b           ==> Decimal('-1')
            a == b          ==> Decimal('0')
            a > b           ==> Decimal('1')
        """
        pass

    def compare_signal(self, *args, **kwargs): # real signature unknown
        """ Identical to compare, except that all NaNs signal. """
        pass

    def compare_total(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Compare two operands using their abstract representation rather than
        their numerical value.  Similar to the compare() method, but the result
        gives a total ordering on Decimal instances.  Two Decimal instances with
        the same numeric value but different representations compare unequal
        in this ordering:
        
            >>> Decimal('12.0').compare_total(Decimal('12'))
            Decimal('-1')
        
        Quiet and signaling NaNs are also included in the total ordering. The result
        of this function is Decimal('0') if both operands have the same representation,
        Decimal('-1') if the first operand is lower in the total order than the second,
        and Decimal('1') if the first operand is higher in the total order than the
        second operand. See the specification for details of the total order.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def compare_total_mag(self, y): # real signature unknown; restored from __doc__
        """
        Compare two operands using their abstract representation rather than their
        value as in compare_total(), but ignoring the sign of each operand.
        
        x.compare_total_mag(y) is equivalent to x.copy_abs().compare_total(y.copy_abs()).
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Return self. """
        pass

    def copy_abs(self, *args, **kwargs): # real signature unknown
        """
        Return the absolute value of the argument.  This operation is unaffected by
        context and is quiet: no flags are changed and no rounding is performed.
        """
        pass

    def copy_negate(self, *args, **kwargs): # real signature unknown
        """
        Return the negation of the argument.  This operation is unaffected by context
        and is quiet: no flags are changed and no rounding is performed.
        """
        pass

    def copy_sign(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a copy of the first operand with the sign set to be the same as the
        sign of the second operand. For example:
        
            >>> Decimal('2.3').copy_sign(Decimal('-1.5'))
            Decimal('-2.3')
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def exp(self, *args, **kwargs): # real signature unknown
        """
        Return the value of the (natural) exponential function e**x at the given
        number.  The function always uses the ROUND_HALF_EVEN mode and the result
        is correctly rounded.
        """
        pass

    def fma(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Fused multiply-add.  Return self*other+third with no rounding of the
        intermediate product self*other.
        
            >>> Decimal(2).fma(3, 5)
            Decimal('11')
        """
        pass

    @classmethod
    def from_float(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Class method that converts a float to a decimal number, exactly.
        Since 0.1 is not exactly representable in binary floating point,
        Decimal.from_float(0.1) is not the same as Decimal('0.1').
        
            >>> Decimal.from_float(0.1)
            Decimal('0.1000000000000000055511151231257827021181583404541015625')
            >>> Decimal.from_float(float('nan'))
            Decimal('NaN')
            >>> Decimal.from_float(float('inf'))
            Decimal('Infinity')
            >>> Decimal.from_float(float('-inf'))
            Decimal('-Infinity')
        """
        pass

    def is_canonical(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is canonical and False otherwise.  Currently,
        a Decimal instance is always canonical, so this operation always returns
        True.
        """
        pass

    def is_finite(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a finite number, and False if the argument
        is infinite or a NaN.
        """
        pass

    def is_infinite(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is either positive or negative infinity and
        False otherwise.
        """
        pass

    def is_nan(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a (quiet or signaling) NaN and False
        otherwise.
        """
        pass

    def is_normal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a normal finite non-zero number with an
        adjusted exponent greater than or equal to Emin. Return False if the
        argument is zero, subnormal, infinite or a NaN.
        """
        pass

    def is_qnan(self, *args, **kwargs): # real signature unknown
        """ Return True if the argument is a quiet NaN, and False otherwise. """
        pass

    def is_signed(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument has a negative sign and False otherwise.
        Note that both zeros and NaNs can carry signs.
        """
        pass

    def is_snan(self, *args, **kwargs): # real signature unknown
        """ Return True if the argument is a signaling NaN and False otherwise. """
        pass

    def is_subnormal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is subnormal, and False otherwise. A number is
        subnormal if it is non-zero, finite, and has an adjusted exponent less
        than Emin.
        """
        pass

    def is_zero(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a (positive or negative) zero and False
        otherwise.
        """
        pass

    def ln(self, *args, **kwargs): # real signature unknown
        """
        Return the natural (base e) logarithm of the operand. The function always
        uses the ROUND_HALF_EVEN mode and the result is correctly rounded.
        """
        pass

    def log10(self, *args, **kwargs): # real signature unknown
        """
        Return the base ten logarithm of the operand. The function always uses the
        ROUND_HALF_EVEN mode and the result is correctly rounded.
        """
        pass

    def logb(self, *args, **kwargs): # real signature unknown
        """
        For a non-zero number, return the adjusted exponent of the operand as a
        Decimal instance.  If the operand is a zero, then Decimal('-Infinity') is
        returned and the DivisionByZero condition is raised. If the operand is
        an infinity then Decimal('Infinity') is returned.
        """
        pass

    def logical_and(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'and' of the two (logical) operands. """
        pass

    def logical_invert(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise inversion of the (logical) operand. """
        pass

    def logical_or(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'or' of the two (logical) operands. """
        pass

    def logical_xor(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'exclusive or' of the two (logical) operands. """
        pass

    def max(self, *args, **kwargs): # real signature unknown
        """
        Maximum of self and other.  If one operand is a quiet NaN and the other is
        numeric, the numeric operand is returned.
        """
        pass

    def max_mag(self, *args, **kwargs): # real signature unknown
        """
        Similar to the max() method, but the comparison is done using the absolute
        values of the operands.
        """
        pass

    def min(self, *args, **kwargs): # real signature unknown
        """
        Minimum of self and other. If one operand is a quiet NaN and the other is
        numeric, the numeric operand is returned.
        """
        pass

    def min_mag(self, *args, **kwargs): # real signature unknown
        """
        Similar to the min() method, but the comparison is done using the absolute
        values of the operands.
        """
        pass

    def next_minus(self, *args, **kwargs): # real signature unknown
        """
        Return the largest number representable in the given context (or in the
        current default context if no context is given) that is smaller than the
        given operand.
        """
        pass

    def next_plus(self, *args, **kwargs): # real signature unknown
        """
        Return the smallest number representable in the given context (or in the
        current default context if no context is given) that is larger than the
        given operand.
        """
        pass

    def next_toward(self, *args, **kwargs): # real signature unknown
        """
        If the two operands are unequal, return the number closest to the first
        operand in the direction of the second operand.  If both operands are
        numerically equal, return a copy of the first operand with the sign set
        to be the same as the sign of the second operand.
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """
        Normalize the number by stripping the rightmost trailing zeros and
        converting any result equal to Decimal('0') to Decimal('0e0').  Used
        for producing canonical values for members of an equivalence class.
        For example, Decimal('32.100') and Decimal('0.321000e+2') both normalize
        to the equivalent value Decimal('32.1').
        """
        pass

    def number_class(self, *args, **kwargs): # real signature unknown
        """
        Return a string describing the class of the operand.  The returned value
        is one of the following ten strings:
        
            * '-Infinity', indicating that the operand is negative infinity.
            * '-Normal', indicating that the operand is a negative normal number.
            * '-Subnormal', indicating that the operand is negative and subnormal.
            * '-Zero', indicating that the operand is a negative zero.
            * '+Zero', indicating that the operand is a positive zero.
            * '+Subnormal', indicating that the operand is positive and subnormal.
            * '+Normal', indicating that the operand is a positive normal number.
            * '+Infinity', indicating that the operand is positive infinity.
            * 'NaN', indicating that the operand is a quiet NaN (Not a Number).
            * 'sNaN', indicating that the operand is a signaling NaN.
        """
        pass

    def quantize(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a value equal to the first operand after rounding and having the
        exponent of the second operand.
        
            >>> Decimal('1.41421356').quantize(Decimal('1.000'))
            Decimal('1.414')
        
        Unlike other operations, if the length of the coefficient after the quantize
        operation would be greater than precision, then an InvalidOperation is signaled.
        This guarantees that, unless there is an error condition, the quantized exponent
        is always equal to that of the right-hand operand.
        
        Also unlike other operations, quantize never signals Underflow, even if the
        result is subnormal and inexact.
        
        If the exponent of the second operand is larger than that of the first, then
        rounding may be necessary. In this case, the rounding mode is determined by the
        rounding argument if given, else by the given context argument; if neither
        argument is given, the rounding mode of the current thread's context is used.
        """
        pass

    def radix(self, base): # real signature unknown; restored from __doc__
        """
        Return Decimal(10), the radix (base) in which the Decimal class does
        all its arithmetic. Included for compatibility with the specification.
        """
        pass

    def remainder_near(self, *args, **kwargs): # real signature unknown
        """
        Return the remainder from dividing self by other.  This differs from
        self % other in that the sign of the remainder is chosen so as to minimize
        its absolute value. More precisely, the return value is self - n * other
        where n is the integer nearest to the exact value of self / other, and
        if two integers are equally near then the even one is chosen.
        
        If the result is zero then its sign will be the sign of self.
        """
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        """
        Return the result of rotating the digits of the first operand by an amount
        specified by the second operand.  The second operand must be an integer in
        the range -precision through precision. The absolute value of the second
        operand gives the number of places to rotate. If the second operand is
        positive then rotation is to the left; otherwise rotation is to the right.
        The coefficient of the first operand is padded on the left with zeros to
        length precision if necessary. The sign and exponent of the first operand are
        unchanged.
        """
        pass

    def same_quantum(self, *args, **kwargs): # real signature unknown
        """
        Test whether self and other have the same exponent or whether both are NaN.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def scaleb(self, *args, **kwargs): # real signature unknown
        """
        Return the first operand with the exponent adjusted the second.  Equivalently,
        return the first operand multiplied by 10**other. The second operand must be
        an integer.
        """
        pass

    def shift(self, *args, **kwargs): # real signature unknown
        """
        Return the result of shifting the digits of the first operand by an amount
        specified by the second operand.  The second operand must be an integer in
        the range -precision through precision. The absolute value of the second
        operand gives the number of places to shift. If the second operand is
        positive, then the shift is to the left; otherwise the shift is to the
        right. Digits shifted into the coefficient are zeros. The sign and exponent
        of the first operand are unchanged.
        """
        pass

    def sqrt(self, *args, **kwargs): # real signature unknown
        """
        Return the square root of the argument to full precision. The result is
        correctly rounded using the ROUND_HALF_EVEN rounding mode.
        """
        pass

    def to_eng_string(self, *args, **kwargs): # real signature unknown
        """
        Convert to an engineering-type string.  Engineering notation has an exponent
        which is a multiple of 3, so there are up to 3 digits left of the decimal
        place. For example, Decimal('123E+1') is converted to Decimal('1.23E+3').
        
        The value of context.capitals determines whether the exponent sign is lower
        or upper case. Otherwise, the context does not affect the operation.
        """
        pass

    def to_integral(self): # real signature unknown; restored from __doc__
        """
        Identical to the to_integral_value() method.  The to_integral() name has been
        kept for compatibility with older versions.
        """
        pass

    def to_integral_exact(self, *args, **kwargs): # real signature unknown
        """
        Round to the nearest integer, signaling Inexact or Rounded as appropriate if
        rounding occurs.  The rounding mode is determined by the rounding parameter
        if given, else by the given context. If neither parameter is given, then the
        rounding mode of the current default context is used.
        """
        pass

    def to_integral_value(self, *args, **kwargs): # real signature unknown
        """
        Round to the nearest integer without signaling Inexact or Rounded.  The
        rounding mode is determined by the rounding parameter if given, else by
        the given context. If neither parameter is given, then the rounding mode
        of the current default context is used.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        pass

    def __complex__(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
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

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Enum(object):
    """
    Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.
    """
    def _add_alias_(self, name): # reliably restored by inspect
        # no doc
        pass

    def _add_value_alias_(self, value): # reliably restored by inspect
        # no doc
        pass

    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the list of values assigned
        """
        pass

    @classmethod
    def _missing_(cls, *args, **kwargs): # real signature unknown
        pass

    def _new_member_(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self): # reliably restored by inspect
        # no doc
        pass

    def __deepcopy__(self, memo): # reliably restored by inspect
        # no doc
        pass

    def __dir__(self): # reliably restored by inspect
        """ Returns public methods and other interesting attributes. """
        pass

    def __format__(self, format_spec): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __reduce_ex__(self, proto): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def __signature__(cls, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    name = None # (!) real value is '<enum.property object at 0x000001D61FD13390>'
    value = None # (!) real value is '<enum.property object at 0x000001D61FDF4A50>'
    _hashable_values_ = []
    _member_map_ = {}
    _member_names_ = []
    _member_type_ = object
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {}
    _value_repr_ = None
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'enum\', \'__firstlineno__\': 1109, \'__doc__\': "\\nCreate a collection of name/value pairs.\\n\\nExample enumeration:\\n\\n>>> class Color(Enum):\\n...     RED = 1\\n...     BLUE = 2\\n...     GREEN = 3\\n\\nAccess them by:\\n\\n- attribute access:\\n\\n  >>> Color.RED\\n  <Color.RED: 1>\\n\\n- value lookup:\\n\\n  >>> Color(1)\\n  <Color.RED: 1>\\n\\n- name lookup:\\n\\n  >>> Color[\'RED\']\\n  <Color.RED: 1>\\n\\nEnumerations can be iterated over, and know how many members they have:\\n\\n>>> len(Color)\\n3\\n\\n>>> list(Color)\\n[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]\\n\\nMethods can be added to enumerations, and members can have their own\\nattributes -- see the documentation for details.\\n", \'__signature__\': <classmethod(<function Enum.__signature__ at 0x000001D61FE27380>)>, \'__new__\': <staticmethod(<function Enum.__new__ at 0x000001D61FE27420>)>, \'__init__\': <function Enum.__init__ at 0x000001D61FE274C0>, \'_add_alias_\': <function Enum._add_alias_ at 0x000001D61FE27560>, \'_add_value_alias_\': <function Enum._add_value_alias_ at 0x000001D61FE27600>, \'_generate_next_value_\': <staticmethod(<function Enum._generate_next_value_ at 0x000001D61FE276A0>)>, \'_missing_\': <classmethod(<function Enum._missing_ at 0x000001D61FE27740>)>, \'__repr__\': <function Enum.__repr__ at 0x000001D61FE277E0>, \'__str__\': <function Enum.__str__ at 0x000001D61FE27880>, \'__dir__\': <function Enum.__dir__ at 0x000001D61FE27920>, \'__format__\': <function Enum.__format__ at 0x000001D61FE279C0>, \'__hash__\': <function Enum.__hash__ at 0x000001D61FE27A60>, \'__reduce_ex__\': <function Enum.__reduce_ex__ at 0x000001D61FE27B00>, \'__deepcopy__\': <function Enum.__deepcopy__ at 0x000001D61FE27BA0>, \'__copy__\': <function Enum.__copy__ at 0x000001D61FE27C40>, \'name\': <enum.property object at 0x000001D61FD13390>, \'value\': <enum.property object at 0x000001D61FDF4A50>, \'__static_attributes__\': (), \'_new_member_\': <function Enum.__new__ at 0x000001D61FE27420>, \'_use_args_\': False, \'_member_names_\': [], \'_member_map_\': {}, \'_value2member_map_\': {}, \'_hashable_values_\': [], \'_unhashable_values_\': [], \'_unhashable_values_map_\': {}, \'_member_type_\': <class \'object\'>, \'_value_repr_\': None, \'__dict__\': <attribute \'__dict__\' of \'Enum\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Enum\' objects>})'
    __firstlineno__ = 1109
    __static_attributes__ = ()


class _GenericAlias(__typing._BaseGenericAlias):
    # no doc
    def copy_with(self, args): # reliably restored by inspect
        # no doc
        pass

    def _determine_new_args(self, args): # reliably restored by inspect
        # no doc
        pass

    def _make_substitution(self, args, new_arg_by_param): # reliably restored by inspect
        """ Create a list of new type arguments. """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(*args, **kwds): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, origin, args, *, inst=True, name=None): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __mro_entries__(self, bases): # reliably restored by inspect
        # no doc
        pass

    def __or__(self, right): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __ror__(self, left): # reliably restored by inspect
        # no doc
        pass

    __firstlineno__ = 1397
    __static_attributes__ = (
        '__args__',
        '__module__',
        '__parameters__',
    )


class _NoDefault(__enum.Enum):
    # no doc
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the list of values assigned
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    no_default = None # (!) forward: no_default, real value is '<no_default>'
    _hashable_values_ = [
        'NO_DEFAULT',
    ]
    _member_map_ = {
        'no_default': None, # (!) forward: no_default, real value is '<no_default>'
    }
    _member_names_ = [
        'no_default',
    ]
    _member_type_ = object
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {
        'NO_DEFAULT': None, # (!) forward: no_default, real value is '<no_default>'
    }
    _value_repr_ = None


# variables with complex values

no_default = None # (!) real value is '<no_default>'

_TYPE_MAP = {
    'c': 'complex',
    'categorical': 'categorical',
    'category': 'categorical',
    'complex128': 'complex',
    'complex256': 'complex',
    'complex64': 'complex',
    'f': 'floating',
    'float128': 'floating',
    'float256': 'floating',
    'float32': 'floating',
    'float64': 'floating',
    'i': 'integer',
    'int16': 'integer',
    'int32': 'integer',
    'int64': 'integer',
    'int8': 'integer',
    'string': 'string',
    'u': 'integer',
    'uint16': 'integer',
    'uint32': 'integer',
    'uint64': 'integer',
    'uint8': 'integer',
    str: 
        'string'
    ,
    'S': 'bytes',
    'U': 'string',
    'bool': 'boolean',
    'b': 'boolean',
    'datetime64[ns]': 'datetime64',
    'M': 'datetime64',
    'timedelta64[ns]': 'timedelta64',
    'm': 'timedelta64',
    'interval': 'interval',
    None:  # (!) forward: Period, real value is "<class 'pandas._libs.tslibs.period.Period'>"
        'period'
    ,
    None:  # (!) real value is "<class 'datetime.datetime'>"
        'datetime64'
    ,
    None:  # (!) real value is "<class 'datetime.date'>"
        'date'
    ,
    None:  # (!) real value is "<class 'datetime.time'>"
        'time'
    ,
    None:  # (!) real value is "<class 'datetime.timedelta'>"
        'timedelta64'
    ,
    Decimal: 
        'decimal'
    ,
    bytes: 
        'bytes'
    ,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D62E881130>'

__pyx_capi__ = {
    'c_is_list_like': None, # (!) real value is '<capsule object "int (PyObject *, int)" at 0x000001D62E8EE930>'
    'eq_NA_compat': None, # (!) real value is '<capsule object "PyArrayObject *(PyArrayObject *, PyObject *, int __pyx_skip_dispatch)" at 0x000001D62E8EE980>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.lib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D62E881130>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\lib.cp313-win_amd64.pyd')"

__test__ = {
    'infer_dtype (line 1494)': "\n    Return a string label of the type of a scalar or list-like of values.\n\n    Parameters\n    ----------\n    value : scalar, list, ndarray, or pandas type\n    skipna : bool, default True\n        Ignore NaN values when inferring the type.\n\n    Returns\n    -------\n    str\n        Describing the common type of the input data.\n    Results can include:\n\n    - string\n    - bytes\n    - floating\n    - integer\n    - mixed-integer\n    - mixed-integer-float\n    - decimal\n    - complex\n    - categorical\n    - boolean\n    - datetime64\n    - datetime\n    - date\n    - timedelta64\n    - timedelta\n    - time\n    - period\n    - mixed\n    - unknown-array\n\n    Raises\n    ------\n    TypeError\n        If ndarray-like but cannot infer the dtype\n\n    Notes\n    -----\n    - 'mixed' is the catchall for anything that is not otherwise\n      specialized\n    - 'mixed-integer-float' are floats and integers\n    - 'mixed-integer' are integers mixed with non-integers\n    - 'unknown-array' is the catchall for something that *is* an array (has\n      a dtype attribute), but has a dtype unknown to pandas (e.g. external\n      extension array)\n\n    Examples\n    --------\n    >>> from pandas.api.types import infer_dtype\n    >>> infer_dtype(['foo', 'bar'])\n    'string'\n\n    >>> infer_dtype(['a', np.nan, 'b'], skipna=True)\n    'string'\n\n    >>> infer_dtype(['a', np.nan, 'b'], skipna=False)\n    'mixed'\n\n    >>> infer_dtype([b'foo', b'bar'])\n    'bytes'\n\n    >>> infer_dtype([1, 2, 3])\n    'integer'\n\n    >>> infer_dtype([1, 2, 3.5])\n    'mixed-integer-float'\n\n    >>> infer_dtype([1.0, 2.0, 3.5])\n    'floating'\n\n    >>> infer_dtype(['a', 1])\n    'mixed-integer'\n\n    >>> from decimal import Decimal\n    >>> infer_dtype([Decimal(1), Decimal(2.0)])\n    'decimal'\n\n    >>> infer_dtype([True, False])\n    'boolean'\n\n    >>> infer_dtype([True, False, np.nan])\n    'boolean'\n\n    >>> infer_dtype([pd.Timestamp('20130101')])\n    'datetime'\n\n    >>> import datetime\n    >>> infer_dtype([datetime.date(2013, 1, 1)])\n    'date'\n\n    >>> infer_dtype([np.datetime64('2013-01-01')])\n    'datetime64'\n\n    >>> infer_dtype([datetime.timedelta(0, 1, 1)])\n    'timedelta'\n\n    >>> infer_dtype(pd.Series(list('aabc')).astype('category'))\n    'categorical'\n    ",
    'is_bool (line 1138)': '\n    Return True if given object is boolean.\n\n    Returns\n    -------\n    bool\n\n    Examples\n    --------\n    >>> pd.api.types.is_bool(True)\n    True\n\n    >>> pd.api.types.is_bool(1)\n    False\n    ',
    'is_complex (line 1157)': '\n    Return True if given object is complex.\n\n    Returns\n    -------\n    bool\n\n    Examples\n    --------\n    >>> pd.api.types.is_complex(1 + 1j)\n    True\n\n    >>> pd.api.types.is_complex(1)\n    False\n    ',
    'is_float (line 1089)': '\n    Return True if given object is float.\n\n    Returns\n    -------\n    bool\n\n    Examples\n    --------\n    >>> pd.api.types.is_float(1.0)\n    True\n\n    >>> pd.api.types.is_float(1)\n    False\n    ',
    'is_integer (line 1108)': '\n    Return True if given object is integer.\n\n    Returns\n    -------\n    bool\n\n    Examples\n    --------\n    >>> pd.api.types.is_integer(1)\n    True\n\n    >>> pd.api.types.is_integer(1.0)\n    False\n    ',
    'is_iterator (line 254)': '\n    Check if the object is an iterator.\n\n    This is intended for generators, not list-like objects.\n\n    Parameters\n    ----------\n    obj : The object to check\n\n    Returns\n    -------\n    is_iter : bool\n        Whether `obj` is an iterator.\n\n    Examples\n    --------\n    >>> import datetime\n    >>> from pandas.api.types import is_iterator\n    >>> is_iterator((x for x in []))\n    True\n    >>> is_iterator([1, 2, 3])\n    False\n    >>> is_iterator(datetime.datetime(2017, 1, 1))\n    False\n    >>> is_iterator("foo")\n    False\n    >>> is_iterator(1)\n    False\n    ',
    'is_list_like (line 1217)': '\n    Check if the object is list-like.\n\n    Objects that are considered list-like are for example Python\n    lists, tuples, sets, NumPy arrays, and Pandas Series.\n\n    Strings and datetime objects, however, are not considered list-like.\n\n    Parameters\n    ----------\n    obj : object\n        Object to check.\n    allow_sets : bool, default True\n        If this parameter is False, sets will not be considered list-like.\n\n    Returns\n    -------\n    bool\n        Whether `obj` has list-like properties.\n\n    Examples\n    --------\n    >>> import datetime\n    >>> from pandas.api.types import is_list_like\n    >>> is_list_like([1, 2, 3])\n    True\n    >>> is_list_like({1, 2, 3})\n    True\n    >>> is_list_like(datetime.datetime(2017, 1, 1))\n    False\n    >>> is_list_like("foo")\n    False\n    >>> is_list_like(1)\n    False\n    >>> is_list_like(np.array([2]))\n    True\n    >>> is_list_like(np.array(2))\n    False\n    ',
    'is_scalar (line 160)': '\n    Return True if given object is scalar.\n\n    Parameters\n    ----------\n    val : object\n        This includes:\n\n        - numpy array scalar (e.g. np.int64)\n        - Python builtin numerics\n        - Python builtin byte arrays and strings\n        - None\n        - datetime.datetime\n        - datetime.timedelta\n        - Period\n        - decimal.Decimal\n        - Interval\n        - DateOffset\n        - Fraction\n        - Number.\n\n    Returns\n    -------\n    bool\n        Return True if given object is scalar.\n\n    Examples\n    --------\n    >>> import datetime\n    >>> dt = datetime.datetime(2018, 10, 3)\n    >>> pd.api.types.is_scalar(dt)\n    True\n\n    >>> pd.api.types.is_scalar([2, 3])\n    False\n\n    >>> pd.api.types.is_scalar({0: 1, 2: 3})\n    False\n\n    >>> pd.api.types.is_scalar((0, 2))\n    False\n\n    pandas supports PEP 3141 numbers:\n\n    >>> from fractions import Fraction\n    >>> pd.api.types.is_scalar(Fraction(3, 5))\n    True\n    ',
    'item_from_zerodim (line 287)': "\n    If the value is a zerodim array, return the item it contains.\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    object\n\n    Examples\n    --------\n    >>> item_from_zerodim(1)\n    1\n    >>> item_from_zerodim('foobar')\n    'foobar'\n    >>> item_from_zerodim(np.array(1))\n    1\n    >>> item_from_zerodim(np.array([1]))\n    array([1])\n    ",
}

