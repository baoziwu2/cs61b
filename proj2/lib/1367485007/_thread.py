# encoding: utf-8
# module _thread
# from (built-in)
# by generator 1.147
"""
This module provides primitive operations to write multi-threaded programs.
The 'threading' module provides a more convenient interface.
"""
# no imports

# Variables with simple values

TIMEOUT_MAX = 4294967.0

# functions

def allocate(*args, **kwargs): # real signature unknown
    """ An obsolete synonym of allocate_lock(). """
    pass

def allocate_lock(*args, **kwargs): # real signature unknown
    """
    Create a new lock object. See help(type(threading.Lock())) for
    information about locks.
    """
    pass

def daemon_threads_allowed(*args, **kwargs): # real signature unknown
    """
    Return True if daemon threads are allowed in the current interpreter,
    and False otherwise.
    """
    pass

def exit(*args, **kwargs): # real signature unknown
    """
    This is synonymous to ``raise SystemExit''.  It will cause the current
    thread to exit silently unless the exception is caught.
    """
    pass

def exit_thread(*args, **kwargs): # real signature unknown
    """ An obsolete synonym of exit(). """
    pass

def get_ident(*args, **kwargs): # real signature unknown
    """
    Return a non-zero integer that uniquely identifies the current thread
    amongst other threads that exist simultaneously.
    This may be used to identify per-thread resources.
    Even though on some platforms threads identities may appear to be
    allocated consecutive numbers starting at 1, this behavior should not
    be relied upon, and the number should be seen purely as a magic cookie.
    A thread's identity may be reused for another thread after it exits.
    """
    pass

def get_native_id(*args, **kwargs): # real signature unknown
    """
    Return a non-negative integer identifying the thread as reported
    by the OS (kernel). This may be used to uniquely identify a
    particular thread within a system.
    """
    pass

def interrupt_main(*args, **kwargs): # real signature unknown
    """
    Simulate the arrival of the given signal in the main thread,
    where the corresponding signal handler will be executed.
    If *signum* is omitted, SIGINT is assumed.
    A subthread can use this function to interrupt the main thread.
    
    Note: the default signal handler for SIGINT raises ``KeyboardInterrupt``.
    """
    pass

def stack_size(*args, **kwargs): # real signature unknown
    """
    Return the thread stack size used when creating new threads.  The
    optional size argument specifies the stack size (in bytes) to be used
    for subsequently created threads, and must be 0 (use platform or
    configured default) or a positive integer value of at least 32,768 (32k).
    If changing the thread stack size is unsupported, a ThreadError
    exception is raised.  If the specified size is invalid, a ValueError
    exception is raised, and the stack size is unmodified.  32k bytes
     currently the minimum supported stack size value to guarantee
    sufficient stack space for the interpreter itself.
    
    Note that some platforms may have particular restrictions on values for
    the stack size, such as requiring a minimum stack size larger than 32 KiB or
    requiring allocation in multiples of the system memory page size
    - platform documentation should be referred to for more information
    (4 KiB pages are common; using multiples of 4096 for the stack size is
    the suggested approach in the absence of more specific information).
    """
    pass

def start_joinable_thread(*args, **kwargs): # real signature unknown
    """
    *For internal use only*: start a new thread.
    
    Like start_new_thread(), this starts a new thread calling the given function.
    Unlike start_new_thread(), this returns a handle object with methods to join
    or detach the given thread.
    This function is not for third-party code, please use the
    `threading` module instead. During finalization the runtime will not wait for
    the thread to exit if daemon is True. If handle is provided it must be a
    newly created thread._ThreadHandle instance.
    """
    pass

def start_new(function, args, kwargs=None): # known case of _thread.start_new
    """ An obsolete synonym of start_new_thread(). """
    return 0

def start_new_thread(*args, **kwargs): # real signature unknown
    """
    Start a new thread and return its identifier.
    
    The thread will call the function with positional arguments from the
    tuple args and keyword arguments taken from the optional dictionary
    kwargs.  The thread exits when the function returns; the return value
    is ignored.  The thread will also exit when the function raises an
    unhandled exception; a stack trace will be printed unless the exception
    is SystemExit.
    """
    pass

def _count(*args, **kwargs): # real signature unknown
    """
    Return the number of currently running Python threads, excluding
    the main thread. The returned number comprises all threads created
    through `start_new_thread()` as well as `threading.Thread`, and not
    yet finished.
    
    This function is meant for internal and specialized purposes only.
    In most applications `threading.enumerate()` should be used instead.
    """
    pass

def _excepthook(*args, **kwargs): # real signature unknown
    """ Handle uncaught Thread.run() exception. """
    pass

