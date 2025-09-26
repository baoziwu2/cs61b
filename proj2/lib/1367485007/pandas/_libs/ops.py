# encoding: utf-8
# module pandas._libs.ops
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\ops.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\operator.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py

# functions

def maybe_convert_bool(*args, **kwargs): # real signature unknown
    pass

def operator(*args, **kwargs): # real signature unknown
    """
    Operator interface.
    
    This module exports a set of functions implemented in C corresponding
    to the intrinsic operators of Python.  For example, operator.add(x, y)
    is equivalent to the expression x+y.  The function names are those
    used for special methods; variants without leading and trailing
    '__' are also provided for convenience.
    """
    pass

def scalar_binop(*args, **kwargs): # real signature unknown
    """
    Apply the given binary operator `op` between each element of the array
        `values` and the scalar `val`.
    
        Parameters
        ----------
        values : ndarray[object]
        val : object
        op : binary operator
    
        Returns
        -------
        result : ndarray[object]
    """
    pass

def scalar_compare(*args, **kwargs): # real signature unknown
    """
    Compare each element of `values` array with the scalar `val`, with
        the comparison operation described by `op`.
    
        Parameters
        ----------
        values : ndarray[object]
        val : object
        op : {operator.eq, operator.ne,
              operator.le, operator.lt,
              operator.ge, operator.gt}
    
        Returns
        -------
        result : ndarray[bool]
    """
    pass

def vec_binop(*args, **kwargs): # real signature unknown
    """
    Apply the given binary operator `op` pointwise to the elements of
        arrays `left` and `right`.
    
        Parameters
        ----------
        left : ndarray[object]
        right : ndarray[object]
        op : binary operator
    
        Returns
        -------
        result : ndarray[object]
    """
    pass

def vec_compare(*args, **kwargs): # real signature unknown
    """
    Compare the elements of `left` with the elements of `right` pointwise,
        with the comparison operation described by `op`.
    
        Parameters
        ----------
        left : ndarray[object]
        right : ndarray[object]
        op : {operator.eq, operator.ne,
              operator.le, operator.lt,
              operator.ge, operator.gt}
    
        Returns
        -------
        result : ndarray[bool]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021422ABB5F0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.ops', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021422ABB5F0>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\ops.cp313-win_amd64.pyd')"

__test__ = {}

