from typing import List
import unittest

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink_bottle = numBottles
        while numBottles >= numExchange:
            exchanged_bottles = (numBottles // numExchange)
            drink_bottle += exchanged_bottles
            numBottles = (numBottles - (exchanged_bottles * numExchange)) + exchanged_bottles
        return drink_bottle
    
class TestSolution(unittest.TestCase):
    def test_num_water_bottles(self):
        sol = Solution()
        self.assertEqual(sol.numWaterBottles(9,3),13)

if __name__ == "__main__":
    unittest.main()