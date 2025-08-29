from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

# Test cases
solution = Solution()

print(solution.findDuplicate([1, 3, 4, 2, 2]))
print(solution.findDuplicate([3, 1, 3, 4, 2]))
print(solution.findDuplicate([3, 3, 3, 3, 3]))
print(solution.findDuplicate([2, 1, 4, 3, 2]))
print(solution.findDuplicate([5, 4, 3, 2, 1, 5]))