# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class OrtDevice(__pybind11_builtins.pybind11_object):
    """ ONNXRuntime device informaion. """
    def cann(self): # real signature unknown; restored from __doc__
        """ cann() -> int """
        return 0

    def cpu(self): # real signature unknown; restored from __doc__
        """ cpu() -> int """
        return 0

    def cuda(self): # real signature unknown; restored from __doc__
        """ cuda() -> int """
        return 0

    def default_memory(self): # real signature unknown; restored from __doc__
        """ default_memory() -> int """
        return 0

    def device_id(self): # real signature unknown; restored from __doc__
        """
        device_id(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> int
        
        Device Id.
        """
        return 0

    def device_type(self): # real signature unknown; restored from __doc__
        """
        device_type(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> int
        
        Device Type.
        """
        return 0

    def dml(self): # real signature unknown; restored from __doc__
        """ dml() -> int """
        return 0

    def fpga(self): # real signature unknown; restored from __doc__
        """ fpga() -> int """
        return 0

    def npu(self): # real signature unknown; restored from __doc__
        """ npu() -> int """
        return 0

    def webgpu(self): # real signature unknown; restored from __doc__
        """ webgpu() -> int """
        return 0

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, arg0, arg1, arg2): # real signature unknown; restored from __doc__
        """ __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice, arg0: int, arg1: int, arg2: int) -> None """
        pass


