from typing import List
import unittest

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk_bottles = numBottles
        empty_bottles = numBottles
        while empty_bottles >= numExchange:
            empty_bottles -= numExchange
            drunk_bottles += 1
            empty_bottles += 1
            numExchange += 1
        return drunk_bottles
    
class TestSolution(unittest.TestCase):
    def test_max_bottles_drink(self):
        sol = Solution()
        self.assertEqual(sol.maxBottlesDrunk(10, 3), 13)

if __name__ == "__main__":
    unittest.main()
    
