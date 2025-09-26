# encoding: utf-8
# module pandas._libs.tslibs.dtypes
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslibs\dtypes.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\warnings.py
import enum as __enum


# functions

def abbrev_to_npy_unit(*args, **kwargs): # real signature unknown
    pass

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

def freq_to_period_freqstr(*args, **kwargs): # real signature unknown
    pass

def periods_per_day(*args, **kwargs): # real signature unknown
    """ How many of the given time units fit into a single day? """
    pass

def periods_per_second(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Enum(object):
    """
    Create a collection of name/value pairs.
    
    Example enumeration:
    
    >>> class Color(Enum):
    ...     RED = 1
    ...     BLUE = 2
    ...     GREEN = 3
    
    Access them by:
    
    - attribute access:
    
      >>> Color.RED
      <Color.RED: 1>
    
    - value lookup:
    
      >>> Color(1)
      <Color.RED: 1>
    
    - name lookup:
    
      >>> Color['RED']
      <Color.RED: 1>
    
    Enumerations can be iterated over, and know how many members they have:
    
    >>> len(Color)
    3
    
    >>> list(Color)
    [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
    
    Methods can be added to enumerations, and members can have their own
    attributes -- see the documentation for details.
    """
    def _add_alias_(self, name): # reliably restored by inspect
        # no doc
        pass

    def _add_value_alias_(self, value): # reliably restored by inspect
        # no doc
        pass

    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the list of values assigned
        """
        pass

    @classmethod
    def _missing_(cls, *args, **kwargs): # real signature unknown
        pass

    def _new_member_(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self): # reliably restored by inspect
        # no doc
        pass

    def __deepcopy__(self, memo): # reliably restored by inspect
        # no doc
        pass

    def __dir__(self): # reliably restored by inspect
        """ Returns public methods and other interesting attributes. """
        pass

    def __format__(self, format_spec): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __reduce_ex__(self, proto): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def __signature__(cls, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    name = None # (!) real value is '<enum.property object at 0x0000029804D03390>'
    value = None # (!) real value is '<enum.property object at 0x0000029804DE4A50>'
    _hashable_values_ = []
    _member_map_ = {}
    _member_names_ = []
    _member_type_ = object
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {}
    _value_repr_ = None
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'enum\', \'__firstlineno__\': 1109, \'__doc__\': "\\nCreate a collection of name/value pairs.\\n\\nExample enumeration:\\n\\n>>> class Color(Enum):\\n...     RED = 1\\n...     BLUE = 2\\n...     GREEN = 3\\n\\nAccess them by:\\n\\n- attribute access:\\n\\n  >>> Color.RED\\n  <Color.RED: 1>\\n\\n- value lookup:\\n\\n  >>> Color(1)\\n  <Color.RED: 1>\\n\\n- name lookup:\\n\\n  >>> Color[\'RED\']\\n  <Color.RED: 1>\\n\\nEnumerations can be iterated over, and know how many members they have:\\n\\n>>> len(Color)\\n3\\n\\n>>> list(Color)\\n[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]\\n\\nMethods can be added to enumerations, and members can have their own\\nattributes -- see the documentation for details.\\n", \'__signature__\': <classmethod(<function Enum.__signature__ at 0x0000029804E17380>)>, \'__new__\': <staticmethod(<function Enum.__new__ at 0x0000029804E17420>)>, \'__init__\': <function Enum.__init__ at 0x0000029804E174C0>, \'_add_alias_\': <function Enum._add_alias_ at 0x0000029804E17560>, \'_add_value_alias_\': <function Enum._add_value_alias_ at 0x0000029804E17600>, \'_generate_next_value_\': <staticmethod(<function Enum._generate_next_value_ at 0x0000029804E176A0>)>, \'_missing_\': <classmethod(<function Enum._missing_ at 0x0000029804E17740>)>, \'__repr__\': <function Enum.__repr__ at 0x0000029804E177E0>, \'__str__\': <function Enum.__str__ at 0x0000029804E17880>, \'__dir__\': <function Enum.__dir__ at 0x0000029804E17920>, \'__format__\': <function Enum.__format__ at 0x0000029804E179C0>, \'__hash__\': <function Enum.__hash__ at 0x0000029804E17A60>, \'__reduce_ex__\': <function Enum.__reduce_ex__ at 0x0000029804E17B00>, \'__deepcopy__\': <function Enum.__deepcopy__ at 0x0000029804E17BA0>, \'__copy__\': <function Enum.__copy__ at 0x0000029804E17C40>, \'name\': <enum.property object at 0x0000029804D03390>, \'value\': <enum.property object at 0x0000029804DE4A50>, \'__static_attributes__\': (), \'_new_member_\': <function Enum.__new__ at 0x0000029804E17420>, \'_use_args_\': False, \'_member_names_\': [], \'_member_map_\': {}, \'_value2member_map_\': {}, \'_hashable_values_\': [], \'_unhashable_values_\': [], \'_unhashable_values_map_\': {}, \'_member_type_\': <class \'object\'>, \'_value_repr_\': None, \'__dict__\': <attribute \'__dict__\' of \'Enum\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Enum\' objects>})'
    __firstlineno__ = 1109
    __static_attributes__ = ()


class FreqGroup(__enum.Enum):
    # no doc
    def from_period_dtype_code(self, *args, **kwargs): # real signature unknown
        pass

    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the list of values assigned
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    FR_ANN = None # (!) real value is '<FreqGroup.FR_ANN: 1000>'
    FR_BUS = None # (!) real value is '<FreqGroup.FR_BUS: 5000>'
    FR_DAY = None # (!) real value is '<FreqGroup.FR_DAY: 6000>'
    FR_HR = None # (!) real value is '<FreqGroup.FR_HR: 7000>'
    FR_MIN = None # (!) real value is '<FreqGroup.FR_MIN: 8000>'
    FR_MS = None # (!) real value is '<FreqGroup.FR_MS: 10000>'
    FR_MTH = None # (!) real value is '<FreqGroup.FR_MTH: 3000>'
    FR_NS = None # (!) real value is '<FreqGroup.FR_NS: 12000>'
    FR_QTR = None # (!) real value is '<FreqGroup.FR_QTR: 2000>'
    FR_SEC = None # (!) real value is '<FreqGroup.FR_SEC: 9000>'
    FR_UND = None # (!) real value is '<FreqGroup.FR_UND: -10000>'
    FR_US = None # (!) real value is '<FreqGroup.FR_US: 11000>'
    FR_WK = None # (!) real value is '<FreqGroup.FR_WK: 4000>'
    _hashable_values_ = [
        1000,
        2000,
        3000,
        4000,
        5000,
        6000,
        7000,
        8000,
        9000,
        10000,
        11000,
        12000,
        -10000,
    ]
    _member_map_ = {
        'FR_ANN': None, # (!) real value is '<FreqGroup.FR_ANN: 1000>'
        'FR_BUS': None, # (!) real value is '<FreqGroup.FR_BUS: 5000>'
        'FR_DAY': None, # (!) real value is '<FreqGroup.FR_DAY: 6000>'
        'FR_HR': None, # (!) real value is '<FreqGroup.FR_HR: 7000>'
        'FR_MIN': None, # (!) real value is '<FreqGroup.FR_MIN: 8000>'
        'FR_MS': None, # (!) real value is '<FreqGroup.FR_MS: 10000>'
        'FR_MTH': None, # (!) real value is '<FreqGroup.FR_MTH: 3000>'
        'FR_NS': None, # (!) real value is '<FreqGroup.FR_NS: 12000>'
        'FR_QTR': None, # (!) real value is '<FreqGroup.FR_QTR: 2000>'
        'FR_SEC': None, # (!) real value is '<FreqGroup.FR_SEC: 9000>'
        'FR_UND': None, # (!) real value is '<FreqGroup.FR_UND: -10000>'
        'FR_US': None, # (!) real value is '<FreqGroup.FR_US: 11000>'
        'FR_WK': None, # (!) real value is '<FreqGroup.FR_WK: 4000>'
    }
    _member_names_ = [
        'FR_ANN',
        'FR_QTR',
        'FR_MTH',
        'FR_WK',
        'FR_BUS',
        'FR_DAY',
        'FR_HR',
        'FR_MIN',
        'FR_SEC',
        'FR_MS',
        'FR_US',
        'FR_NS',
        'FR_UND',
    ]
    _member_type_ = object
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {
        -10000: None, # (!) real value is '<FreqGroup.FR_UND: -10000>'
        1000: None, # (!) real value is '<FreqGroup.FR_ANN: 1000>'
        2000: None, # (!) real value is '<FreqGroup.FR_QTR: 2000>'
        3000: None, # (!) real value is '<FreqGroup.FR_MTH: 3000>'
        4000: None, # (!) real value is '<FreqGroup.FR_WK: 4000>'
        5000: None, # (!) real value is '<FreqGroup.FR_BUS: 5000>'
        6000: None, # (!) real value is '<FreqGroup.FR_DAY: 6000>'
        7000: None, # (!) real value is '<FreqGroup.FR_HR: 7000>'
        8000: None, # (!) real value is '<FreqGroup.FR_MIN: 8000>'
        9000: None, # (!) real value is '<FreqGroup.FR_SEC: 9000>'
        10000: None, # (!) real value is '<FreqGroup.FR_MS: 10000>'
        11000: None, # (!) real value is '<FreqGroup.FR_US: 11000>'
        12000: None, # (!) real value is '<FreqGroup.FR_NS: 12000>'
    }
    _value_repr_ = None


class NpyDatetimeUnit(__enum.Enum):
    """ Python-space analogue to NPY_DATETIMEUNIT. """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the list of values assigned
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    NPY_FR_as = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_as: 13>'
    NPY_FR_D = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_D: 4>'
    NPY_FR_fs = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_fs: 12>'
    NPY_FR_GENERIC = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_GENERIC: 14>'
    NPY_FR_h = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_h: 5>'
    NPY_FR_M = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_M: 1>'
    NPY_FR_m = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_m: 6>'
    NPY_FR_ms = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_ms: 8>'
    NPY_FR_ns = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_ns: 10>'
    NPY_FR_ps = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_ps: 11>'
    NPY_FR_s = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_s: 7>'
    NPY_FR_us = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_us: 9>'
    NPY_FR_W = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_W: 2>'
    NPY_FR_Y = None # (!) real value is '<NpyDatetimeUnit.NPY_FR_Y: 0>'
    _hashable_values_ = [
        0,
        1,
        2,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ]
    _member_map_ = {
        'NPY_FR_D': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_D: 4>'
        'NPY_FR_GENERIC': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_GENERIC: 14>'
        'NPY_FR_M': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_M: 1>'
        'NPY_FR_W': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_W: 2>'
        'NPY_FR_Y': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_Y: 0>'
        'NPY_FR_as': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_as: 13>'
        'NPY_FR_fs': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_fs: 12>'
        'NPY_FR_h': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_h: 5>'
        'NPY_FR_m': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_m: 6>'
        'NPY_FR_ms': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_ms: 8>'
        'NPY_FR_ns': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_ns: 10>'
        'NPY_FR_ps': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_ps: 11>'
        'NPY_FR_s': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_s: 7>'
        'NPY_FR_us': None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_us: 9>'
    }
    _member_names_ = [
        'NPY_FR_Y',
        'NPY_FR_M',
        'NPY_FR_W',
        'NPY_FR_D',
        'NPY_FR_h',
        'NPY_FR_m',
        'NPY_FR_s',
        'NPY_FR_ms',
        'NPY_FR_us',
        'NPY_FR_ns',
        'NPY_FR_ps',
        'NPY_FR_fs',
        'NPY_FR_as',
        'NPY_FR_GENERIC',
    ]
    _member_type_ = object
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {
        0: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_Y: 0>'
        1: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_M: 1>'
        2: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_W: 2>'
        4: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_D: 4>'
        5: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_h: 5>'
        6: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_m: 6>'
        7: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_s: 7>'
        8: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_ms: 8>'
        9: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_us: 9>'
        10: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_ns: 10>'
        11: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_ps: 11>'
        12: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_fs: 12>'
        13: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_as: 13>'
        14: None, # (!) real value is '<NpyDatetimeUnit.NPY_FR_GENERIC: 14>'
    }
    _value_repr_ = None


class PeriodDtypeBase(object):
    """
    Similar to an actual dtype, this contains all of the information
        describing a PeriodDtype in an integer code.
    """
    def _get_to_timestamp_base(self, *args, **kwargs): # real signature unknown
        """
        Return frequency code group used for base of to_timestamp against
                frequency code.
        
                Return day freq code against longer freq than day.
                Return second freq code against hour between second.
        
                Returns
                -------
                int
        """
        pass

    def _is_tick_like(self, *args, **kwargs): # real signature unknown
        pass

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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _creso = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dtype_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _freqstr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _freq_group_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _resolution_obj = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _td64_unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000298136EAB60>'


class Resolution(__enum.Enum):
    # no doc
    @classmethod
    def from_attrname(cls, second): # real signature unknown; restored from __doc__
        """
        Return resolution str against resolution code.
        
                Examples
                --------
                >>> Resolution.from_attrname('second')
                <Resolution.RESO_SEC: 3>
        
                >>> Resolution.from_attrname('second') == Resolution.RESO_SEC
                True
        """
        pass

    @classmethod
    def get_reso_from_freqstr(cls, h): # real signature unknown; restored from __doc__
        """
        Return resolution code against frequency str.
        
                `freq` is given by the `offset.freqstr` for some DateOffset object.
        
                Examples
                --------
                >>> Resolution.get_reso_from_freqstr('h')
                <Resolution.RESO_HR: 5>
        
                >>> Resolution.get_reso_from_freqstr('h') == Resolution.RESO_HR
                True
        """
        pass

    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the list of values assigned
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    attrname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return datetime attribute name corresponding to this Resolution.

        Examples
        --------
        >>> Resolution.RESO_SEC.attrname
        'second'
        """

    attr_abbrev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    RESO_DAY = None # (!) real value is '<Resolution.RESO_DAY: 6>'
    RESO_HR = None # (!) real value is '<Resolution.RESO_HR: 5>'
    RESO_MIN = None # (!) real value is '<Resolution.RESO_MIN: 4>'
    RESO_MS = None # (!) real value is '<Resolution.RESO_MS: 2>'
    RESO_MTH = None # (!) real value is '<Resolution.RESO_MTH: 7>'
    RESO_NS = None # (!) real value is '<Resolution.RESO_NS: 0>'
    RESO_QTR = None # (!) real value is '<Resolution.RESO_QTR: 8>'
    RESO_SEC = None # (!) real value is '<Resolution.RESO_SEC: 3>'
    RESO_US = None # (!) real value is '<Resolution.RESO_US: 1>'
    RESO_YR = None # (!) real value is '<Resolution.RESO_YR: 9>'
    _hashable_values_ = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]
    _member_map_ = {
        'RESO_DAY': None, # (!) real value is '<Resolution.RESO_DAY: 6>'
        'RESO_HR': None, # (!) real value is '<Resolution.RESO_HR: 5>'
        'RESO_MIN': None, # (!) real value is '<Resolution.RESO_MIN: 4>'
        'RESO_MS': None, # (!) real value is '<Resolution.RESO_MS: 2>'
        'RESO_MTH': None, # (!) real value is '<Resolution.RESO_MTH: 7>'
        'RESO_NS': None, # (!) real value is '<Resolution.RESO_NS: 0>'
        'RESO_QTR': None, # (!) real value is '<Resolution.RESO_QTR: 8>'
        'RESO_SEC': None, # (!) real value is '<Resolution.RESO_SEC: 3>'
        'RESO_US': None, # (!) real value is '<Resolution.RESO_US: 1>'
        'RESO_YR': None, # (!) real value is '<Resolution.RESO_YR: 9>'
    }
    _member_names_ = [
        'RESO_NS',
        'RESO_US',
        'RESO_MS',
        'RESO_SEC',
        'RESO_MIN',
        'RESO_HR',
        'RESO_DAY',
        'RESO_MTH',
        'RESO_QTR',
        'RESO_YR',
    ]
    _member_type_ = object
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {
        0: None, # (!) real value is '<Resolution.RESO_NS: 0>'
        1: None, # (!) real value is '<Resolution.RESO_US: 1>'
        2: None, # (!) real value is '<Resolution.RESO_MS: 2>'
        3: None, # (!) real value is '<Resolution.RESO_SEC: 3>'
        4: None, # (!) real value is '<Resolution.RESO_MIN: 4>'
        5: None, # (!) real value is '<Resolution.RESO_HR: 5>'
        6: None, # (!) real value is '<Resolution.RESO_DAY: 6>'
        7: None, # (!) real value is '<Resolution.RESO_MTH: 7>'
        8: None, # (!) real value is '<Resolution.RESO_QTR: 8>'
        9: None, # (!) real value is '<Resolution.RESO_YR: 9>'
    }
    _value_repr_ = None


