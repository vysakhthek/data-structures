class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-(2*k)+1):
            first_ok = True
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1]:
                    first_ok = False
                    break

            second_ok = True
            for j in range(i + k, i + 2*k - 1):
                if nums[j] >= nums[j + 1]:
                    second_ok = False
                    break

            if first_ok and second_ok:
                return True

        return False

