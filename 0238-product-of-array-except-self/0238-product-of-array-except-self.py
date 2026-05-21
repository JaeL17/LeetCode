class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # First pass: store product of all numbers to the left
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Second pass: multiply by product of all numbers to the right
        right_product = 1
        for i in range(n):
            answer[n-i-1] *= right_product
            right_product *= nums[n-i-1] 
            

        return answer