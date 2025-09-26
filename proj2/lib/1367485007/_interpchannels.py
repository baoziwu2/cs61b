# encoding: utf-8
# module _interpchannels
# from (built-in)
# by generator 1.147
"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""
# no imports

# functions

def close(cid, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    channel_close(cid, *, send=None, recv=None, force=False)
    
    Close the channel for all interpreters.
    
    If the channel is empty then the keyword args are ignored and both
    ends are immediately closed.  Otherwise, if 'force' is True then
    all queued items are released and both ends are immediately
    closed.
    
    If the channel is not empty *and* 'force' is False then following
    happens:
    
     * recv is True (regardless of send):
       - raise ChannelNotEmptyError
     * recv is None and send is None:
       - raise ChannelNotEmptyError
     * send is True and recv is not True:
       - fully close the 'send' end
       - close the 'recv' end to interpreters not already receiving
       - fully close it once empty
    
    Closing an already closed channel results in a ChannelClosedError.
    
    Once the channel's ID has no more ref counts in any interpreter
    the channel will be destroyed.
    """
    pass

def create(unboundop): # real signature unknown; restored from __doc__
    """
    channel_create(unboundop) -> cid
    
    Create a new cross-interpreter channel and return a unique generated ID.
    """
    pass

def destroy(cid): # real signature unknown; restored from __doc__
    """
    channel_destroy(cid)
    
    Close and finalize the channel.  Afterward attempts to use the channel
    will behave as though it never existed.
    """
    pass

def get_channel_defaults(cid): # real signature unknown; restored from __doc__
    """
    get_channel_defaults(cid)
    
    Return the channel's default values, set when it was created.
    """
    pass

def get_count(cid): # real signature unknown; restored from __doc__
    """
    get_count(cid)
    
    Return the number of items in the channel.
    """
    pass

def get_info(cid): # real signature unknown; restored from __doc__
    """
    get_info(cid)
    
    Return details about the channel.
    """
    pass

def list_all(): # real signature unknown; restored from __doc__
    """
    channel_list_all() -> [cid]
    
    Return the list of all IDs for active channels.
    """
    pass

def list_interpreters(cid, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    channel_list_interpreters(cid, *, send) -> [id]
    
    Return the list of all interpreter IDs associated with an end of the channel.
    
    The 'send' argument should be a boolean indicating whether to use the send or
    receive end.
    """
    pass

def recv(cid, default=None): # real signature unknown; restored from __doc__
    """
    channel_recv(cid, [default]) -> (obj, unboundop)
    
    Return a new object from the data at the front of the channel's queue.
    
    If there is nothing to receive then raise ChannelEmptyError, unless
    a default value is provided.  In that case return it.
    """
    pass

def release(cid, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    channel_release(cid, *, send=None, recv=None, force=True)
    
    Close the channel for the current interpreter.  'send' and 'recv'
    (bool) may be used to indicate the ends to close.  By default both
    ends are closed.  Closing an already closed end is a noop.
    """
    pass

def send(cid, obj, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    channel_send(cid, obj, *, blocking=True, timeout=None)
    
    Add the object's data to the channel's queue.
    By default this waits for the object to be received.
    """
    pass

def send_buffer(cid, obj, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    channel_send_buffer(cid, obj, *, blocking=True, timeout=None)
    
    Add the object's buffer to the channel's queue.
    By default this waits for the object to be received.
    """
    pass

def _channel_id(*args, **kwargs): # real signature unknown
    pass

def _register_end_types(*args, **kwargs): # real signature unknown
    pass

# classes

class ChannelError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class ChannelClosedError(ChannelError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ChannelEmptyError(ChannelError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ChannelID(object):
    """ A channel ID identifies a channel and may be used as an int. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """'send', 'recv', or 'both'"""

    recv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the 'recv' end of the channel"""

    send = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the 'send' end of the channel"""



class ChannelInfo(tuple):
    """
    ChannelInfo
    
    A named tuple of a channel's state.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __replace__(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the structure with new values for the specified fields. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """both ends are closed"""

    closing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """send is closed, recv is non-empty"""

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """queued objects"""

    num_interp_both = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """interpreters bound to both ends"""

    num_interp_both_recv_released = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """interpreters bound to both ends and released_from_the recv end"""

    num_interp_both_released = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """interpreters bound to both ends and released_from_both"""

    num_interp_both_send_released = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """interpreters bound to both ends and released_from_the send end"""

    num_interp_recv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """interpreters bound to the send end"""

    num_interp_recv_released = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """interpreters bound to the send end and released"""

    num_interp_send = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """interpreters bound to the send end"""

    num_interp_send_released = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """interpreters bound to the send end and released"""

    open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """both ends are open"""

    recv_associated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current interpreter is bound to the recv end"""

    recv_released = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current interpreter *was* bound to the recv end"""

    send_associated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current interpreter is bound to the send end"""

    send_released = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current interpreter *was* bound to the send end"""


    n_fields = 16
    n_sequence_fields = 8
    n_unnamed_fields = 0
    __match_args__ = (
        'open',
        'closing',
        'closed',
        'count',
        'num_interp_send',
        'num_interp_send_released',
        'num_interp_recv',
        'num_interp_recv_released',
    )


class ChannelNotEmptyError(ChannelError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ChannelNotFoundError(ChannelError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class __loader__(object):
    """
    Meta path import for built-in modules.
    
    All methods are either class or static methods to avoid the need to
    instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
        This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 971, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000002647FC73380>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000002647FC73420>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000002647FC734C0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000002647FC73600>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000002647FC73740>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000002647FC73880>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000002647FC72700>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 971
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_interpchannels', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

