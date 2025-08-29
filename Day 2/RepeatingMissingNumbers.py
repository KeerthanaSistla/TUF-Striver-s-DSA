from typing import List

class Solution:
    def findRepeatedAndMissing(self, nums: List[int]) -> List[int]:
        n = len(nums)
        Sn = n * (n + 1) // 2
        S2n = n * (n + 1) * (2 * n + 1) // 6

        S = sum(nums)
        S2 = sum(x * x for x in nums)

        diff = S - Sn
        sq_diff = S2 - S2n

        sum_xy = sq_diff // diff

        x = (diff + sum_xy) // 2
        y = x - diff

        return [x, y]

# Test cases
solution = Solution()

print(solution.findRepeatedAndMissing([1, 2, 2, 4]))
print(solution.findRepeatedAndMissing([3, 1, 3]))
print(solution.findRepeatedAndMissing([1, 5, 3, 2, 2, 6]))