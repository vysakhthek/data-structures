from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j

if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = sol.removeDuplicates(nums)
    print(f"After removing duplicates: {nums[:k]}, new length: {k}")
    