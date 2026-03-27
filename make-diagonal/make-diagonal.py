import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # v = np.asarray(v,dtype=float)
    # n = v.size
    # A = np.zeros((n,n))
    # for i in range(n):
    #     A[i,i] = v[i]
    # return A
    return np.diag(np.asarray(v,dtype=float))
    pass
