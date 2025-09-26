# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class AdapterFormat(__pybind11_builtins.pybind11_object):
    # no doc
    def export_adapter(self, arg0): # real signature unknown; restored from __doc__
        """
        export_adapter(self: onnxruntime.capi.onnxruntime_pybind11_state.AdapterFormat, arg0: str) -> None
        
        "Save adapter parameters into a onnxruntime adapter file format.
        """
        pass

    def read_adapter(self, arg0): # real signature unknown; restored from __doc__
        """
        read_adapter(arg0: str) -> onnxruntime.capi.onnxruntime_pybind11_state.AdapterFormat
        
        The function returns an instance of the class that contains a dictionary of name -> numpy arrays
        """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.AdapterFormat) -> None """
        pass

    adapter_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """"Enables user to read/write adapter version stored in the file""""

    format_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """"Enables user to read format version stored in the file""""

    model_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """"Enables user to read/write model version this adapter was created for""""

    parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """"Enables user to read/write adapter version stored in the file""""



