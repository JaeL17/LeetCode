
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter: dict[int, int] = dict()
        for num in nums:
            if num in counter:
                return True
            else:
                counter[num] = 0
        
        return False

        # return len(nums) != len(set(nums))
        