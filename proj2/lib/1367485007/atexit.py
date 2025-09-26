# encoding: utf-8
# module atexit
# from (built-in)
# by generator 1.147
"""
allow programmer to define multiple exit functions to be executed
upon normal program termination.

Two public functions, register and unregister, are defined.
"""
# no imports

# functions

def register(*args, **kwargs): # real signature unknown
    """
    Register a function to be executed upon normal program termination
    
        func - function to be called at exit
        args - optional arguments to pass to func
        kwargs - optional keyword arguments to pass to func
    
        func is returned to facilitate usage as a decorator.
    """
    pass

def unregister(*args, **kwargs): # real signature unknown
    """
    Unregister an exit function which was previously registered using
    atexit.register
    
        func - function to be unregistered
    """
    pass

def _clear(*args, **kwargs): # real signature unknown
    """ Clear the list of previously registered exit functions. """
    pass

def _ncallbacks(*args, **kwargs): # real signature unknown
    """ Return the number of registered exit functions. """
    pass

def _run_exitfuncs(*args, **kwargs): # real signature unknown
    """
    Run all registered exit functions.
    
    If a callback raises an exception, it is logged with sys.unraisablehook.
    """
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 971, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x00000144A27B3380>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x00000144A27B3420>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x00000144A27B34C0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x00000144A27B3600>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x00000144A27B3740>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x00000144A27B3880>)>, 'load_module': <classmethod(<function _load_module_shim at 0x00000144A27B2700>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 971
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='atexit', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

