# encoding: utf-8
# module pandas._libs.parsers
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\parsers.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\warnings.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
import pandas._libs.lib as lib # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\lib.cp313-win_amd64.pyd
import numpy as __numpy
import pandas.core.arraylike as __pandas_core_arraylike
import pandas.core.arrays.base as __pandas_core_arrays_base
import pandas.core.arrays.masked as __pandas_core_arrays_masked
import pandas.core.arrays.numeric as __pandas_core_arrays_numeric
import pandas.core.arrays._arrow_string_mixins as __pandas_core_arrays__arrow_string_mixins
import pandas.core.dtypes.base as __pandas_core_dtypes_base
import pandas.core.dtypes.dtypes as __pandas_core_dtypes_dtypes
import pandas.core.strings.base as __pandas_core_strings_base


# Variables with simple values

DEFAULT_BUFFER_HEURISTIC = 1048576

QUOTE_MINIMAL = 0
QUOTE_NONE = 3
QUOTE_NONNUMERIC = 2

# functions

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

def is_dict_like(obj): # reliably restored by inspect
    """
    Check if the object is dict-like.
    
    Parameters
    ----------
    obj : The object to check
    
    Returns
    -------
    bool
        Whether `obj` has dict-like properties.
    
    Examples
    --------
    >>> from pandas.api.types import is_dict_like
    >>> is_dict_like({1: 2})
    True
    >>> is_dict_like([1, 2, 3])
    False
    >>> is_dict_like(dict)
    False
    >>> is_dict_like(dict())
    True
    """
    pass

def sanitize_objects(*args, **kwargs): # real signature unknown
    """
    Convert specified values, including the given set na_values to np.nan.
    
        Parameters
        ----------
        values : ndarray[object]
        na_values : set
    
        Returns
        -------
        na_count : int
    """
    pass

def _compute_na_values(*args, **kwargs): # real signature unknown
    pass

def _ensure_encoded(*args, **kwargs): # real signature unknown
    pass

