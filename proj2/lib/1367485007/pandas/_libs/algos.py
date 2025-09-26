# encoding: utf-8
# module pandas._libs.algos
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\algos.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py

# functions

def backfill(*args, **kwargs): # real signature unknown
    """
    Backfilling logic for generating fill vector
    
        Diagram of what's going on
    
        Old      New    Fill vector    Mask
                .        0               1
                .        0               1
                .        0               1
        A        A        0               1
                .        1               1
                .        1               1
                .        1               1
                .        1               1
                .        1               1
        B        B        1               1
                .        2               1
                .        2               1
                .        2               1
        C        C        2               1
                .                        0
                .                        0
        D
    """
    pass

def backfill_2d_inplace(*args, **kwargs): # real signature unknown
    pass

def backfill_inplace(*args, **kwargs): # real signature unknown
    pass

def diff_2d(*args, **kwargs): # real signature unknown
    pass

def ensure_float64(*args, **kwargs): # real signature unknown
    pass

def ensure_int16(*args, **kwargs): # real signature unknown
    pass

def ensure_int32(*args, **kwargs): # real signature unknown
    pass

def ensure_int64(*args, **kwargs): # real signature unknown
    pass

def ensure_int8(*args, **kwargs): # real signature unknown
    pass

def ensure_object(*args, **kwargs): # real signature unknown
    pass

def ensure_platform_int(*args, **kwargs): # real signature unknown
    pass

def ensure_uint64(*args, **kwargs): # real signature unknown
    pass

def get_fill_indexer(*args, **kwargs): # real signature unknown
    """ Find an indexer to use for ffill to `take` on the array being filled. """
    pass

def groupsort_indexer(*args, **kwargs): # real signature unknown
    """
    Compute a 1-d indexer.
    
        The indexer is an ordering of the passed index,
        ordered by the groups.
    
        Parameters
        ----------
        index: np.ndarray[np.intp]
            Mappings from group -> position.
        ngroups: int64
            Number of groups.
    
        Returns
        -------
        ndarray[intp_t, ndim=1]
            Indexer
        ndarray[intp_t, ndim=1]
            Group Counts
    
        Notes
        -----
        This is a reverse of the label factorization process.
    """
    pass

def is_lexsorted(*args, **kwargs): # real signature unknown
    pass

def is_monotonic(*args, **kwargs): # real signature unknown
    """
    Returns
        -------
        tuple
            is_monotonic_inc : bool
            is_monotonic_dec : bool
            is_strict_monotonic : bool
    """
    pass

def kth_smallest(*args, **kwargs): # real signature unknown
    """
    Compute the kth smallest value in arr. Note that the input
        array will be modified.
    
        Parameters
        ----------
        arr : numeric[::1]
            Array to compute the kth smallest value for, must be
            contiguous
        k : Py_ssize_t
    
        Returns
        -------
        numeric
            The kth smallest value in arr
    """
    pass

def nancorr(*args, **kwargs): # real signature unknown
    pass

def nancorr_spearman(*args, **kwargs): # real signature unknown
    pass

def pad(*args, **kwargs): # real signature unknown
    pass

def pad_2d_inplace(*args, **kwargs): # real signature unknown
    pass

def pad_inplace(*args, **kwargs): # real signature unknown
    pass

def rank_1d(*args, **kwargs): # real signature unknown
    """
    Fast NaN-friendly version of ``scipy.stats.rankdata``.
    
        Parameters
        ----------
        values : array of numeric_object_t values to be ranked
        labels : np.ndarray[np.intp] or None
            Array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`. If not called
            from a groupby operation, will be None.
        is_datetimelike : bool, default False
            True if `values` contains datetime-like entries.
        ties_method : {'average', 'min', 'max', 'first', 'dense'}, default
            'average'
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
        mask : np.ndarray[bool], optional, default None
            Specify locations to be treated as NA, for e.g. Categorical.
    """
    pass

def rank_2d(*args, **kwargs): # real signature unknown
    """ Fast NaN-friendly version of ``scipy.stats.rankdata``. """
    pass

