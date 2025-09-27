import unittest

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for ch in s + t:
            ans ^= ord(ch)

        return(chr(ans))
    
class TestSolution(unittest.TestCase):
    def test_find_the_difference(self):
        sol = Solution()
        self.assertEqual(sol.findTheDifference("abcd", "abcde"), "e")

if __name__ == "__main__":
    unittest.main()