from typing import List
import unittest

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-3, -1, -1):
            if((nums[i] + nums[i+1]) > nums[i+2]):
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
    

class TestSolution(unittest.TestCase):
    def test_largest_perimeter(self):
        sol = Solution()
        self.assertEqual(sol.largestPerimeter([2,1,2]), 5)
        self.assertEqual(sol.largestPerimeter([1,2,1,10]), 0)

if __name__ == "__main__":
    unittest.main()