def _get_main_thread_ident(*args, **kwargs): # real signature unknown
    """
    Internal only. Return a non-zero integer that uniquely identifies the main thread
    of the main interpreter.
    """
    pass

def _is_main_interpreter(*args, **kwargs): # real signature unknown
    """ Return True if the current interpreter is the main Python interpreter. """
    pass

def _make_thread_handle(*args, **kwargs): # real signature unknown
    """
    Internal only. Make a thread handle for threads not spawned
    by the _thread or threading module.
    """
    pass

def _shutdown(*args, **kwargs): # real signature unknown
    """ Wait for all non-daemon threads (other than the calling thread) to stop. """
    pass

# classes

class error(Exception):
    """ Unspecified run-time error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class LockType(object):
    """
    A lock object is a synchronization primitive.  To create a lock,
    call threading.Lock().  Methods are:
    
    acquire() -- lock the lock, possibly blocking until it can be obtained
    release() -- unlock of the lock
    locked() -- test whether the lock is currently locked
    
    A lock is not owned by the thread that locked it; another thread may
    unlock it.  A thread attempting to lock a lock that it has already locked
    will block until another thread unlocks it.  Deadlocks may ensue.
    """
    def acquire(self, *args, **kwargs): # real signature unknown
        """
        Lock the lock.  Without argument, this blocks if the lock is already
        locked (even by the same thread), waiting for another thread to release
        the lock, and return True once the lock is acquired.
        With an argument, this will only block if the argument is true,
        and the return value reflects whether the lock is acquired.
        The blocking operation is interruptible.
        """
        pass

    def acquire_lock(self, *args, **kwargs): # real signature unknown
        """ An obsolete synonym of acquire(). """
        pass

    def locked(self, *args, **kwargs): # real signature unknown
        """ Return whether the lock is in the locked state. """
        pass

    def locked_lock(self, *args, **kwargs): # real signature unknown
        """ An obsolete synonym of locked(). """
        pass

    def release(self, *args, **kwargs): # real signature unknown
        """
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        but it needn't be locked by the same thread that unlocks it.
        """
        pass

    def release_lock(self, *args, **kwargs): # real signature unknown
        """ An obsolete synonym of release(). """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ Lock the lock. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ Release the lock. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


lock = LockType


class RLock(object):
    # no doc
    def acquire(self, *args, **kwargs): # real signature unknown
        """
        Lock the lock.  `blocking` indicates whether we should wait
        for the lock to be available or not.  If `blocking` is False
        and another thread holds the lock, the method will return False
        immediately.  If `blocking` is True and another thread holds
        the lock, the method will wait for the lock to be released,
        take it and then return True.
        (note: the blocking operation is interruptible.)
        
        In all other cases, the method will return True immediately.
        Precisely, if the current thread already holds the lock, its
        internal counter is simply incremented. If nobody holds the lock,
        the lock is taken and its internal counter initialized to 1.
        """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        and must be locked by the same thread that unlocks it; otherwise a
        `RuntimeError` is raised.
        
        Do note that if the lock was acquire()d several times in a row by the
        current thread, release() needs to be called as many times for the lock
        to be available for other threads.
        """
        pass

    def _acquire_restore(self, *args, **kwargs): # real signature unknown
        """ For internal use by `threading.Condition`. """
        pass

    def _is_owned(self, *args, **kwargs): # real signature unknown
        """ For internal use by `threading.Condition`. """
        pass

    def _recursion_count(self, *args, **kwargs): # real signature unknown
        """ For internal use by reentrancy checks. """
        pass

    def _release_save(self, *args, **kwargs): # real signature unknown
        """ For internal use by `threading.Condition`. """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ Lock the lock. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ Release the lock. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class _ExceptHookArgs(tuple):
    """
    ExceptHookArgs
    
    Type used to pass arguments to threading.excepthook.
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

    exc_traceback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Exception traceback"""

    exc_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Exception type"""

    exc_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Exception value"""

    thread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Thread"""


    n_fields = 4
    n_sequence_fields = 4
    n_unnamed_fields = 0
    __match_args__ = (
        'exc_type',
        'exc_value',
        'exc_traceback',
        'thread',
    )


class _local(object):
    """ Thread-local data """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class _ThreadHandle(object):
    # no doc
    def is_done(self, *args, **kwargs): # real signature unknown
        pass

    def join(self, *args, **kwargs): # real signature unknown
        pass

    def _set_done(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    ident = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 971, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000002C2BCDA3380>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000002C2BCDA3420>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000002C2BCDA34C0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000002C2BCDA3600>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000002C2BCDA3740>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000002C2BCDA3880>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000002C2BCDA2700>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 971
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_thread', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

