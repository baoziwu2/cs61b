# encoding: utf-8
# module zmq.backend.cython._zmq
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\zmq\backend\cython\_zmq.pyd
# by generator 1.147
""" Cython backend for pyzmq """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\warnings.py
import zmq as zmq # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\zmq\__init__.py
from time import monotonic

import enum as __enum
import zmq.error as __zmq_error


# Variables with simple values

IPC_PATH_MAX_LEN = 0

PYZMQ_DRAFT_API = False

_gc = None

# functions

def curve_keypair(*args, **kwargs): # real signature unknown
    """
    generate a Z85 key pair for use with zmq.CURVE security
    
        Requires libzmq (≥ 4.0) to have been built with CURVE support.
    
        .. versionadded:: libzmq-4.0
        .. versionadded:: 14.0
    
        Returns
        -------
        public: bytes
            The public key as 40 byte z85-encoded bytestring.
        private: bytes
            The private key as 40 byte z85-encoded bytestring.
    """
    pass

def curve_public(*args, **kwargs): # real signature unknown
    """
    Compute the public key corresponding to a secret key for use
        with zmq.CURVE security
    
        Requires libzmq (≥ 4.2) to have been built with CURVE support.
    
        Parameters
        ----------
        private
            The private key as a 40 byte z85-encoded bytestring
    
        Returns
        -------
        bytes
            The public key as a 40 byte z85-encoded bytestring
    """
    pass

def has(*args, **kwargs): # real signature unknown
    """
    Check for zmq capability by name (e.g. 'ipc', 'curve')
    
        .. versionadded:: libzmq-4.1
        .. versionadded:: 14.1
    """
    pass

def monitored_queue(*args, **kwargs): # real signature unknown
    """
    Start a monitored queue device.
    
        A monitored queue is very similar to the zmq.proxy device (monitored queue came first).
    
        Differences from zmq.proxy:
    
        - monitored_queue supports both in and out being ROUTER sockets
          (via swapping IDENTITY prefixes).
        - monitor messages are prefixed, making in and out messages distinguishable.
    
        Parameters
        ----------
        in_socket : zmq.Socket
            One of the sockets to the Queue. Its messages will be prefixed with
            'in'.
        out_socket : zmq.Socket
            One of the sockets to the Queue. Its messages will be prefixed with
            'out'. The only difference between in/out socket is this prefix.
        mon_socket : zmq.Socket
            This socket sends out every message received by each of the others
            with an in/out prefix specifying which one it was.
        in_prefix : str
            Prefix added to broadcast messages from in_socket.
        out_prefix : str
            Prefix added to broadcast messages from out_socket.
    """
    pass

def proxy(replacement_for_device): # real signature unknown; restored from __doc__
    """
    Start a zeromq proxy (replacement for device).
    
        .. versionadded:: libzmq-3.2
        .. versionadded:: 13.0
    
        Parameters
        ----------
        frontend : Socket
            The Socket instance for the incoming traffic.
        backend : Socket
            The Socket instance for the outbound traffic.
        capture : Socket (optional)
            The Socket instance for capturing traffic.
    """
    pass

def proxy_steerable(*args, **kwargs): # real signature unknown
    """
    Start a zeromq proxy with control flow.
    
        .. versionadded:: libzmq-4.1
        .. versionadded:: 18.0
    
        Parameters
        ----------
        frontend : Socket
            The Socket instance for the incoming traffic.
        backend : Socket
            The Socket instance for the outbound traffic.
        capture : Socket (optional)
            The Socket instance for capturing traffic.
        control : Socket (optional)
            The Socket instance for control flow.
    """
    pass

def strerror(*args, **kwargs): # real signature unknown
    """ Return the error string given the error number. """
    pass

def zmq_errno(*args, **kwargs): # real signature unknown
    """ Return the integer errno of the most recent zmq error. """
    pass

def zmq_poll(sockets, timeout=-1): # real signature unknown; restored from __doc__
    """
    zmq_poll(sockets, timeout=-1)
    
        Poll a set of 0MQ sockets, native file descs. or sockets.
    
        Parameters
        ----------
        sockets : list of tuples of (socket, flags)
            Each element of this list is a two-tuple containing a socket
            and a flags. The socket may be a 0MQ socket or any object with
            a ``fileno()`` method. The flags can be zmq.POLLIN (for detecting
            for incoming messages), zmq.POLLOUT (for detecting that send is OK)
            or zmq.POLLIN|zmq.POLLOUT for detecting both.
        timeout : int
            The number of milliseconds to poll for. Negative means no timeout.
    """
    pass

def zmq_version_info(*args, **kwargs): # real signature unknown
    """ Return the version of ZeroMQ itself as a 3-tuple of ints. """
    pass

