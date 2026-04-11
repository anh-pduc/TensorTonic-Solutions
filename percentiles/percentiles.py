import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # x = np.asarray(x,dtype=float).sort()
    per = np.percentile(x, q, method = 'linear')
    return per
    pass