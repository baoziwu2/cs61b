# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class SessionIOBinding(__pybind11_builtins.pybind11_object):
    # no doc
    def bind_input(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        bind_input(*args, **kwargs)
        Overloaded function.
        
        1. bind_input(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: object) -> None
        
        2. bind_input(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice, arg2: int, arg3: list[int], arg4: int) -> None
        
        3. bind_input(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice, arg2: object, arg3: list[int], arg4: int) -> None
        """
        pass

    def bind_ortvalue_input(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ bind_ortvalue_input(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> None """
        pass

    def bind_ortvalue_output(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ bind_ortvalue_output(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> None """
        pass

    def bind_output(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        bind_output(*args, **kwargs)
        Overloaded function.
        
        1. bind_output(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice, arg2: int, arg3: list[int], arg4: int) -> None
        
        2. bind_output(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice, arg2: object, arg3: list[int], arg4: int) -> None
        
        3. bind_output(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> None
        """
        pass

    def clear_binding_inputs(self): # real signature unknown; restored from __doc__
        """ clear_binding_inputs(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding) -> None """
        pass

    def clear_binding_outputs(self): # real signature unknown; restored from __doc__
        """ clear_binding_outputs(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding) -> None """
        pass

    def copy_outputs_to_cpu(self): # real signature unknown; restored from __doc__
        """ copy_outputs_to_cpu(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding) -> list """
        return []

    def get_outputs(self): # real signature unknown; restored from __doc__
        """ get_outputs(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding) -> onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector """
        pass

    def synchronize_inputs(self): # real signature unknown; restored from __doc__
        """ synchronize_inputs(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding) -> None """
        pass

    def synchronize_outputs(self): # real signature unknown; restored from __doc__
        """ synchronize_outputs(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding) -> None """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession) -> None """
        pass


