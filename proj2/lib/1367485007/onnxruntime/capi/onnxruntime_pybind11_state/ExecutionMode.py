# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class ExecutionMode(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      ORT_SEQUENTIAL
    
      ORT_PARALLEL
    """
    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, other): # real signature unknown; restored from __doc__
        """ __eq__(self: object, other: object) -> bool """
        return False

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: object) -> int """
        return 0

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: object) -> int """
        return 0

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: onnxruntime.capi.onnxruntime_pybind11_state.ExecutionMode) -> int """
        return 0

    def __init__(self, value): # real signature unknown; restored from __doc__
        """ __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.ExecutionMode, value: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: onnxruntime.capi.onnxruntime_pybind11_state.ExecutionMode) -> int """
        return 0

    def __ne__(self, other): # real signature unknown; restored from __doc__
        """ __ne__(self: object, other: object) -> bool """
        return False

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: object) -> str """
        return ""

    def __setstate__(self, state): # real signature unknown; restored from __doc__
        """ __setstate__(self: onnxruntime.capi.onnxruntime_pybind11_state.ExecutionMode, state: int) -> None """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: object) -> str """
        return ""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name(self: object) -> str
"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ORT_PARALLEL = None # (!) real value is '<ExecutionMode.ORT_PARALLEL: 1>'
    ORT_SEQUENTIAL = None # (!) real value is '<ExecutionMode.ORT_SEQUENTIAL: 0>'
    __entries = {
        'ORT_PARALLEL': (
            None, # (!) real value is '<ExecutionMode.ORT_PARALLEL: 1>'
            None,
        ),
        'ORT_SEQUENTIAL': (
            None, # (!) real value is '<ExecutionMode.ORT_SEQUENTIAL: 0>'
            None,
        ),
    }
    __members__ = {
        'ORT_PARALLEL': None, # (!) real value is '<ExecutionMode.ORT_PARALLEL: 1>'
        'ORT_SEQUENTIAL': None, # (!) real value is '<ExecutionMode.ORT_SEQUENTIAL: 0>'
    }