def _check_version(min_version_info, msg=None): # reliably restored by inspect
    """
    Check for libzmq
    
    raises ZMQVersionError if current zmq version is not at least min_version
    
    min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().
    """
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class ZMQError(__zmq_error.ZMQBaseError):
    """
    Wrap an errno style error.
    
    Parameters
    ----------
    errno : int
        The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
        used.
    msg : str
        Description of the error or None.
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        """
        Wrap an errno style error.
        
        Parameters
        ----------
        errno : int
            The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
            used.
        msg : string
            Description of the error or None.
        """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    errno = None
    __annotations__ = {
        'errno': 'int | None',
        'strerror': 'str',
    }
    __firstlineno__ = 30
    __static_attributes__ = (
        'errno',
        'strerror',
    )


class Again(__zmq_error.ZMQError):
    """
    Wrapper for zmq.EAGAIN
    
    .. versionadded:: 13.0
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        # no doc
        pass

    __firstlineno__ = 114
    __static_attributes__ = ()


class Context(object):
    """
    Manage the lifecycle of a 0MQ context.
    
        Parameters
        ----------
        io_threads : int
            The number of IO threads.
    """
    def get(self, *args, **kwargs): # real signature unknown
        """
        Get the value of a context option.
        
                See the 0MQ API documentation for zmq_ctx_get
                for details on specific options.
        
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                option : int
                    The option to get.  Available values will depend on your
                    version of libzmq.  Examples include::
        
                        zmq.IO_THREADS, zmq.MAX_SOCKETS
        
                Returns
                -------
                optval : int
                    The value of the option as an integer.
        """
        pass

    def set(self, *args, **kwargs): # real signature unknown
        """
        Set a context option.
        
                See the 0MQ API documentation for zmq_ctx_set
                for details on specific options.
        
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                option : int
                    The option to set.  Available values will depend on your
                    version of libzmq.  Examples include::
        
                        zmq.IO_THREADS, zmq.MAX_SOCKETS
        
                optval : int
                    The value of the option to set.
        """
        pass

    def term(self, *args, **kwargs): # real signature unknown
        """
        Close or terminate the context.
        
                This can be called to close the context by hand. If this is not called,
                the context will automatically be closed when it is garbage collected.
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

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the underlying libzmq context"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000228B3200630>'


class ContextTerminated(__zmq_error.ZMQError):
    """
    Wrapper for zmq.ETERM
    
    .. versionadded:: 13.0
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        # no doc
        pass

    __firstlineno__ = 102
    __static_attributes__ = ()


class Event(object):
    """
    Class implementing event objects.
    
    Events manage a flag that can be set to true with the set() method and reset
    to false with the clear() method. The wait() method blocks until the flag is
    true.  The flag is initially false.
    """
    def clear(self): # reliably restored by inspect
        """
        Reset the internal flag to false.
        
        Subsequently, threads calling wait() will block until set() is called to
        set the internal flag to true again.
        """
        pass

    def isSet(self): # reliably restored by inspect
        """
        Return true if and only if the internal flag is true.
        
        This method is deprecated, use is_set() instead.
        """
        pass

    def is_set(self): # reliably restored by inspect
        """ Return true if and only if the internal flag is true. """
        pass

    def set(self): # reliably restored by inspect
        """
        Set the internal flag to true.
        
        All threads waiting for it to become true are awakened. Threads
        that call wait() once the flag is true will not block at all.
        """
        pass

    def wait(self, timeout=None): # reliably restored by inspect
        """
        Block until the internal flag is true.
        
        If the internal flag is true on entry, return immediately. Otherwise,
        block until another thread calls set() to set the flag to true, or until
        the optional timeout occurs.
        
        When the timeout argument is present and not None, it should be a
        floating-point number specifying a timeout for the operation in seconds
        (or fractions thereof).
        
        This method returns the internal flag on exit, so it will always return
        True except if a timeout is given and the operation times out.
        """
        pass

    def _at_fork_reinit(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'threading', '__firstlineno__': 581, '__doc__': 'Class implementing event objects.\\n\\nEvents manage a flag that can be set to true with the set() method and reset\\nto false with the clear() method. The wait() method blocks until the flag is\\ntrue.  The flag is initially false.\\n\\n', '__init__': <function Event.__init__ at 0x00000228B2D9D8A0>, '__repr__': <function Event.__repr__ at 0x00000228B2D9D940>, '_at_fork_reinit': <function Event._at_fork_reinit at 0x00000228B2D9D9E0>, 'is_set': <function Event.is_set at 0x00000228B2D9DA80>, 'isSet': <function Event.isSet at 0x00000228B2D9DB20>, 'set': <function Event.set at 0x00000228B2D9DBC0>, 'clear': <function Event.clear at 0x00000228B2D9DC60>, 'wait': <function Event.wait at 0x00000228B2D9DD00>, '__static_attributes__': ('_cond', '_flag'), '__dict__': <attribute '__dict__' of 'Event' objects>, '__weakref__': <attribute '__weakref__' of 'Event' objects>})"
    __firstlineno__ = 581
    __static_attributes__ = (
        '_cond',
        '_flag',
    )


