import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    MIN = np.min(X,axis=axis,keepdims=True)
    MAX = np.max(X, axis = axis,keepdims=True)
    X_ = (X - MIN)/np.maximum((MAX-MIN),eps)
    return X_
    pass