def _maybe_upcast(*args, **kwargs): # real signature unknown
    """
    Sets nullable dtypes or upcasts if nans are present.
    
        Upcast, if use_dtype_backend is false and nans are present so that the
        current dtype can not hold the na value. We use nullable dtypes if the
        flag is true for every array.
    
        Parameters
        ----------
        arr: ndarray
            Numpy array that is potentially being upcast.
    
        use_dtype_backend: bool, default False
            If true, we cast to the associated nullable dtypes.
    
        Returns
        -------
        The casted array.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class ArrowExtensionArray(__pandas_core_arraylike.OpsMixin, __pandas_core_arrays_base.ExtensionArraySupportsAnyAll, __pandas_core_arrays__arrow_string_mixins.ArrowStringArrayMixin, __pandas_core_strings_base.BaseStringArrayMethods):
    """
    Pandas ExtensionArray backed by a PyArrow ChunkedArray.
    
    .. warning::
    
       ArrowExtensionArray is considered experimental. The implementation and
       parts of the API may change without warning.
    
    Parameters
    ----------
    values : pyarrow.Array or pyarrow.ChunkedArray
    
    Attributes
    ----------
    None
    
    Methods
    -------
    None
    
    Returns
    -------
    ArrowExtensionArray
    
    Notes
    -----
    Most methods are implemented using `pyarrow compute functions. <https://arrow.apache.org/docs/python/api/compute.html>`__
    Some methods may either raise an exception or raise a ``PerformanceWarning`` if an
    associated compute function is not available based on the installed version of PyArrow.
    
    Please install the latest version of PyArrow to enable the best functionality and avoid
    potential bugs in prior versions of PyArrow.
    
    Examples
    --------
    Create an ArrowExtensionArray with :func:`pandas.array`:
    
    >>> pd.array([1, 1, None], dtype="int64[pyarrow]")
    <ArrowExtensionArray>
    [1, 1, <NA>]
    Length: 3, dtype: int64[pyarrow]
    """
    def all(self, *, skipna=True, **kwargs): # reliably restored by inspect
        """
        Return whether all elements are truthy.
        
        Returns True unless there is at least one element that is falsey.
        By default, NAs are skipped. If ``skipna=False`` is specified and
        missing values are present, similar :ref:`Kleene logic <boolean.kleene>`
        is used as for logical operations.
        
        Parameters
        ----------
        skipna : bool, default True
            Exclude NA values. If the entire array is NA and `skipna` is
            True, then the result will be True, as for an empty array.
            If `skipna` is False, the result will still be False if there is
            at least one element that is falsey, otherwise NA will be returned
            if there are NA's present.
        
        Returns
        -------
        bool or :attr:`pandas.NA`
        
        See Also
        --------
        ArrowExtensionArray.any : Return whether any element is truthy.
        
        Examples
        --------
        The result indicates whether all elements are truthy (and by default
        skips NAs):
        
        >>> pd.array([True, True, pd.NA], dtype="boolean[pyarrow]").all()
        True
        >>> pd.array([1, 1, pd.NA], dtype="boolean[pyarrow]").all()
        True
        >>> pd.array([True, False, pd.NA], dtype="boolean[pyarrow]").all()
        False
        >>> pd.array([], dtype="boolean[pyarrow]").all()
        True
        >>> pd.array([pd.NA], dtype="boolean[pyarrow]").all()
        True
        >>> pd.array([pd.NA], dtype="float64[pyarrow]").all()
        True
        
        With ``skipna=False``, the result can be NA if this is logically
        required (whether ``pd.NA`` is True or False influences the result):
        
        >>> pd.array([True, True, pd.NA], dtype="boolean[pyarrow]").all(skipna=False)
        <NA>
        >>> pd.array([1, 1, pd.NA], dtype="boolean[pyarrow]").all(skipna=False)
        <NA>
        >>> pd.array([True, False, pd.NA], dtype="boolean[pyarrow]").all(skipna=False)
        False
        >>> pd.array([1, 0, pd.NA], dtype="boolean[pyarrow]").all(skipna=False)
        False
        """
        pass

    def any(self, *, skipna=True, **kwargs): # reliably restored by inspect
        """
        Return whether any element is truthy.
        
        Returns False unless there is at least one element that is truthy.
        By default, NAs are skipped. If ``skipna=False`` is specified and
        missing values are present, similar :ref:`Kleene logic <boolean.kleene>`
        is used as for logical operations.
        
        Parameters
        ----------
        skipna : bool, default True
            Exclude NA values. If the entire array is NA and `skipna` is
            True, then the result will be False, as for an empty array.
            If `skipna` is False, the result will still be True if there is
            at least one element that is truthy, otherwise NA will be returned
            if there are NA's present.
        
        Returns
        -------
        bool or :attr:`pandas.NA`
        
        See Also
        --------
        ArrowExtensionArray.all : Return whether all elements are truthy.
        
        Examples
        --------
        The result indicates whether any element is truthy (and by default
        skips NAs):
        
        >>> pd.array([True, False, True], dtype="boolean[pyarrow]").any()
        True
        >>> pd.array([True, False, pd.NA], dtype="boolean[pyarrow]").any()
        True
        >>> pd.array([False, False, pd.NA], dtype="boolean[pyarrow]").any()
        False
        >>> pd.array([], dtype="boolean[pyarrow]").any()
        False
        >>> pd.array([pd.NA], dtype="boolean[pyarrow]").any()
        False
        >>> pd.array([pd.NA], dtype="float64[pyarrow]").any()
        False
        
        With ``skipna=False``, the result can be NA if this is logically
        required (whether ``pd.NA`` is True or False influences the result):
        
        >>> pd.array([True, False, pd.NA], dtype="boolean[pyarrow]").any(skipna=False)
        True
        >>> pd.array([1, 0, pd.NA], dtype="boolean[pyarrow]").any(skipna=False)
        True
        >>> pd.array([False, False, pd.NA], dtype="boolean[pyarrow]").any(skipna=False)
        <NA>
        >>> pd.array([0, 0, pd.NA], dtype="boolean[pyarrow]").any(skipna=False)
        <NA>
        """
        pass

    def argmax(self, skipna=True): # reliably restored by inspect
        # no doc
        pass

    def argmin(self, skipna=True): # reliably restored by inspect
        # no doc
        pass

    def argsort(self, *, ascending=True, kind=None, na_position=None, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def copy(self): # reliably restored by inspect
        """
        Return a shallow copy of the array.
        
        Underlying ChunkedArray is immutable, so a deep copy is unnecessary.
        
        Returns
        -------
        type(self)
        """
        pass

    def dropna(self): # reliably restored by inspect
        """
        Return ArrowExtensionArray without NA values.
        
        Returns
        -------
        ArrowExtensionArray
        """
        pass

    def duplicated(self, keep=None): # reliably restored by inspect
        """
        Return boolean ndarray denoting duplicate values.
        
        Parameters
        ----------
        keep : {'first', 'last', False}, default 'first'
            - ``first`` : Mark duplicates as ``True`` except for the first occurrence.
            - ``last`` : Mark duplicates as ``True`` except for the last occurrence.
            - False : Mark all duplicates as ``True``.
        
        Returns
        -------
        ndarray[bool]
        
        Examples
        --------
        >>> pd.array([1, 1, 2, 3, 3], dtype="Int64").duplicated()
        array([False,  True, False, False,  True])
        """
        pass

    def equals(self, other): # reliably restored by inspect
        # no doc
        pass

    def factorize(self, use_na_sentinel=True): # reliably restored by inspect
        """
        Encode the extension array as an enumerated type.
        
        Parameters
        ----------
        use_na_sentinel : bool, default True
            If True, the sentinel -1 will be used for NaN values. If False,
            NaN values will be encoded as non-negative integers and will not drop the
            NaN from the uniques of the values.
        
            .. versionadded:: 1.5.0
        
        Returns
        -------
        codes : ndarray
            An integer NumPy array that's an indexer into the original
            ExtensionArray.
        uniques : ExtensionArray
            An ExtensionArray containing the unique values of `self`.
        
            .. note::
        
               uniques will *not* contain an entry for the NA value of
               the ExtensionArray if there are any missing values present
               in `self`.
        
        See Also
        --------
        factorize : Top-level factorize method that dispatches here.
        
        Notes
        -----
        :meth:`pandas.factorize` offers a `sort` keyword as well.
        
        Examples
        --------
        >>> idx1 = pd.PeriodIndex(["2014-01", "2014-01", "2014-02", "2014-02",
        ...                       "2014-03", "2014-03"], freq="M")
        >>> arr, idx = idx1.factorize()
        >>> arr
        array([0, 0, 1, 1, 2, 2])
        >>> idx
        PeriodIndex(['2014-01', '2014-02', '2014-03'], dtype='period[M]')
        """
        pass

    def fillna(self, value=None, method=None, limit=None, copy=True): # reliably restored by inspect
        """
        Fill NA/NaN values using the specified method.
        
        Parameters
        ----------
        value : scalar, array-like
            If a scalar value is passed it is used to fill all missing values.
            Alternatively, an array-like "value" can be given. It's expected
            that the array-like have the same length as 'self'.
        method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
            Method to use for filling holes in reindexed Series:
        
            * pad / ffill: propagate last valid observation forward to next valid.
            * backfill / bfill: use NEXT valid observation to fill gap.
        
            .. deprecated:: 2.1.0
        
        limit : int, default None
            If method is specified, this is the maximum number of consecutive
            NaN values to forward/backward fill. In other words, if there is
            a gap with more than this number of consecutive NaNs, it will only
            be partially filled. If method is not specified, this is the
            maximum number of entries along the entire axis where NaNs will be
            filled.
        
            .. deprecated:: 2.1.0
        
        copy : bool, default True
            Whether to make a copy of the data before filling. If False, then
            the original should be modified and no new memory should be allocated.
            For ExtensionArray subclasses that cannot do this, it is at the
            author's discretion whether to ignore "copy=False" or to raise.
            The base class implementation ignores the keyword in pad/backfill
            cases.
        
        Returns
        -------
        ExtensionArray
            With NA/NaN filled.
        
        Examples
        --------
        >>> arr = pd.array([np.nan, np.nan, 2, 3, np.nan, np.nan])
        >>> arr.fillna(0)
        <IntegerArray>
        [0, 0, 2, 3, 0, 0]
        Length: 6, dtype: Int64
        """
        pass

    def interpolate(self, *, method, axis, index, limit, limit_direction, limit_area, copy, **kwargs): # reliably restored by inspect
        """ See NDFrame.interpolate.__doc__. """
        pass

    def isin(self, values): # reliably restored by inspect
        # no doc
        pass

    def isna(self): # reliably restored by inspect
        """
        Boolean NumPy array indicating if each value is missing.
        
        This should return a 1-D array the same length as 'self'.
        """
        pass

    def map(self, mapper, na_action=None): # reliably restored by inspect
        # no doc
        pass

    def reshape(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def round(self, decimals=0, *args, **kwargs): # reliably restored by inspect
        """
        Round each value in the array a to the given number of decimals.
        
        Parameters
        ----------
        decimals : int, default 0
            Number of decimal places to round to. If decimals is negative,
            it specifies the number of positions to the left of the decimal point.
        *args, **kwargs
            Additional arguments and keywords have no effect.
        
        Returns
        -------
        ArrowExtensionArray
            Rounded values of the ArrowExtensionArray.
        
        See Also
        --------
        DataFrame.round : Round values of a DataFrame.
        Series.round : Round values of a Series.
        """
        pass

    def searchsorted(self, value, side=None, sorter=None): # reliably restored by inspect
        """
        Find indices where elements should be inserted to maintain order.
        
        Find the indices into a sorted array `self` (a) such that, if the
        corresponding elements in `value` were inserted before the indices,
        the order of `self` would be preserved.
        
        Assuming that `self` is sorted:
        
        ======  ================================
        `side`  returned index `i` satisfies
        ======  ================================
        left    ``self[i-1] < value <= self[i]``
        right   ``self[i-1] <= value < self[i]``
        ======  ================================
        
        Parameters
        ----------
        value : array-like, list or scalar
            Value(s) to insert into `self`.
        side : {'left', 'right'}, optional
            If 'left', the index of the first suitable location found is given.
            If 'right', return the last such index.  If there is no suitable
            index, return either 0 or N (where N is the length of `self`).
        sorter : 1-D array-like, optional
            Optional array of integer indices that sort array a into ascending
            order. They are typically the result of argsort.
        
        Returns
        -------
        array of ints or int
            If value is array-like, array of insertion points.
            If value is scalar, a single integer.
        
        See Also
        --------
        numpy.searchsorted : Similar method from NumPy.
        
        Examples
        --------
        >>> arr = pd.array([1, 2, 3, 5])
        >>> arr.searchsorted([4])
        array([3])
        """
        pass

    def take(self, indices, allow_fill=False, fill_value=None): # reliably restored by inspect
        """
        Take elements from an array.
        
        Parameters
        ----------
        indices : sequence of int or one-dimensional np.ndarray of int
            Indices to be taken.
        allow_fill : bool, default False
            How to handle negative values in `indices`.
        
            * False: negative values in `indices` indicate positional indices
              from the right (the default). This is similar to
              :func:`numpy.take`.
        
            * True: negative values in `indices` indicate
              missing values. These values are set to `fill_value`. Any other
              other negative values raise a ``ValueError``.
        
        fill_value : any, optional
            Fill value to use for NA-indices when `allow_fill` is True.
            This may be ``None``, in which case the default NA value for
            the type, ``self.dtype.na_value``, is used.
        
            For many ExtensionArrays, there will be two representations of
            `fill_value`: a user-facing "boxed" scalar, and a low-level
            physical NA value. `fill_value` should be the user-facing version,
            and the implementation should handle translating that to the
            physical version for processing the take if necessary.
        
        Returns
        -------
        ExtensionArray
        
        Raises
        ------
        IndexError
            When the indices are out of bounds for the array.
        ValueError
            When `indices` contains negative values other than ``-1``
            and `allow_fill` is True.
        
        See Also
        --------
        numpy.take
        api.extensions.take
        
        Notes
        -----
        ExtensionArray.take is called by ``Series.__getitem__``, ``.loc``,
        ``iloc``, when `indices` is a sequence of values. Additionally,
        it's called by :meth:`Series.reindex`, or any other method
        that causes realignment, with a `fill_value`.
        """
        pass

    def to_numpy(self, dtype=None, copy=False, na_value='<no_default>'): # reliably restored by inspect
        """
        Convert to a NumPy ndarray.
        
        This is similar to :meth:`numpy.asarray`, but may provide additional control
        over how the conversion is done.
        
        Parameters
        ----------
        dtype : str or numpy.dtype, optional
            The dtype to pass to :meth:`numpy.asarray`.
        copy : bool, default False
            Whether to ensure that the returned value is a not a view on
            another array. Note that ``copy=False`` does not *ensure* that
            ``to_numpy()`` is no-copy. Rather, ``copy=True`` ensure that
            a copy is made, even if not strictly necessary.
        na_value : Any, optional
            The value to use for missing values. The default value depends
            on `dtype` and the type of the array.
        
        Returns
        -------
        numpy.ndarray
        """
        pass

    def unique(self): # reliably restored by inspect
        """
        Compute the ArrowExtensionArray of unique values.
        
        Returns
        -------
        ArrowExtensionArray
        """
        pass

    def value_counts(self, dropna=True): # reliably restored by inspect
        """
        Return a Series containing counts of each unique value.
        
        Parameters
        ----------
        dropna : bool, default True
            Don't include counts of missing values.
        
        Returns
        -------
        counts : Series
        
        See Also
        --------
        Series.value_counts
        """
        pass

    def _accumulate(self, name, *, skipna=True, **kwargs): # reliably restored by inspect
        """
        Return an ExtensionArray performing an accumulation operation.
        
        The underlying data type might change.
        
        Parameters
        ----------
        name : str
            Name of the function, supported values are:
            - cummin
            - cummax
            - cumsum
            - cumprod
        skipna : bool, default True
            If True, skip NA values.
        **kwargs
            Additional keyword arguments passed to the accumulation function.
            Currently, there is no supported kwarg.
        
        Returns
        -------
        array
        
        Raises
        ------
        NotImplementedError : subclass does not define accumulations
        """
        pass

    def _apply_elementwise(self, func): # reliably restored by inspect
        """ Apply a callable to each element while maintaining the chunking structure. """
        pass

    def _argmin_max(self, skipna, method): # reliably restored by inspect
        # no doc
        pass

    def _arith_method(self, other, op): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _box_pa(cls, *args, **kwargs): # real signature unknown
        """
        Box value into a pyarrow Array, ChunkedArray or Scalar.
        
        Parameters
        ----------
        value : any
        pa_type : pa.DataType | None
        
        Returns
        -------
        pa.Array or pa.ChunkedArray or pa.Scalar
        """
        pass

    @classmethod
    def _box_pa_array(cls, *args, **kwargs): # real signature unknown
        """
        Box value into a pyarrow Array or ChunkedArray.
        
        Parameters
        ----------
        value : Sequence
        pa_type : pa.DataType | None
        
        Returns
        -------
        pa.Array or pa.ChunkedArray
        """
        pass

    @classmethod
    def _box_pa_scalar(cls, *args, **kwargs): # real signature unknown
        """
        Box value into a pyarrow Scalar.
        
        Parameters
        ----------
        value : any
        pa_type : pa.DataType | None
        
        Returns
        -------
        pa.Scalar
        """
        pass

    def _cmp_method(self, other, op): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _concat_same_type(cls, *args, **kwargs): # real signature unknown
        """
        Concatenate multiple ArrowExtensionArrays.
        
        Parameters
        ----------
        to_concat : sequence of ArrowExtensionArrays
        
        Returns
        -------
        ArrowExtensionArray
        """
        pass

    def _convert_bool_result(self, result, na='<no_default>', method_name=None): # reliably restored by inspect
        # no doc
        pass

    def _convert_int_result(self, result): # reliably restored by inspect
        # no doc
        pass

    def _convert_rank_result(self, result): # reliably restored by inspect
        # no doc
        pass

    def _dt_as_unit(self, unit): # reliably restored by inspect
        # no doc
        pass

    def _dt_ceil(self, freq, ambiguous=None, nonexistent=None): # reliably restored by inspect
        # no doc
        pass

    def _dt_day_name(self, locale=None): # reliably restored by inspect
        # no doc
        pass

    def _dt_floor(self, freq, ambiguous=None, nonexistent=None): # reliably restored by inspect
        # no doc
        pass

    def _dt_isocalendar(self): # reliably restored by inspect
        # no doc
        pass

    def _dt_month_name(self, locale=None): # reliably restored by inspect
        # no doc
        pass

    def _dt_normalize(self): # reliably restored by inspect
        # no doc
        pass

    def _dt_round(self, freq, ambiguous=None, nonexistent=None): # reliably restored by inspect
        # no doc
        pass

    def _dt_strftime(self, format): # reliably restored by inspect
        # no doc
        pass

    def _dt_total_seconds(self): # reliably restored by inspect
        # no doc
        pass

    def _dt_to_pydatetime(self): # reliably restored by inspect
        # no doc
        pass

    def _dt_to_pytimedelta(self): # reliably restored by inspect
        # no doc
        pass

    def _dt_tz_convert(self, tz): # reliably restored by inspect
        # no doc
        pass

    def _dt_tz_localize(self, tz, ambiguous=None, nonexistent=None): # reliably restored by inspect
        # no doc
        pass

    def _evaluate_op_method(self, other, op, arrow_funcs): # reliably restored by inspect
        # no doc
        pass

    def _explode(self): # reliably restored by inspect
        """ See Series.explode.__doc__. """
        pass

    @classmethod
    def _from_sequence(cls, *args, **kwargs): # real signature unknown
        """ Construct a new ExtensionArray from a sequence of scalars. """
        pass

    @classmethod
    def _from_sequence_of_strings(cls, *args, **kwargs): # real signature unknown
        """ Construct a new ExtensionArray from a sequence of strings. """
        pass

    def _groupby_op(self, *, how, has_dropped_na, min_count, ngroups, ids, **kwargs): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _if_else(cls, *args, **kwargs): # real signature unknown
        """
        Choose values based on a condition.
        
        Analogous to pyarrow.compute.if_else, with logic
        to fallback to numpy for unsupported types.
        
        Parameters
        ----------
        cond : npt.NDArray[np.bool_] or bool
        left : ArrayLike | Scalar
        right : ArrayLike | Scalar
        
        Returns
        -------
        pa.Array
        """
        pass

    def _logical_method(self, other, op): # reliably restored by inspect
        # no doc
        pass

    def _maybe_convert_datelike_array(self): # reliably restored by inspect
        """ Maybe convert to a datelike array. """
        pass

    def _maybe_convert_setitem_value(self, value): # reliably restored by inspect
        """ Maybe convert value to be pyarrow compatible. """
        pass

    def _mode(self, dropna=True): # reliably restored by inspect
        """
        Returns the mode(s) of the ExtensionArray.
        
        Always returns `ExtensionArray` even if only one value.
        
        Parameters
        ----------
        dropna : bool, default True
            Don't consider counts of NA values.
        
        Returns
        -------
        same type as self
            Sorted, if possible.
        """
        pass

    def _op_method_error_message(self, other, op): # reliably restored by inspect
        # no doc
        pass

    def _pad_or_backfill(self, *, method, limit=None, limit_area=None, copy=True): # reliably restored by inspect
        # no doc
        pass

    def _quantile(self, qs, interpolation): # reliably restored by inspect
        """
        Compute the quantiles of self for each quantile in `qs`.
        
        Parameters
        ----------
        qs : np.ndarray[float64]
        interpolation: str
        
        Returns
        -------
        same type as self
        """
        pass

    def _rank(self, *, axis=0, method=None, na_option=None, ascending=True, pct=False): # reliably restored by inspect
        """ See Series.rank.__doc__. """
        pass

    def _rank_calc(self, *, axis=0, method=None, na_option=None, ascending=True, pct=False): # reliably restored by inspect
        # no doc
        pass

    def _reduce(self, name, *, skipna=True, keepdims=False, **kwargs): # reliably restored by inspect
        """
        Return a scalar result of performing the reduction operation.
        
        Parameters
        ----------
        name : str
            Name of the function, supported values are:
            { any, all, min, max, sum, mean, median, prod,
            std, var, sem, kurt, skew }.
        skipna : bool, default True
            If True, skip NaN values.
        **kwargs
            Additional keyword arguments passed to the reduction function.
            Currently, `ddof` is the only supported kwarg.
        
        Returns
        -------
        scalar
        
        Raises
        ------
        TypeError : subclass does not define reductions
        """
        pass

    def _reduce_calc(self, name, *, skipna=True, keepdims=False, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def _reduce_pyarrow(self, name, *, skipna=True, **kwargs): # reliably restored by inspect
        """
        Return a pyarrow scalar result of performing the reduction operation.
        
        Parameters
        ----------
        name : str
            Name of the function, supported values are:
            { any, all, min, max, sum, mean, median, prod,
            std, var, sem, kurt, skew }.
        skipna : bool, default True
            If True, skip NaN values.
        **kwargs
            Additional keyword arguments passed to the reduction function.
            Currently, `ddof` is the only supported kwarg.
        
        Returns
        -------
        pyarrow scalar
        
        Raises
        ------
        TypeError : subclass does not define reductions
        """
        pass

    @classmethod
    def _replace_with_mask(cls, *args, **kwargs): # real signature unknown
        """
        Replace items selected with a mask.
        
        Analogous to pyarrow.compute.replace_with_mask, with logic
        to fallback to numpy for unsupported types.
        
        Parameters
        ----------
        values : pa.Array or pa.ChunkedArray
        mask : npt.NDArray[np.bool_] or bool
        replacements : ArrayLike or Scalar
            Replacement value(s)
        
        Returns
        -------
        pa.Array or pa.ChunkedArray
        """
        pass

    def _round_temporally(self, method, freq, ambiguous=None, nonexistent=None): # reliably restored by inspect
        # no doc
        pass

    def _str_accumulate(self, name, *, skipna=True, **kwargs): # reliably restored by inspect
        """
        Accumulate implementation for strings, see `_accumulate` docstring for details.
        
        pyarrow.compute does not implement these methods for strings.
        """
        pass

    def _str_casefold(self): # reliably restored by inspect
        # no doc
        pass

    def _str_count(self, pat, flags=0): # reliably restored by inspect
        # no doc
        pass

    def _str_encode(self, encoding, errors=None): # reliably restored by inspect
        # no doc
        pass

    def _str_extract(self, pat, flags=0, expand=True): # reliably restored by inspect
        # no doc
        pass

    def _str_findall(self, pat, flags=0): # reliably restored by inspect
        # no doc
        pass

    def _str_get_dummies(self, sep=None): # reliably restored by inspect
        # no doc
        pass

    def _str_index(self, sub, start=0, end=None): # reliably restored by inspect
        # no doc
        pass

    def _str_join(self, sep): # reliably restored by inspect
        # no doc
        pass

    def _str_normalize(self, form): # reliably restored by inspect
        # no doc
        pass

    def _str_partition(self, sep, expand): # reliably restored by inspect
        # no doc
        pass

    def _str_repeat(self, repeats): # reliably restored by inspect
        # no doc
        pass

    def _str_rfind(self, sub, start=0, end=None): # reliably restored by inspect
        # no doc
        pass

    def _str_rindex(self, sub, start=0, end=None): # reliably restored by inspect
        # no doc
        pass

    def _str_rpartition(self, sep, expand): # reliably restored by inspect
        # no doc
        pass

    def _str_rsplit(self, pat=None, n=-1): # reliably restored by inspect
        # no doc
        pass

    def _str_split(self, pat=None, n=-1, expand=False, regex=None): # reliably restored by inspect
        # no doc
        pass

    def _str_translate(self, table): # reliably restored by inspect
        # no doc
        pass

    def _str_wrap(self, width, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def _to_datetimearray(self): # reliably restored by inspect
        """ Convert a pyarrow timestamp typed array to a DatetimeArray. """
        pass

    def _to_masked(self): # reliably restored by inspect
        # no doc
        pass

    def _to_timedeltaarray(self): # reliably restored by inspect
        """ Convert a pyarrow duration typed array to a TimedeltaArray. """
        pass

    def _values_for_factorize(self): # reliably restored by inspect
        """
        Return an array and missing value suitable for factorization.
        
        Returns
        -------
        values : ndarray
        na_value : pd.NA
        
        Notes
        -----
        The values returned by this method are also used in
        :func:`pandas.util.hash_pandas_object`.
        """
        pass

    def _values_for_json(self): # reliably restored by inspect
        # no doc
        pass

    def __abs__(self): # reliably restored by inspect
        # no doc
        pass

    def __array__(self, dtype=None, copy=None): # reliably restored by inspect
        """ Correctly construct numpy arrays when passed to `np.asarray()`. """
        pass

    def __arrow_array__(self, type=None): # reliably restored by inspect
        """ Convert myself to a pyarrow ChunkedArray. """
        pass

    def __contains__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(self, item): # reliably restored by inspect
        """
        Select a subset of self.
        
        Parameters
        ----------
        item : int, slice, or ndarray
            * int: The position in 'self' to get.
            * slice: A slice object, where 'start', 'stop', and 'step' are
              integers or None
            * ndarray: A 1-d boolean NumPy ndarray the same length as 'self'
        
        Returns
        -------
        item : scalar or ExtensionArray
        
        Notes
        -----
        For scalar ``item``, return a scalar value suitable for the array's
        type. This should be an instance of ``self.dtype.type``.
        For slice ``key``, return an instance of ``ExtensionArray``, even
        if the slice is length 0 or 1.
        For a boolean mask, return an instance of ``ExtensionArray``, filtered
        to the values where ``item`` is True.
        """
        pass

    def __getstate__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, values): # reliably restored by inspect
        # no doc
        pass

    def __invert__(self): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        """ Iterate over elements of the array. """
        pass

    def __len__(self): # reliably restored by inspect
        """
        Length of this array.
        
        Returns
        -------
        length : int
        """
        pass

    def __neg__(self): # reliably restored by inspect
        # no doc
        pass

    def __pos__(self): # reliably restored by inspect
        # no doc
        pass

    def __setitem__(self, key, value): # reliably restored by inspect
        """
        Set one or more values inplace.
        
        Parameters
        ----------
        key : int, ndarray, or slice
            When called from, e.g. ``Series.__setitem__``, ``key`` will be
            one of
        
            * scalar int
            * ndarray of integers.
            * boolean ndarray
            * slice object
        
        value : ExtensionDtype.type, Sequence[ExtensionDtype.type], or object
            value or values to be set of ``key``.
        
        Returns
        -------
        None
        """
        pass

    def __setstate__(self, state): # reliably restored by inspect
        # no doc
        pass

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
An instance of 'ExtensionDtype'.
"""

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The number of bytes needed to store this object in memory.
"""

    _dt_date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_day_of_week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_day_of_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_milliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dt_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _hasna = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x000001A453466680>'
    __abstractmethods__ = frozenset()
    __annotations__ = {
        '_dtype': 'ArrowDtype',
        '_pa_array': 'pa.ChunkedArray',
    }
    __firstlineno__ = 240
    __static_attributes__ = (
        '_dtype',
        '_pa_array',
    )


class BooleanArray(__pandas_core_arrays_masked.BaseMaskedArray):
    """
    Array of boolean (True/False) data with missing values.
    
    This is a pandas Extension array for boolean data, under the hood
    represented by 2 numpy arrays: a boolean array with the data and
    a boolean array with the mask (True indicating missing).
    
    BooleanArray implements Kleene logic (sometimes called three-value
    logic) for logical operations. See :ref:`boolean.kleene` for more.
    
    To construct an BooleanArray from generic array-like input, use
    :func:`pandas.array` specifying ``dtype="boolean"`` (see examples
    below).
    
    .. warning::
    
       BooleanArray is considered experimental. The implementation and
       parts of the API may change without warning.
    
    Parameters
    ----------
    values : numpy.ndarray
        A 1-d boolean-dtype array with the data.
    mask : numpy.ndarray
        A 1-d boolean-dtype array indicating missing values (True
        indicates missing).
    copy : bool, default False
        Whether to copy the `values` and `mask` arrays.
    
    Attributes
    ----------
    None
    
    Methods
    -------
    None
    
    Returns
    -------
    BooleanArray
    
    Examples
    --------
    Create an BooleanArray with :func:`pandas.array`:
    
    >>> pd.array([True, False, None], dtype="boolean")
    <BooleanArray>
    [True, False, <NA>]
    Length: 3, dtype: boolean
    """
    def _accumulate(self, name, *, skipna=True, **kwargs): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _coerce_to_array(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_sequence_of_strings(cls, *args, **kwargs): # real signature unknown
        pass

    def _logical_method(self, other, op): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _simple_new(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, values, mask, copy=False): # reliably restored by inspect
        # no doc
        pass

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _falsey_value = False
    _FALSE_VALUES = None # (!) real value is "{'0.0', 'False', '0', 'FALSE', 'false'}"
    _HANDLED_TYPES = (
        np.ndarray,
        None, # (!) real value is "<class 'numbers.Number'>"
        bool,
        np.bool,
    )
    _internal_fill_value = False
    _TRUE_VALUES = None # (!) real value is "{'1.0', 'True', '1', 'TRUE', 'true'}"
    _truthy_value = True
    __firstlineno__ = 239
    __static_attributes__ = (
        '_dtype',
    )


class ExtensionDtype(object):
    """
    A custom data type, to be paired with an ExtensionArray.
    
    See Also
    --------
    extensions.register_extension_dtype: Register an ExtensionType
        with pandas as class decorator.
    extensions.ExtensionArray: Abstract base class for custom 1-D array types.
    
    Notes
    -----
    The interface includes the following abstract methods that must
    be implemented by subclasses:
    
    * type
    * name
    * construct_array_type
    
    The following attributes and methods influence the behavior of the dtype in
    pandas operations
    
    * _is_numeric
    * _is_boolean
    * _get_common_dtype
    
    The `na_value` class attribute can be used to set the default NA value
    for this type. :attr:`numpy.nan` is used by default.
    
    ExtensionDtypes are required to be hashable. The base class provides
    a default implementation, which relies on the ``_metadata`` class
    attribute. ``_metadata`` should be a tuple containing the strings
    that define your data type. For example, with ``PeriodDtype`` that's
    the ``freq`` attribute.
    
    **If you have a parametrized dtype you should set the ``_metadata``
    class property**.
    
    Ideally, the attributes in ``_metadata`` will match the
    parameters to your ``ExtensionDtype.__init__`` (if any). If any of
    the attributes in ``_metadata`` don't implement the standard
    ``__eq__`` or ``__hash__``, the default implementations here will not
    work.
    
    Examples
    --------
    
    For interaction with Apache Arrow (pyarrow), a ``__from_arrow__`` method
    can be implemented: this method receives a pyarrow Array or ChunkedArray
    as only argument and is expected to return the appropriate pandas
    ExtensionArray for this dtype and the passed values:
    
    >>> import pyarrow
    >>> from pandas.api.extensions import ExtensionArray
    >>> class ExtensionDtype:
    ...     def __from_arrow__(
    ...         self,
    ...         array: pyarrow.Array | pyarrow.ChunkedArray
    ...     ) -> ExtensionArray:
    ...         ...
    
    This class does not inherit from 'abc.ABCMeta' for performance reasons.
    Methods and properties required by the interface raise
    ``pandas.errors.AbstractMethodError`` and no ``register`` method is
    provided for registering virtual subclasses.
    """
    @classmethod
    def construct_array_type(cls, *args, **kwargs): # real signature unknown
        """
        Return the array type associated with this dtype.
        
        Returns
        -------
        type
        """
        pass

    @classmethod
    def construct_from_string(cls, cls_1, string): # real signature unknown; restored from __doc__
        """
        Construct this type from a string.
        
        This is useful mainly for data types that accept parameters.
        For example, a period dtype accepts a frequency parameter that
        can be set as ``period[h]`` (where H means hourly frequency).
        
        By default, in the abstract class, just the name of the type is
        expected. But subclasses can overwrite this method to accept
        parameters.
        
        Parameters
        ----------
        string : str
            The name of the type, for example ``category``.
        
        Returns
        -------
        ExtensionDtype
            Instance of the dtype.
        
        Raises
        ------
        TypeError
            If a class cannot be constructed from this 'string'.
        
        Examples
        --------
        For extension dtypes with arguments the following may be an
        adequate implementation.
        
        >>> import re
        >>> @classmethod
        ... def construct_from_string(cls, string):
        ...     pattern = re.compile(r"^my_type\[(?P<arg_name>.+)\]$")
        ...     match = pattern.match(string)
        ...     if match:
        ...         return cls(**match.groupdict())
        ...     else:
        ...         raise TypeError(
        ...             f"Cannot construct a '{cls.__name__}' from '{string}'"
        ...         )
        """
        pass

    def empty(self, shape): # reliably restored by inspect
        """
        Construct an ExtensionArray of this dtype with the given shape.
        
        Analogous to numpy.empty.
        
        Parameters
        ----------
        shape : int or tuple[int]
        
        Returns
        -------
        ExtensionArray
        """
        pass

    @classmethod
    def is_dtype(cls, *args, **kwargs): # real signature unknown
        """
        Check if we match 'dtype'.
        
        Parameters
        ----------
        dtype : object
            The object to check.
        
        Returns
        -------
        bool
        
        Notes
        -----
        The default implementation is True if
        
        1. ``cls.construct_from_string(dtype)`` is an instance
           of ``cls``.
        2. ``dtype`` is an object and is an instance of ``cls``
        3. ``dtype`` has a ``dtype`` attribute, and any of the above
           conditions is true for ``dtype.dtype``.
        """
        pass

    def _get_common_dtype(self, dtypes): # reliably restored by inspect
        """
        Return the common dtype, if one exists.
        
        Used in `find_common_type` implementation. This is for example used
        to determine the resulting dtype in a concat operation.
        
        If no common dtype exists, return None (which gives the other dtypes
        the chance to determine a common dtype). If all dtypes in the list
        return None, then the common dtype will be "object" dtype (this means
        it is never needed to return "object" dtype from this method itself).
        
        Parameters
        ----------
        dtypes : list of dtypes
            The dtypes for which to determine a common dtype. This is a list
            of np.dtype or ExtensionDtype instances.
        
        Returns
        -------
        Common dtype (np.dtype or ExtensionDtype) or None
        """
        pass

    def __eq__(self, other): # reliably restored by inspect
        """
        Check whether 'other' is equal to self.
        
        By default, 'other' is considered equal if either
        
        * it's a string matching 'self.name'.
        * it's an instance of this type and all of the attributes
          in ``self._metadata`` are equal between `self` and `other`.
        
        Parameters
        ----------
        other : Any
        
        Returns
        -------
        bool
        """
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A character code (one of 'biufcmMOSUV'), default 'O'

This should match the NumPy dtype used when the array is
converted to an ndarray, which is probably 'O' for object if
the extension type cannot be represented as a built-in NumPy
type.

See Also
--------
numpy.dtype.kind
"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A string identifying the data type.

Will be used for display in, e.g. ``Series.dtype``
"""

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Ordered list of field names, or None if there are no fields.

