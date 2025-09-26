# encoding: utf-8
# module _interpreters
# from (built-in)
# by generator 1.147
"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""

# imports
import interpreters as __interpreters


# Variables with simple values

WHENCE_CAPI = 3

WHENCE_LEGACY_CAPI = 2

WHENCE_RUNTIME = 1
WHENCE_STDLIB = 5
WHENCE_UNKNOWN = 0
WHENCE_XI = 4

# functions

def call(id, callable, args=None, kwargs=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    call(id, callable, args=None, kwargs=None, *, restrict=False)
    
    Call the provided object in the identified interpreter.
    Pass the given args and kwargs, if possible.
    
    "callable" may be a plain function with no free vars that takes
    no arguments.
    
    The function's code object is used and all its state
    is ignored, including its __globals__ dict.
    """
    pass

def capture_exception(exc=None): # real signature unknown; restored from __doc__
    """
    capture_exception(exc=None) -> types.SimpleNamespace
    
    Return a snapshot of an exception.  If "exc" is None
    then the current exception, if any, is used (but not cleared).
    
    The returned snapshot is the same as what _interpreters.exec() returns.
    """
    pass

def create(config=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    create([config], *, reqrefs=False) -> ID
    
    Create a new interpreter and return a unique generated ID.
    
    The caller is responsible for destroying the interpreter before exiting,
    typically by using _interpreters.destroy().  This can be managed 
    automatically by passing "reqrefs=True" and then using _incref() and
    _decref()` appropriately.
    
    "config" must be a valid interpreter config or the name of a
    predefined config ("isolated" or "legacy").  The default
    is "isolated".
    """
    pass

def decref(*args, **kwargs): # real signature unknown
    pass

def destroy(id, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    destroy(id, *, restrict=False)
    
    Destroy the identified interpreter.
    
    Attempting to destroy the current interpreter raises InterpreterError.
    So does an unrecognized ID.
    """
    pass

def exec(id, code, shared=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    exec(id, code, shared=None, *, restrict=False)
    
    Execute the provided code in the identified interpreter.
    This is equivalent to running the builtin exec() under the target
    interpreter, using the __dict__ of its __main__ module as both
    globals and locals.
    
    "code" may be a string containing the text of a Python script.
    
    Functions (and code objects) are also supported, with some restrictions.
    The code/function must not take any arguments or be a closure
    (i.e. have cell vars).  Methods and other callables are not supported.
    
    If a function is provided, its code object is used and all its state
    is ignored, including its __globals__ dict.
    """
    pass

def get_config(id, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    get_config(id, *, restrict=False) -> types.SimpleNamespace
    
    Return a representation of the config used to initialize the interpreter.
    """
    pass

def get_current(): # real signature unknown; restored from __doc__
    """
    get_current() -> (ID, whence)
    
    Return the ID of current interpreter.
    """
    pass

def get_main(): # real signature unknown; restored from __doc__
    """
    get_main() -> (ID, whence)
    
    Return the ID of main interpreter.
    """
    pass

def incref(*args, **kwargs): # real signature unknown
    pass

def is_running(id, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    is_running(id, *, restrict=False) -> bool
    
    Return whether or not the identified interpreter is running.
    """
    pass

def is_shareable(obj): # real signature unknown; restored from __doc__
    """
    is_shareable(obj) -> bool
    
    Return True if the object's data may be shared between interpreters and
    False otherwise.
    """
    return False

def list_all(): # real signature unknown; restored from __doc__
    """
    list_all() -> [(ID, whence)]
    
    Return a list containing the ID of every existing interpreter.
    """
    pass

def new_config(name='isolated', *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    new_config(name='isolated', /, **overrides) -> type.SimpleNamespace
    
    Return a representation of a new PyInterpreterConfig.
    
    The name determines the initial values of the config.  Supported named
    configs are: default, isolated, legacy, and empty.
    
    Any keyword arguments are set on the corresponding config fields,
    overriding the initial values.
    """
    pass

def run_func(id, func, shared=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    run_func(id, func, shared=None, *, restrict=False)
    
    Execute the body of the provided function in the identified interpreter.
    Code objects are also supported.  In both cases, closures and args
    are not supported.  Methods and other callables are not supported either.
    
    (See _interpreters.exec().
    """
    pass

def run_string(id, script, shared=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    run_string(id, script, shared=None, *, restrict=False)
    
    Execute the provided string in the identified interpreter.
    
    (See _interpreters.exec().
    """
    pass

def set___main___attrs(id, ns, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set___main___attrs(id, ns, *, restrict=False)
    
    Bind the given attributes in the interpreter's __main__ module.
    """
    pass

def whence(id): # real signature unknown; restored from __doc__
    """
    whence(id) -> int
    
    Return an identifier for where the interpreter was created.
    """
    return 0

# classes

class CrossInterpreterBufferView(object):
    # no doc
    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterpreterError(Exception):
    """ A cross-interpreter operation failed """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterpreterNotFoundError(__interpreters.InterpreterError):
    """ An interpreter was not found """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NotShareableError(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 971, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000002C288A53380>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000002C288A53420>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000002C288A534C0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000002C288A53600>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000002C288A53740>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000002C288A53880>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000002C288A52700>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 971
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_interpreters', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

