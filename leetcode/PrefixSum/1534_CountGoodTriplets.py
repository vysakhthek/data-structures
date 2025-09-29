from typing import List
import unittest

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if (abs(arr[i] - arr[j]) <= a):
                    for k in range(j+1, len(arr)):
                        if (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                            count += 1

        return count
    

class TestSolution(unittest.TestCase):
    def test_count_good_triplets(self):
        sol = Solution()
        self.assertEqual(sol.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3), 4)

if __name__ == "__main__":
    unittest.main()