This is for compatibility with NumPy arrays, and may be removed in the
future.
"""

    na_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Default NA value to use for this type.

This is used in e.g. ExtensionArray.take. This should be the
user-facing "boxed" version of the NA value, not the physical NA value
for storage.  e.g. for JSONArray, this is an empty dictionary.
"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The scalar type for the array, e.g. ``int``

It's expected ``ExtensionArray[item]`` returns an instance
of ``ExtensionDtype.type`` for scalar ``item``, assuming
that value is valid (not NA). NA values do not need to be
instances of `type`.
"""

    _can_fast_transpose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Is transposing an array with this dtype zero-copy?

Only relevant for cases where _supports_2d is True.
"""

    _can_hold_na = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Can arrays of this dtype hold NA values?
"""

    _is_boolean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Whether this dtype should be considered boolean.

By default, ExtensionDtypes are assumed to be non-numeric.
Setting this to True will affect the behavior of several places,
e.g.

* is_bool
* boolean indexing

Returns
-------
bool
"""

    _is_immutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Can arrays with this dtype be modified with __setitem__? If not, return
True.

Immutable arrays are expected to raise TypeError on __setitem__ calls.
"""

    _is_numeric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Whether columns with this dtype should be considered numeric.

By default ExtensionDtypes are assumed to be non-numeric.
They'll be excluded from operations that exclude non-numeric
columns, like (groupby) reductions, plotting, etc.
"""

    _supports_2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Do ExtensionArrays with this dtype support 2D arrays?

Historically ExtensionArrays were limited to 1D. By returning True here,
authors can indicate that their arrays support 2D instances. This can
improve performance in some cases, particularly operations with `axis=1`.

Arrays that support 2D values should:

    - implement Array.reshape
    - subclass the Dim2CompatTests in tests.extension.base
    - _concat_same_type should support `axis` keyword
    - _reduce and reductions should support `axis` keyword
"""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    index_class = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4534DEB00>'
    _metadata = ()
    __annotations__ = {
        '_metadata': 'tuple[str, ...]',
    }
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas.core.dtypes.base\', \'__firstlineno__\': 43, \'__annotations__\': {\'_metadata\': \'tuple[str, ...]\'}, \'__doc__\': "\\nA custom data type, to be paired with an ExtensionArray.\\n\\nSee Also\\n--------\\nextensions.register_extension_dtype: Register an ExtensionType\\n    with pandas as class decorator.\\nextensions.ExtensionArray: Abstract base class for custom 1-D array types.\\n\\nNotes\\n-----\\nThe interface includes the following abstract methods that must\\nbe implemented by subclasses:\\n\\n* type\\n* name\\n* construct_array_type\\n\\nThe following attributes and methods influence the behavior of the dtype in\\npandas operations\\n\\n* _is_numeric\\n* _is_boolean\\n* _get_common_dtype\\n\\nThe `na_value` class attribute can be used to set the default NA value\\nfor this type. :attr:`numpy.nan` is used by default.\\n\\nExtensionDtypes are required to be hashable. The base class provides\\na default implementation, which relies on the ``_metadata`` class\\nattribute. ``_metadata`` should be a tuple containing the strings\\nthat define your data type. For example, with ``PeriodDtype`` that\'s\\nthe ``freq`` attribute.\\n\\n**If you have a parametrized dtype you should set the ``_metadata``\\nclass property**.\\n\\nIdeally, the attributes in ``_metadata`` will match the\\nparameters to your ``ExtensionDtype.__init__`` (if any). If any of\\nthe attributes in ``_metadata`` don\'t implement the standard\\n``__eq__`` or ``__hash__``, the default implementations here will not\\nwork.\\n\\nExamples\\n--------\\n\\nFor interaction with Apache Arrow (pyarrow), a ``__from_arrow__`` method\\ncan be implemented: this method receives a pyarrow Array or ChunkedArray\\nas only argument and is expected to return the appropriate pandas\\nExtensionArray for this dtype and the passed values:\\n\\n>>> import pyarrow\\n>>> from pandas.api.extensions import ExtensionArray\\n>>> class ExtensionDtype:\\n...     def __from_arrow__(\\n...         self,\\n...         array: pyarrow.Array | pyarrow.ChunkedArray\\n...     ) -> ExtensionArray:\\n...         ...\\n\\nThis class does not inherit from \'abc.ABCMeta\' for performance reasons.\\nMethods and properties required by the interface raise\\n``pandas.errors.AbstractMethodError`` and no ``register`` method is\\nprovided for registering virtual subclasses.\\n", \'_metadata\': (), \'__str__\': <function ExtensionDtype.__str__ at 0x000001A4534D0AE0>, \'__eq__\': <function ExtensionDtype.__eq__ at 0x000001A4534D2C00>, \'__hash__\': <function ExtensionDtype.__hash__ at 0x000001A4534D2CA0>, \'__ne__\': <function ExtensionDtype.__ne__ at 0x000001A4534D2D40>, \'na_value\': <property object at 0x000001A4534E02C0>, \'type\': <property object at 0x000001A4534E1AD0>, \'kind\': <property object at 0x000001A4534E1030>, \'name\': <property object at 0x000001A4534E1B20>, \'names\': <property object at 0x000001A4534E1B70>, \'construct_array_type\': <classmethod(<function ExtensionDtype.construct_array_type at 0x000001A4534D3100>)>, \'empty\': <function ExtensionDtype.empty at 0x000001A4534D31A0>, \'construct_from_string\': <classmethod(<function ExtensionDtype.construct_from_string at 0x000001A4534D3240>)>, \'is_dtype\': <classmethod(<function ExtensionDtype.is_dtype at 0x000001A4534D32E0>)>, \'_is_numeric\': <property object at 0x000001A4534E1BC0>, \'_is_boolean\': <property object at 0x000001A4534E1C10>, \'_get_common_dtype\': <function ExtensionDtype._get_common_dtype at 0x000001A4534D34C0>, \'_can_hold_na\': <property object at 0x000001A4534E1C60>, \'_is_immutable\': <property object at 0x000001A4534E1CB0>, \'index_class\': <pandas._libs.properties.CachedProperty object at 0x000001A4534DEB00>, \'_supports_2d\': <property object at 0x000001A4534E1D00>, \'_can_fast_transpose\': <property object at 0x000001A4534E1D50>, \'__static_attributes__\': (), \'__dict__\': <attribute \'__dict__\' of \'ExtensionDtype\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'ExtensionDtype\' objects>})'
    __firstlineno__ = 43
    __static_attributes__ = ()


