import numpy as np
def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    n = len(y_true)
    assert len(y_true) == len(y_pred), "incorrect sample matching"
    assert n_bins > 0, "n_bins must > 0"
    
    bins = []
    width = 1.0/n_bins
    for i in range(n_bins):
        left = i * width
        right = (i+1) * width
        if i == n_bins - 1:
            bins.append((left, right, True))
        else:
            bins.append((left, right, False))

    ECE = 0.0
    for (left, right, is_last) in bins:
        count = 0
        acc = 0
        conf = 0.0
        for i in range(n):
            if (left <= y_pred[i] <= right) if is_last else (left <= y_pred[i] < right):
                count += 1
                acc += y_true[i]
                conf += y_pred[i]
        if count == 0:
            continue
        acc /= count
        conf /= count
        ECE += count/n * np.abs(acc - conf)

    # bin_edges = np.linspace(0,1, n_bins + 1)
    # bin_ids = np.digitize(y_pred, bin_edges, right = True) - 1
    # bin_ids = np.clip(bin_ids, 0, n_bins - 1)
    # counts = np.bincount(bin_ids, minlength = n_bins)

    # sum_acc = np.bincount(bin_ids, weights = y_true, minlength = n_bins)
    # sum_conf = np.bincount(bin_ids, weights = y_pred, minlength = n_bins)

    # nonzero = counts>0
    # acc = np.zeros(n_bins)
    # conf = np.zeros(n_bins)
    # acc[nonzero] = sum_acc[nonzero]/ counts[nonzero]
    # conf[nonzero] = sum_conf[nonzero]/ counts[nonzero]

    # ECE = np.sum((counts[nonzero]/n)*np.abs(acc[nonzero]-conf[nonzero]))
    return ECE
    
    pass