import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    X = np.asarray(values, dtype=float)
    w = np.maximum((np.max(X)-np.min(X))/num_bins,1e-12)
    BIN = np.minimum(((X-np.min(X))/w).astype(int), num_bins-1).tolist()
    return BIN