class BooleanDtype(__pandas_core_dtypes_dtypes.BaseMaskedDtype):
    """
    Extension dtype for boolean data.
    
    .. warning::
    
       BooleanDtype is considered experimental. The implementation and
       parts of the API may change without warning.
    
    Attributes
    ----------
    None
    
    Methods
    -------
    None
    
    Examples
    --------
    >>> pd.BooleanDtype()
    BooleanDtype
    """
    @classmethod
    def construct_array_type(cls, *args, **kwargs): # real signature unknown
        """
        Return the array type associated with this dtype.
        
        Returns
        -------
        type
        """
        pass

    def __from_arrow__(self, array): # reliably restored by inspect
        """ Construct BooleanArray from pyarrow Array/ChunkedArray. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numpy_dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_boolean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_numeric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    name = 'boolean'
    __annotations__ = {
        'name': 'ClassVar[str]',
    }
    __firstlineno__ = 40
    __static_attributes__ = ()


class CategoricalDtype(__pandas_core_dtypes_dtypes.PandasExtensionDtype, __pandas_core_dtypes_base.ExtensionDtype):
    """
    Type for categorical data with the categories and orderedness.
    
    Parameters
    ----------
    categories : sequence, optional
        Must be unique, and must not contain any nulls.
        The categories are stored in an Index,
        and if an index is provided the dtype of that index will be used.
    ordered : bool or None, default False
        Whether or not this categorical is treated as a ordered categorical.
        None can be used to maintain the ordered value of existing categoricals when
        used in operations that combine categoricals, e.g. astype, and will resolve to
        False if there is no existing ordered to maintain.
    
    Attributes
    ----------
    categories
    ordered
    
    Methods
    -------
    None
    
    See Also
    --------
    Categorical : Represent a categorical variable in classic R / S-plus fashion.
    
    Notes
    -----
    This class is useful for specifying the type of a ``Categorical``
    independent of the values. See :ref:`categorical.categoricaldtype`
    for more.
    
    Examples
    --------
    >>> t = pd.CategoricalDtype(categories=['b', 'a'], ordered=True)
    >>> pd.Series(['a', 'b', 'a', 'c'], dtype=t)
    0      a
    1      b
    2      a
    3    NaN
    dtype: category
    Categories (2, object): ['b' < 'a']
    
    An empty CategoricalDtype with a specific dtype can be created
    by providing an empty index. As follows,
    
    >>> pd.CategoricalDtype(pd.DatetimeIndex([])).categories.dtype
    dtype('<M8[ns]')
    """
    @classmethod
    def construct_array_type(cls, *args, **kwargs): # real signature unknown
        """
        Return the array type associated with this dtype.
        
        Returns
        -------
        type
        """
        pass

    @classmethod
    def construct_from_string(cls, *args, **kwargs): # real signature unknown
        """
        Construct a CategoricalDtype from a string.
        
        Parameters
        ----------
        string : str
            Must be the string "category" in order to be successfully constructed.
        
        Returns
        -------
        CategoricalDtype
            Instance of the dtype.
        
        Raises
        ------
        TypeError
            If a CategoricalDtype cannot be constructed from the input.
        """
        pass

    def update_dtype(self, dtype): # reliably restored by inspect
        """
        Returns a CategoricalDtype with categories and ordered taken from dtype
        if specified, otherwise falling back to self if unspecified
        
        Parameters
        ----------
        dtype : CategoricalDtype
        
        Returns
        -------
        new_dtype : CategoricalDtype
        """
        pass

    def validate_categories(categories, fastpath=False): # reliably restored by inspect
        """
        Validates that we have good categories
        
        Parameters
        ----------
        categories : array-like
        fastpath : bool
            Whether to skip nan and uniqueness checks
        
        Returns
        -------
        categories : Index
        """
        pass

    def validate_ordered(ordered): # reliably restored by inspect
        """
        Validates that we have a valid ordered parameter. If
        it is not a boolean, a TypeError will be raised.
        
        Parameters
        ----------
        ordered : object
            The parameter to be verified.
        
        Raises
        ------
        TypeError
            If 'ordered' is not a boolean.
        """
        pass

    def _finalize(self, categories, ordered, fastpath=False): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _from_categorical_dtype(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_fastpath(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_values_or_dtype(cls): # real signature unknown; restored from __doc__
        """
        Construct dtype from the input parameters used in :class:`Categorical`.
        
        This constructor method specifically does not do the factorization
        step, if that is needed to find the categories. This constructor may
        therefore return ``CategoricalDtype(categories=None, ordered=None)``,
        which may not be useful. Additional steps may therefore have to be
        taken to create the final dtype.
        
        The return dtype is specified from the inputs in this prioritized
        order:
        1. if dtype is a CategoricalDtype, return dtype
        2. if dtype is the string 'category', create a CategoricalDtype from
           the supplied categories and ordered parameters, and return that.
        3. if values is a categorical, use value.dtype, but override it with
           categories and ordered if either/both of those are not None.
        4. if dtype is None and values is not a categorical, construct the
           dtype from categories and ordered, even if either of those is None.
        
        Parameters
        ----------
        values : list-like, optional
            The list-like must be 1-dimensional.
        categories : list-like, optional
            Categories for the CategoricalDtype.
        ordered : bool, optional
            Designating if the categories are ordered.
        dtype : CategoricalDtype or the string "category", optional
            If ``CategoricalDtype``, cannot be used together with
            `categories` or `ordered`.
        
        Returns
        -------
        CategoricalDtype
        
        Examples
        --------
        >>> pd.CategoricalDtype._from_values_or_dtype()
        CategoricalDtype(categories=None, ordered=None, categories_dtype=None)
        >>> pd.CategoricalDtype._from_values_or_dtype(
        ...     categories=['a', 'b'], ordered=True
        ... )
        CategoricalDtype(categories=['a', 'b'], ordered=True, categories_dtype=object)
        >>> dtype1 = pd.CategoricalDtype(['a', 'b'], ordered=True)
        >>> dtype2 = pd.CategoricalDtype(['x', 'y'], ordered=False)
        >>> c = pd.Categorical([0, 1], dtype=dtype1)
        >>> pd.CategoricalDtype._from_values_or_dtype(
        ...     c, ['x', 'y'], ordered=True, dtype=dtype2
        ... )
        Traceback (most recent call last):
            ...
        ValueError: Cannot specify `categories` or `ordered` together with
        `dtype`.
        
        The supplied dtype takes precedence over values' dtype:
        
        >>> pd.CategoricalDtype._from_values_or_dtype(c, dtype=dtype2)
        CategoricalDtype(categories=['x', 'y'], ordered=False, categories_dtype=object)
        """
        pass

    def _get_common_dtype(self, dtypes): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        """
        Rules for CDT equality:
        1) Any CDT is equal to the string 'category'
        2) Any CDT is equal to itself
        3) Any CDT is equal to a CDT with categories=None regardless of ordered
        4) A CDT with ordered=True is only equal to another CDT with
           ordered=True and identical categories in the same order
        5) A CDT with ordered={False, None} is only equal to another CDT with
           ordered={False, None} and identical categories, but same order is
           not required. There is no distinction between False/None.
        6) Any other comparison returns False
        """
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, categories=None, ordered=False): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setstate__(self, state): # reliably restored by inspect
        # no doc
        pass

    categories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
An ``Index`` containing the unique categories allowed.

Examples
--------
>>> cat_type = pd.CategoricalDtype(categories=['a', 'b'], ordered=True)
>>> cat_type.categories
Index(['a', 'b'], dtype='object')
"""

    ordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Whether the categories have an ordered relationship.

