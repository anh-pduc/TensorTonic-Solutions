import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    cond = n>0 and 0<=p<=1 and 0<=k<=n
    assert cond, "invalid input"
    pmf = comb(n,k) * (p**k) * ((1-p)**(n-k))
    cdf = 0
    for i in range(k+1):
        cd = comb(n,i) * (p**i) * ((1-p)**(n-i))
        cdf = cdf + cd
    return (pmf, cdf)
    pass