class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
        # return [nums[x] for x in nums]
        