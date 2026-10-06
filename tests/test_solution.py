import unittest
from solution import find_kth_largest

class TestKthLargest(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
        self.assertEqual(find_kth_largest([1], 1), 1)

if __name__ == "__main__":
    unittest.main()
