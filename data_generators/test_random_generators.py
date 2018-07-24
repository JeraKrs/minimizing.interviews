# -*- coding: utf-8 -*-

import unittest

from random_generators import *

class TestRandomGeneratorsFunc(unittest.TestCase):
    def test_random_preferences(self):
        """Test method random_preferences(m)"""

        self.assertEqual(([], []), random_preferences(0),
                "random_preferences is failed in m = 0")
        self.assertEqual(([], []), random_preferences(-1),
                "random_preferences is failed in m < 0")
        self.assertIsInstance(random_preferences(2), tuple,
                ("random_preferences is failed since the type"
                " of return variable is incorrect"))

        a, e = random_preferences(3)
        self.assertIsInstance(a, list,
                ("random_preferences is failed since the type"
                " of return variable is incorrect"))
        self.assertIsInstance(e, list,
                ("random_preferences is failed since the type"
                " of return variable is incorrect"))
        self.assertEqual(3, len(a),
                ("random_preferences is failed since the size"
                " of return variable is incorrect"))
        self.assertEqual(3, len(e),
                ("random_preferences is failed since the size"
                " of return variable is incorrect"))

    def test_random_partition(self):
        """Test method random_partition(preference, m)"""
        preference = [1, 4, 5, 0, 2, 3]
        partitioned_preference = random_partition(preference, 3)

        self.assertEqual([1, 4, 5, 0, 2, 3], preference,
                ("random_partition is failed since it"
                " changed the input variable"))
        self.assertEqual(3, len(partitioned_preference),
                ("random_partition is failed since the size"
                " of return variable is incorrect"))

    def test_random_partition_preferences(self):
        """Test method preferences(preferences)"""
        preferences = [[0, 2, 1], [1, 2, 0], [1, 2, 0]]
        partitioned_preferences = \
                random_partition_preferences(preferences)

        self.assertEqual([[0, 2, 1], [1, 2, 0], [1, 2, 0]],
                preferences, ("random_partition_preferences is"
                " failed since it changed the input variable"))
        self.assertEqual(3, len(partitioned_preferences),
                ("random_partition_preferences is failed since"
                " the size of return variable is incorrect"))


if __name__ == '__main__':
    unittest.main()
