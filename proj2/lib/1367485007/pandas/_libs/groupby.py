# encoding: utf-8
# module pandas._libs.groupby
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\groupby.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
from pandas._libs.algos import (groupsort_indexer, rank_1d, 
    take_2d_axis1_bool_bool, take_2d_axis1_float64_float64)


# functions

def group_any_all(*args, **kwargs): # real signature unknown
    """
    Aggregated boolean values to show truthfulness of group elements. If the
        input is a nullable type (result_mask is not None), the result will be computed
        using Kleene logic.
    
        Parameters
        ----------
        out : np.ndarray[np.int8]
            Values into which this method will write its results.
        labels : np.ndarray[np.intp]
            Array containing unique label for each group, with its
            ordering matching up to the corresponding record in `values`
        values : np.ndarray[np.int8]
            Containing the truth value of each element.
        mask : np.ndarray[np.uint8]
            Indicating whether a value is na or not.
        val_test : {'any', 'all'}
            String object dictating whether to use any or all truth testing
        skipna : bool
            Flag to ignore nan values during truth testing
        result_mask : ndarray[bool, ndim=2], optional
            If not None, these specify locations in the output that are NA.
            Modified in-place.
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object.
        The returned values will either be 0, 1 (False or True, respectively), or
        -1 to signify a masked position in the case of a nullable input.
    """
    pass

def group_cummax(*args, **kwargs): # real signature unknown
    """ See group_cummin_max.__doc__ """
    pass

def group_cummin(*args, **kwargs): # real signature unknown
    """ See group_cummin_max.__doc__ """
    pass

def group_cumprod(*args, **kwargs): # real signature unknown
    """
    Cumulative product of columns of `values`, in row groups `labels`.
    
        Parameters
        ----------
        out : np.ndarray[np.float64, ndim=2]
            Array to store cumprod in.
        values : np.ndarray[np.float64, ndim=2]
            Values to take cumprod of.
        labels : np.ndarray[np.intp]
            Labels to group by.
        ngroups : int
            Number of groups, larger than all entries of `labels`.
        is_datetimelike : bool
            Always false, `values` is never datetime-like.
        skipna : bool
            If true, ignore nans in `values`.
        mask : np.ndarray[uint8], optional
            Mask of values
        result_mask : np.ndarray[int8], optional
            Mask of out array
    
        Notes
        -----
        This method modifies the `out` parameter, rather than returning an object.
    """
    pass

def group_cumsum(*args, **kwargs): # real signature unknown
    """
    Cumulative sum of columns of `values`, in row groups `labels`.
    
        Parameters
        ----------
        out : np.ndarray[ndim=2]
            Array to store cumsum in.
        values : np.ndarray[ndim=2]
            Values to take cumsum of.
        labels : np.ndarray[np.intp]
            Labels to group by.
        ngroups : int
            Number of groups, larger than all entries of `labels`.
        is_datetimelike : bool
            True if `values` contains datetime-like entries.
        skipna : bool
            If true, ignore nans in `values`.
        mask : np.ndarray[uint8], optional
            Mask of values
        result_mask : np.ndarray[int8], optional
            Mask of out array
    
        Notes
        -----
        This method modifies the `out` parameter, rather than returning an object.
    """
    pass

def group_fillna_indexer(*args, **kwargs): # real signature unknown
    """
    Indexes how to fill values forwards or backwards within a group.
    
        Parameters
        ----------
        out : np.ndarray[np.intp]
            Values into which this method will write its results.
        labels : np.ndarray[np.intp]
            Array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`.
        sorted_labels : np.ndarray[np.intp]
            obtained by `np.argsort(labels, kind="mergesort")`
        values : np.ndarray[np.uint8]
            Containing the truth value of each element.
        mask : np.ndarray[np.uint8]
            Indicating whether a value is na or not.
        limit : Consecutive values to fill before stopping, or -1 for no limit
        dropna : Flag to indicate if NaN groups should return all NaN values
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object
    """
    pass