class Frame(object):
    # no doc
    def get(self, *args, **kwargs): # real signature unknown
        """
        Get a Frame option or property.
        
                See the 0MQ API documentation for zmq_msg_get and zmq_msg_gets
                for details on specific options.
        
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                .. versionchanged:: 14.3
                    add support for zmq_msg_gets (requires libzmq-4.1)
                    All message properties are strings.
        
                .. versionchanged:: 17.0
                    Added support for `routing_id` and `group`.
                    Only available if draft API is enabled
                    with libzmq >= 4.2.
        """
        pass

    def set(self, *args, **kwargs): # real signature unknown
        """
        Set a Frame option.
        
                See the 0MQ API documentation for zmq_msg_set
                for details on specific options.
        
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
                .. versionchanged:: 17.0
                    Added support for `routing_id` and `group`.
                    Only available if draft API is enabled
                    with libzmq >= 4.2.
        """
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A memoryview of the message contents."""

    bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The message content as a Python bytes object.

        The first time this property is accessed, a copy of the message
        contents is made. From then on that same copy of the message is
        returned.
        """

    more = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tracker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tracker_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000228B3200A40>'


class InterruptedSystemCall(__zmq_error.ZMQError, InterruptedError):
    """
    Wrapper for EINTR
    
    This exception should be caught internally in pyzmq
    to retry system calls, and not propagate to the user.
    
    .. versionadded:: 14.7
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    errno = 4
    __annotations__ = {
        'strerror': 'str',
    }
    __firstlineno__ = 126
    __static_attributes__ = ()


class MessageTracker(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ref(object):
    # no doc
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __callback__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Socket(object):
    """
    A 0MQ socket.
    
        These objects will generally be constructed via the socket() method of a Context object.
    
        Note: 0MQ Sockets are *not* threadsafe. **DO NOT** share them across threads.
    
        Parameters
        ----------
        context : Context
            The 0MQ Context this Socket belongs to.
        socket_type : int
            The socket type, which can be any of the 0MQ socket types:
            REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, XPUB, XSUB.
    
        See Also
        --------
        .Context.socket : method for creating a socket bound to a Context.
    """
    def bind(self, *args, **kwargs): # real signature unknown
        """
        Bind the socket to an address.
        
                This causes the socket to listen on a network port. Sockets on the
                other side of this connection will use ``Socket.connect(addr)`` to
                connect to this socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported include
                    tcp, udp, pgm, epgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """
        Close the socket.
        
                If linger is specified, LINGER sockopt will be set prior to closing.
        
                This can be called to close the socket by hand. If this is not
                called, the socket will automatically be closed when it is
                garbage collected.
        """
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        """
        Connect to a remote 0MQ socket.
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def disconnect(self, *args, **kwargs): # real signature unknown
        """
        Disconnect from a remote 0MQ socket (undoes a call to connect).
        
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
        """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """
        Get the value of a socket option.
        
                See the 0MQ API documentation for details on specific options.
        
                .. versionchanged:: 27
                    Added experimental support for ZMQ_FD for draft sockets via `zmq_poller_fd`.
                    Requires libzmq >=4.3.2 built with draft support.
        
                Parameters
                ----------
                option : int
                    The option to get.  Available values will depend on your
                    version of libzmq.  Examples include::
        
                        zmq.IDENTITY, HWM, LINGER, FD, EVENTS
        
                Returns
                -------
                optval : int or bytes
                    The value of the option as a bytestring or int.
        """
        pass

    def join(self, *args, **kwargs): # real signature unknown
        """
        Join a RADIO-DISH group
        
                Only for DISH sockets.
        
                libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API
        
                .. versionadded:: 17
        """
        pass

    def leave(self, *args, **kwargs): # real signature unknown
        """
        Leave a RADIO-DISH group
        
                Only for DISH sockets.
        
                libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API
        
                .. versionadded:: 17
        """
        pass

    def monitor(self, *args, **kwargs): # real signature unknown
        """
        Start publishing socket events on inproc.
                See libzmq docs for zmq_monitor for details.
        
                While this function is available from libzmq 3.2,
                pyzmq cannot parse monitor messages from libzmq prior to 4.0.
        
                .. versionadded: libzmq-3.2
                .. versionadded: 14.0
        
                Parameters
                ----------
                addr : str | None
                    The inproc url used for monitoring. Passing None as
                    the addr will cause an existing socket monitor to be
                    deregistered.
                events : int
                    default: zmq.EVENT_ALL
                    The zmq event bitmask for which events will be sent to the monitor.
        """
        pass

    def recv(self, *args, **kwargs): # real signature unknown
        """
        Receive a message.
        
                With flags=NOBLOCK, this raises :class:`ZMQError` if no messages have
                arrived; otherwise, this waits until a message arrives.
                See :class:`Poller` for more general non-blocking I/O.
        
                Parameters
                ----------
                flags : int
                    0 or NOBLOCK.
                copy : bool
                    Should the message be received in a copying or non-copying manner?
                    If False a Frame object is returned, if True a string copy of
                    message is returned.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                msg : bytes or Frame
                    The received message frame.  If `copy` is False, then it will be a Frame,
                    otherwise it will be bytes.
        
                Raises
                ------
                ZMQError
                    for any of the reasons zmq_msg_recv might fail (including if
                    NOBLOCK is set and no new messages have arrived).
        """
        pass

    def recv_into(self, bytearray, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Receive up to nbytes bytes from the socket,
                storing the data into a buffer rather than allocating a new Frame.
        
                The next message frame can be discarded by receiving into an empty buffer::
        
                    sock.recv_into(bytearray())
        
                .. versionadded:: 26.4
        
                Parameters
                ----------
                buffer : memoryview
                    Any object providing the buffer interface (i.e. `memoryview(buffer)` works),
                    where the memoryview is contiguous and writable.
                nbytes: int, default=0
                    The maximum number of bytes to receive.
                    If nbytes is not specified (or 0), receive up to the size available in the given buffer.
                    If the next frame is larger than this, the frame will be truncated and message content discarded.
                flags: int, default=0
                    See `socket.recv`
        
                Returns
                -------
                bytes_received: int
                    Returns the number of bytes received.
                    This is always the size of the received frame.
                    If the returned `bytes_received` is larger than `nbytes` (or size of `buffer` if `nbytes=0`),
                    the message has been truncated and the rest of the frame discarded.
                    Truncated data cannot be recovered.
        
                Raises
                ------
                ZMQError
                    for any of the reasons `zmq_recv` might fail.
                BufferError
                    for invalid buffers, such as readonly or not contiguous.
        """
        pass

    def send(self, *args, **kwargs): # real signature unknown
        """
        Send a single zmq message frame on this socket.
        
                This queues the message to be sent by the IO thread at a later time.
        
                With flags=NOBLOCK, this raises :class:`ZMQError` if the queue is full;
                otherwise, this waits until space is available.
                See :class:`Poller` for more general non-blocking I/O.
        
                Parameters
                ----------
                data : bytes, Frame, memoryview
                    The content of the message. This can be any object that provides
                    the Python buffer API (`memoryview(data)` can be called).
                flags : int
                    0, NOBLOCK, SNDMORE, or NOBLOCK|SNDMORE.
                copy : bool
                    Should the message be sent in a copying or non-copying manner.
                track : bool
                    Should the message be tracked for notification that ZMQ has
                    finished with it? (ignored if copy=True)
        
                Returns
                -------
                None : if `copy` or not track
                    None if message was sent, raises an exception otherwise.
                MessageTracker : if track and not copy
                    a MessageTracker object, whose `done` property will
                    be False until the send is completed.
        
                Raises
                ------
                TypeError
                    If a unicode object is passed
                ValueError
                    If `track=True`, but an untracked Frame is passed.
                ZMQError
                    for any of the reasons zmq_msg_send might fail (including
                    if NOBLOCK is set and the outgoing queue is full).
        """
        pass

    def set(self, *args, **kwargs): # real signature unknown
        """
        Set socket options.
        
                See the 0MQ API documentation for details on specific options.
        
                Parameters
                ----------
                option : int
                    The option to set.  Available values will depend on your
                    version of libzmq.  Examples include::
        
                        zmq.SUBSCRIBE, UNSUBSCRIBE, IDENTITY, HWM, LINGER, FD
        
                optval : int or bytes
                    The value of the option to set.
        
                Notes
                -----
                .. warning::
        
                    All options other than zmq.SUBSCRIBE, zmq.UNSUBSCRIBE and
                    zmq.LINGER only take effect for subsequent socket bind/connects.
        """
        pass

    def unbind(self, *args, **kwargs): # real signature unknown
        """
        Unbind from an address (undoes a call to bind).
        
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                addr : str
                    The address string. This has the form 'protocol://interface:port',
                    for example 'tcp://127.0.0.1:5555'. Protocols supported are
                    tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
                    encoded to utf-8 first.
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

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the socket is closed"""

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the underlying libzmq socket"""

    _closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000228B3200F40>'


class SocketOption(__enum.IntEnum):
    """
    Options for Socket.get/set
    
    .. versionadded:: 23
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the list of values assigned
        """
        pass

    def _new_member_(cls, value, opt_type="<_OptType.int: 'int'>"): # reliably restored by inspect
        """ Attach option type as `._opt_type` """
        pass

    def _value_repr_(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Convert to a string according to format_spec. """
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    def __new_member__(cls, value, opt_type="<_OptType.int: 'int'>"): # reliably restored by inspect
        """ Attach option type as `._opt_type` """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    AFFINITY = 4
    BACKLOG = 19
    BINDTODEVICE = 92
    BLOCKY = 70
    BUSY_POLL = 113
    CONFLATE = 54
    CONNECT_RID = 61
    CONNECT_ROUTING_ID = 61
    CONNECT_TIMEOUT = 79
    CURVE_PUBLICKEY = 48
    CURVE_SECRETKEY = 49
    CURVE_SERVER = 47
    CURVE_SERVERKEY = 50
    DELAY_ATTACH_ON_CONNECT = 39
    DISCONNECT_MSG = 111
    EVENTS = 15
    FAIL_UNROUTABLE = 33
    FD = 14
    GSSAPI_PLAINTEXT = 65
    GSSAPI_PRINCIPAL = 63
    GSSAPI_PRINCIPAL_NAMETYPE = 90
    GSSAPI_SERVER = 62
    GSSAPI_SERVICE_PRINCIPAL = 64
    GSSAPI_SERVICE_PRINCIPAL_NAMETYPE = 91
    HANDSHAKE_IVL = 66
    HEARTBEAT_IVL = 75
    HEARTBEAT_TIMEOUT = 77
    HEARTBEAT_TTL = 76
    HELLO_MSG = 110
    HICCUP_MSG = 114
    HWM = 1
    IDENTITY = 5
    IMMEDIATE = 39
    INVERT_MATCHING = 74
    IN_BATCH_SIZE = 101
    IPC_FILTER_GID = 60
    IPC_FILTER_PID = 58
    IPC_FILTER_UID = 59
    IPV4ONLY = 31
    IPV6 = 42
    LAST_ENDPOINT = 32
    LINGER = 17
    LOOPBACK_FASTPATH = 94
    MAXMSGSIZE = 22
    MECHANISM = 43
    METADATA = 95
    MULTICAST_HOPS = 25
    MULTICAST_LOOP = 96
    MULTICAST_MAXTPDU = 84
    NORM_BLOCK_SIZE = 121
    NORM_BUFFER_SIZE = 119
    NORM_MODE = 117
    NORM_NUM_AUTOPARITY = 123
    NORM_NUM_PARITY = 122
    NORM_PUSH = 124
    NORM_SEGMENT_SIZE = 120
    NORM_UNICAST_NACK = 118
    ONLY_FIRST_SUBSCRIBE = 108
    OUT_BATCH_SIZE = 102
    PLAIN_PASSWORD = 46
    PLAIN_SERVER = 44
    PLAIN_USERNAME = 45
    PRIORITY = 112
    PROBE_ROUTER = 51
    RATE = 8
    RCVBUF = 12
    RCVHWM = 24
    RCVMORE = 13
    RCVTIMEO = 27
    RECONNECT_IVL = 18
    RECONNECT_IVL_MAX = 21
    RECONNECT_STOP = 109
    RECOVERY_IVL = 9
    REQ_CORRELATE = 52
    REQ_RELAXED = 53
    ROUTER_BEHAVIOR = 33
    ROUTER_HANDOVER = 56
    ROUTER_MANDATORY = 33
    ROUTER_NOTIFY = 97
    ROUTER_RAW = 41
    ROUTING_ID = 5
    SNDBUF = 11
    SNDHWM = 23
    SNDTIMEO = 28
    SOCKS_PASSWORD = 100
    SOCKS_PROXY = 68
    SOCKS_USERNAME = 99
    STREAM_NOTIFY = 73
    SUBSCRIBE = 6
    TCP_ACCEPT_FILTER = 38
    TCP_KEEPALIVE = 34
    TCP_KEEPALIVE_CNT = 35
    TCP_KEEPALIVE_IDLE = 36
    TCP_KEEPALIVE_INTVL = 37
    TCP_MAXRT = 80
    THREAD_SAFE = 81
    TOPICS_COUNT = 116
    TOS = 57
    TYPE = 16
    UNSUBSCRIBE = 7
    USE_FD = 89
    VMCI_BUFFER_MAX_SIZE = 87
    VMCI_BUFFER_MIN_SIZE = 86
    VMCI_BUFFER_SIZE = 85
    VMCI_CONNECT_TIMEOUT = 88
    WSS_CERT_PEM = 104
    WSS_HOSTNAME = 106
    WSS_KEY_PEM = 103
    WSS_TRUST_PEM = 105
    WSS_TRUST_SYSTEM = 107
    XPUB_MANUAL = 71
    XPUB_MANUAL_LAST_VALUE = 98
    XPUB_NODROP = 69
    XPUB_VERBOSE = 40
    XPUB_VERBOSER = 78
    XPUB_WELCOME_MSG = 72
    XSUB_VERBOSE_UNSUBSCRIBE = 115
    ZAP_DOMAIN = 55
    ZAP_ENFORCE_DOMAIN = 93
    _hashable_values_ = [
        1,
        4,
        5,
        6,
        7,
        8,
        9,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        21,
        22,
        23,
        24,
        25,
        27,
        28,
        32,
        33,
        34,
        35,
        36,
        37,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        61,
        62,
        63,
        64,
        65,
        66,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        38,
        58,
        59,
        60,
        31,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        123,
        124,
    ]
    _member_map_ = {
        'AFFINITY': 4,
        'BACKLOG': 19,
        'BINDTODEVICE': 92,
        'BLOCKY': 70,
        'BUSY_POLL': 113,
        'CONFLATE': 54,
        'CONNECT_RID': 61,
        'CONNECT_ROUTING_ID': 61,
        'CONNECT_TIMEOUT': 79,
        'CURVE_PUBLICKEY': 48,
        'CURVE_SECRETKEY': 49,
        'CURVE_SERVER': 47,
        'CURVE_SERVERKEY': 50,
        'DELAY_ATTACH_ON_CONNECT': 39,
        'DISCONNECT_MSG': 111,
        'EVENTS': 15,
        'FAIL_UNROUTABLE': 33,
        'FD': 14,
        'GSSAPI_PLAINTEXT': 65,
        'GSSAPI_PRINCIPAL': 63,
        'GSSAPI_PRINCIPAL_NAMETYPE': 90,
        'GSSAPI_SERVER': 62,
        'GSSAPI_SERVICE_PRINCIPAL': 64,
        'GSSAPI_SERVICE_PRINCIPAL_NAMETYPE': 91,
        'HANDSHAKE_IVL': 66,
        'HEARTBEAT_IVL': 75,
        'HEARTBEAT_TIMEOUT': 77,
        'HEARTBEAT_TTL': 76,
        'HELLO_MSG': 110,
        'HICCUP_MSG': 114,
        'HWM': 1,
        'IDENTITY': 5,
        'IMMEDIATE': 39,
        'INVERT_MATCHING': 74,
        'IN_BATCH_SIZE': 101,
        'IPC_FILTER_GID': 60,
        'IPC_FILTER_PID': 58,
        'IPC_FILTER_UID': 59,
        'IPV4ONLY': 31,
        'IPV6': 42,
        'LAST_ENDPOINT': 32,
        'LINGER': 17,
        'LOOPBACK_FASTPATH': 94,
        'MAXMSGSIZE': 22,
        'MECHANISM': 43,
        'METADATA': 95,
        'MULTICAST_HOPS': 25,
        'MULTICAST_LOOP': 96,
        'MULTICAST_MAXTPDU': 84,
        'NORM_BLOCK_SIZE': 121,
        'NORM_BUFFER_SIZE': 119,
        'NORM_MODE': 117,
        'NORM_NUM_AUTOPARITY': 123,
        'NORM_NUM_PARITY': 122,
        'NORM_PUSH': 124,
        'NORM_SEGMENT_SIZE': 120,
        'NORM_UNICAST_NACK': 118,
        'ONLY_FIRST_SUBSCRIBE': 108,
        'OUT_BATCH_SIZE': 102,
        'PLAIN_PASSWORD': 46,
        'PLAIN_SERVER': 44,
        'PLAIN_USERNAME': 45,
        'PRIORITY': 112,
        'PROBE_ROUTER': 51,
        'RATE': 8,
        'RCVBUF': 12,
        'RCVHWM': 24,
        'RCVMORE': 13,
        'RCVTIMEO': 27,
        'RECONNECT_IVL': 18,
        'RECONNECT_IVL_MAX': 21,
        'RECONNECT_STOP': 109,
        'RECOVERY_IVL': 9,
        'REQ_CORRELATE': 52,
        'REQ_RELAXED': 53,
        'ROUTER_BEHAVIOR': 33,
        'ROUTER_HANDOVER': 56,
        'ROUTER_MANDATORY': 33,
        'ROUTER_NOTIFY': 97,
        'ROUTER_RAW': 41,
        'ROUTING_ID': 5,
        'SNDBUF': 11,
        'SNDHWM': 23,
        'SNDTIMEO': 28,
        'SOCKS_PASSWORD': 100,
        'SOCKS_PROXY': 68,
        'SOCKS_USERNAME': 99,
        'STREAM_NOTIFY': 73,
        'SUBSCRIBE': 6,
        'TCP_ACCEPT_FILTER': 38,
        'TCP_KEEPALIVE': 34,
        'TCP_KEEPALIVE_CNT': 35,
        'TCP_KEEPALIVE_IDLE': 36,
        'TCP_KEEPALIVE_INTVL': 37,
        'TCP_MAXRT': 80,
        'THREAD_SAFE': 81,
        'TOPICS_COUNT': 116,
        'TOS': 57,
        'TYPE': 16,
        'UNSUBSCRIBE': 7,
        'USE_FD': 89,
        'VMCI_BUFFER_MAX_SIZE': 87,
        'VMCI_BUFFER_MIN_SIZE': 86,
        'VMCI_BUFFER_SIZE': 85,
        'VMCI_CONNECT_TIMEOUT': 88,
        'WSS_CERT_PEM': 104,
        'WSS_HOSTNAME': 106,
        'WSS_KEY_PEM': 103,
        'WSS_TRUST_PEM': 105,
        'WSS_TRUST_SYSTEM': 107,
        'XPUB_MANUAL': 71,
        'XPUB_MANUAL_LAST_VALUE': 98,
        'XPUB_NODROP': 69,
        'XPUB_VERBOSE': 40,
        'XPUB_VERBOSER': 78,
        'XPUB_WELCOME_MSG': 72,
        'XSUB_VERBOSE_UNSUBSCRIBE': 115,
        'ZAP_DOMAIN': 55,
        'ZAP_ENFORCE_DOMAIN': 93,
    }
    _member_names_ = [
        'HWM',
        'AFFINITY',
        'ROUTING_ID',
        'SUBSCRIBE',
        'UNSUBSCRIBE',
        'RATE',
        'RECOVERY_IVL',
        'SNDBUF',
        'RCVBUF',
        'RCVMORE',
        'FD',
        'EVENTS',
        'TYPE',
        'LINGER',
        'RECONNECT_IVL',
        'BACKLOG',
        'RECONNECT_IVL_MAX',
        'MAXMSGSIZE',
        'SNDHWM',
        'RCVHWM',
        'MULTICAST_HOPS',
        'RCVTIMEO',
        'SNDTIMEO',
        'LAST_ENDPOINT',
        'ROUTER_MANDATORY',
        'TCP_KEEPALIVE',
        'TCP_KEEPALIVE_CNT',
        'TCP_KEEPALIVE_IDLE',
        'TCP_KEEPALIVE_INTVL',
        'IMMEDIATE',
        'XPUB_VERBOSE',
        'ROUTER_RAW',
        'IPV6',
        'MECHANISM',
        'PLAIN_SERVER',
        'PLAIN_USERNAME',
        'PLAIN_PASSWORD',
        'CURVE_SERVER',
        'CURVE_PUBLICKEY',
        'CURVE_SECRETKEY',
        'CURVE_SERVERKEY',
        'PROBE_ROUTER',
        'REQ_CORRELATE',
        'REQ_RELAXED',
        'CONFLATE',
        'ZAP_DOMAIN',
        'ROUTER_HANDOVER',
        'TOS',
        'CONNECT_ROUTING_ID',
        'GSSAPI_SERVER',
        'GSSAPI_PRINCIPAL',
        'GSSAPI_SERVICE_PRINCIPAL',
        'GSSAPI_PLAINTEXT',
        'HANDSHAKE_IVL',
        'SOCKS_PROXY',
        'XPUB_NODROP',
        'BLOCKY',
        'XPUB_MANUAL',
        'XPUB_WELCOME_MSG',
        'STREAM_NOTIFY',
        'INVERT_MATCHING',
        'HEARTBEAT_IVL',
        'HEARTBEAT_TTL',
        'HEARTBEAT_TIMEOUT',
        'XPUB_VERBOSER',
        'CONNECT_TIMEOUT',
        'TCP_MAXRT',
        'THREAD_SAFE',
        'MULTICAST_MAXTPDU',
        'VMCI_BUFFER_SIZE',
        'VMCI_BUFFER_MIN_SIZE',
        'VMCI_BUFFER_MAX_SIZE',
        'VMCI_CONNECT_TIMEOUT',
        'USE_FD',
        'GSSAPI_PRINCIPAL_NAMETYPE',
        'GSSAPI_SERVICE_PRINCIPAL_NAMETYPE',
        'BINDTODEVICE',
        'TCP_ACCEPT_FILTER',
        'IPC_FILTER_PID',
        'IPC_FILTER_UID',
        'IPC_FILTER_GID',
        'IPV4ONLY',
        'ZAP_ENFORCE_DOMAIN',
        'LOOPBACK_FASTPATH',
        'METADATA',
        'MULTICAST_LOOP',
        'ROUTER_NOTIFY',
        'XPUB_MANUAL_LAST_VALUE',
        'SOCKS_USERNAME',
        'SOCKS_PASSWORD',
        'IN_BATCH_SIZE',
        'OUT_BATCH_SIZE',
        'WSS_KEY_PEM',
        'WSS_CERT_PEM',
        'WSS_TRUST_PEM',
        'WSS_HOSTNAME',
        'WSS_TRUST_SYSTEM',
        'ONLY_FIRST_SUBSCRIBE',
        'RECONNECT_STOP',
        'HELLO_MSG',
        'DISCONNECT_MSG',
        'PRIORITY',
        'BUSY_POLL',
        'HICCUP_MSG',
        'XSUB_VERBOSE_UNSUBSCRIBE',
        'TOPICS_COUNT',
        'NORM_MODE',
        'NORM_UNICAST_NACK',
        'NORM_BUFFER_SIZE',
        'NORM_SEGMENT_SIZE',
        'NORM_BLOCK_SIZE',
        'NORM_NUM_PARITY',
        'NORM_NUM_AUTOPARITY',
        'NORM_PUSH',
    ]
    _member_type_ = int
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = True
    _value2member_map_ = {
        1: 1,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        27: 27,
        28: 28,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
        45: 45,
        46: 46,
        47: 47,
        48: 48,
        49: 49,
        50: 50,
        51: 51,
        52: 52,
        53: 53,
        54: 54,
        55: 55,
        56: 56,
        57: 57,
        58: 58,
        59: 59,
        60: 60,
        61: 61,
        62: 62,
        63: 63,
        64: 64,
        65: 65,
        66: 66,
        68: 68,
        69: 69,
        70: 70,
        71: 71,
        72: 72,
        73: 73,
        74: 74,
        75: 75,
        76: 76,
        77: 77,
        78: 78,
        79: 79,
        80: 80,
        81: 81,
        84: 84,
        85: 85,
        86: 86,
        87: 87,
        88: 88,
        89: 89,
        90: 90,
        91: 91,
        92: 92,
        93: 93,
        94: 94,
        95: 95,
        96: 96,
        97: 97,
        98: 98,
        99: 99,
        100: 100,
        101: 101,
        102: 102,
        103: 103,
        104: 104,
        105: 105,
        106: 106,
        107: 107,
        108: 108,
        109: 109,
        110: 110,
        111: 111,
        112: 112,
        113: 113,
        114: 114,
        115: 115,
        116: 116,
        117: 117,
        118: 118,
        119: 119,
        120: 120,
        121: 121,
        122: 122,
        123: 123,
        124: 124,
    }
    __annotations__ = {
        '_opt_type': '_OptType',
    }
    __firstlineno__ = 134
    __static_attributes__ = ()


