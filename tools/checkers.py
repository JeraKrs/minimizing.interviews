# -*- coding: utf-8 -*-
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import numpy as np

from tools import utils
from data_accessors.interview import interview


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


def count_blocking_pairs(matching_a, matching_e, u_applicant, u_employer):
    isinstance(matching_a, list)
    isinstance(matching_e, list)

    m = len(matching_a)
    c = 0

    rank = list()
    for i in range(m):
        rank.append(utils.list_to_rank(u_applicant[i], m))

    for employer in range(m):
        if employer == -1:
            c += 1
            continue

        for i in range(m):
            alternatives = u_employer[employer][i]

            if alternatives == matching_e[employer]:
                break

            matched_employer = matching_a[alternatives]
            if matched_employer < 0 or rank[alternatives][employer] < \
                    rank[alternatives][matched_employer]:
                c += 1
                break
    return c


def gs_checker(m, c):

    ranks = dict(applicant=list(), employer=list())
    for i in range(m):
        ranks['applicant'].append(utils.minusones(m))
        ranks['employer'].append(utils.minusones(m))

    samples = list()
    for i in range(m):
        for j in range(m):
            samples.append((i, j))

    for i in np.random.choice(range(m*m), c, replace=False):
        applicant = int(i/m)
        employer = int(i%m)
        interview(applicant, employer,
            dict(applicant=ranks['applicant'][applicant],
                employer=ranks['employer'][employer]))

    matching_a, matching_e = utils.minusones(m), utils.minusones(m)
    position = utils.initlists(m, 0)

    applicant_lists = list()
    for i in range(m):
        applicant_lists.append(
                utils.rank_to_list(ranks['applicant'][i]))

    def find_unmatched():
        for i in range(m):
            if matching_a[i] == -1 and \
                    position[i] < len(applicant_lists[i]):
                return i
        return -1

    while True:
        applicant = find_unmatched()
        if applicant == -1:
            break
        
        s = position[applicant]
        for i in range(s, len(applicant_lists[applicant])):
            employer = applicant_lists[applicant][i]
            position[applicant] = i + 1
            if matching_e[employer] == -1:
                matching_e[employer] = applicant
                matching_a[applicant] = employer
                break
            elif ranks['employer'][employer][matching_e[employer]] > \
                    ranks['employer'][employer][applicant]:
                matching_a[matching_e[employer]] = -1
                matching_e[employer] = applicant
                matching_a[applicant] = employer
                break

    return matching_a, matching_e
