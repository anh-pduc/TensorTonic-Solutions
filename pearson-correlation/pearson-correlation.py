import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    X = np.asarray(X,dtype=float)
    if X.ndim != 2 or X.shape[0] <2:
        return None
    mu = np.mean(X, axis = 0)
    X_cen = X - mu
    sig = np.std(X, axis = 0, ddof = 1)
    cov = np.dot(X_cen.T,X_cen)/(X.shape[0]-1)
    return cov/np.outer(sig, sig)
    pass