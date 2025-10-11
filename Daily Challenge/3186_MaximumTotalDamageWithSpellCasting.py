from typing import List
from collections import Counter

"""
    input -> array power
        each element -> damage of spell
        multiple spells -> same damage value
        cannot cast power[i]+-2
        each spell can be casty only once
    output -> max possible total damage
        
        
"""
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        damage_count = Counter(power)
        print(damage_count)
        spells = [(-10**9, 0)]  # dummy starter
        print(spells)

        # store (damage_value, frequency)
        for dmg in sorted(damage_count.keys()):
            spells.append((dmg, damage_count[dmg]))

        n = len(spells)
        dp = [0] * n   # dp[i] = max total damage up to i
        best_prev = 0  # best valid total from earlier non-conflicting spells
        left = 1       # sliding pointer

        for i in range(1, n):
            # move 'left' until difference > 2 (non-conflicting)
            while left < i and spells[left][0] < spells[i][0] - 2:
                best_prev = max(best_prev, dp[left])
                left += 1

            # include all spells of current damage type
            dp[i] = best_prev + spells[i][0] * spells[i][1]

        return max(dp)
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumTotalDamage([1,1,3,4]))