# variables with complex values

OFFSET_TO_PERIOD_FREQSTR = {
    'B': 'B',
    'BME': 'M',
    'BQE': 'Q',
    'BQE-APR': 'Q',
    'BQE-AUG': 'Q',
    'BQE-DEC': 'Q',
    'BQE-FEB': 'Q',
    'BQE-JAN': 'Q',
    'BQE-JUL': 'Q',
    'BQE-JUN': 'Q',
    'BQE-MAR': 'Q',
    'BQE-MAY': 'Q',
    'BQE-NOV': 'Q',
    'BQE-OCT': 'Q',
    'BQE-SEP': 'Q',
    'BQS': 'Q',
    'BQS-APR': 'Q',
    'BQS-AUG': 'Q',
    'BQS-DEC': 'Q',
    'BQS-FEB': 'Q',
    'BQS-JAN': 'Q',
    'BQS-JUL': 'Q',
    'BQS-JUN': 'Q',
    'BQS-MAR': 'Q',
    'BQS-MAY': 'Q',
    'BQS-NOV': 'Q',
    'BQS-OCT': 'Q',
    'BQS-SEP': 'Q',
    'BYE': 'Y',
    'BYE-APR': 'Y',
    'BYE-AUG': 'Y',
    'BYE-DEC': 'Y',
    'BYE-FEB': 'Y',
    'BYE-JAN': 'Y',
    'BYE-JUL': 'Y',
    'BYE-JUN': 'Y',
    'BYE-MAR': 'Y',
    'BYE-MAY': 'Y',
    'BYE-NOV': 'Y',
    'BYE-OCT': 'Y',
    'BYE-SEP': 'Y',
    'BYS': 'Y',
    'BYS-APR': 'Y',
    'BYS-AUG': 'Y',
    'BYS-DEC': 'Y',
    'BYS-FEB': 'Y',
    'BYS-JAN': 'Y',
    'BYS-JUL': 'Y',
    'BYS-JUN': 'Y',
    'BYS-MAR': 'Y',
    'BYS-MAY': 'Y',
    'BYS-NOV': 'Y',
    'BYS-OCT': 'Y',
    'BYS-SEP': 'Y',
    'D': 'D',
    'EOM': 'M',
    'ME': 'M',
    'MS': 'M',
    'Q-APR': 'Q-APR',
    'Q-AUG': 'Q-AUG',
    'Q-DEC': 'Q-DEC',
    'Q-FEB': 'Q-FEB',
    'Q-JAN': 'Q-JAN',
    'Q-JUL': 'Q-JUL',
    'Q-JUN': 'Q-JUN',
    'Q-MAR': 'Q-MAR',
    'Q-MAY': 'Q-MAY',
    'Q-NOV': 'Q-NOV',
    'Q-OCT': 'Q-OCT',
    'Q-SEP': 'Q-SEP',
    'QE': 'Q',
    'QE-APR': 'Q-APR',
    'QE-AUG': 'Q-AUG',
    'QE-DEC': 'Q-DEC',
    'QE-FEB': 'Q-FEB',
    'QE-JAN': 'Q-JAN',
    'QE-JUL': 'Q-JUL',
    'QE-JUN': 'Q-JUN',
    'QE-MAR': 'Q-MAR',
    'QE-MAY': 'Q-MAY',
    'QE-NOV': 'Q-NOV',
    'QE-OCT': 'Q-OCT',
    'QE-SEP': 'Q-SEP',
    'QS': 'Q',
    'QS-APR': 'Q',
    'QS-AUG': 'Q',
    'QS-DEC': 'Q',
    'QS-FEB': 'Q',
    'QS-JAN': 'Q',
    'QS-JUL': 'Q',
    'QS-JUN': 'Q',
    'QS-MAR': 'Q',
    'QS-MAY': 'Q',
    'QS-NOV': 'Q',
    'QS-OCT': 'Q',
    'QS-SEP': 'Q',
    'SME': 'M',
    'W': 'W',
    'W-FRI': 'W-FRI',
    'W-MON': 'W-MON',
    'W-SAT': 'W-SAT',
    'W-SUN': 'W-SUN',
    'W-THU': 'W-THU',
    'W-TUE': 'W-TUE',
    'W-WED': 'W-WED',
    'WEEKDAY': 'D',
    'Y': 'Y',
    'Y-APR': 'Y-APR',
    'Y-AUG': 'Y-AUG',
    'Y-DEC': 'Y-DEC',
    'Y-FEB': 'Y-FEB',
    'Y-JAN': 'Y-JAN',
    'Y-JUL': 'Y-JUL',
    'Y-JUN': 'Y-JUN',
    'Y-MAR': 'Y-MAR',
    'Y-MAY': 'Y-MAY',
    'Y-NOV': 'Y-NOV',
    'Y-OCT': 'Y-OCT',
    'Y-SEP': 'Y-SEP',
    'YE': 'Y',
    'YE-APR': 'Y-APR',
    'YE-AUG': 'Y-AUG',
    'YE-DEC': 'Y-DEC',
    'YE-FEB': 'Y-FEB',
    'YE-JAN': 'Y-JAN',
    'YE-JUL': 'Y-JUL',
    'YE-JUN': 'Y-JUN',
    'YE-MAR': 'Y-MAR',
    'YE-MAY': 'Y-MAY',
    'YE-NOV': 'Y-NOV',
    'YE-OCT': 'Y-OCT',
    'YE-SEP': 'Y-SEP',
    'YS': 'Y',
    'YS-APR': 'Y',
    'YS-AUG': 'Y',
    'YS-DEC': 'Y',
    'YS-FEB': 'Y',
    'YS-JAN': 'Y',
    'YS-JUL': 'Y',
    'YS-JUN': 'Y',
    'YS-MAR': 'Y',
    'YS-MAY': 'Y',
    'YS-NOV': 'Y',
    'YS-OCT': 'Y',
    'YS-SEP': 'Y',
    'h': 'h',
    'min': 'min',
    'ms': 'ms',
    'ns': 'ns',
    's': 's',
    'us': 'us',
}

