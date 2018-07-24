# -*- coding: utf-8 -*- 
import os, sys                                                                                                                
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

import numpy as np
import queue

from data_accessors.interview import interview
from tools.utils import rank_to_list, minusones


def remove_available(applicant, employer, available, p_applicant):
    l = 0
    n = len(p_applicant)

    while l < n and employer not in p_applicant[l]:
        l = l + 1
    l = l + 1

    while l < n:
        for i in p_applicant[l]:
            available[i][applicant] = 1
        l = l + 1


def Lazy_Gale_Shapley(m, p_applicant, p_employer):

    available = np.zeros([m, m])
    matching_a, matching_e = minusones(m), minusones(m)

    interviewed_rank = dict()
    interviewed_level = dict()

    applicants_ranks = dict()
    for i in range(m):
        applicants_ranks[i] = minusones(m)


    unmatched = m
    while unmatched:
        # get a unmatched employer
        employer = matching_e.index(-1)

        q = interviewed_rank.get(employer, queue.Queue())
        interviewed_rank[employer] = q

        while matching_e[employer] == -1:

            while q.qsize() == 0:
                l = interviewed_level.get(employer, 0)
                interviewed_level[employer] = l + 1

                undetermined_rank = minusones(m)
                for i in p_employer[employer][l]:
                    if available[employer][i] == 1:
                        continue
                    interview(i, employer, \
                            dict(applicant=applicants_ranks[i], employer=undetermined_rank))

                undetermined_list = rank_to_list(undetermined_rank)
                for i in undetermined_list:
                    q.put(i)


            applicant = q.get()
            pre_matched = matching_a[applicant]
            rank = applicants_ranks.get(applicant)

            if pre_matched == -1 or \
                    rank[employer] < rank[pre_matched]:
                matching_a[applicant] = employer
                matching_e[employer] = applicant

                if pre_matched != -1:
                    matching_e[pre_matched] = -1
                else:
                    unmatched -= 1

                remove_available(applicant, employer, available, p_applicant[applicant])

    return matching_a, matching_e
