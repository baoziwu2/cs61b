# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class OrtValueVector(__pybind11_builtins.pybind11_object):
    # no doc
    def bool_tensor_indices(self): # real signature unknown; restored from __doc__
        """
        bool_tensor_indices(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector) -> list[int]
        
        Returns the indices of every boolean tensor in this vector of OrtValue. In case of a boolean tensor, method to_dlpacks returns a uint8 tensor instead of a boolean tensor. If torch consumes the dlpack structure, `.to(torch.bool)` must be applied to the torch tensor to get a boolean tensor.
        """
        return []

    def dlpack_at(self, arg0): # real signature unknown; restored from __doc__
        """ dlpack_at(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector, arg0: int) -> object """
        return object()

    def element_type_at(self, idx): # real signature unknown; restored from __doc__
        """
        element_type_at(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector, idx: int) -> int
        
        Returns an integer equal to the ONNX proto type of the tensor at position i. This integer is one type defined by ONNX TensorProto_DataType (such as onnx.TensorProto.FLOAT).Raises an exception in any other case.
        """
        return 0

    def push_back(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        push_back(*args, **kwargs)
        Overloaded function.
        
        1. push_back(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector, arg0: onnxruntime.capi.onnxruntime_pybind11_state.OrtValue) -> None
        
        2. push_back(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector, dlpack_tensor: object, is_bool_tensor: bool = False) -> None
        
        Add a new OrtValue after being ownership was transferred from the DLPack structure.
        """
        pass

    def push_back_batch(self, arg0, p_object=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        push_back_batch(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector, arg0: list[object], arg1: list[int], arg2: list[object], arg3: list[list[int]], arg4: list[onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice]) -> None
        
        Add a batch of OrtValue's by wrapping PyTorch tensors.
        """
        pass

    def reserve(self, arg0): # real signature unknown; restored from __doc__
        """ reserve(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector, arg0: int) -> None """
        pass

    def shrink_to_fit(self): # real signature unknown; restored from __doc__
        """ shrink_to_fit(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector) -> None """
        pass

    def to_dlpacks(self, to_tensor): # real signature unknown; restored from __doc__
        """
        to_dlpacks(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector, to_tensor: object) -> list
        
        Converts all OrtValue into tensors through DLPack protocol, the method creates
        a DLPack structure for every tensors, then calls python function `to_tensor` to a new object
        consuming the DLPack structure or return a list of capsule if this function is None.
        
        :param to_tensor: this function takes a capsule holding a pointer onto a DLPack structure and returns
            a new tensor which becomes the new owner of the data. This function takes one python object and
            returns a new python object. It fits the same signature as `torch.utils.from_dlpack`,
            if None, the method returns a capsule for every new DLPack structure.
        :return: a list containing the new tensors or a the new capsules if *to_tensor* is None
        
        This method is used to replace `tuple(torch._C._from_dlpack(ov.to_dlpack()) for ov in ort_values)`
        by a faster instruction `tuple(ort_values.to_dlpack(torch._C._from_dlpack))`. This loop
        is difficult to parallelize as it goes through the GIL many times.
        It creates many tensors acquiring ownership of existing OrtValue.
        This method saves one object creation and an C++ allocation
        for every transferred tensor.
        """
        return []

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, arg0): # real signature unknown; restored from __doc__
        """ __getitem__(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector, arg0: int) -> onnxruntime.capi.onnxruntime_pybind11_state.OrtValue """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector) -> None """
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ __iter__(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector) -> Iterator[onnxruntime.capi.onnxruntime_pybind11_state.OrtValue] """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ __len__(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector) -> int """
        return 0


