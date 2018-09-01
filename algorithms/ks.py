# -*- coding: utf-8 -*- 
import os, sys                                                                                                                
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import numpy as np
import math

from data_accessors.interview import interview
from tools.utils import minusones, initlists, rank_to_list


START_SCORE = 100
K = 5

def get_threshold(n, m):
    return m * m / K
    # return (n + n / (m-1) * k) / (2*n)


def heuristic_interview(applicant, employer, scores, ranks, m, epsilon):
    interview(applicant, employer,
            dict(applicant=ranks['applicant'][applicant],
                employer=ranks['employer'][employer]))

    applicant_rank = ranks['employer'][employer][applicant]
    for i in range(m):
        c = ranks['employer'][employer][i]
        if c == -1 or i == applicant:
            continue
        elif c > applicant_rank:
            scores['applicant'][applicant] += epsilon
            scores['applicant'][i] -= epsilon
        else:
            scores['applicant'][applicant] -= epsilon
            scores['applicant'][i] += epsilon

    employer_rank = ranks['applicant'][applicant][employer]
    for i in range(m):
        c = ranks['applicant'][applicant][i]
        if c == -1 or i == employer:
            continue
        elif c > employer_rank:
            scores['employer'][employer] += epsilon
            scores['employer'][i] -= epsilon
        else:
            scores['employer'][employer] -= epsilon
            scores['employer'][i] += epsilon


def Gale_shapley(m, interviewed_ranks):
    matching_a, matching_e = minusones(m), minusones(m)
    position = initlists(m, 0)

    applicant_lists = list()
    for i in range(m):
        applicant_lists.append(
                rank_to_list(interviewed_ranks['applicant'][i]))

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
            elif interviewed_ranks['employer'][employer][matching_e[employer]] > \
                    interviewed_ranks['employer'][employer][applicant]:
                matching_a[matching_e[employer]] = -1
                matching_e[employer] = applicant
                matching_a[applicant] = employer
                break

    return matching_a, matching_e


def remove_possible(employer, matched, scores, tags, employer_ranks, m, k):
    if matched == -1:
        for i in range(m):
            tags[i][employer] = -1
        return

    cs = scores['applicant'][matched]
    # TODO
    threshold = (cs + k) / (2 * cs)
    for i in range(m):
        if employer_ranks[employer][i] != -1 or tags[i][employer] != -1:
            continue

        ts = scores['applicant'][i]
        if cs / (cs + ts) > threshold:
            tags[i][employer] = 0


def init_tags(m):
    tags = list()
    for i in range(m):
        tags.append(minusones(m))
    return tags


def heuristic_algorithm(m):

    epsilon = START_SCORE / (m*(m-1))
    threshold = get_threshold(START_SCORE, m)

    scores = dict(applicant=initlists(m, START_SCORE), \
            employer=initlists(m, START_SCORE))
    interviewed_ranks = dict(applicant=list(), employer=list())
    tags = init_tags(m)
    for i in range(m):
        interviewed_ranks['applicant'].append(minusones(m))
        interviewed_ranks['employer'].append(minusones(m))

    # initial step
    for i in range(m):
        heuristic_interview(i, i, scores, interviewed_ranks, m, epsilon)
        heuristic_interview(i, (i+1)%m, scores, interviewed_ranks, m, epsilon)

    matching_a, matching_e = Gale_shapley(m, interviewed_ranks)
    for i in range(m):
        remove_possible(i, matching_e[i], scores, tags, \
                interviewed_ranks['employer'], m, threshold * epsilon)

    def find_progress_applicant():
        for i in range(m):
            if matching_a[i] == -1:
                for j in range(m):
                    if interviewed_ranks['applicant'][i][j] == -1 and tags[i][j] == -1:
                        return i, j
            else:
                cs = scores['employer'][matching_a[i]]
                for j in range(m):
                    if interviewed_ranks['applicant'][i][j] == -1 \
                            and tags[i][j] == -1 and cs <= scores['employer'][j]:
                            # and tags[i][j] == -1 and cs - bias < scores['employer'][j]:
                        return i, j
        return -1, -1

    while True:
        pro_applicant, target = find_progress_applicant()
        if pro_applicant == -1:
            break

        heuristic_interview(pro_applicant, target, scores, \
                interviewed_ranks, m, epsilon)

        matching_a, matching_e = Gale_shapley(m, interviewed_ranks)
        for i in range(m):
            remove_possible(i, matching_e[i], scores, tags, \
                    interviewed_ranks['employer'], m, threshold * epsilon)

    return matching_a, matching_e
