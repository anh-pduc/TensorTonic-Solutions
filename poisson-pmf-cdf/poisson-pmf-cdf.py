import numpy as np
from math import factorial
def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    assert lam>0 and k>=0, "invalid input"
    pmf = np.exp(lam*(-1))*lam**k/factorial(k)
    cdf = 0
    for i in range(k+1):
        c = np.exp(lam*(-1))*lam**i/factorial(i)
        cdf = cdf + c
    return pmf, cdf
    pass