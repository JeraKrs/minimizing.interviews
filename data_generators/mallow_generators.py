# -*- coding: utf-8 -*- 
import os, sys 
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import copy
import math
import numpy as np

from tools.utils import list_to_rank


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


def sample_permutation(mu, time):
    m = len(mu)
    c = copy.deepcopy(mu)
    time = np.random.choice(range(int(time)+1), 1)[0]
    for i in np.random.choice(range(m-1), int(time)):
        l, r = int(i), int(i + 1)
        c[l], c[r] = c[r], c[l]
    return c


def mallow_model(m, sigma, mu, pro_f, n=1):

    k = 100
    p, v = list(), list()
    for i in range(m*k):
        c = sample_permutation(mu, int(m*100*(1-sigma)))
        p.append(c)
        v.append(math.exp(-sigma * pro_f(list_to_rank(mu, m), list_to_rank(c, m))))

    z = sum(v)
    v = [x/z for x in v]

    r = list()
    for i in np.random.choice(range(m*k), n, p=v):
        r.append(p[i])

    return r


def mallow_preferences(m, sigma, pros="spearman"): 
    if pros == "spearman":
        applicants = mallow_model(m, sigma, list(np.random.permutation(m)), spearman, m)
        employers = mallow_model(m, sigma, list(np.random.permutation(m)), spearman, m)
    elif pros == "footrule":
        applicants = mallow_model(m, sigma, list(np.random.permutation(m)), footrule, m)
        employers = mallow_model(m, sigma, list(np.random.permutation(m)), footrule, m)

    return applicants, employers
