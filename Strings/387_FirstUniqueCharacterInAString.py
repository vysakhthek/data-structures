from typing import List
import unittest

class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_count = {}
        for ch in s:
            string_count[ch] = string_count.get(ch, 0) + 1
            
        for idx, ch in enumerate(s):
            if string_count[ch] == 1:
                return idx

        return -1
    
class TestSolution(unittest.TestCase):
    def test_first_uniq_char(self):
        sol = Solution()
        self.assertEqual(sol.firstUniqChar("lovelivecode"), 5)

if __name__ == "__main__":
    unittest.main()