def group_idxmin_idxmax(*args, **kwargs): # real signature unknown
    """
    Compute index of minimum/maximum of columns of `values`, in row groups `labels`.
    
        This function only computes the row number where the minimum/maximum occurs, we'll
        take the corresponding index value after this function.
    
        Parameters
        ----------
        out : np.ndarray[intp, ndim=2]
            Array to store result in.
        counts : np.ndarray[int64]
            Input as a zeroed array, populated by group sizes during algorithm
        values : np.ndarray[numeric_object_t, ndim=2]
            Values to find column-wise min/max of.
        labels : np.ndarray[np.intp]
            Labels to group by.
        min_count : Py_ssize_t, default -1
            The minimum number of non-NA group elements, NA result if threshold
            is not met.
        is_datetimelike : bool
            True if `values` contains datetime-like entries.
        name : {"idxmin", "idxmax"}, default "idxmin"
            Whether to compute idxmin or idxmax.
        mask : ndarray[bool, ndim=2], optional
            If not None, indices represent missing values,
            otherwise the mask will not be used
        skipna : bool, default True
            Flag to ignore nan values during truth testing
        result_mask : ndarray[bool, ndim=2], optional
            If not None, these specify locations in the output that are NA.
            Modified in-place.
    
        Notes
        -----
        This method modifies the `out` parameter, rather than returning an object.
        `counts` is modified to hold group sizes
    """
    pass

def group_last(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_max(*args, **kwargs): # real signature unknown
    """ See group_min_max.__doc__ """
    pass

def group_mean(*args, **kwargs): # real signature unknown
    """
    Compute the mean per label given a label assignment for each value.
        NaN values are ignored.
    
        Parameters
        ----------
        out : np.ndarray[floating]
            Values into which this method will write its results.
        counts : np.ndarray[int64]
            A zeroed array of the same shape as labels,
            populated by group sizes during algorithm.
        values : np.ndarray[floating]
            2-d array of the values to find the mean of.
        labels : np.ndarray[np.intp]
            Array containing unique label for each group, with its
            ordering matching up to the corresponding record in `values`.
        min_count : Py_ssize_t
            Only used in sum and prod. Always -1.
        is_datetimelike : bool
            True if `values` contains datetime-like entries.
        mask : ndarray[bool, ndim=2], optional
            Mask of the input values.
        result_mask : ndarray[bool, ndim=2], optional
            Mask of the out array
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object.
        `counts` is modified to hold group sizes
    """
    pass

def group_median_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_min(*args, **kwargs): # real signature unknown
    """ See group_min_max.__doc__ """
    pass

def group_nth(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_ohlc(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_prod(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_quantile(*args, **kwargs): # real signature unknown
    """
    Calculate the quantile per group.
    
        Parameters
        ----------
        out : np.ndarray[np.float64, ndim=2]
            Array of aggregated values that will be written to.
        values : np.ndarray
            Array containing the values to apply the function against.
        labels : ndarray[np.intp]
            Array containing the unique group labels.
        qs : ndarray[float64_t]
            The quantile values to search for.
        starts : ndarray[int64]
            Positions at which each group begins.
        ends : ndarray[int64]
            Positions at which each group ends.
        interpolation : {'linear', 'lower', 'highest', 'nearest', 'midpoint'}
        result_mask : ndarray[bool, ndim=2] or None
        is_datetimelike : bool
            Whether int64 values represent datetime64-like values.
    
        Notes
        -----
        Rather than explicitly returning a value, this function modifies the
        provided `out` parameter.
    """
    pass

def group_rank(*args, **kwargs): # real signature unknown
    """
    Provides the rank of values within each group.
    
        Parameters
        ----------
        out : np.ndarray[np.float64, ndim=2]
            Values to which this method will write its results.
        values : np.ndarray of numeric_object_t values to be ranked
        labels : np.ndarray[np.intp]
            Array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`
        ngroups : int
            This parameter is not used, is needed to match signatures of other
            groupby functions.
        is_datetimelike : bool
            True if `values` contains datetime-like entries.
        ties_method : {'average', 'min', 'max', 'first', 'dense'}, default 'average'
            * average: average rank of group
            * min: lowest rank in group
            * max: highest rank in group
            * first: ranks assigned in order they appear in the array
            * dense: like 'min', but rank always increases by 1 between groups
        ascending : bool, default True
            False for ranks by high (1) to low (N)
            na_option : {'keep', 'top', 'bottom'}, default 'keep'
        pct : bool, default False
            Compute percentage rank of data within each group
        na_option : {'keep', 'top', 'bottom'}, default 'keep'
            * keep: leave NA values where they are
            * top: smallest rank if ascending
            * bottom: smallest rank if descending
        mask : np.ndarray[bool] or None, default None
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object
    """
    pass

def group_shift_indexer(*args, **kwargs): # real signature unknown
    pass

def group_skew(*args, **kwargs): # real signature unknown
    pass

def group_sum(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 using Kahan summation """
    pass

def group_var(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F950205BB0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.groupby', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F950205BB0>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\groupby.cp313-win_amd64.pyd')"

__test__ = {}

