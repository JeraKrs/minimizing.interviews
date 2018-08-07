# -*- coding: utf-8 -*- 
import os, sys 
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import math
import numpy as np

from data_generators.bradley_terry_generators import bradley_terry_model

def spearman(a, b):
    isinstance(a, list)
    isinstance(b, list)

    r = 0
    for i, j in zip(a, b):
        r += (i-j)*(i-j)
    return r


def footrule(a, b):
    isinstance(a, list)
    isinstance(b, list)

    r = 0
    for i, j in zip(a, b):
        r += math.fabs(i-j)
    return r


def mallow_model(m, sigma, pro_f):
    mu = list(np.random.permutation(m))

    score = [m - i*sigma for i in mu]
    p, v = list(), list()
    for i in range(m*m):
        c = bradley_terry_model(score)
        p.append(c)
        v.append(math.exp(-sigma * pro_f(mu, c)))

    z = sum(v)
    v = [x/z for x in v]

    r = list()
    for i in np.random.choice(range(m*m), m, p=v):
        r.append(p[i])

    return r


def mallow_preferences(m, sigma, pros="spearman"):

    if pros == "spearman":
        applicants = mallow_model(m, sigma, spearman)
        employers = mallow_model(m, sigma, spearman)
    elif pros == "footrule":
        applicants = mallow_model(m, sigma, footrule)
        employers = mallow_model(m, sigma, footrule)

    return applicants, employers
