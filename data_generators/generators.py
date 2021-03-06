# -*- coding: utf-8 -*-
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from data_generators.random_generators import \
        random_preferences, random_partition_preferences

def generate_partitioned_preferences(m, method="random"):

    if method == "random":
        [underlying_applicants, underlying_employers] = \
                random_preferences(m)
        partitioned_applicants = \
                random_partition_preferences(underlying_applicants)
        partitioned_employers = \
                random_partition_preferences(underlying_employers)

    return underlying_applicants, underlying_employers, \
            partitioned_applicants, partitioned_employers