def take_1d_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_1d_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_1d_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_1d_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_1d_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_1d_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis0_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_axis1_object_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_bool_bool(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_bool_object(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float32_float32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_float64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int16(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int16_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int32_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int64_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int64_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_float64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int32(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int64(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_int8_int8(*args, **kwargs): # real signature unknown
    pass

def take_2d_multi_object_object(*args, **kwargs): # real signature unknown
    pass

def unique_deltas(*args, **kwargs): # real signature unknown
    """
    Efficiently find the unique first-differences of the given array.
    
        Parameters
        ----------
        arr : ndarray[int64_t]
    
        Returns
        -------
        ndarray[int64_t]
            An ordered ndarray[int64_t]
    """
    pass

def validate_limit(*args, **kwargs): # real signature unknown
    """
    Check that the `limit` argument is a positive integer.
    
        Parameters
        ----------
        nobs : int
        limit : object
    
        Returns
        -------
        int
            The limit.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class Infinity(object):
    """ Provide a positive Infinity comparison method for ranking. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.algos', '__doc__': '\\n    Provide a positive Infinity comparison method for ranking.\\n    ', '__lt__': <cyfunction Infinity.__lt__ at 0x00000243523F1900>, '__le__': <cyfunction Infinity.__le__ at 0x00000243523F1A80>, '__eq__': <cyfunction Infinity.__eq__ at 0x00000243523F1B40>, '__ne__': <cyfunction Infinity.__ne__ at 0x00000243523F1C00>, '__gt__': <cyfunction Infinity.__gt__ at 0x00000243523F1CC0>, '__ge__': <cyfunction Infinity.__ge__ at 0x00000243523F1D80>, '__dict__': <attribute '__dict__' of 'Infinity' objects>, '__weakref__': <attribute '__weakref__' of 'Infinity' objects>, '__hash__': None})"
    __hash__ = None


class NegInfinity(object):
    """ Provide a negative Infinity comparison method for ranking. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.algos', '__doc__': '\\n    Provide a negative Infinity comparison method for ranking.\\n    ', '__lt__': <cyfunction NegInfinity.__lt__ at 0x00000243523F1E40>, '__le__': <cyfunction NegInfinity.__le__ at 0x00000243523F1F00>, '__eq__': <cyfunction NegInfinity.__eq__ at 0x00000243523F1FC0>, '__ne__': <cyfunction NegInfinity.__ne__ at 0x00000243523F2080>, '__gt__': <cyfunction NegInfinity.__gt__ at 0x00000243523F2140>, '__ge__': <cyfunction NegInfinity.__ge__ at 0x00000243523F2200>, '__dict__': <attribute '__dict__' of 'NegInfinity' objects>, '__weakref__': <attribute '__weakref__' of 'NegInfinity' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

tiebreakers = {
    'average': 0,
    'dense': 5,
    'first': 3,
    'max': 2,
    'min': 1,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024352229370>'

__pyx_capi__ = {
    '__pyx_fuse_0get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int8_t (int, __pyx_t_5numpy_int8_t, struct __pyx_fuse_0__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x00000243523D3B50>'
    '__pyx_fuse_0kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int8_t (__pyx_t_5numpy_int8_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D3510>'
    '__pyx_fuse_10get_rank_nan_fill_val': None, # (!) real value is '<capsule object "PyObject *(int, PyObject *, struct __pyx_fuse_10__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x000002435240C1D0>'
    '__pyx_fuse_1get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int16_t (int, __pyx_t_5numpy_int16_t, struct __pyx_fuse_1__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x00000243523D3BF0>'
    '__pyx_fuse_1kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int16_t (__pyx_t_5numpy_int16_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D35B0>'
    '__pyx_fuse_2get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int32_t (int, __pyx_t_5numpy_int32_t, struct __pyx_fuse_2__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x00000243523D3C90>'
    '__pyx_fuse_2kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int32_t (__pyx_t_5numpy_int32_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D3650>'
    '__pyx_fuse_3get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (int, __pyx_t_5numpy_int64_t, struct __pyx_fuse_3__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x00000243523D3D30>'
    '__pyx_fuse_3kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D36F0>'
    '__pyx_fuse_4get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint8_t (int, __pyx_t_5numpy_uint8_t, struct __pyx_fuse_4__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x00000243523D3DD0>'
    '__pyx_fuse_4kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint8_t (__pyx_t_5numpy_uint8_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D3790>'
    '__pyx_fuse_5get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint16_t (int, __pyx_t_5numpy_uint16_t, struct __pyx_fuse_5__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x00000243523D3E70>'
    '__pyx_fuse_5kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint16_t (__pyx_t_5numpy_uint16_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D3830>'
    '__pyx_fuse_6get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint32_t (int, __pyx_t_5numpy_uint32_t, struct __pyx_fuse_6__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x00000243523D3F10>'
    '__pyx_fuse_6kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint32_t (__pyx_t_5numpy_uint32_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D38D0>'
    '__pyx_fuse_7get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint64_t (int, __pyx_t_5numpy_uint64_t, struct __pyx_fuse_7__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x00000243523D3FB0>'
    '__pyx_fuse_7kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_uint64_t (__pyx_t_5numpy_uint64_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D3970>'
    '__pyx_fuse_8get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (int, __pyx_t_5numpy_float32_t, struct __pyx_fuse_8__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x000002435240C090>'
    '__pyx_fuse_8kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float32_t (__pyx_t_5numpy_float32_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D3A10>'
    '__pyx_fuse_9get_rank_nan_fill_val': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (int, __pyx_t_5numpy_float64_t, struct __pyx_fuse_9__pyx_opt_args_6pandas_5_libs_5algos_get_rank_nan_fill_val *__pyx_optional_args)" at 0x000002435240C130>'
    '__pyx_fuse_9kth_smallest_c': None, # (!) real value is '<capsule object "__pyx_t_5numpy_float64_t (__pyx_t_5numpy_float64_t *, Py_ssize_t, Py_ssize_t)" at 0x00000243523D3AB0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.algos', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024352229370>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\algos.cp313-win_amd64.pyd')"

__test__ = {}

