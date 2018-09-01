import numpy as np
import yaml

from algorithms.ks import heuristic_algorithm
from data_accessors.interview import init_data, get_count
from tools import checkers
from data_generators.mallow_generators import mallow_preferences


# read configs
with open("config_comparison.yaml", 'r') as stream:
    try:
        configs = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for key, val in configs.items():
    print("{}:{}".format(key, val))

n = configs.get("length", 0)
theta = configs.get("theta", 1)
case = configs.get("case", 0)

Ru_MUL, Ru_Random, Ri = 0, 0, 0

for i in range(case):
    u_applicant, u_employer = mallow_preferences(n, theta, "footrule")

    init_data(u_applicant, u_employer)
    result = heuristic_algorithm(n)

    a = checkers.count_blocking_pairs(result[0], result[1], u_applicant, u_employer)
    e = checkers.count_blocking_pairs(result[1], result[0], u_employer, u_applicant)
    Ru_MUL = Ru_MUL + (a + e) / (2*n)

    count = get_count()
    Ri = Ri + count / (n*n)

    result = checkers.gs_checker(n, count)
    a = checkers.count_blocking_pairs(result[0], result[1], u_applicant, u_employer)
    e = checkers.count_blocking_pairs(result[1], result[0], u_employer, u_applicant)
    Ru_Random = Ru_Random + (a + e) / (2*n)

print("Ru (MUL) = ", Ru_MUL / case)
print("Ru (Random) = ", Ru_Random / case)
print("Ri = ", Ri / case)
