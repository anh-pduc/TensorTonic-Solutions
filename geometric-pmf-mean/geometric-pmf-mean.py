import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    k = np.asarray(k,dtype=float)
    cond = (k>=1).all() and 0<p<=1
    assert cond, "invalid input"
    pmf = (1-p)**(k-1) * p
    mean = 1/p
    return(pmf, mean)
    pass