# encoding: utf-8
# module pandas._libs.testing
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\testing.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import cmath as cmath # <module 'cmath' (built-in)>
import math as math # <module 'math' (built-in)>
import warnings as warnings # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\warnings.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py

# functions

def array_equivalent(left, right, strict_nan=False, dtype_equal=False): # reliably restored by inspect
    """
    True if two arrays, left and right, have equal non-NaN elements, and NaNs
    in corresponding locations.  False otherwise. It is assumed that left and
    right are NumPy arrays of the same dtype. The behavior of this function
    (particularly with respect to NaNs) is not defined if the dtypes are
    different.
    
    Parameters
    ----------
    left, right : ndarrays
    strict_nan : bool, default False
        If True, consider NaN and None to be different.
    dtype_equal : bool, default False
        Whether `left` and `right` are known to have the same dtype
        according to `is_dtype_equal`. Some methods like `BlockManager.equals`.
        require that the dtypes match. Setting this to ``True`` can improve
        performance, but will give different results for arrays that are
        equal but different dtypes.
    
    Returns
    -------
    b : bool
        Returns True if the arrays are equivalent.
    
    Examples
    --------
    >>> array_equivalent(
    ...     np.array([1, 2, np.nan]),
    ...     np.array([1, 2, np.nan]))
    True
    >>> array_equivalent(
    ...     np.array([1, np.nan, 2]),
    ...     np.array([1, 2, np.nan]))
    False
    """
    pass

def assert_almost_equal(*args, **kwargs): # real signature unknown
    """
    Check that left and right objects are almost equal.
    
        Parameters
        ----------
        a : object
        b : object
        rtol : float, default 1e-5
            Relative tolerance.
        atol : float, default 1e-8
            Absolute tolerance.
        check_dtype: bool, default True
            check dtype if both a and b are np.ndarray.
        obj : str, default None
            Specify object name being compared, internally used to show
            appropriate assertion message.
        lobj : str, default None
            Specify left object name being compared, internally used to show
            appropriate assertion message.
        robj : str, default None
            Specify right object name being compared, internally used to show
            appropriate assertion message.
        index_values : Index | ndarray, default None
            Specify shared index values of objects being compared, internally used
            to show appropriate assertion message.
    """
    pass

def assert_dict_equal(*args, **kwargs): # real signature unknown
    pass

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025A693155B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.testing', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025A693155B0>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\testing.cp313-win_amd64.pyd')"

__test__ = {}

