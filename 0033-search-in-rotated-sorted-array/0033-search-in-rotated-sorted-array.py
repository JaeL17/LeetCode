from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_val_idx = 0

        for i, num in enumerate(nums):
            if num < nums[min_val_idx]:
                min_val_idx = i

        sorted_nums = nums[min_val_idx:] + nums[:min_val_idx]

        left = 0
        right = len(sorted_nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if sorted_nums[mid] == target:
                return (mid + min_val_idx) % len(nums)

            elif sorted_nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1