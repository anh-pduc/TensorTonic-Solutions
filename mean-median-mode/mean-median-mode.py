import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.asarray(x, dtype=float)
    mean = np.mean(x)
    med = np.median(x)
    mod = Counter(x).most_common(1)[0][0]
    return (mean, med, mod)
    
    pass