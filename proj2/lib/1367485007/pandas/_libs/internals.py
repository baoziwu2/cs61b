# encoding: utf-8
# module pandas._libs.internals
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\internals.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import weakref as weakref # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\weakref.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
from pandas._libs.algos import ensure_int64


# functions

def get_blkno_indexers(*args, **kwargs): # real signature unknown
    """
    Enumerate contiguous runs of integers in ndarray.
    
        Iterate over elements of `blknos` yielding ``(blkno, slice(start, stop))``
        pairs for each contiguous run found.
    
        If `group` is True and there is more than one run for a certain blkno,
        ``(blkno, array)`` with an array containing positions of all elements equal
        to blkno.
    
        Returns
        -------
        list[tuple[int, slice | np.ndarray]]
    """
    pass

def get_blkno_placements(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        blknos : np.ndarray[int64]
        group : bool, default True
    
        Returns
        -------
        iterator
            yield (blkno, BlockPlacement)
    """
    pass

def get_concat_blkno_indexers(*args, **kwargs): # real signature unknown
    """
    Given the mgr.blknos for a list of mgrs, break range(len(mgrs[0])) into
        slices such that within each slice blknos_list[i] is constant for each i.
    
        This is a multi-Manager analogue to get_blkno_indexers with group=False.
    """
    pass

def slice_len(*args, **kwargs): # real signature unknown
    """
    Get length of a bounded slice.
    
        The slice must not have any "open" bounds that would create dependency on
        container size, i.e.:
        - if ``s.step is None or s.step > 0``, ``s.stop`` is not ``None``
        - if ``s.step < 0``, ``s.start`` is not ``None``
    
        Otherwise, the result is unreliable.
    """
    pass

def update_blklocs_and_blknos(*args, **kwargs): # real signature unknown
    """ Update blklocs and blknos when a new column is inserted at 'loc'. """
    pass

def _unpickle_block(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Block(object):
    """ Defining __init__ in a cython class significantly improves performance. """
    def slice_block_rows(self, *args, **kwargs): # real signature unknown
        """
        Perform __getitem__-like specialized to slicing along index.
        
                Assumes self.ndim == 2
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _mgr_locs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000025A15AD8EF0>'


class BlockManager(object):
    # no doc
    def get_slice(self, *args, **kwargs): # real signature unknown
        pass

    def _post_setstate(self, *args, **kwargs): # real signature unknown
        pass

    def _rebuild_blknos_and_blklocs(self, *args, **kwargs): # real signature unknown
        """ Update mgr._blknos / mgr._blklocs. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    axes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _blklocs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _blknos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_consolidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _known_consolidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000025A15AD90D0>'


class BlockPlacement(object):
    # no doc
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def append(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def increment_above(self, *args, **kwargs): # real signature unknown
        """ Increment any entries of 'loc' or above by one. """
        pass

    def tile_for_unstack(self, *args, **kwargs): # real signature unknown
        """ Find the new mgr_locs for the un-stacked version of a Block. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    as_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    as_slice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indexer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_slice_like = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000025A15AD8E00>'


class BlockValuesRefs(object):
    """
    Tracks all references to a given array.
    
        Keeps track of all blocks (through weak references) that reference the same
        data.
    """
    def add_index_reference(self, *args, **kwargs): # real signature unknown
        """
        Adds a new reference to our reference collection when creating an index.
        
                Parameters
                ----------
                index : Index
                    The index that the new reference should point to.
        """
        pass

    def add_reference(self, *args, **kwargs): # real signature unknown
        """
        Adds a new reference to our reference collection.
        
                Parameters
                ----------
                blk : Block
                    The block that the new references should point to.
        """
        pass

    def has_reference(self, *args, **kwargs): # real signature unknown
        """
        Checks if block has foreign references.
        
                A reference is only relevant if it is still alive. The reference to
                ourselves does not count.
        
                Returns
                -------
                bool
        """
        pass

    def _clear_dead_references(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    clear_counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    referenced_blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class defaultdict(dict):
    """
    defaultdict(default_factory=None, /, [...]) --> dict with default factory
    
    The default factory is called without arguments to produce
    a new value when a key is not present, in __getitem__ only.
    A defaultdict compares equal to a dict with the same items.
    All remaining arguments are treated the same as if they were
    passed to the dict constructor, including keyword arguments.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ D.copy() -> a shallow copy of D. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, default_factory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __missing__(self, key): # real signature unknown; restored from __doc__
        """
        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory()
          return value
        """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    default_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Factory for default value called by __missing__()."""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025A15A8A390>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.internals', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025A15A8A390>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\internals.cp313-win_amd64.pyd')"

__test__ = {}

