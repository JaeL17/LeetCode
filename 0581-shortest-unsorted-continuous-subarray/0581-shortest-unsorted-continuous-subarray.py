class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0
        
        # start and end index for two pointer methods
        max_val = float('-inf')
        min_val = float('inf')
        start = 0
        end = 0
        n = len(nums)

        for i in range(n):
            
            # updating end pointer
            max_val = max(max_val, nums[i])
            if nums[i] < max_val:
                end = i
                # min_val = nums[i]

            # updating start pointer
            j = n - 1 - i
            min_val = min(min_val, nums[j])
            if nums[j] >min_val:
                start = j
                # max_val = nums[j]
        return end - start +1
