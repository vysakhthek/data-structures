from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for i in range(len(nums)):
            single_num ^= nums[i]
        return single_num

if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,1]
    print(f"Single number in {nums} is {sol.singleNumber(nums)}")
    nums = [4,1,2,1,2]
    print(f"Single number in {nums} is {sol.singleNumber(nums)}")
    nums = [1]
    print(f"Single number in {nums} is {sol.singleNumber(nums)}")