from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

nums1 = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums1)
print(nums1)

nums2 = [2, 0, 1]
Solution().sortColors(nums2)
print(nums2)

nums3 = [0]
Solution().sortColors(nums3)
print(nums3)

nums4 = [1, 2, 0]
Solution().sortColors(nums4)
print(nums4)

nums5 = [2, 2, 2, 1, 1, 0, 0]
Solution().sortColors(nums5)
print(nums5)