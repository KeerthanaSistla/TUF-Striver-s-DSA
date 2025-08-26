from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5,4,-1,7,8]))
print(s.maxSubArray([-1,-2,-3,-4]))
print(s.maxSubArray([1,2,3,4,5]))