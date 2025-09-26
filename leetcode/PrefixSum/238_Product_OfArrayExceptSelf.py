from typing import List
import unittest

def productExceptSelf(self, nums: List[int]) -> List[int]:
    nums_len = len(nums)
    output_array = [1]*nums_len

    for i in range(1, nums_len):
        output_array[i] = output_array[i-1] * nums[i-1]
    
    right_product = 1
    for j in range(nums_len-1, -1, -1):
        output_array[j] *= right_product
        right_product *= nums[j]

    return output_array


#test case using unittest
class TestSolution(unittest.TestCase):
    def test_product(self):
        self.assertEqual(productExceptSelf([1,2,3,4]), [24,12,8, 6])

if __name__ == "__main__":
    unittest.main()


# if __name__ == "__main__":
#     sol = Solution()
#     output_array = sol.productExceptSelf([1,2,3,4]) #[24, 12, 8, 6]
#     print(output_array)
             


#Brute force approach
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         nums_len = len(nums)

#         left = [1]*nums_len
#         right = [1]*nums_len
#         output_product_array = [1]*nums_len

#         for i in range(1, nums_len):
#             left[i] = left[i-1] * nums[i-1]
        
#         for j in range(nums_len-2, -1, -1):
#             right[j] = right[j+1] * nums[j+1]

#         for k in range(nums_len):
#             output_product_array[k] = left[k] * right[k]

#         return output_product_array
             