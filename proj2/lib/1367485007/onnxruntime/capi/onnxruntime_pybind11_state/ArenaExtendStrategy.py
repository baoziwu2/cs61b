# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class ArenaExtendStrategy(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      kNextPowerOfTwo
    
      kSameAsRequested
    """
    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, other): # real signature unknown; restored from __doc__
        """ __eq__(self: object, other: object) -> bool """
        return False

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: object) -> int """
        return 0

    def __ge__(self, other): # real signature unknown; restored from __doc__
        """ __ge__(self: object, other: object) -> bool """
        return False

    def __gt__(self, other): # real signature unknown; restored from __doc__
        """ __gt__(self: object, other: object) -> bool """
        return False

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: object) -> int """
        return 0

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: onnxruntime.capi.onnxruntime_pybind11_state.ArenaExtendStrategy) -> int """
        return 0

    def __init__(self, value): # real signature unknown; restored from __doc__
        """ __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.ArenaExtendStrategy, value: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: onnxruntime.capi.onnxruntime_pybind11_state.ArenaExtendStrategy) -> int """
        return 0

    def __le__(self, other): # real signature unknown; restored from __doc__
        """ __le__(self: object, other: object) -> bool """
        return False

    def __lt__(self, other): # real signature unknown; restored from __doc__
        """ __lt__(self: object, other: object) -> bool """
        return False

    def __ne__(self, other): # real signature unknown; restored from __doc__
        """ __ne__(self: object, other: object) -> bool """
        return False

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: object) -> str """
        return ""

    def __setstate__(self, state): # real signature unknown; restored from __doc__
        """ __setstate__(self: onnxruntime.capi.onnxruntime_pybind11_state.ArenaExtendStrategy, state: int) -> None """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: object) -> str """
        return ""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name(self: object) -> str
"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    kNextPowerOfTwo = None # (!) forward: kNextPowerOfTwo, real value is '<ArenaExtendStrategy.kNextPowerOfTwo: 0>'
    kSameAsRequested = None # (!) forward: kSameAsRequested, real value is '<ArenaExtendStrategy.kSameAsRequested: 1>'
    __entries = {
        'kNextPowerOfTwo': (
            None, # (!) forward: kNextPowerOfTwo, real value is '<ArenaExtendStrategy.kNextPowerOfTwo: 0>'
            None,
        ),
        'kSameAsRequested': (
            None, # (!) forward: kSameAsRequested, real value is '<ArenaExtendStrategy.kSameAsRequested: 1>'
            None,
        ),
    }
    __members__ = {
        'kNextPowerOfTwo': None, # (!) forward: kNextPowerOfTwo, real value is '<ArenaExtendStrategy.kNextPowerOfTwo: 0>'
        'kSameAsRequested': None, # (!) forward: kSameAsRequested, real value is '<ArenaExtendStrategy.kSameAsRequested: 1>'
    }


