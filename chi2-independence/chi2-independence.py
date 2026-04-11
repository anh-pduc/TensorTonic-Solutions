import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    C = np.asarray(C, dtype=float)
    h,w = C.shape
    sum_row = np.sum(C, axis=1).tolist()
    sum_col = np.sum(C, axis=0).tolist()
    total = np.sum(C)
    E = []
    for i in range(h):
        for j in range(w):
            E.append((sum_row[i]*sum_col[j])/total)
    E = np.array(E).reshape(h,w)
    chi = np.sum((C-E)**2/E)
    return chi, E
    pass