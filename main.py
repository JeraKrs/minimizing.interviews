# -*- coding: utf-8 -*- 
from algorithms.lazy_gale_shapley import Lazy_Gale_Shapley
from data_generators.generators \
        import generate_partitioned_preferences
from data_accessors.interview import init_data, get_count
from tools import utils, checkers

m = 100

[u_applicant, u_employer, p_applicant, p_employer] = \
        generate_partitioned_preferences(m)

# u_applicant = [[1, 0, 2], [0, 1, 2], [0, 1, 2]]
# u_employer = [[0, 1, 2], [0, 2, 1], [0, 1, 2]]
# p_applicant = [[[0, 1], [2]], [[0, 1], [2]], [[0, 1], [2]]]
# p_employer = [[[0, 1], [2]], [[0, 2], [1]], [[0], [1, 2]]]

init_data(u_applicant, u_employer)

[matching_a, matching_e] = Lazy_Gale_Shapley(m, p_applicant, p_employer)


result = checkers.is_stable_matching(
        matching_a, matching_e, u_applicant, u_employer)
if result == False:
    print("u_applicant:{}".format(u_applicant))
    print("u_employer:{}".format(u_employer))

    print("p_applicant:{}".format(p_applicant))
    print("p_employer:{}".format(p_employer))

    print("matching_applicant:{}".format(matching_a))
    print("matching_employer:{}".format(matching_e))

print(result)
print(get_count())
