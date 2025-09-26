# encoding: utf-8
# module pandas._libs.window.aggregations
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\window\aggregations.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
from pandas._libs.algos import is_monotonic


# functions

def ewm(*args, **kwargs): # real signature unknown
    """
    Compute exponentially-weighted moving average or sum using center-of-mass.
    
        Parameters
        ----------
        vals : ndarray (float64 type)
        start: ndarray (int64 type)
        end: ndarray (int64 type)
        minp : int
        com : float64
        adjust : bool
        ignore_na : bool
        deltas : ndarray (float64 type), optional. If None, implicitly assumes equally
                 spaced points (used when `times` is not passed)
        normalize : bool, optional.
                    If True, calculate the mean. If False, calculate the sum.
    
        Returns
        -------
        np.ndarray[float64_t]
    """
    pass

def ewmcov(*args, **kwargs): # real signature unknown
    """
    Compute exponentially-weighted moving variance using center-of-mass.
    
        Parameters
        ----------
        input_x : ndarray (float64 type)
        start: ndarray (int64 type)
        end: ndarray (int64 type)
        minp : int
        input_y : ndarray (float64 type)
        com : float64
        adjust : bool
        ignore_na : bool
        bias : bool
    
        Returns
        -------
        np.ndarray[float64_t]
    """
    pass

def roll_apply(*args, **kwargs): # real signature unknown
    pass

def roll_kurt(*args, **kwargs): # real signature unknown
    pass

def roll_max(*args, **kwargs): # real signature unknown
    """
    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.
    
        Parameters
        ----------
        values : np.ndarray[np.float64]
        window : int, size of rolling window
        minp : if number of observations in window
              is below this, output a NaN
        index : ndarray, optional
           index for window computation
        closed : 'right', 'left', 'both', 'neither'
                make the interval closed on the right, left,
                both or neither endpoints
    
        Returns
        -------
        np.ndarray[float]
    """
    pass

def roll_mean(*args, **kwargs): # real signature unknown
    pass

def roll_median_c(*args, **kwargs): # real signature unknown
    pass

def roll_min(*args, **kwargs): # real signature unknown
    """
    Moving min of 1d array of any numeric type along axis=0 ignoring NaNs.
    
        Parameters
        ----------
        values : np.ndarray[np.float64]
        window : int, size of rolling window
        minp : if number of observations in window
              is below this, output a NaN
        index : ndarray, optional
           index for window computation
    
        Returns
        -------
        np.ndarray[float]
    """
    pass

def roll_quantile(*args, **kwargs): # real signature unknown
    """ O(N log(window)) implementation using skip list """
    pass

def roll_rank(*args, **kwargs): # real signature unknown
    """
    O(N log(window)) implementation using skip list
    
        derived from roll_quantile
    """
    pass

def roll_skew(*args, **kwargs): # real signature unknown
    pass

def roll_sum(*args, **kwargs): # real signature unknown
    pass

def roll_var(*args, **kwargs): # real signature unknown
    """ Numerically stable implementation using Welford's method. """
    pass

def roll_weighted_mean(*args, **kwargs): # real signature unknown
    pass

def roll_weighted_sum(*args, **kwargs): # real signature unknown
    pass

def roll_weighted_var(*args, **kwargs): # real signature unknown
    """
    Calculates weighted rolling variance using West's online algorithm.
    
        Paper: https://dl.acm.org/citation.cfm?id=359153
    
        Parameters
        ----------
        values: float64_t[:]
            values to roll window over
        weights: float64_t[:]
            array of weights whose length is window size
        minp: int64_t
            minimum number of observations to calculate
            variance of a window
        ddof: unsigned int
             the divisor used in variance calculations
             is the window size - ddof
    
        Returns
        -------
        output: float64_t[:]
            weighted variances of windows
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

interpolation_types = {
    'higher': 2,
    'linear': 0,
    'lower': 1,
    'midpoint': 4,
    'nearest': 3,
}

rolling_rank_tiebreakers = {
    'average': 0,
    'max': 2,
    'min': 1,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FAD16068D0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.window.aggregations', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FAD16068D0>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\window\\\\aggregations.cp313-win_amd64.pyd')"

__test__ = {}

