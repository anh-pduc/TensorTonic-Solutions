import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    x = np.asarray(x, dtype=float)
    mean = np.mean(x)
    n = len(x)
    if n<2:
        raise ValueError
    var = np.sum((x-mean)**2)/(n-1)
    std = np.sqrt(var)
    return (mean-mu0)/(std/np.sqrt(n))
    pass