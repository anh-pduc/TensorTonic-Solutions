import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.asarray(X,dtype=float)
    if X.ndim != 2 or X.shape[0] <2:
        return None
    mu = np.mean(X, axis = 0)
    X_cen = X - mu
    X_cen_t = np.transpose(X_cen)
    n = X.shape[0]
    cov = np.dot(X_cen_t,X_cen)
    cov = 1/(n-1)*cov
    return cov
    pass