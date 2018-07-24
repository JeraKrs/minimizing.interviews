# -*- coding: utf-8 -*-
import unittest

from utils import *


class TestUtilsFunc(unittest.TestCase):
    def test_minusones(self):
        """Test method minusones(m)"""
        self.assertEqual([], minusones(0),
                "minusones is failed in m = 0")
        self.assertEqual([], minusones(-1),
                "minusones is failed in m < 0")
        self.assertEqual([-1, -1, -1], minusones(3),
                "minusones is failed in m > 0")

    def test_shuffle(self):
        """Test method shuffle(preferences)"""
        preferences = [1, 2, 3]
        random_preferences = shuffle(preferences)

        self.assertEqual([1, 2, 3], preferences,
                "shuffle is failed since it changed the input variable")
        self.assertIsInstance(random_preferences, list,
                "shuffle is failed since the return variable is not a list")
        self.assertEqual(3, len(random_preferences),
                "shuffle is failed since the size of return variable is incorrect")
        self.assertIn(1, random_preferences,
                "shuffle is failed since the element lose")
        self.assertIn(2, random_preferences,
                "shuffle is failed since the element lose")
        self.assertIn(3, random_preferences,
                "shuffle is failed since the element lose")
        

    def test_list_to_rank(self):
        """Test method list_to_rank(preference_list, m)"""
        preference_list = [2, 0, 1]
        list_to_rank(preference_list, 3)
        self.assertEqual([2, 0, 1], preference_list,
                "list_to_rank is failed since it changed the input variable")
        self.assertEqual([1, 2, 0], list_to_rank([2, 0, 1], 3),
                "list_to_rank is failed in full rank")
        self.assertEqual([2, 1, -1, 0, -1], list_to_rank([3, 1, 0], 5),
                "list_to_rank is failed in partitioned rank")

    def test_rank_to_list(self):
        """Test method rank_to_list(preference_rank)"""
        preference_rank = [1, 2, 0]
        rank_to_list(preference_rank)
        self.assertEqual([1, 2, 0], preference_rank,
                "rank_to_list is failed since it changed the input variable")
        self.assertEqual([2, 0, 1], rank_to_list([1, 2, 0]),
                "rank_to_list is failed in full rank")
        self.assertEqual([3, 1, 0], rank_to_list([2, 1, -1, 0, -1]),
                "rank_to_list is failed in partitioned rank")


if __name__ == '__main__':
    unittest.main()