Examples
--------
>>> cat_type = pd.CategoricalDtype(categories=['a', 'b'], ordered=True)
>>> cat_type.ordered
True

>>> cat_type = pd.CategoricalDtype(categories=['a', 'b'], ordered=False)
>>> cat_type.ordered
False
"""

    _is_boolean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    base = dtype('O')
    index_class = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4534F7240>'
    kind = 'O'
    name = 'category'
    str = '|O08'
    type = None # (!) real value is "<class 'pandas.core.dtypes.dtypes.CategoricalDtypeType'>"
    _cache_dtypes = {}
    _can_fast_transpose = False
    _hash_categories = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4534F7080>'
    _metadata = (
        'categories',
        'ordered',
    )
    _supports_2d = False
    __annotations__ = {
        '_cache_dtypes': 'dict[str_type, PandasExtensionDtype]',
        'kind': 'str_type',
        'type': 'type[CategoricalDtypeType]',
    }
    __firstlineno__ = 155
    __static_attributes__ = (
        '_categories',
        '_ordered',
    )


class defaultdict(dict):
    """
    defaultdict(default_factory=None, /, [...]) --> dict with default factory
    
    The default factory is called without arguments to produce
    a new value when a key is not present, in __getitem__ only.
    A defaultdict compares equal to a dict with the same items.
    All remaining arguments are treated the same as if they were
    passed to the dict constructor, including keyword arguments.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ D.copy() -> a shallow copy of D. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, default_factory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __missing__(self, key): # real signature unknown; restored from __doc__
        """
        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory()
          return value
        """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    default_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Factory for default value called by __missing__()."""



class EmptyDataError(ValueError):
    """
    Exception raised in ``pd.read_csv`` when empty data or header is encountered.
    
    Examples
    --------
    >>> from io import StringIO
    >>> empty = StringIO()
    >>> pd.read_csv(empty)
    Traceback (most recent call last):
    EmptyDataError: No columns to parse from file
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __firstlineno__ = 198
    __static_attributes__ = ()


