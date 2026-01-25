class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort() # python uses Timesort O(nlogn)
        n = len(nums) # Length look up so O(1)
        best = float('inf')
        for i in range(n - k + 1):
            best = min(best, nums[i+k-1]-nums[i])
        return best

        if k == 1:
            return 0

        sorted_list = sorted(nums)
        min_diff = sorted_list[-1] - sorted_list[0]
        for i in range(len(nums)):
            
            new_list = sorted_list[i:i+k]
            if len(new_list) < k:
                break
            min_diff = min(min_diff, new_list[-1] - new_list[0])

        return min_diff


        
        