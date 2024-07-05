class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums[:]]
        
        res = []

        for _ in range(len(nums)):
            tar = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(tar)
            
            res.extend(perms)
            nums.append(tar)
        
        return res
            