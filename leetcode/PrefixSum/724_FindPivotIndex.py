from typing import List
import unittest

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        for num in nums:
            right_sum += num
        
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1


class TestPivotIndex(unittest.TestCase):
    def test_pivot_index(self):
        sol=Solution()
        self.assertEqual(sol.pivotIndex([1,7,3,6,5,6]), 3)

if __name__ == "__main__":
    unittest.main()