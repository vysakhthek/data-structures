from typing import List

class SolutionBrute:
    def sumRange(slef, nums: List, left: int, right: int) -> List:
        sum = 0
        for i in range(left, right+1):
            sum += nums[i]
        return sum
    

class NumArray:
    def __init__(self, nums: List[int]):
        self.rangeSum = nums
        for i in range(1, len(nums)):
            self.rangeSum[i] += self.rangeSum[i-1] 

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.rangeSum[right]
        return self.rangeSum[right] - self.rangeSum[left-1]

if __name__ == "__main__":
    # numArray = NumArray([-2, 0, 3, -5, 2, -1])
    # print(f"Sum of elements between indices 0 and 2: {numArray.sumRange(0, 2)}")  # Output: 1
    # print(f"Sum of elements between indices 2 and 5: {numArray.sumRange(2, 5)}")  # Output: -1
    # print(f"Sum of elements between indices 0 and 5: {numArray.sumRange(0, 5)}")  # Output: -3

    sol = SolutionBrute()
    nums = [-2, 0, 3, -5, 2, -1]
    sum = sol.sumRange(nums, 0, 2)
    print(sum)
    sum = sol.sumRange(nums,2,5)
    print(sum)
    sum = sol.sumRange(nums,0,5)
    print(sum)