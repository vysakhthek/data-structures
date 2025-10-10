from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        current_energy = energy[:]
        for i in range(len(energy) - k - 1, -1, -1):
            current_energy[i] += current_energy[i + k]
        return max(current_energy)

        # n = len(energy)
        # current_energy = [0] * n
        # max_energy = float('-inf')

        # for i in range(n - 1, -1, -1):
        #     if i + k < n:
        #         current_energy[i] = energy[i] + current_energy[i + k]
        #     else:
        #         current_energy[i] = energy[i]
        #     max_energy = max(max_energy, current_energy[i])

        # return max_energy

#brute force
# class Solution:
#     def maximumEnergy(self, energy: List[int], k: int) -> int:
#         max_energy = []
#         for i in range(len(energy)):
#             current_energy = energy[i]
#             for j in range(i+k, len(energy), k):
#                 current_energy += energy[j]
#             max_energy.append(current_energy)
#         return max(max_energy)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumEnergy([5,2,-10,-5,1], 3))
    print(sol.maximumEnergy([-2,-3,-1], 2))
    