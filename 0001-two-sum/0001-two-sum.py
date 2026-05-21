
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in dict_:
                return [i, dict_[needed]]
            else:
                dict_[nums[i]] = i
       

        