# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class SessionOptions(__pybind11_builtins.pybind11_object):
    """ Configuration information for a session. """
    def add_external_initializers(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ add_external_initializers(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions, arg0: list, arg1: list) -> None """
        pass

    def add_free_dimension_override_by_denotation(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        add_free_dimension_override_by_denotation(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions, arg0: str, arg1: int) -> None
        
        Specify the dimension size for each denotation associated with an input's free dimension.
        """
        pass

    def add_free_dimension_override_by_name(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        add_free_dimension_override_by_name(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions, arg0: str, arg1: int) -> None
        
        Specify values of named dimensions within model inputs.
        """
        pass

    def add_initializer(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ add_initializer(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions, arg0: str, arg1: object) -> None """
        pass

    def add_session_config_entry(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        add_session_config_entry(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions, arg0: str, arg1: str) -> None
        
        Set a single session configuration entry as a pair of strings.
        """
        pass

    def get_session_config_entry(self, arg0): # real signature unknown; restored from __doc__
        """
        get_session_config_entry(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions, arg0: str) -> str
        
        Get a single session configuration value using the given configuration key.
        """
        return ""

    def register_custom_ops_library(self, arg0): # real signature unknown; restored from __doc__
        """
        register_custom_ops_library(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions, arg0: str) -> None
        
        Specify the path to the shared library containing the custom op kernels required to run a model.
        """
        pass

    def set_load_cancellation_flag(self, arg0): # real signature unknown; restored from __doc__
        """
        set_load_cancellation_flag(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions, arg0: bool) -> None
        
        Request inference session load cancellation
        """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions) -> None """
        pass

    enable_cpu_mem_arena = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable memory arena on CPU. Default is true."""

    enable_mem_pattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable the memory pattern optimization. Default is true."""

    enable_mem_reuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable the memory reuse optimization. Default is true."""

    enable_profiling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable profiling for this session. Default is false."""

    execution_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the execution mode. Default is sequential."""

    execution_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the execution order. Default is basic topological order."""

    graph_optimization_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Graph optimization level for this session."""

    inter_op_num_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the number of threads used to parallelize the execution of the graph (across nodes). Default is 0 to let onnxruntime choose."""

    intra_op_num_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the number of threads used to parallelize the execution within nodes. Default is 0 to let onnxruntime choose."""

    logid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Logger id to use for session output."""

    log_severity_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Log severity level. Applies to session load, initialization, etc.
0:Verbose, 1:Info, 2:Warning. 3:Error, 4:Fatal. Default is 2."""

    log_verbosity_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """VLOG level if DEBUG build and session_log_severity_level is 0.
Applies to session load, initialization, etc. Default is 0."""

    optimized_model_filepath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
File path to serialize optimized model to.
Optimized model is not serialized unless optimized_model_filepath is set.
Serialized model format will default to ONNX unless:
- add_session_config_entry is used to set 'session.save_model_format' to 'ORT', or
- there is no 'session.save_model_format' config entry and optimized_model_filepath ends in '.ort' (case insensitive)

"""

    profile_file_prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The prefix of the profile file. The current time will be appended to the file name."""

    use_deterministic_compute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to use deterministic compute. Default is false."""