_period_code_map = {
    'B': 5000,
    'D': 6000,
    'M': 3000,
    'Q-APR': 2004,
    'Q-AUG': 2008,
    'Q-DEC': 2000,
    'Q-FEB': 2002,
    'Q-JAN': 2001,
    'Q-JUL': 2007,
    'Q-JUN': 2006,
    'Q-MAR': 2003,
    'Q-MAY': 2005,
    'Q-NOV': 2011,
    'Q-OCT': 2010,
    'Q-SEP': 2009,
    'W-FRI': 4005,
    'W-MON': 4001,
    'W-SAT': 4006,
    'W-SUN': 4000,
    'W-THU': 4004,
    'W-TUE': 4002,
    'W-WED': 4003,
    'Y-APR': 1004,
    'Y-AUG': 1008,
    'Y-DEC': 1000,
    'Y-FEB': 1002,
    'Y-JAN': 1001,
    'Y-JUL': 1007,
    'Y-JUN': 1006,
    'Y-MAR': 1003,
    'Y-MAY': 1005,
    'Y-NOV': 1011,
    'Y-OCT': 1010,
    'Y-SEP': 1009,
    'h': 7000,
    'min': 8000,
    'ms': 10000,
    'ns': 12000,
    's': 9000,
    'us': 11000,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002981365B540>'

__pyx_capi__ = {
    'abbrev_to_npy_unit': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (PyObject *, int __pyx_skip_dispatch)" at 0x00000298136E9170>'
    'attrname_to_abbrevs': None, # (!) real value is '<capsule object "PyObject *" at 0x00000298136E9030>'
    'attrname_to_npy_unit': None, # (!) real value is '<capsule object "PyObject *" at 0x00000298136E90D0>'
    'c_DEPR_ABBREVS': None, # (!) real value is '<capsule object "PyObject *" at 0x00000298136E8FE0>'
    'c_OFFSET_DEPR_FREQSTR': None, # (!) real value is '<capsule object "PyObject *" at 0x00000298136E8F40>'
    'c_OFFSET_TO_PERIOD_FREQSTR': None, # (!) real value is '<capsule object "PyObject *" at 0x00000298136E8EF0>'
    'c_REVERSE_OFFSET_DEPR_FREQSTR': None, # (!) real value is '<capsule object "PyObject *" at 0x00000298136E8F90>'
    'freq_group_code_to_npy_unit': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (int)" at 0x00000298136E91C0>'
    'freq_to_period_freqstr': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x00000298136EA7A0>'
    'get_supported_reso': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (NPY_DATETIMEUNIT)" at 0x00000298136E9300>'
    'is_supported_unit': None, # (!) real value is '<capsule object "int (NPY_DATETIMEUNIT)" at 0x00000298136E9350>'
    'npy_unit_to_abbrev': None, # (!) real value is '<capsule object "PyObject *(NPY_DATETIMEUNIT)" at 0x00000298136E9120>'
    'npy_unit_to_attrname': None, # (!) real value is '<capsule object "PyObject *" at 0x00000298136E9080>'
    'periods_per_day': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_6dtypes_periods_per_day *__pyx_optional_args)" at 0x00000298136E9260>'
    'periods_per_second': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (NPY_DATETIMEUNIT, int __pyx_skip_dispatch)" at 0x00000298136E92B0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.dtypes', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002981365B540>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\dtypes.cp313-win_amd64.pyd')"

__test__ = {
    'Resolution.attrname (line 462)': "\n        Return datetime attribute name corresponding to this Resolution.\n\n        Examples\n        --------\n        >>> Resolution.RESO_SEC.attrname\n        'second'\n        ",
    'Resolution.from_attrname (line 474)': "\n        Return resolution str against resolution code.\n\n        Examples\n        --------\n        >>> Resolution.from_attrname('second')\n        <Resolution.RESO_SEC: 3>\n\n        >>> Resolution.from_attrname('second') == Resolution.RESO_SEC\n        True\n        ",
    'Resolution.get_reso_from_freqstr (line 489)': "\n        Return resolution code against frequency str.\n\n        `freq` is given by the `offset.freqstr` for some DateOffset object.\n\n        Examples\n        --------\n        >>> Resolution.get_reso_from_freqstr('h')\n        <Resolution.RESO_HR: 5>\n\n        >>> Resolution.get_reso_from_freqstr('h') == Resolution.RESO_HR\n        True\n        ",
}

