

interviewed_number = 0
underlying_preference_lists = dict(applicant=None, employer=None)
underlying_preference_ranks = dict(applicant=None, employer=None)


def interview(applicant, employer, interviewed_ranks)

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

    applicant_viewed_rank[employer] = 0
    for i in range(m):
        if applicant_viewed_rank[i] == -1 or i == employer:
            continue
        elif underlying_preference_ranks['applicant'][i] > \
                underlying_preference_ranks['applicant'][employer]:
            applicant_viewed_rank[i] += 1
        else:
            applicant_viewed_rank[employer] += 1

    employer_viewed_rank[applicant] = 0
    for i in range(m):
        if employer_viewed_rank[i] == -1 or i == applicant:
            continue
        elif underlying_preference_ranks['employer'][i] > \
                underlying_preference_ranks['employer'][applicant]:
            employer_viewed_rank[i] += 1
        else:
            employer_viewed_rank[applicant] += 1


