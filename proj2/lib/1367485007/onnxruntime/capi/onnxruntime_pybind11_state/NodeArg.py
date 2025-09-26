# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class NodeArg(__pybind11_builtins.pybind11_object):
    """
    Node argument definition, for both input and output,
    including arg name, arg type (contains both type and shape).
    """
    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """
        __str__(self: onnxruntime.capi.onnxruntime_pybind11_state.NodeArg) -> str
        
        converts the node into a readable string
        """
        return ""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """node name"""

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """node shape (assuming the node holds a tensor)"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """node type"""



