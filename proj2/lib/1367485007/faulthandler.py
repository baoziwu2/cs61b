# encoding: utf-8
# module faulthandler
# from (built-in)
# by generator 1.147
""" faulthandler module. """
# no imports

# Variables with simple values

_EXCEPTION_ACCESS_VIOLATION = -1073741819

_EXCEPTION_INT_DIVIDE_BY_ZERO = -1073741676

_EXCEPTION_NONCONTINUABLE = 1

_EXCEPTION_NONCONTINUABLE_EXCEPTION = -1073741787

_EXCEPTION_STACK_OVERFLOW = -1073741571

# functions

def cancel_dump_traceback_later(*args, **kwargs): # real signature unknown
    """ Cancel the previous call to dump_traceback_later(). """
    pass

def disable(*args, **kwargs): # real signature unknown
    """ Disable the fault handler. """
    pass

def dump_traceback(*args, **kwargs): # real signature unknown
    """ Dump the traceback of the current thread, or of all threads if all_threads is True, into file. """
    pass

def dump_traceback_later(*args, **kwargs): # real signature unknown
    """
    Dump the traceback of all threads in timeout seconds,
    or each timeout seconds if repeat is True. If exit is True, call _exit(1) which is not safe.
    """
    pass

def enable(*args, **kwargs): # real signature unknown
    """ Enable the fault handler. """
    pass

def is_enabled(*args, **kwargs): # real signature unknown
    """ Check if the handler is enabled. """
    pass

def _fatal_error_c_thread(*args, **kwargs): # real signature unknown
    """ Call Py_FatalError() in a new C thread. """
    pass

def _raise_exception(*args, **kwargs): # real signature unknown
    """ Call RaiseException(code, flags). """
    pass

def _read_null(*args, **kwargs): # real signature unknown
    """ Read from NULL, raise a SIGSEGV or SIGBUS signal depending on the platform. """
    pass

def _sigabrt(*args, **kwargs): # real signature unknown
    """ Raise a SIGABRT signal. """
    pass

def _sigfpe(*args, **kwargs): # real signature unknown
    """ Raise a SIGFPE signal. """
    pass

def _sigsegv(*args, **kwargs): # real signature unknown
    """ Raise a SIGSEGV signal. """
    pass

# classes

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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 971, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x0000028385F63380>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x0000028385F63420>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x0000028385F634C0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x0000028385F63600>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x0000028385F63740>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x0000028385F63880>)>, 'load_module': <classmethod(<function _load_module_shim at 0x0000028385F62700>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 971
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='faulthandler', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

