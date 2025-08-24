from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
        
        nums[i + 1:] = reversed(nums[i + 1:])

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 3]
    print(f"Input: nums = {nums1}")
    solution.nextPermutation(nums1)
    print(f"Output: {nums1}\n")
    
    # Example 2
    nums2 = [3, 2, 1]
    print(f"Input: nums = {nums2}")
    solution.nextPermutation(nums2)
    print(f"Output: {nums2}\n")
    
    # Example 3
    nums3 = [1, 1, 5]
    print(f"Input: nums = {nums3}")
    solution.nextPermutation(nums3)
    print(f"Output: {nums3}")