class _OptType(__enum.Enum):
    # no doc
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

    bytes = None # (!) real value is "<_OptType.bytes: 'bytes'>"
    fd = None # (!) real value is "<_OptType.fd: 'fd'>"
    int = None # (!) real value is "<_OptType.int: 'int'>"
    int64 = None # (!) real value is "<_OptType.int64: 'int64'>"
    _hashable_values_ = [
        'int',
        'int64',
        'bytes',
        'fd',
    ]
    _member_map_ = {
        'bytes': None, # (!) real value is "<_OptType.bytes: 'bytes'>"
        'fd': None, # (!) real value is "<_OptType.fd: 'fd'>"
        'int': None, # (!) real value is "<_OptType.int: 'int'>"
        'int64': None, # (!) real value is "<_OptType.int64: 'int64'>"
    }
    _member_names_ = [
        'int',
        'int64',
        'bytes',
        'fd',
    ]
    _member_type_ = object
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {
        'bytes': None, # (!) real value is "<_OptType.bytes: 'bytes'>"
        'fd': None, # (!) real value is "<_OptType.fd: 'fd'>"
        'int': None, # (!) real value is "<_OptType.int: 'int'>"
        'int64': None, # (!) real value is "<_OptType.int64: 'int64'>"
    }
    _value_repr_ = None
    __firstlineno__ = 127
    __static_attributes__ = ()


# variables with complex values

__all__ = [
    'IPC_PATH_MAX_LEN',
    'PYZMQ_DRAFT_API',
    'Context',
    'Socket',
    'Frame',
    'has',
    'curve_keypair',
    'curve_public',
    'zmq_version_info',
    'zmq_errno',
    'zmq_poll',
    'strerror',
    'proxy',
    'proxy_steerable',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000228B312DD00>'

__spec__ = None # (!) real value is "ModuleSpec(name='zmq.backend.cython._zmq', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000228B312DD00>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\zmq\\\\backend\\\\cython\\\\_zmq.pyd')"

__test__ = {}

