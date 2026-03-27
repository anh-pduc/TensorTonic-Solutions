import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    try:
        A = np.asarray(matrix, dtype=float)
    except:
        return None
    if A.ndim != 2:
        return None
    if A.shape[0] != A.shape[1]:
        return None
    eig = np.linalg.eigvals(A)
    # eig = np.lexsort(eig)
    return eig
    pass