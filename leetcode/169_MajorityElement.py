from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
    
if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,3]
    print(f"Majority element in {nums} is {sol.majorityElement(nums)}")
    nums = [2,2,1,1,1,2,2]
    print(f"Majority element in {nums} is {sol.majorityElement(nums)}")