# -*- coding: utf-8 -*-
from tools import utils

def is_stable_matching(matching_a, matching_e, u_applicant, u_employer):
    isinstance(matching_a, list)
    isinstance(matching_e, list)

    m = len(matching_a)

    rank = list()
    for i in range(m):
        rank.append(utils.list_to_rank(u_applicant[i], m))

    for employer in range(m):
        for i in range(m):
            alternatives = u_employer[employer][i]

            if alternatives == matching_e[employer]:
                break

            matched_employer = matching_a[alternatives]
            if rank[alternatives][employer] < \
                    rank[alternatives][matched_employer]:
                return False

    return True
