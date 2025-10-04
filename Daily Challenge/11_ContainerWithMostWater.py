from typing import List
import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area_height = min(height[left], height[right])
            width = right - left
            max_area = max(max_area, area_height*width)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1

        return max_area

class TestSolution(unittest.TestCase):
    def test_max_area(self):
        sol = Solution()
        self.assertEqual(sol.maxArea([1,8,6,2,5,4,8,3,7]), 49)

if __name__ == "__main__":
    unittest.main()

#brute force
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         area = 0
#         for i in range(len(height)):
#             width = 1
#             for j in range(i+1, len(height)):
#                 area_height = min(height[i], height[j])
#                 new_area = area_height * width
#                 if new_area > area:
#                     area = new_area
#                 width += 1
#         return area
