# -*- coding: utf-8 -*-
import numpy as np

# scores = gaussian_distribution(10, 10, 50)
def gaussian_distribution(m, sigma=10, mean=50):
    isinstance(m, int)
    if m < 0:
        m = 0
    return list(np.random.normal(mean, sigma, m))
