# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class ModelMetadata(__pybind11_builtins.pybind11_object):
    """
    Pre-defined and custom metadata about the model.
    It is usually used to identify the model used to run the prediction and
    facilitate the comparison.
    """
    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    custom_metadata_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """additional metadata"""

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """description of the model"""

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ONNX domain"""

    graph_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """description of the graph hosted in the model"""

    graph_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """graph name"""

    producer_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """producer name"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """version of the model"""



