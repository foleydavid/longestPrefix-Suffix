import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_combinationSum3(self):
        self.assertEqual(self.sol.longestPrefix("level"), "l")
        self.assertEqual(self.sol.longestPrefix("ababab"), "abab")
        self.assertEqual(self.sol.longestPrefix("leetcodeleet"), "leet")
        self.assertEqual(self.sol.longestPrefix("a"), "")

        long_str = ""
        for i in range(10_000):
            long_str += "a"
        long_ans = long_str[:len(long_str) - 1]

        self.assertEqual(self.sol.longestPrefix(long_str), long_ans)

if __name__ == "__main__":
    unittest.main()
