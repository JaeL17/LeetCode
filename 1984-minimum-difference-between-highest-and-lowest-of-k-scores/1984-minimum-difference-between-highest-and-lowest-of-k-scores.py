class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort() # python uses Timesort O(nlogn)
        n = len(nums) # Length look up so O(1)
        best = float('inf')
        for i in range(n - k + 1):
            best = min(best, nums[i+k-1]-nums[i])
        return best


        
        