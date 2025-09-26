# encoding: utf-8
# module _multibytecodec
# from (built-in)
# by generator 1.147
# no doc
# no imports

# functions

def __create_codec(*args, **kwargs): # real signature unknown
    pass

# classes

class MultibyteIncrementalDecoder(object):
    # no doc
    def decode(self, *args, **kwargs): # real signature unknown
        pass

    def getstate(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def setstate(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how to treat errors"""



class MultibyteIncrementalEncoder(object):
    # no doc
    def encode(self, *args, **kwargs): # real signature unknown
        pass

    def getstate(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def setstate(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how to treat errors"""



class MultibyteStreamReader(object):
    # no doc
    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        pass

    def readlines(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how to treat errors"""

    stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class MultibyteStreamWriter(object):
    # no doc
    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def writelines(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how to treat errors"""

    stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 971, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000002484AF13380>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000002484AF13420>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000002484AF134C0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000002484AF13600>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000002484AF13740>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000002484AF13880>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000002484AF12700>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 971
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_multibytecodec', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

