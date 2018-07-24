# -*- coding: utf-8 -*- 
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from tools import utils


interviewed_number = -1
underlying_preference_lists = dict(applicant=None, employer=None)
underlying_preference_ranks = dict(applicant=None, employer=None)


def init_data(u_applicant, u_employer):
    global interviewed_number
    global underlying_preference_lists
    global underlying_preference_ranks

    isinstance(u_applicant, list)
    isinstance(u_employer, list)

    m = len(u_applicant)
    interviewed_number = 0
    underlying_preference_lists['applicant'] = u_applicant
    underlying_preference_lists['employer'] = u_employer

    applicant_ranks, employer_ranks = list(), list()
    for i in range(m):
        applicant_ranks.append(utils.list_to_rank(u_applicant[i], m))
        employer_ranks.append(utils.list_to_rank(u_employer[i], m))

    underlying_preference_ranks['applicant'] = applicant_ranks
    underlying_preference_ranks['employer'] = employer_ranks


def get_count():
    global interviewed_number
    return interviewed_number


def interview(applicant, employer, interviewed_ranks):
    global interviewed_number
    global underlying_preference_lists
    global underlying_preference_ranks
    # print("applicant {}, employer {}".format(applicant, employer))

    # Error checking
    isinstance(applicant, int)
    isinstance(employer, int)
    isinstance(interviewed_ranks, dict)

    applicant_viewed_rank = interviewed_ranks['applicant']
    employer_viewed_rank = interviewed_ranks['employer']

    isinstance(applicant_viewed_rank, list)
    isinstance(employer_viewed_rank, list)

    if applicant_viewed_rank[employer] != -1 or \
            employer_viewed_rank[applicant] != -1:
        raise RuntimeError('interview error')

    # Update the rank by the result of interview
    m = len(applicant_viewed_rank)
    interviewed_number += 1

    r_applicant = underlying_preference_ranks['applicant'][applicant]
    r_employer = underlying_preference_ranks['employer'][employer]

    applicant_viewed_rank[employer] = 0
    for i in range(m):
        if applicant_viewed_rank[i] == -1 or i == employer:
            continue
        elif r_applicant[i] > r_applicant[employer]:
            applicant_viewed_rank[i] += 1
        else:
            applicant_viewed_rank[employer] += 1

    employer_viewed_rank[applicant] = 0
    for i in range(m):
        if employer_viewed_rank[i] == -1 or i == applicant:
            continue
        elif r_employer[i] > r_employer[applicant]:
            employer_viewed_rank[i] += 1
        else:
            employer_viewed_rank[applicant] += 1
