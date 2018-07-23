import numpy as np

def shuffle(preferences):
    np.random.shuffle(preferences)
    return preferences


def list_to_rank(preference_list, m):
    preference_rank = list(np.zeros(m) - 1)
    for i in range(m):
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
