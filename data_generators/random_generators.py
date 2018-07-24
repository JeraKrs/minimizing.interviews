# -*- coding: utf-8 -*-

import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import numpy as np
import random as rd

from tools.utils import shuffle


# [applicants, employers] = random_preferences(5)
def random_preferences(m):

    isinstance(m, int)

    applicants, employers = list(), list()

    for i in range(m):
        applicants.append(list(np.random.permutation(m)))
        employers.append(list(np.random.permutation(m)))

    return applicants, employers


# partitioned_preference = random_partition([1, 4, 5, 0, 2, 3], 3)
def random_partition(preference, k):

    isinstance(preference, list)
    isinstance(k, int)

    m = len(preference)
    partitioned_preference = list()

    split_positions = rd.sample(range(1, m), k-1)
    split_positions.sort()

    p = 0
    for i in split_positions:
        partitioned_preference.append(shuffle(preference[p:i]))
        p = i
    partitioned_preference.append(shuffle(preference[p:m]))

    return partitioned_preference


# partitioned_preferences = \
#   random_partition_preferences([[0, 2, 1], [1, 2, 0], [1, 2, 0]])
def random_partition_preferences(preferences):

    isinstance(preferences, list)

    m = len(preferences)
    partitioned_preferences = list()

    for p in preferences:
        partitioned_preferences.append(
                random_partition(p, rd.randint(1, m)))

    return partitioned_preferences
