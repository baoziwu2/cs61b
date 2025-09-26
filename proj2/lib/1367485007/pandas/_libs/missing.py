# encoding: utf-8
# module pandas._libs.missing
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pandas\_libs\missing.cp313-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numbers as numbers # C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\numbers.py
import numpy as np # C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\__init__.py
from pandas._libs.ops_dispatch import maybe_dispatch_ufunc_to_dunder_op


# Variables with simple values

maxsize = 9223372036854775807

# functions

def checknull(*args, **kwargs): # real signature unknown
    """
    Return boolean describing of the input is NA-like, defined here as any
        of:
         - None
         - nan
         - NaT
         - np.datetime64 representation of NaT
         - np.timedelta64 representation of NaT
         - NA
         - Decimal("NaN")
    
        Parameters
        ----------
        val : object
        inf_as_na : bool, default False
            Whether to treat INF and -INF as NA values.
    
        Returns
        -------
        bool
    """
    pass

def check_na_tuples_nonequal(*args, **kwargs): # real signature unknown
    """
    When we have NA in one of the tuples but not the other we have to check here,
        because our regular checks fail before with ambiguous boolean value.
    
        Parameters
        ----------
        left: Any
        right: Any
    
        Returns
        -------
        True if we are dealing with tuples that have NA on one side and non NA on
        the other side.
    """
    pass

def isnaobj(*args, **kwargs): # real signature unknown
    """
    Return boolean mask denoting which elements of a 1-D array are na-like,
        according to the criteria defined in `checknull`:
         - None
         - nan
         - NaT
         - np.datetime64 representation of NaT
         - np.timedelta64 representation of NaT
         - NA
         - Decimal("NaN")
    
        Parameters
        ----------
        arr : ndarray
    
        Returns
        -------
        result : ndarray (dtype=np.bool_)
    """
    pass

def isneginf_scalar(*args, **kwargs): # real signature unknown
    pass

def isposinf_scalar(*args, **kwargs): # real signature unknown
    pass

def is_matching_na(*args, **kwargs): # real signature unknown
    """
    Check if two scalars are both NA of matching types.
    
        Parameters
        ----------
        left : Any
        right : Any
        nan_matches_none : bool, default False
            For backwards compatibility, consider NaN as matching None.
    
        Returns
        -------
        bool
    """
    pass

def is_numeric_na(*args, **kwargs): # real signature unknown
    """
    Check for NA values consistent with IntegerArray/FloatingArray.
    
        Similar to a vectorized is_valid_na_for_dtype restricted to numeric dtypes.
    
        Returns
        -------
        ndarray[bool]
    """
    pass

def _create_binary_propagating_op(*args, **kwargs): # real signature unknown
    pass

