# -*- coding: utf-8 -*-
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import math
import numpy as np

from data_generators.score_generators \
        import gaussian_distribution


# rank = luce_model([5.0, 4.5, 4.5, 3.0])
def luce_model(scores):
    isinstance(scores, list)

    m = len(scores)
    exp_s = [math.exp(x) for x in scores]
    F = sum(exp_s)

    rank = list()
    for i in range(m):
        probs = [x/F for x in exp_s]

        k = np.random.choice(range(m), 1, p=probs)[0]

        rank.append(k)
        F -= exp_s[k]
        exp_s[k] = 0

    return rank
    


# [applicants, employers] = luce_preferences(5, 2)
def luce_preferences(m, sigma=0, mean=5):
    isinstance(m, int)
    isinstance(sigma, float)

    score_applicant = gaussian_distribution(m, sigma, mean)
    score_employer = gaussian_distribution(m, sigma, mean)

    applicants, employers = list(), list()
    for i in range(m):
        applicants.append(luce_model(score_applicant))
        employers.append(luce_model(score_employer))

    return applicants, employers
