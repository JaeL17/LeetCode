class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        list_sum: int = sum(nums)
        answer : List[int] = []
        left_sum = 0

        for i in range(len(nums)):
            right_sum = list_sum - nums[i] - left_sum
            answer.append(abs(left_sum - right_sum))
            left_sum += nums[i]

        return answer
        