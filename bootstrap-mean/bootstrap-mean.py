import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    x = np.asarray(x, dtype=float)
    if rng is None:
        rng = np.default_rng()
    boot_means = []
    for _ in range(n_bootstrap):
        Xb = rng.choice(x, size=len(x), replace=True)
        boot_means.append(np.mean(Xb))

    boot_means = np.asarray(boot_means, dtype=float)

    alpha = 1 - ci
    lower = np.percentile(boot_means, 100 * (alpha/2))
    upper = np.percentile(boot_means, 100 * (1-alpha/2))
    
    return boot_means, lower, upper
    
    
    pass
