# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class InferenceSession(__pybind11_builtins.pybind11_object):
    """ This is the main class used to run a model. """
    def end_profiling(self): # real signature unknown; restored from __doc__
        """ end_profiling(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession) -> str """
        return ""

    def get_providers(self): # real signature unknown; restored from __doc__
        """ get_providers(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession) -> list[str] """
        return []

    def get_provider_options(self): # real signature unknown; restored from __doc__
        """ get_provider_options(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession) -> dict[str, dict[str, str]] """
        return {}

    def get_tuning_results(self): # real signature unknown; restored from __doc__
        """ get_tuning_results(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession) -> list """
        return []

    def initialize_session(self, arg0, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        initialize_session(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession, arg0: list[str], arg1: list[dict[str, str]], arg2: set[str]) -> None
        
        Load a model saved in ONNX or ORT format.
        """
        pass

    def run(self, arg0, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ run(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession, arg0: list[str], arg1: dict[str, object], arg2: onnxruntime.capi.onnxruntime_pybind11_state.RunOptions) -> list """
        pass

    def run_async(self, arg0, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ run_async(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession, arg0: list[str], arg1: dict[str, object], arg2: Callable[[list[object], object, str], None], arg3: object, arg4: onnxruntime.capi.onnxruntime_pybind11_state.RunOptions) -> None """
        pass

    def run_with_iobinding(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ run_with_iobinding(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession, arg0: onnxruntime::SessionIOBinding, arg1: onnxruntime.capi.onnxruntime_pybind11_state.RunOptions) -> None """
        pass

    def run_with_ortvaluevector(self, arg0, arg1, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ run_with_ortvaluevector(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession, arg0: onnxruntime.capi.onnxruntime_pybind11_state.RunOptions, arg1: list[str], arg2: std::vector<OrtValue,std::allocator<OrtValue> >, arg3: list[str], arg4: std::vector<OrtValue,std::allocator<OrtValue> >, arg5: list[onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice]) -> None """
        pass

    def run_with_ort_values(self, arg0, arg1, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ run_with_ort_values(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession, arg0: dict, arg1: list[str], arg2: onnxruntime.capi.onnxruntime_pybind11_state.RunOptions) -> std::vector<OrtValue,std::allocator<OrtValue> > """
        pass

    def set_tuning_results(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ set_tuning_results(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession, arg0: list, arg1: bool) -> None """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, arg0, arg1, arg2, arg3): # real signature unknown; restored from __doc__
        """ __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession, arg0: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions, arg1: str, arg2: bool, arg3: bool) -> None """
        pass

    get_profiling_start_time_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inputs_meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model_meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    outputs_meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    overridable_initializers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    session_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



