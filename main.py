from algorithms.lazy_gale_shapley import Lazy_Gale_Shapley
from data_generators.generators \
        import generate_partitioned_preferences
from tools import utils
from interview import interviewed_number, underlying_preference_lists, underlying_preference_ranks

m = 3
interviewed_number = 0

[u_applicant, u_employer, p_applicant, p_employer] = \
        generate_partitioned_preferences(m)

underlying_preference_lists['applicant'] = u_applicant
underlying_preference_lists['employer'] = u_employer

applicant_ranks = list()
employer_ranks = list()
for i in range(m):
    applicant_ranks.append(utils.list_to_rank(u_applicant[i], m))
    employer_ranks.append(utils.list_to_rank(u_employer[i], m))

underlying_preference_ranks['applicant'] = applicant_ranks
underlying_preference_ranks['employer'] = employer_ranks


[matching_a, matching_e] = Lazy_Gale_Shapley(m, p_applicant, p_employer)

print(u_applicant)
print(u_employer)

print(matching_a)
print(matching_e)
