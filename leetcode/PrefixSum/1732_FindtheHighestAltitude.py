from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]*(len(gain)+1)
        altitude[1] = gain[0]
        gain_sum = 0
        for i in range(len(gain)):
            gain_sum += gain[i]
            altitude[i+1] = gain_sum
        return max(altitude)

if __name__ == "__main__":
    sol = Solution()
    answer= sol.largestAltitude([-4,-3,-2,-1,4,3,2])