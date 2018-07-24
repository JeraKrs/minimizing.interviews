 # -*- coding: utf-8 -*-
from copy import deepcopy
import numpy as np

def minusones(m):
    return [-1 for i in range(m)]


def shuffle(preferences):
    random_preferences = deepcopy(preferences)
    np.random.shuffle(random_preferences)
    return random_preferences


def list_to_rank(preference_list, m):
    preference_rank = minusones(m)
    for i in range(len(preference_list)):
        preference_rank[preference_list[i]] = i
    return preference_rank


def rank_to_list(preference_rank):
    m = len(preference_rank)
    n = max(preference_rank) + 1

    preference_list = list(np.zeros(n))
    for i in range(m):
        if preference_rank[i] == -1:
            continue
        preference_list[preference_rank[i]] = i

    return preference_list
