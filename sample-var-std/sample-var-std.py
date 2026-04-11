import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n<2:
        raise ValueError
    mean = np.mean(x)
    v = []
    var = np.sum((x-mean)**2)/(n-1)
    std = np.sqrt(var)
    return var, std
    pass