class FloatingArray(__pandas_core_arrays_numeric.NumericArray):
    """
    Array of floating (optional missing) values.
    
    .. warning::
    
       FloatingArray is currently experimental, and its API or internal
       implementation may change without warning. Especially the behaviour
       regarding NaN (distinct from NA missing values) is subject to change.
    
    We represent a FloatingArray with 2 numpy arrays:
    
    - data: contains a numpy float array of the appropriate dtype
    - mask: a boolean array holding a mask on the data, True is missing
    
    To construct an FloatingArray from generic array-like input, use
    :func:`pandas.array` with one of the float dtypes (see examples).
    
    See :ref:`integer_na` for more.
    
    Parameters
    ----------
    values : numpy.ndarray
        A 1-d float-dtype array.
    mask : numpy.ndarray
        A 1-d boolean-dtype array indicating missing values.
    copy : bool, default False
        Whether to copy the `values` and `mask`.
    
    Attributes
    ----------
    None
    
    Methods
    -------
    None
    
    Returns
    -------
    FloatingArray
    
    Examples
    --------
    Create an FloatingArray with :func:`pandas.array`:
    
    >>> pd.array([0.1, None, 0.3], dtype=pd.Float32Dtype())
    <FloatingArray>
    [0.1, <NA>, 0.3]
    Length: 3, dtype: Float32
    
    String aliases for the dtypes are also available. They are capitalized.
    
    >>> pd.array([0.1, None, 0.3], dtype="Float32")
    <FloatingArray>
    [0.1, <NA>, 0.3]
    Length: 3, dtype: Float32
    """
    def __init__(self, values, mask, copy=False): # reliably restored by inspect
        # no doc
        pass

    _dtype_cls = None # (!) real value is "<class 'pandas.core.arrays.floating.FloatingDtype'>"
    _falsey_value = 0.0
    _internal_fill_value = nan
    _truthy_value = 1.0
    __firstlineno__ = 56
    __static_attributes__ = ()


