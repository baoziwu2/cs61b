# encoding: utf-8
# module _opcode
# from (built-in)
# by generator 1.147
""" Opcode support module. """
# no imports

# Variables with simple values

ENABLE_SPECIALIZATION = 1

# functions

def get_executor(*args, **kwargs): # real signature unknown
    """ Return the executor object at offset in code if exists, None otherwise. """
    pass

def get_intrinsic1_descs(*args, **kwargs): # real signature unknown
    """ Return a list of names of the unary intrinsics. """
    pass

def get_intrinsic2_descs(*args, **kwargs): # real signature unknown
    """ Return a list of names of the binary intrinsics. """
    pass

def get_nb_ops(*args, **kwargs): # real signature unknown
    """
    Return array of symbols of binary ops.
    
    Indexed by the BINARY_OP oparg value.
    """
    pass

def get_specialization_stats(*args, **kwargs): # real signature unknown
    """ Return the specialization stats """
    pass

def has_arg(*args, **kwargs): # real signature unknown
    """ Return True if the opcode uses its oparg, False otherwise. """
    pass

def has_const(*args, **kwargs): # real signature unknown
    """ Return True if the opcode accesses a constant, False otherwise. """
    pass

def has_exc(*args, **kwargs): # real signature unknown
    """ Return True if the opcode sets an exception handler, False otherwise. """
    pass

def has_free(*args, **kwargs): # real signature unknown
    """
    Return True if the opcode accesses a free variable, False otherwise.
    
    Note that 'free' in this context refers to names in the current scope
    that are referenced by inner scopes or names in outer scopes that are
    referenced from this scope. It does not include references to global
    or builtin scopes.
    """
    pass

def has_jump(*args, **kwargs): # real signature unknown
    """ Return True if the opcode has a jump target, False otherwise. """
    pass

def has_local(*args, **kwargs): # real signature unknown
    """ Return True if the opcode accesses a local variable, False otherwise. """
    pass

def has_name(*args, **kwargs): # real signature unknown
    """ Return True if the opcode accesses an attribute by name, False otherwise. """
    pass

def is_valid(*args, **kwargs): # real signature unknown
    """ Return True if opcode is valid, False otherwise. """
    pass

def stack_effect(*args, **kwargs): # real signature unknown
    """ Compute the stack effect of the opcode. """
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 971, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x00000249E2CE3380>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x00000249E2CE3420>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x00000249E2CE34C0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x00000249E2CE3600>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x00000249E2CE3740>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x00000249E2CE3880>)>, 'load_module': <classmethod(<function _load_module_shim at 0x00000249E2CE2700>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 971
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_opcode', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

