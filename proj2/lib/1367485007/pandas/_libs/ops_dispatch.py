# encoding: utf-8
# module pandas._libs.ops_dispatch
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\ops_dispatch.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def maybe_dispatch_ufunc_to_dunder_op(*args, **kwargs): # real signature unknown
    """
    Dispatch a ufunc to the equivalent dunder method.
    
        Parameters
        ----------
        self : ArrayLike
            The array whose dunder method we dispatch to
        ufunc : Callable
            A NumPy ufunc
        method : {'reduce', 'accumulate', 'reduceat', 'outer', 'at', '__call__'}
        inputs : ArrayLike
            The input arrays.
        kwargs : Any
            The additional keyword arguments, e.g. ``out``.
    
        Returns
        -------
        result : Any
            The result of applying the ufunc
    """
    pass

# no classes
# variables with complex values

DISPATCHED_UFUNCS = None # (!) real value is "{'abs', 'lt', 'gt', 'eq', 'matmul', 'sub', 'neg', 'add', 'or', 'pos', 'mul', 'remainder', 'and', 'le', 'divmod', 'xor', 'truediv', 'ge', 'mod', 'pow', 'floordiv', 'ne'}"

REVERSED_NAMES = {
    'eq': '__eq__',
    'ge': '__le__',
    'gt': '__lt__',
    'le': '__ge__',
    'lt': '__gt__',
    'ne': '__ne__',
}

UFUNC_ALIASES = {
    'absolute': 'abs',
    'bitwise_and': 'and',
    'bitwise_or': 'or',
    'bitwise_xor': 'xor',
    'divide': 'truediv',
    'equal': 'eq',
    'floor_divide': 'floordiv',
    'greater': 'gt',
    'greater_equal': 'ge',
    'less': 'lt',
    'less_equal': 'le',
    'multiply': 'mul',
    'negative': 'neg',
    'not_equal': 'ne',
    'positive': 'pos',
    'power': 'pow',
    'remainder': 'mod',
    'subtract': 'sub',
    'true_divide': 'truediv',
}

UNARY_UFUNCS = None # (!) real value is "{'abs', 'pos', 'neg'}"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D8FFF59550>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.ops_dispatch', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D8FFF59550>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\ops_dispatch.cp313-win_amd64.pyd')"

__test__ = {}

