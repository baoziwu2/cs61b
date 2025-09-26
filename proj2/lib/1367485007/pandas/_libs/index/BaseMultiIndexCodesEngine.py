# encoding: utf-8
# module pandas._libs.index
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\index.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
import pandas._libs.algos as algos # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\algos.cp313-win_amd64.pyd
import pandas._libs.hashtable as _hash # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\hashtable.cp313-win_amd64.pyd

from .object import object

class BaseMultiIndexCodesEngine(object):
    """
    Base class for MultiIndexUIntEngine and MultiIndexPyIntEngine, which
        represent each label in a MultiIndex as an integer, by juxtaposing the bits
        encoding each level, with appropriate offsets.
    
        For instance: if 3 levels have respectively 3, 6 and 1 possible values,
        then their labels can be represented using respectively 2, 3 and 1 bits,
        as follows:
         _ _ _ _____ _ __ __ __
        |0|0|0| ... |0| 0|a1|a0| -> offset 0 (first level)
         — — — ————— — —— —— ——
        |0|0|0| ... |0|b2|b1|b0| -> offset 2 (bits required for first level)
         — — — ————— — —— —— ——
        |0|0|0| ... |0| 0| 0|c0| -> offset 5 (bits required for first two levels)
         ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾
        and the resulting unsigned integer representation will be:
         _ _ _ _____ _ __ __ __ __ __ __
        |0|0|0| ... |0|c0|b2|b1|b0|a1|a0|
         ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾
    
        Offsets are calculated at initialization, labels are transformed by method
        _codes_to_ints.
    
        Keys are located by first locating each component against the respective
        level, then locating (the integer representation of) codes.
    """
    def get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Returns an array giving the positions of each value of `target` in
                `self.values`, where -1 represents a value in `target` which does not
                appear in `self.values`
        
                Parameters
                ----------
                target : np.ndarray
        
                Returns
                -------
                np.ndarray[intp_t, ndim=1] of the indexer of `target` into
                `self.values`
        """
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def _codes_to_ints(self, *args, **kwargs): # real signature unknown
        pass

    def _extract_level_codes(self, *args, **kwargs): # real signature unknown
        """
        Map the requested list of (tuple) keys to their integer representations
                for searching in the underlying integer index.
        
                Parameters
                ----------
                target : MultiIndex
        
                Returns
                ------
                int_keys : 1-dimensional array of dtype uint64 or object
                    Integers representing one combination each
        """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return bool(key in self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                levels : list-like of numpy arrays
                    Levels of the MultiIndex.
                labels : list-like of numpy arrays of integer dtype
                    Labels of the MultiIndex.
                offsets : numpy array of uint64 dtype
                    Pre-calculated offsets, one for each level of the index.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


