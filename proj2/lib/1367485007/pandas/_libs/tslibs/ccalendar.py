# encoding: utf-8
# module pandas._libs.tslibs.ccalendar
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\tslibs\ccalendar.cp313-win_amd64.pyd
# by generator 1.147
""" Cython implementations of functions resembling the stdlib calendar module """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def get_days_in_month(*args, **kwargs): # real signature unknown
    """
    Return the number of days in the given month of the given year.
    
        Parameters
        ----------
        year : int
        month : int
    
        Returns
        -------
        days_in_month : int
    
        Notes
        -----
        Assumes that the arguments are valid.  Passing a month not between 1 and 12
        risks a segfault.
    """
    pass

def get_day_of_year(*args, **kwargs): # real signature unknown
    """
    Return the ordinal day-of-year for the given day.
    
        Parameters
        ----------
        year : int
        month : int
        day : int
    
        Returns
        -------
        day_of_year : int32_t
    
        Notes
        -----
        Assumes the inputs describe a valid date.
    """
    pass

def get_firstbday(*args, **kwargs): # real signature unknown
    """
    Find the first day of the month that is a business day.
    
        Parameters
        ----------
        year : int
        month : int
    
        Returns
        -------
        first_bday : int
    """
    pass

def get_iso_calendar(*args, **kwargs): # real signature unknown
    """
    Return the year, week, and day of year corresponding to ISO 8601
    
        Parameters
        ----------
        year : int
        month : int
        day : int
    
        Returns
        -------
        year : int32_t
        week : int32_t
        day : int32_t
    
        Notes
        -----
        Assumes the inputs describe a valid date.
    """
    pass

def get_lastbday(*args, **kwargs): # real signature unknown
    """
    Find the last day of the month that is a business day.
    
        Parameters
        ----------
        year : int
        month : int
    
        Returns
        -------
        last_bday : int
    """
    pass

def get_week_of_year(*args, **kwargs): # real signature unknown
    """
    Return the ordinal week-of-year for the given day.
    
        Parameters
        ----------
        year : int
        month : int
        day : int
    
        Returns
        -------
        week_of_year : int32_t
    
        Notes
        -----
        Assumes the inputs describe a valid date.
    """
    pass

# no classes
# variables with complex values

DAYS = [
    'MON',
    'TUE',
    'WED',
    'THU',
    'FRI',
    'SAT',
    'SUN',
]

DAYS_FULL = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

int_to_weekday = {
    0: 'MON',
    1: 'TUE',
    2: 'WED',
    3: 'THU',
    4: 'FRI',
    5: 'SAT',
    6: 'SUN',
}

MONTHS = [
    'JAN',
    'FEB',
    'MAR',
    'APR',
    'MAY',
    'JUN',
    'JUL',
    'AUG',
    'SEP',
    'OCT',
    'NOV',
    'DEC',
]

MONTHS_FULL = [
    '',
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

MONTH_ALIASES = {
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUN',
    7: 'JUL',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC',
}

MONTH_NUMBERS = {
    'APR': 3,
    'AUG': 7,
    'DEC': 11,
    'FEB': 1,
    'JAN': 0,
    'JUL': 6,
    'JUN': 5,
    'MAR': 2,
    'MAY': 4,
    'NOV': 10,
    'OCT': 9,
    'SEP': 8,
}

weekday_to_int = {
    'FRI': 4,
    'MON': 0,
    'SAT': 5,
    'SUN': 6,
    'THU': 3,
    'TUE': 1,
    'WED': 2,
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CA775DB620>'

__pyx_capi__ = {
    'MONTH_TO_CAL_NUM': None, # (!) real value is '<capsule object "PyObject *" at 0x000001CA77666D90>'
    'c_MONTH_NUMBERS': None, # (!) real value is '<capsule object "PyObject *" at 0x000001CA77666D40>'
    'dayofweek': None, # (!) real value is '<capsule object "int (int, int, int)" at 0x000001CA77666E30>'
    'get_day_of_year': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int32_t (int, int, int, int __pyx_skip_dispatch)" at 0x000001CA77666FC0>'
    'get_days_in_month': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int32_t (int, Py_ssize_t, int __pyx_skip_dispatch)" at 0x000001CA77666ED0>'
    'get_firstbday': None, # (!) real value is '<capsule object "int (int, int, int __pyx_skip_dispatch)" at 0x000001CA77667060>'
    'get_iso_calendar': None, # (!) real value is '<capsule object "__pyx_t_6pandas_5_libs_6tslibs_9ccalendar_iso_calendar_t (int, int, int, int __pyx_skip_dispatch)" at 0x000001CA77666F70>'
    'get_lastbday': None, # (!) real value is '<capsule object "int (int, int, int __pyx_skip_dispatch)" at 0x000001CA77667010>'
    'get_week_of_year': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int32_t (int, int, int, int __pyx_skip_dispatch)" at 0x000001CA77666F20>'
    'is_leapyear': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_int64_t)" at 0x000001CA77666E80>'
    'month_offset': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int32_t *" at 0x000001CA77666DE0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.ccalendar', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CA775DB620>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\ccalendar.cp313-win_amd64.pyd')"

__test__ = {}

