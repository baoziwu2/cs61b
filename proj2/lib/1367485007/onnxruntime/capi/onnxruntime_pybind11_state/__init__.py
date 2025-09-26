# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


# functions

def create_and_register_allocator(arg0, arg1): # real signature unknown; restored from __doc__
    """ create_and_register_allocator(arg0: OrtMemoryInfo, arg1: OrtArenaCfg) -> None """
    pass

def create_and_register_allocator_v2(arg0, arg1, arg2, p_str=None, p_str=None_1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ create_and_register_allocator_v2(arg0: str, arg1: OrtMemoryInfo, arg2: dict[str, str], arg3: OrtArenaCfg) -> None """
    pass

def disable_telemetry_events(): # real signature unknown; restored from __doc__
    """
    disable_telemetry_events() -> None
    
    Disables platform-specific telemetry collection.
    """
    pass

def enable_telemetry_events(): # real signature unknown; restored from __doc__
    """
    enable_telemetry_events() -> None
    
    Enables platform-specific telemetry collection where applicable.
    """
    pass

def get_all_operator_schema(): # real signature unknown; restored from __doc__
    """
    get_all_operator_schema() -> list[onnx::OpSchema]
    
    Return a vector of OpSchema all registered operators
    """
    return []

def get_all_opkernel_def(): # real signature unknown; restored from __doc__
    """
    get_all_opkernel_def() -> list[onnxruntime::KernelDef]
    
    Return a vector of KernelDef for all registered OpKernels
    """
    return []

def get_all_providers(): # real signature unknown; restored from __doc__
    """
    get_all_providers() -> list[str]
    
    Return list of Execution Providers that this version of Onnxruntime can support. The order of elements represents the default priority order of Execution Providers from highest to lowest.
    """
    return []

def get_available_providers(): # real signature unknown; restored from __doc__
    """
    get_available_providers() -> list[str]
    
    Return list of available Execution Providers in this installed version of Onnxruntime. The order of elements represents the default priority order of Execution Providers from highest to lowest.
    """
    return []

def get_build_info(): # real signature unknown; restored from __doc__
    """ get_build_info() -> str """
    return ""

def get_default_session_options(): # real signature unknown; restored from __doc__
    """
    get_default_session_options() -> OrtSessionOptions
    
    Return a default session_options instance.
    """
    pass

def get_device(): # real signature unknown; restored from __doc__
    """
    get_device() -> str
    
    Return the device used to compute the prediction (CPU, MKL, ...)
    """
    return ""

def get_session_initializer(): # real signature unknown; restored from __doc__
    """
    get_session_initializer() -> onnxruntime::python::SessionObjectInitializer
    
    Return a default session object initializer.
    """
    pass

def get_version_string(): # real signature unknown; restored from __doc__
    """ get_version_string() -> str """
    return ""

def has_collective_ops(): # real signature unknown; restored from __doc__
    """ has_collective_ops() -> bool """
    return False

def is_dlpack_uint8_tensor(arg0): # real signature unknown; restored from __doc__
    """
    is_dlpack_uint8_tensor(arg0: capsule) -> bool
    
    Tells if a DLPack structure is a uint8 tensor.
    .. note::
        Boolean tensors are also uint8 tensor once converted with DLPack protocol.
    """
    return False

def quantize_matmul_4bits(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    quantize_matmul_4bits(*args, **kwargs)
    Overloaded function.
    
    1. quantize_matmul_4bits(arg0: numpy.ndarray[numpy.uint8], arg1: numpy.ndarray[numpy.float32], arg2: numpy.ndarray[numpy.float32], arg3: numpy.ndarray[numpy.uint8], arg4: int, arg5: int, arg6: int, arg7: bool) -> None
    
    2. quantize_matmul_4bits(arg0: numpy.ndarray[numpy.uint8], arg1: numpy.ndarray[float16], arg2: numpy.ndarray[float16], arg3: numpy.ndarray[numpy.uint8], arg4: int, arg5: int, arg6: int, arg7: bool) -> None
    """
    pass

def quantize_matmul_8bits(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    quantize_matmul_8bits(*args, **kwargs)
    Overloaded function.
    
    1. quantize_matmul_8bits(arg0: numpy.ndarray[numpy.uint8], arg1: numpy.ndarray[numpy.float32], arg2: numpy.ndarray[numpy.float32], arg3: numpy.ndarray[numpy.uint8], arg4: int, arg5: int, arg6: int, arg7: bool) -> None
    
    2. quantize_matmul_8bits(arg0: numpy.ndarray[numpy.uint8], arg1: numpy.ndarray[float16], arg2: numpy.ndarray[float16], arg3: numpy.ndarray[numpy.uint8], arg4: int, arg5: int, arg6: int, arg7: bool) -> None
    """
    pass

def quantize_matmul_bnb4(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    quantize_matmul_bnb4(*args, **kwargs)
    Overloaded function.
    
    1. quantize_matmul_bnb4(arg0: numpy.ndarray[numpy.uint8], arg1: numpy.ndarray[numpy.float32], arg2: numpy.ndarray[numpy.float32], arg3: int, arg4: int, arg5: int, arg6: int) -> None
    
    2. quantize_matmul_bnb4(arg0: numpy.ndarray[numpy.uint8], arg1: numpy.ndarray[float16], arg2: numpy.ndarray[float16], arg3: int, arg4: int, arg5: int, arg6: int) -> None
    """
    pass

def quantize_qdq_matmul_4bits(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    quantize_qdq_matmul_4bits(*args, **kwargs)
    Overloaded function.
    
    1. quantize_qdq_matmul_4bits(arg0: numpy.ndarray[numpy.uint8], arg1: numpy.ndarray[numpy.float32], arg2: numpy.ndarray[numpy.float32], arg3: numpy.ndarray[numpy.uint8], arg4: int, arg5: int, arg6: int, arg7: bool) -> bool
    
    2. quantize_qdq_matmul_4bits(arg0: numpy.ndarray[numpy.uint8], arg1: numpy.ndarray[float16], arg2: numpy.ndarray[float16], arg3: numpy.ndarray[numpy.uint8], arg4: int, arg5: int, arg6: int, arg7: bool) -> bool
    """
    pass

def set_default_logger_severity(arg0): # real signature unknown; restored from __doc__
    """
    set_default_logger_severity(arg0: int) -> None
    
    Sets the default logging severity. 0:Verbose, 1:Info, 2:Warning, 3:Error, 4:Fatal
    """
    pass

def set_default_logger_verbosity(arg0): # real signature unknown; restored from __doc__
    """
    set_default_logger_verbosity(arg0: int) -> None
    
    Sets the default logging verbosity level. To activate the verbose log, you need to set the default logging severity to 0:Verbose level.
    """
    pass

def set_seed(arg0): # real signature unknown; restored from __doc__
    """
    set_seed(arg0: int) -> None
    
    Sets the seed used for random number generation in Onnxruntime.
    """
    pass

# classes

from .AdapterFormat import AdapterFormat
from .ArenaExtendStrategy import ArenaExtendStrategy
from .EngineError import EngineError
from .EPFail import EPFail
from .ExecutionMode import ExecutionMode
from .ExecutionOrder import ExecutionOrder
from .Fail import Fail
from .GraphOptimizationLevel import GraphOptimizationLevel
from .InferenceSession import InferenceSession
from .InvalidArgument import InvalidArgument
from .InvalidGraph import InvalidGraph
from .InvalidProtobuf import InvalidProtobuf
from .LoraAdapter import LoraAdapter
from .ModelLoaded import ModelLoaded
from .ModelMetadata import ModelMetadata
from .NodeArg import NodeArg
from .NoModel import NoModel
from .NoSuchFile import NoSuchFile
from .NotImplemented import NotImplemented
from .OrtAllocatorType import OrtAllocatorType
from .OrtArenaCfg import OrtArenaCfg
from .OrtDevice import OrtDevice
from .OrtMemoryInfo import OrtMemoryInfo
from .OrtMemType import OrtMemType
from .OrtSparseFormat import OrtSparseFormat
from .OrtValue import OrtValue
from .OrtValueVector import OrtValueVector
from .RunOptions import RunOptions
from .RuntimeException import RuntimeException
from .SessionIOBinding import SessionIOBinding
from .SessionObjectInitializer import SessionObjectInitializer
from .SessionOptions import SessionOptions
from .SparseBlockSparseView import SparseBlockSparseView
from .SparseCooView import SparseCooView
from .SparseCsrView import SparseCsrView
from .SparseTensor import SparseTensor
# variables with complex values

kNextPowerOfTwo = None # (!) real value is '<ArenaExtendStrategy.kNextPowerOfTwo: 0>'

kSameAsRequested = None # (!) real value is '<ArenaExtendStrategy.kSameAsRequested: 1>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000215A27ADF20>'

__spec__ = None # (!) real value is "ModuleSpec(name='onnxruntime.capi.onnxruntime_pybind11_state', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000215A27ADF20>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\onnxruntime\\\\capi\\\\onnxruntime_pybind11_state.pyd')"

