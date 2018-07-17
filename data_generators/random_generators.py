import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import numpy as np
import random as rd

from utils.utils import shuffle


# [applicants, employers] = random_preferences(5)
def random_preferences(m):

    isinstance(m, int)

    applicants = list()
    employers = list()

    for i in range(m):
        applicants.append(list(np.random.permutation(m)))

    for i in range(m):
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


def random_partition_preferences(preferences):
    m = len(preferences)
    partitioned_preferences = list()

    for p in preferences:
        partitioned_preferences.append(
                random_partition(p, rd.randint(1, m)))

    return partitioned_preferences
