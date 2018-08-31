import numpy as np
import yaml

from data_generators.score_generators import gaussian_distribution
from data_generators.luce_generators import luce_model
from data_generators.bradley_terry_generators import bradley_terry_model
from data_generators.mallow_generators import footrule, mallow_model
from tools.utils import list_to_rank, sort_by_score

# read configs
with open("config_generation.yaml", 'r') as stream:
    try:
        configs = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for key, val in configs.items():
    print("{}:{}".format(key, val))


# set configs
m = configs.get('length', 10)
n = configs.get('sample', 100)
model = configs.get('model', 'random')
theta = configs.get('theta', 1)
is_print = configs.get('print', False)

if model == "random":

    """Random Model for generating the permutation"""
    mu = list(np.random.permutation(m))
    permutations = list()
    for i in range(n):
        permutations.append(list(np.random.permutation(m)))

elif model == "luce":

    """Luce Model for generating the permutation"""
    scores = gaussian_distribution(m, theta*2, 5)

    mu = sort_by_score(scores)
    permutations = list()
    for i in range(n):
        permutations.append(luce_model(scores))

elif model == "bradley":

    """Bradley-Terry Model for generating the permutation"""
    scores = gaussian_distribution(m, theta*4, 5)
    mu = sort_by_score(scores)
    permutations = list()
    for i in range(n):
        permutations.append(bradley_terry_model(scores))

elif model == "mallows":
    """Mallows Model for generating the permutation"""
    mu = list(np.random.permutation(m))
    permutations = mallow_model(m, theta, mu, footrule, n)


dis = list()
for i in range(len(permutations)):
    r = permutations[i]
    dis.append(footrule(list_to_rank(mu, m), list_to_rank(r, m)) / m)

if is_print:
    print("preference lists:")
    for i in permutations:
        print('    ', i)

print("average distance =", dis)
