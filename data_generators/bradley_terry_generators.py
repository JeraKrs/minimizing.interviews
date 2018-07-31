# -*- coding: utf-8 -*-
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import math
import numpy as np

from data_generators.score_generators \
        import gaussian_distribution


# rank = bradley_terry_model([5.0, 4.5, 4.5, 3.0])
def bradley_terry_model(scores):
    isinstance(scores, list)

    m = len(scores)
    f = list(np.zeros(m))
    lw = [math.log(x) for x in scores]
    slw = list(np.zeros(m))
    for i in range(m):
        for j in range(i+1, m):
            l = math.log(scores[i] + scores[j])
            slw[i], slw[j] = slw[i] + l, slw[j] + l

    rank = list()
    for i in range(m):
        # k * log w_i - log(w_i + w_j) ...
        H = [math.exp((m-f[j]-1)*lw[j]-slw[j]) for j in range(m)]
        F = sum(H)
        probs = [x/F for x in H]

        k = np.random.choice(range(m), 1, p=probs)[0]
        rank.append(k)

        f[k] = m
        for j in range(m):
            f[j] = max(f[j], i+1)
            slw[j] -= math.log(scores[k] + scores[j])

    return rank
    


# [applicants, employers] = bradley_terry_preferences(5, 2)
def bradley_terry_preferences(m, sigma=0, mean=5):
    isinstance(m, int)
    isinstance(sigma, float)

    score_applicant = gaussian_distribution(m, sigma, mean)
    score_employer = gaussian_distribution(m, sigma, mean)

    applicants, employers = list(), list()
    for i in range(m):
        applicants.append(bradley_terry_model(score_applicant))
        employers.append(bradley_terry_model(score_employer))

    return applicants, employers
