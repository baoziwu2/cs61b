# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class OrtArenaCfg(__pybind11_builtins.pybind11_object):
    # no doc
    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtArenaCfg, arg0: int, arg1: int, arg2: int, arg3: int) -> None
        
        2. __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtArenaCfg, arg0: dict) -> None
        """
        pass

    arena_extend_strategy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_chunk_size_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_growth_chunk_size_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_dead_bytes_per_chunk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_mem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_power_of_two_extend_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



