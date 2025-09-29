from typing import List
import unittest

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for i in range(len(accounts)):
            for j in range(1, len(accounts[0])):
                accounts[i][j] += accounts[i][j-1]
        
        max_wealth = max([max(row) for row in accounts])
        return max_wealth
    
class TestSolution(unittest.TestCase):
    def test_maximum_wealth(self):
        sol = Solution()
        self.assertEqual(sol.maximumWealth([[1,2,3],[3,2,1]]), 6)
        self.assertEqual(sol.maximumWealth([[1,5],[7,3],[3,5]]), 10)
        self.assertEqual(sol.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]), 17)

if __name__ == "__main__":
    unittest.main()