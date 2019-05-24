from run import Solution
from unittest import TestCase


class ChairsTest(TestCase):

    def test_chairs_map_one(self):
        actual = Solution().min_swaps_couples([0, 2, 1, 3])
        self.assertEqual(1, actual)

    def test_chairs_map_one(self):
        actual = Solution().min_swaps_couples([3, 2, 0, 1])
        self.assertEqual(2, actual)

