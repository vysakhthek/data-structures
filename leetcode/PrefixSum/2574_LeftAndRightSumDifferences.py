from typing import List

#Brute force Solution
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        left_sum = [0]*len(nums)
        right_sum = [0]*len(nums)
        for i in range(1, len(nums)):
                left_sum[i] = left_sum[i-1] + nums[i-1]
        for j in range(len(nums)-2, -1, -1):  
                right_sum[j] = right_sum[j+1] + nums[j+1]
        for k in range(len(nums)):
              answer[k] = abs(left_sum[k] - right_sum[k])

        return answer

if __name__ == "__main__":
    sol = Solution()
    answer= sol.leftRightDifference([10,4,8,3])
    print(answer)


class OptimizedSolution:
      def leftRightDifference(self, nums: List[int]) -> List[int]:
            output = []
            for i in range(len(nums)):
                  output.append((sum))