def _create_unary_propagating_op(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_C_NAType(*args, **kwargs): # real signature unknown
    pass

# classes

class C_NAType(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class Decimal(object):
    """
    Construct a new Decimal object. 'value' can be an integer, string, tuple,
    or another Decimal object. If no value is given, return Decimal('0'). The
    context does not affect the conversion and is only passed to determine if
    the InvalidOperation trap is active.
    """
    def adjusted(self, *args, **kwargs): # real signature unknown
        """ Return the adjusted exponent of the number.  Defined as exp + digits - 1. """
        pass

    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Decimal.as_integer_ratio() -> (int, int)
        
        Return a pair of integers, whose ratio is exactly equal to the original
        Decimal and with a positive denominator. The ratio is in lowest terms.
        Raise OverflowError on infinities and a ValueError on NaNs.
        """
        pass

    def as_tuple(self, *args, **kwargs): # real signature unknown
        """ Return a tuple representation of the number. """
        pass

    def canonical(self, *args, **kwargs): # real signature unknown
        """
        Return the canonical encoding of the argument.  Currently, the encoding
        of a Decimal instance is always canonical, so this operation returns its
        argument unchanged.
        """
        pass

    def compare(self, *args, **kwargs): # real signature unknown
        """
        Compare self to other.  Return a decimal value:
        
            a or b is a NaN ==> Decimal('NaN')
            a < b           ==> Decimal('-1')
            a == b          ==> Decimal('0')
            a > b           ==> Decimal('1')
        """
        pass

    def compare_signal(self, *args, **kwargs): # real signature unknown
        """ Identical to compare, except that all NaNs signal. """
        pass

    def compare_total(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Compare two operands using their abstract representation rather than
        their numerical value.  Similar to the compare() method, but the result
        gives a total ordering on Decimal instances.  Two Decimal instances with
        the same numeric value but different representations compare unequal
        in this ordering:
        
            >>> Decimal('12.0').compare_total(Decimal('12'))
            Decimal('-1')
        
        Quiet and signaling NaNs are also included in the total ordering. The result
        of this function is Decimal('0') if both operands have the same representation,
        Decimal('-1') if the first operand is lower in the total order than the second,
        and Decimal('1') if the first operand is higher in the total order than the
        second operand. See the specification for details of the total order.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def compare_total_mag(self, y): # real signature unknown; restored from __doc__
        """
        Compare two operands using their abstract representation rather than their
        value as in compare_total(), but ignoring the sign of each operand.
        
        x.compare_total_mag(y) is equivalent to x.copy_abs().compare_total(y.copy_abs()).
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Return self. """
        pass

    def copy_abs(self, *args, **kwargs): # real signature unknown
        """
        Return the absolute value of the argument.  This operation is unaffected by
        context and is quiet: no flags are changed and no rounding is performed.
        """
        pass

    def copy_negate(self, *args, **kwargs): # real signature unknown
        """
        Return the negation of the argument.  This operation is unaffected by context
        and is quiet: no flags are changed and no rounding is performed.
        """
        pass

    def copy_sign(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a copy of the first operand with the sign set to be the same as the
        sign of the second operand. For example:
        
            >>> Decimal('2.3').copy_sign(Decimal('-1.5'))
            Decimal('-2.3')
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def exp(self, *args, **kwargs): # real signature unknown
        """
        Return the value of the (natural) exponential function e**x at the given
        number.  The function always uses the ROUND_HALF_EVEN mode and the result
        is correctly rounded.
        """
        pass

    def fma(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Fused multiply-add.  Return self*other+third with no rounding of the
        intermediate product self*other.
        
            >>> Decimal(2).fma(3, 5)
            Decimal('11')
        """
        pass

    @classmethod
    def from_float(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Class method that converts a float to a decimal number, exactly.
        Since 0.1 is not exactly representable in binary floating point,
        Decimal.from_float(0.1) is not the same as Decimal('0.1').
        
            >>> Decimal.from_float(0.1)
            Decimal('0.1000000000000000055511151231257827021181583404541015625')
            >>> Decimal.from_float(float('nan'))
            Decimal('NaN')
            >>> Decimal.from_float(float('inf'))
            Decimal('Infinity')
            >>> Decimal.from_float(float('-inf'))
            Decimal('-Infinity')
        """
        pass

    def is_canonical(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is canonical and False otherwise.  Currently,
        a Decimal instance is always canonical, so this operation always returns
        True.
        """
        pass

    def is_finite(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a finite number, and False if the argument
        is infinite or a NaN.
        """
        pass

    def is_infinite(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is either positive or negative infinity and
        False otherwise.
        """
        pass

    def is_nan(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a (quiet or signaling) NaN and False
        otherwise.
        """
        pass

    def is_normal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a normal finite non-zero number with an
        adjusted exponent greater than or equal to Emin. Return False if the
        argument is zero, subnormal, infinite or a NaN.
        """
        pass

    def is_qnan(self, *args, **kwargs): # real signature unknown
        """ Return True if the argument is a quiet NaN, and False otherwise. """
        pass

    def is_signed(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument has a negative sign and False otherwise.
        Note that both zeros and NaNs can carry signs.
        """
        pass

    def is_snan(self, *args, **kwargs): # real signature unknown
        """ Return True if the argument is a signaling NaN and False otherwise. """
        pass

    def is_subnormal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is subnormal, and False otherwise. A number is
        subnormal if it is non-zero, finite, and has an adjusted exponent less
        than Emin.
        """
        pass

    def is_zero(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a (positive or negative) zero and False
        otherwise.
        """
        pass

    def ln(self, *args, **kwargs): # real signature unknown
        """
        Return the natural (base e) logarithm of the operand. The function always
        uses the ROUND_HALF_EVEN mode and the result is correctly rounded.
        """
        pass

    def log10(self, *args, **kwargs): # real signature unknown
        """
        Return the base ten logarithm of the operand. The function always uses the
        ROUND_HALF_EVEN mode and the result is correctly rounded.
        """
        pass

    def logb(self, *args, **kwargs): # real signature unknown
        """
        For a non-zero number, return the adjusted exponent of the operand as a
        Decimal instance.  If the operand is a zero, then Decimal('-Infinity') is
        returned and the DivisionByZero condition is raised. If the operand is
        an infinity then Decimal('Infinity') is returned.
        """
        pass

    def logical_and(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'and' of the two (logical) operands. """
        pass

    def logical_invert(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise inversion of the (logical) operand. """
        pass

    def logical_or(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'or' of the two (logical) operands. """
        pass

    def logical_xor(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'exclusive or' of the two (logical) operands. """
        pass

    def max(self, *args, **kwargs): # real signature unknown
        """
        Maximum of self and other.  If one operand is a quiet NaN and the other is
        numeric, the numeric operand is returned.
        """
        pass

    def max_mag(self, *args, **kwargs): # real signature unknown
        """
        Similar to the max() method, but the comparison is done using the absolute
        values of the operands.
        """
        pass

    def min(self, *args, **kwargs): # real signature unknown
        """
        Minimum of self and other. If one operand is a quiet NaN and the other is
        numeric, the numeric operand is returned.
        """
        pass

    def min_mag(self, *args, **kwargs): # real signature unknown
        """
        Similar to the min() method, but the comparison is done using the absolute
        values of the operands.
        """
        pass

    def next_minus(self, *args, **kwargs): # real signature unknown
        """
        Return the largest number representable in the given context (or in the
        current default context if no context is given) that is smaller than the
        given operand.
        """
        pass

    def next_plus(self, *args, **kwargs): # real signature unknown
        """
        Return the smallest number representable in the given context (or in the
        current default context if no context is given) that is larger than the
        given operand.
        """
        pass

    def next_toward(self, *args, **kwargs): # real signature unknown
        """
        If the two operands are unequal, return the number closest to the first
        operand in the direction of the second operand.  If both operands are
        numerically equal, return a copy of the first operand with the sign set
        to be the same as the sign of the second operand.
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """
        Normalize the number by stripping the rightmost trailing zeros and
        converting any result equal to Decimal('0') to Decimal('0e0').  Used
        for producing canonical values for members of an equivalence class.
        For example, Decimal('32.100') and Decimal('0.321000e+2') both normalize
        to the equivalent value Decimal('32.1').
        """
        pass

    def number_class(self, *args, **kwargs): # real signature unknown
        """
        Return a string describing the class of the operand.  The returned value
        is one of the following ten strings:
        
            * '-Infinity', indicating that the operand is negative infinity.
            * '-Normal', indicating that the operand is a negative normal number.
            * '-Subnormal', indicating that the operand is negative and subnormal.
            * '-Zero', indicating that the operand is a negative zero.
            * '+Zero', indicating that the operand is a positive zero.
            * '+Subnormal', indicating that the operand is positive and subnormal.
            * '+Normal', indicating that the operand is a positive normal number.
            * '+Infinity', indicating that the operand is positive infinity.
            * 'NaN', indicating that the operand is a quiet NaN (Not a Number).
            * 'sNaN', indicating that the operand is a signaling NaN.
        """
        pass

    def quantize(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a value equal to the first operand after rounding and having the
        exponent of the second operand.
        
            >>> Decimal('1.41421356').quantize(Decimal('1.000'))
            Decimal('1.414')
        
        Unlike other operations, if the length of the coefficient after the quantize
        operation would be greater than precision, then an InvalidOperation is signaled.
        This guarantees that, unless there is an error condition, the quantized exponent
        is always equal to that of the right-hand operand.
        
        Also unlike other operations, quantize never signals Underflow, even if the
        result is subnormal and inexact.
        
        If the exponent of the second operand is larger than that of the first, then
        rounding may be necessary. In this case, the rounding mode is determined by the
        rounding argument if given, else by the given context argument; if neither
        argument is given, the rounding mode of the current thread's context is used.
        """
        pass

    def radix(self, base): # real signature unknown; restored from __doc__
        """
        Return Decimal(10), the radix (base) in which the Decimal class does
        all its arithmetic. Included for compatibility with the specification.
        """
        pass

    def remainder_near(self, *args, **kwargs): # real signature unknown
        """
        Return the remainder from dividing self by other.  This differs from
        self % other in that the sign of the remainder is chosen so as to minimize
        its absolute value. More precisely, the return value is self - n * other
        where n is the integer nearest to the exact value of self / other, and
        if two integers are equally near then the even one is chosen.
        
        If the result is zero then its sign will be the sign of self.
        """
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        """
        Return the result of rotating the digits of the first operand by an amount
        specified by the second operand.  The second operand must be an integer in
        the range -precision through precision. The absolute value of the second
        operand gives the number of places to rotate. If the second operand is
        positive then rotation is to the left; otherwise rotation is to the right.
        The coefficient of the first operand is padded on the left with zeros to
        length precision if necessary. The sign and exponent of the first operand are
        unchanged.
        """
        pass

    def same_quantum(self, *args, **kwargs): # real signature unknown
        """
        Test whether self and other have the same exponent or whether both are NaN.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def scaleb(self, *args, **kwargs): # real signature unknown
        """
        Return the first operand with the exponent adjusted the second.  Equivalently,
        return the first operand multiplied by 10**other. The second operand must be
        an integer.
        """
        pass

    def shift(self, *args, **kwargs): # real signature unknown
        """
        Return the result of shifting the digits of the first operand by an amount
        specified by the second operand.  The second operand must be an integer in
        the range -precision through precision. The absolute value of the second
        operand gives the number of places to shift. If the second operand is
        positive, then the shift is to the left; otherwise the shift is to the
        right. Digits shifted into the coefficient are zeros. The sign and exponent
        of the first operand are unchanged.
        """
        pass

    def sqrt(self, *args, **kwargs): # real signature unknown
        """
        Return the square root of the argument to full precision. The result is
        correctly rounded using the ROUND_HALF_EVEN rounding mode.
        """
        pass

    def to_eng_string(self, *args, **kwargs): # real signature unknown
        """
        Convert to an engineering-type string.  Engineering notation has an exponent
        which is a multiple of 3, so there are up to 3 digits left of the decimal
        place. For example, Decimal('123E+1') is converted to Decimal('1.23E+3').
        
        The value of context.capitals determines whether the exponent sign is lower
        or upper case. Otherwise, the context does not affect the operation.
        """
        pass

    def to_integral(self): # real signature unknown; restored from __doc__
        """
        Identical to the to_integral_value() method.  The to_integral() name has been
        kept for compatibility with older versions.
        """
        pass

    def to_integral_exact(self, *args, **kwargs): # real signature unknown
        """
        Round to the nearest integer, signaling Inexact or Rounded as appropriate if
        rounding occurs.  The rounding mode is determined by the rounding parameter
        if given, else by the given context. If neither parameter is given, then the
        rounding mode of the current default context is used.
        """
        pass

    def to_integral_value(self, *args, **kwargs): # real signature unknown
        """
        Round to the nearest integer without signaling Inexact or Rounded.  The
        rounding mode is determined by the rounding parameter if given, else by
        the given context. If neither parameter is given, then the rounding mode
        of the current default context is used.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        pass

    def __complex__(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class NAType(C_NAType):
    """
    NA ("not available") missing value indicator.
    
        .. warning::
    
           Experimental: the behaviour of NA can still change without warning.
    
        The NA singleton is a missing value indicator defined by pandas. It is
        used in certain new extension dtypes (currently the "string" dtype).
    
        Examples
        --------
        >>> pd.NA
        <NA>
    
        >>> True | pd.NA
        True
    
        >>> True & pd.NA
        <NA>
    
        >>> pd.NA != pd.NA
        <NA>
    
        >>> pd.NA == pd.NA
        <NA>
    
        >>> True | pd.NA
        True
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        pass

    def __array_ufunc__(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    def __matmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmatmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _HANDLED_TYPES = (
        np.ndarray,
        numbers.Number,
        str,
        np.bool,
    )
    _instance = None # (!) forward: NA, real value is '<NA>'
    __array_priority__ = 1000
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.missing\', \'__doc__\': \'\\n    NA ("not available") missing value indicator.\\n\\n    .. warning::\\n\\n       Experimental: the behaviour of NA can still change without warning.\\n\\n    The NA singleton is a missing value indicator defined by pandas. It is\\n    used in certain new extension dtypes (currently the "string" dtype).\\n\\n    Examples\\n    --------\\n    >>> pd.NA\\n    <NA>\\n\\n    >>> True | pd.NA\\n    True\\n\\n    >>> True & pd.NA\\n    <NA>\\n\\n    >>> pd.NA != pd.NA\\n    <NA>\\n\\n    >>> pd.NA == pd.NA\\n    <NA>\\n\\n    >>> True | pd.NA\\n    True\\n    \', \'_instance\': <NA>, \'__new__\': <staticmethod(<cyfunction NAType.__new__ at 0x000001B67AD49B40>)>, \'__repr__\': <cyfunction NAType.__repr__ at 0x000001B67AD49C00>, \'__format__\': <cyfunction NAType.__format__ at 0x000001B67AD49CC0>, \'__bool__\': <cyfunction NAType.__bool__ at 0x000001B67AD49D80>, \'__hash__\': <cyfunction NAType.__hash__ at 0x000001B67AD49E40>, \'__reduce__\': <cyfunction NAType.__reduce__ at 0x000001B67AD49F00>, \'__add__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD49FC0>, \'__radd__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A080>, \'__sub__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A140>, \'__rsub__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A200>, \'__mul__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A2C0>, \'__rmul__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A380>, \'__matmul__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A440>, \'__rmatmul__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A500>, \'__truediv__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A5C0>, \'__rtruediv__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A680>, \'__floordiv__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A740>, \'__rfloordiv__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A800>, \'__mod__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A8C0>, \'__rmod__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4A980>, \'__divmod__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4AA40>, \'__rdivmod__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4AB00>, \'__eq__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4ABC0>, \'__ne__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4AC80>, \'__le__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4AD40>, \'__lt__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4AE00>, \'__gt__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4AEC0>, \'__ge__\': <cyfunction _create_binary_propagating_op.<locals>.method at 0x000001B67AD4AF80>, \'__neg__\': <cyfunction _create_unary_propagating_op.<locals>.method at 0x000001B67AD4B040>, \'__pos__\': <cyfunction _create_unary_propagating_op.<locals>.method at 0x000001B67AD4B100>, \'__abs__\': <cyfunction _create_unary_propagating_op.<locals>.method at 0x000001B67AD4B1C0>, \'__invert__\': <cyfunction _create_unary_propagating_op.<locals>.method at 0x000001B67AD4B280>, \'__pow__\': <cyfunction NAType.__pow__ at 0x000001B67AD4B340>, \'__rpow__\': <cyfunction NAType.__rpow__ at 0x000001B67AD4B400>, \'__and__\': <cyfunction NAType.__and__ at 0x000001B67AD4B4C0>, \'__rand__\': <cyfunction NAType.__and__ at 0x000001B67AD4B4C0>, \'__or__\': <cyfunction NAType.__or__ at 0x000001B67AD4B580>, \'__ror__\': <cyfunction NAType.__or__ at 0x000001B67AD4B580>, \'__xor__\': <cyfunction NAType.__xor__ at 0x000001B67AD4B640>, \'__rxor__\': <cyfunction NAType.__xor__ at 0x000001B67AD4B640>, \'__array_priority__\': 1000, \'_HANDLED_TYPES\': (<class \'numpy.ndarray\'>, <class \'numbers.Number\'>, <class \'str\'>, <class \'numpy.bool\'>), \'__array_ufunc__\': <cyfunction NAType.__array_ufunc__ at 0x000001B67AD4B700>, \'__dict__\': <attribute \'__dict__\' of \'NAType\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'NAType\' objects>})'


# variables with complex values

NA = None # (!) real value is '<NA>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B67AB94FD0>'

__pyx_capi__ = {
    'C_NA': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_7missing_C_NAType *" at 0x000001B67ABCFDD0>'
    'check_na_tuples_nonequal': None, # (!) real value is '<capsule object "int (PyObject *, PyObject *, int __pyx_skip_dispatch)" at 0x000001B67ABCFE70>'
    'checknull': None, # (!) real value is '<capsule object "int (PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_7missing_checknull *__pyx_optional_args)" at 0x000001B67ABCFEC0>'
    'checknull_with_nat_and_na': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001B67ABD8040>'
    'is_matching_na': None, # (!) real value is '<capsule object "int (PyObject *, PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_7missing_is_matching_na *__pyx_optional_args)" at 0x000001B67ABCFE20>'
    'is_null_datetime64': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001B67ABCFF60>'
    'is_null_timedelta64': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001B67ABCFFB0>'
    'isnaobj': None, # (!) real value is '<capsule object "PyArrayObject *(PyArrayObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_7missing_isnaobj *__pyx_optional_args)" at 0x000001B67ABCFF10>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.missing', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B67AB94FD0>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\pandas\\\\_libs\\\\missing.cp313-win_amd64.pyd')"

__test__ = {}

