from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid

            # left / mid / right

            # left side is sorted:
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: # target is inside this half
                    right = mid -1
                else:
                    left = mid +1

            else: # right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
        return -1