class IntegerArray(__pandas_core_arrays_numeric.NumericArray):
    """
    Array of integer (optional missing) values.
    
    Uses :attr:`pandas.NA` as the missing value.
    
    .. warning::
    
       IntegerArray is currently experimental, and its API or internal
       implementation may change without warning.
    
    We represent an IntegerArray with 2 numpy arrays:
    
    - data: contains a numpy integer array of the appropriate dtype
    - mask: a boolean array holding a mask on the data, True is missing
    
    To construct an IntegerArray from generic array-like input, use
    :func:`pandas.array` with one of the integer dtypes (see examples).
    
    See :ref:`integer_na` for more.
    
    Parameters
    ----------
    values : numpy.ndarray
        A 1-d integer-dtype array.
    mask : numpy.ndarray
        A 1-d boolean-dtype array indicating missing values.
    copy : bool, default False
        Whether to copy the `values` and `mask`.
    
    Attributes
    ----------
    None
    
    Methods
    -------
    None
    
    Returns
    -------
    IntegerArray
    
    Examples
    --------
    Create an IntegerArray with :func:`pandas.array`.
    
    >>> int_array = pd.array([1, None, 3], dtype=pd.Int32Dtype())
    >>> int_array
    <IntegerArray>
    [1, <NA>, 3]
    Length: 3, dtype: Int32
    
    String aliases for the dtypes are also available. They are capitalized.
    
    >>> pd.array([1, None, 3], dtype='Int32')
    <IntegerArray>
    [1, <NA>, 3]
    Length: 3, dtype: Int32
    
    >>> pd.array([1, None, 3], dtype='UInt16')
    <IntegerArray>
    [1, <NA>, 3]
    Length: 3, dtype: UInt16
    """
    def __init__(self, values, mask, copy=False): # reliably restored by inspect
        # no doc
        pass

    _dtype_cls = None # (!) real value is "<class 'pandas.core.arrays.integer.IntegerDtype'>"
    _falsey_value = 0
    _internal_fill_value = 1
    _truthy_value = 1
    __firstlineno__ = 64
    __static_attributes__ = ()


