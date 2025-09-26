# encoding: utf-8
# module onnxruntime.capi.onnxruntime_pybind11_state
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\onnxruntime\capi\onnxruntime_pybind11_state.pyd
# by generator 1.147
""" pybind11 stateful interface to ONNX runtime """

# imports
import onnxruntime.capi.onnxruntime_pybind11_state.schemadef as schemadef # <module 'onnxruntime.capi.onnxruntime_pybind11_state.schemadef'>
import onnxruntime.capi.onnxruntime_pybind11_state.opkernel as opkernel # <module 'onnxruntime.capi.onnxruntime_pybind11_state.opkernel'>
import pybind11_builtins as __pybind11_builtins


class SparseTensor(__pybind11_builtins.pybind11_object):
    # no doc
    def blocksparse_from_numpy(self, arg0, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ blocksparse_from_numpy(arg0: list[int], arg1: numpy.ndarray, arg2: numpy.ndarray[numpy.int32], arg3: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor """
        pass

    def data_type(self): # real signature unknown; restored from __doc__
        """ data_type(self: onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor) -> str """
        return ""

    def dense_shape(self): # real signature unknown; restored from __doc__
        """ dense_shape(self: onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor) -> list """
        return []

    def device_name(self): # real signature unknown; restored from __doc__
        """ device_name(self: onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor) -> str """
        return ""

    def get_blocksparse_data(self): # real signature unknown; restored from __doc__
        """ get_blocksparse_data(self: onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor) -> onnxruntime.capi.onnxruntime_pybind11_state.SparseBlockSparseView """
        pass

    def get_coo_data(self): # real signature unknown; restored from __doc__
        """ get_coo_data(self: onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor) -> onnxruntime.capi.onnxruntime_pybind11_state.SparseCooView """
        pass

    def get_csrc_data(self): # real signature unknown; restored from __doc__
        """ get_csrc_data(self: onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor) -> onnxruntime.capi.onnxruntime_pybind11_state.SparseCsrView """
        pass

    def sparse_coo_from_numpy(self, arg0, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sparse_coo_from_numpy(arg0: list[int], arg1: numpy.ndarray, arg2: numpy.ndarray[numpy.int64], arg3: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor """
        pass

    def sparse_csr_from_numpy(self, arg0, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sparse_csr_from_numpy(arg0: list[int], arg1: numpy.ndarray, arg2: numpy.ndarray[numpy.int64], arg3: numpy.ndarray[numpy.int64], arg4: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor """
        pass

    def to_cuda(self, arg0): # real signature unknown; restored from __doc__
        """ to_cuda(self: onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor, arg0: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -> None """
        pass

    def values(self): # real signature unknown; restored from __doc__
        """ values(self: onnxruntime.capi.onnxruntime_pybind11_state.SparseTensor) -> numpy.ndarray """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



