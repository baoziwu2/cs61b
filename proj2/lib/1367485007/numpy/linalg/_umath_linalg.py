# encoding: utf-8
# module numpy.linalg._umath_linalg
# from C:\Users\baozi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\numpy\linalg\_umath_linalg.cp313-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

_ilp64 = True

__version__ = '0.1.5'

# functions

def cholesky_lo(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cholesky_lo(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    cholesky decomposition of hermitian positive-definite matrices,
    using lower triangle. Broadcast to all outer dimensions.
        "(m,m)->(m,m)"
    """
    pass

def cholesky_up(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cholesky_up(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    cholesky decomposition of hermitian positive-definite matrices,
    using upper triangle. Broadcast to all outer dimensions.
        "(m,m)->(m,m)"
    """
    pass

def det(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    det(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    det of the last two dimensions and broadcast on the rest. 
        "(m,m)->()"
    """
    pass

def eig(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eig(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    eig on the last two dimension and broadcast to the rest. 
    Results in a vector with the  eigenvalues and a matrix with the eigenvectors. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigh_lo(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigh_lo(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    eigh on the last two dimension and broadcast to the rest, using lower triangle 
    Results in a vector of eigenvalues and a matrix with theeigenvectors. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigh_up(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigh_up(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    eigh on the last two dimension and broadcast to the rest, using upper triangle. 
    Results in a vector of eigenvalues and a matrix with the eigenvectors. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigvals(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigvals(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    eigvals on the last two dimension and broadcast to the rest. 
    Results in a vector of eigenvalues.
    """
    pass

def eigvalsh_lo(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigvalsh_lo(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    eigh on the last two dimension and broadcast to the rest, using lower triangle. 
    Results in a vector of eigenvalues and a matrix with theeigenvectors. 
        "(m,m)->(m)"
    """
    pass

def eigvalsh_up(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigvalsh_up(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    eigvalsh on the last two dimension and broadcast to the rest, using upper triangle. 
    Results in a vector of eigenvalues and a matrix with theeigenvectors.
        "(m,m)->(m)"
    """
    pass

def inv(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    inv(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    compute the inverse of the last two dimensions and broadcast to the rest. 
    Results in the inverse matrices. 
        "(m,m)->(m,m)"
    """
    pass

def lstsq(x1, x2, x3, out1=None, out2=None, out3=None, out4=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    lstsq(x1, x2, x3[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    least squares on the last two dimensions and broadcast to the rest.
    """
    pass

def qr_complete(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qr_complete(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    Compute Q matrix for the last two dimensions 
    and broadcast to the rest. For m > n.
    """
    pass

def qr_reduced(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qr_reduced(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    Compute Q matrix for the last two dimensions 
    and broadcast to the rest.
    """
    pass

def qr_r_raw(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qr_r_raw(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    Compute TAU vector for the last two dimensions 
    and broadcast to the rest.
    """
    pass

def slogdet(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    slogdet(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    slogdet on the last two dimensions and broadcast on the rest. 
    Results in two arrays, one with sign and the other with log of the determinants. 
        "(m,m)->(),()"
    """
    pass

def solve(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    solve(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    solve the system a x = b, on the last two dimensions, broadcast to the rest. 
    Results in a matrices with the solutions. 
        "(m,m),(m,n)->(m,n)"
    """
    pass

def solve1(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    solve1(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    solve the system a x = b, for b being a vector, broadcast in the outer dimensions. 
    Results in vectors with the solutions. 
        "(m,m),(m)->(m)"
    """
    pass

def svd(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    svd(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    Singular values of array with shape (m, n).
    Return value is 1-d array with shape (min(m, n),).
    """
    pass

def svd_f(x, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    svd_f(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    svd (full_matrices=True)
    """
    pass

def svd_s(x, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    svd_s(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])
    
    svd (full_matrices=False)
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D79443F050>'

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.linalg._umath_linalg', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D79443F050>, origin='C:\\\\Users\\\\baozi\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python313\\\\site-packages\\\\numpy\\\\linalg\\\\_umath_linalg.cp313-win_amd64.pyd')"

