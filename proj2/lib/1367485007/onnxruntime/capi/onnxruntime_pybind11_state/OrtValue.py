# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class OrtValue(__pybind11_builtins.pybind11_object):
    # no doc
    def as_sparse_tensor(self): # real signature unknown; restored from __doc__
        """ as_sparse_tensor(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> onnxruntime::python::PySparseTensor """
        pass

    def data_ptr(self): # real signature unknown; restored from __doc__
        """ data_ptr(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> int """
        return 0

    def data_type(self): # real signature unknown; restored from __doc__
        """ data_type(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> str """
        return ""

    def device_name(self): # real signature unknown; restored from __doc__
        """ device_name(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> str """
        return ""

    def element_type(self): # real signature unknown; restored from __doc__
        """
        element_type(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> int
        
        Returns an integer equal to the ONNX tensor proto type of the tensor or sequence. This integer is one type defined by ONNX TensorProto_DataType (such as onnx.TensorProto.FLOAT).Raises an exception in any other case.
        """
        return 0

    def from_dlpack(self, data, is_bool_tensor=False): # real signature unknown; restored from __doc__
        """
        from_dlpack(data: object, is_bool_tensor: bool = False) -> onnxruntime.capi.onnxruntime_pybind11_state.OrtValue
        
        Converts a tensor from a external library into an OrtValue by means of the __dlpack__ protocol.
        """
        pass

    def has_value(self): # real signature unknown; restored from __doc__
        """ has_value(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> bool """
        return False

    def is_sparse_tensor(self): # real signature unknown; restored from __doc__
        """ is_sparse_tensor(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> bool """
        return False

    def is_tensor(self): # real signature unknown; restored from __doc__
        """ is_tensor(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> bool """
        return False

    def is_tensor_sequence(self): # real signature unknown; restored from __doc__
        """ is_tensor_sequence(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> bool """
        return False

    def numpy(self): # real signature unknown; restored from __doc__
        """ numpy(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> object """
        return object()

    def ortvalue_from_numpy(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ ortvalue_from_numpy(arg0: object, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> onnxruntime.capi.onnxruntime_pybind11_state.OrtValue """
        pass

    def ortvalue_from_numpy_with_onnx_type(self, arg0, arg1): # real signature unknown; restored from __doc__
        """ ortvalue_from_numpy_with_onnx_type(arg0: numpy.ndarray, arg1: int) -> onnxruntime.capi.onnxruntime_pybind11_state.OrtValue """
        pass

    def ortvalue_from_shape_and_onnx_type(self, arg0, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ortvalue_from_shape_and_onnx_type(arg0: list[int], arg1: int, arg2: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> onnxruntime.capi.onnxruntime_pybind11_state.OrtValue """
        pass

    def ortvalue_from_shape_and_type(self, arg0, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ortvalue_from_shape_and_type(arg0: list[int], arg1: object, arg2: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> onnxruntime.capi.onnxruntime_pybind11_state.OrtValue """
        pass

    def ort_value_from_sparse_tensor(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ort_value_from_sparse_tensor(arg0: onnxruntime::python::PySparseTensor) -> onnxruntime.capi.onnxruntime_pybind11_state.OrtValue """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> list """
        return []

    def to_dlpack(self): # real signature unknown; restored from __doc__
        """
        to_dlpack(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> object
        
        Returns a DLPack representing the tensor. This method does not copy the pointer shape, instead, it copies the pointer value. The OrtValue must be persist until the dlpack structure is consumed.
        """
        return object()

    def update_inplace(self, arg0): # real signature unknown; restored from __doc__
        """ update_inplace(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue, arg0: numpy.ndarray) -> None """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __dlpack_device__(self): # real signature unknown; restored from __doc__
        """
        __dlpack_device__(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> tuple
        
        Returns a tuple of integers, (device, device index) (part of __dlpack__ protocol).
        """
        return ()

    def __dlpack__(self, stream=None): # real signature unknown; restored from __doc__
        """
        __dlpack__(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue, stream: object = None) -> object
        
        Returns a DLPack representing the tensor (part of __dlpack__ protocol). This method does not copy the pointer shape, instead, it copies the pointer value. The OrtValue must persist until the dlpack structure is consumed.
        """
        return object()

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