class k(__numpy.generic):
    """
    Any Python object.
    
        :Character code: ``'O'``
    """
    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return bool(key in self). """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __release_buffer__(self, *args, **kwargs): # real signature unknown
        """ Release the buffer object that exposes the underlying memory of the object. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class ParserError(ValueError):
    """
    Exception that is raised by an error encountered in parsing file contents.
    
    This is a generic error raised for errors encountered when functions like
    `read_csv` or `read_html` are parsing contents of a file.
    
    See Also
    --------
    read_csv : Read CSV (comma-separated) file into a DataFrame.
    read_html : Read HTML table into a DataFrame.
    
    Examples
    --------
    >>> data = '''a,b,c
    ... cat,foo,bar
    ... dog,foo,"baz'''
    >>> from io import StringIO
    >>> pd.read_csv(StringIO(data), skipfooter=1, engine='python')
    Traceback (most recent call last):
    ParserError: ',' expected after '"'. Error could possibly be due
    to parsing errors in the skipped footer rows
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __firstlineno__ = 118
    __static_attributes__ = ()


class ParserWarning(Warning):
    """
    Warning raised when reading a file that doesn't use the default 'c' parser.
    
    Raised by `pd.read_csv` and `pd.read_table` when it is necessary to change
    parsers, generally from the default 'c' parser to 'python'.
    
    It happens due to a lack of support or functionality for parsing a
    particular attribute of a CSV file with the requested engine.
    
    Currently, 'c' unsupported options include the following parameters:
    
    1. `sep` other than a single character (e.g. regex separators)
    2. `skipfooter` higher than 0
    3. `sep=None` with `delim_whitespace=False`
    
    The warning can be avoided by adding `engine='python'` as a parameter in
    `pd.read_csv` and `pd.read_table` methods.
    
    See Also
    --------
    pd.read_csv : Read CSV (comma-separated) file into DataFrame.
    pd.read_table : Read general delimited file into DataFrame.
    
    Examples
    --------
    Using a `sep` in `pd.read_csv` other than a single character:
    
    >>> import io
    >>> csv = '''a;b;c
    ...           1;1,8
    ...           1;2,1'''
    >>> df = pd.read_csv(io.StringIO(csv), sep='[;,]')  # doctest: +SKIP
    ... # ParserWarning: Falling back to the 'python' engine...
    
    Adding `engine='python'` to `pd.read_csv` removes the Warning:
    
    >>> df = pd.read_csv(io.StringIO(csv), sep='[;,]', engine='python')
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __firstlineno__ = 212
    __static_attributes__ = ()


class StringDtype(__pandas_core_dtypes_base.StorageExtensionDtype):
    """
    Extension dtype for string data.
    
    .. warning::
    
       StringDtype is considered experimental. The implementation and
       parts of the API may change without warning.
    
    Parameters
    ----------
    storage : {"python", "pyarrow"}, optional
        If not given, the value of ``pd.options.mode.string_storage``.
    na_value : {np.nan, pd.NA}, default pd.NA
        Whether the dtype follows NaN or NA missing value semantics.
    
    Attributes
    ----------
    None
    
    Methods
    -------
    None
    
    Examples
    --------
    >>> pd.StringDtype()
    string[python]
    
    >>> pd.StringDtype(storage="pyarrow")
    string[pyarrow]
    """
    def construct_array_type(self): # reliably restored by inspect
        """
        Return the array type associated with this dtype.
        
        Returns
        -------
        type
        """
        pass

    @classmethod
    def construct_from_string(cls, *args, **kwargs): # real signature unknown
        """
        Construct a StringDtype from a string.
        
        Parameters
        ----------
        string : str
            The type of the name. The storage type will be taking from `string`.
            Valid options and their storage types are
        
            ========================== ==============================================
            string                     result storage
            ========================== ==============================================
            ``'string'``               pd.options.mode.string_storage, default python
            ``'string[python]'``       python
            ``'string[pyarrow]'``      pyarrow
            ========================== ==============================================
        
        Returns
        -------
        StringDtype
        
        Raise
        -----
        TypeError
            If the string is not a valid option.
        """
        pass

    def _get_common_dtype(self, dtypes): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __from_arrow__(self, array): # reliably restored by inspect
        """ Construct StringArray from pyarrow Array/ChunkedArray. """
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, storage=None, na_value='<NA>'): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setstate__(self, state): # reliably restored by inspect
        # no doc
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    na_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _metadata = (
        'storage',
        '_na_value',
    )
    __firstlineno__ = 93
    __static_attributes__ = (
        '_na_value',
        'storage',
    )


class TextReader(object):
    """
    # source: StringIO or file object
    
        ..versionchange:: 1.2.0
            removed 'compression', 'memory_map', and 'encoding' argument.
            These arguments are outsourced to CParserWrapper.
            'source' has to be a file handle.
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """ rows=None --> read all rows """
        pass

    def read_low_memory(self, *args, **kwargs): # real signature unknown
        """ rows=None --> read all rows """
        pass

    def remove_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def set_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def _convert_column_data(self, *args, **kwargs): # real signature unknown
        pass

    def _get_converter(self, *args, **kwargs): # real signature unknown
        pass

    def _set_quoting(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    converters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype_backend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_col = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    na_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skiprows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unnamed_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usecols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A453EE68E0>'


# variables with complex values

na_values = {
    np.float32: 
        nan
    ,
    np.double: 
        nan
    ,
    np.int64: 
        -9223372036854775808
    ,
    np.int32: 
        -2147483648
    ,
    np.int16: 
        -32768
    ,
    np.byte: 
        -128
    ,
    np.uint: 
        18446744073709551615
    ,
    np.uint32: 
        4294967295
    ,
    np.uint16: 
        65535
    ,
    np.ubyte: 
        255
    ,
    np.bool: 
        255
    ,
    np.object_: 
        nan
    ,
    dtype('float32'): 
        nan
    ,
    dtype('float64'): 
        nan
    ,
    dtype('int64'): 
        -9223372036854775808
    ,
    dtype('int32'): 
        -2147483648
    ,
    dtype('int16'): 
        -32768
    ,
    dtype('int8'): 
        -128
    ,
    dtype('uint64'): 
        18446744073709551615
    ,
    dtype('uint32'): 
        4294967295
    ,
    dtype('uint16'): 
        65535
    ,
    dtype('uint8'): 
        255
    ,
    dtype('bool'): 
        255
    ,
    dtype('O'): 
        nan
    ,
}

STR_NA_VALUES = None # (!) real value is "{'', 'NA', 'NULL', 'n/a', '-1.#IND', '-NaN', '#N/A N/A', 'N/A', '1.#IND', '1.#QNAN', 'NaN', '-1.#QNAN', '#NA', 'null', 'None', 'nan', '<NA>', '#N/A', '-nan'}"

_NA_VALUES = [
    b'',
    b'NA',
    b'NULL',
    b'n/a',
    b'-1.#IND',
    b'-NaN',
    b'#N/A N/A',
    b'N/A',
    b'1.#IND',
    b'1.#QNAN',
    b'NaN',
    b'-1.#QNAN',
    b'#NA',
    b'null',
    b'None',
    b'nan',
    b'<NA>',
    b'#N/A',
    b'-nan',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A453ECE750>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.parsers', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A453ECE750>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\parsers.cp313-win_amd64.pyd')"

__test__ = {}

