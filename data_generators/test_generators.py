# -*- coding: utf-8 -*-
import unittest

from random_generators import *
from score_generators import *
from luce_generators import *
from bradley_terry_generators import *


class TestScoreGeneratorsFunc(unittest.TestCase):
    def test_gaussian_distribution(self):
        """Test method gaussian_distribution(m, sigma, mean)"""
        self.assertEqual([], gaussian_distribution(0),
                "gaussian_distribution is failed in m = 0")
        self.assertEqual([], gaussian_distribution(-1),
                "gaussian_distribution is failed in m = -1")
        self.assertIsInstance(gaussian_distribution(5, 2), list,
                ("gaussian_distribution is failed since the type"
                " of return variable is incorrect"))
        self.assertEqual(5, len(gaussian_distribution(5, 2)),
                ("gaussian_distribution is failed since the size"
                " of return variable is incorrect"))


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


class TestLuceGeneratorsFunc(unittest.TestCase):
    def test_luce_preferences(self):
        """Test method luce_preferences(m, sigma, mean)"""
        self.assertEqual(([], []), luce_preferences(0),
                "luce_preferences is failed in m = 0")
        self.assertEqual(([], []), luce_preferences(-1),
                "luce_preferences is failed in m = -1")
        self.assertIsInstance(luce_preferences(5, 2), tuple,
                ("luce_preferences is failed since the type"
                " of return variable is incorrect"))

        a, e = luce_preferences(5, 2)
        self.assertIsInstance(a, list,
                ("luce_preferences is failed since the type"
                " of return variable is incorrect"))
        self.assertIsInstance(e, list,
                ("luce_preferences is failed since the type"
                " of return variable is incorrect"))
        self.assertEqual(5, len(a),
                ("luce_preferences is failed since the size"
                " of return variable is incorrect"))
        self.assertEqual(5, len(e),
                ("luce_preferences is failed since the size"
                " of return variable is incorrect"))

    def test_luce_model(self):
        """Test method luce_model(scores)"""
        self.assertEqual([], luce_model([]),
                "luce_model is failed in scores = []")

        scores = [5.0, 4.5, 4.5, 3.0]
        rank = luce_model(scores)
        self.assertEqual([5.0, 4.5, 4.5, 3.0], scores,
                ("luce_model is failed since it"
                " changed the input variable"))
        self.assertEqual(4, len(rank),
                ("luce_mode is failed since the size"
                " of return variable is incorrect"))


class TestBradleyTerryGeneratorsFunc(unittest.TestCase):
    def test_bradley_terry_preferences(self):
        """Test method bradley_terry_preferences(m, sigma, mean)"""
        self.assertEqual(([], []), bradley_terry_preferences(0),
                "bradley_terry_preferences is failed in m = 0")
        self.assertEqual(([], []), bradley_terry_preferences(-1),
                "bradley_terry_preferences is failed in m = -1")
        self.assertIsInstance(bradley_terry_preferences(5, 2), tuple,
                ("bradley_terry_preferences is failed since the type"
                " of return variable is incorrect"))

        a, e = luce_preferences(5, 2)
        self.assertIsInstance(a, list,
                ("bradley_terry_preferences is failed since the type"
                " of return variable is incorrect"))
        self.assertIsInstance(e, list,
                ("bradley_terry_preferences is failed since the type"
                " of return variable is incorrect"))
        self.assertEqual(5, len(a),
                ("bradley_terry_preferences is failed since the size"
                " of return variable is incorrect"))
        self.assertEqual(5, len(e),
                ("bradley_terry_preferences is failed since the size"
                " of return variable is incorrect"))

    def test_bradley_terry_model(self):
        """Test method bradley_terry_model(scores)"""
        self.assertEqual([], bradley_terry_model([]),
                "bradley_terry_model is failed in scores = []")

        scores = [5.0, 4.5, 4.5, 3.0]
        rank = bradley_terry_model(scores)
        self.assertEqual([5.0, 4.5, 4.5, 3.0], scores,
                ("bradley_terry_model is failed since it"
                " changed the input variable"))
        self.assertEqual(4, len(rank),
                ("bradley_terry_model is failed since the size"
                " of return variable is incorrect"))



if __name__ == '__main__':
    unittest.main()
