# class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     count =0
    #     stack = [(0, 0)]

    #     while stack:
    #         idx, num = stack.pop()

    #         if idx < len(nums):
    #             stack.append((idx+1, num + nums[idx]))
    #             stack.append((idx+1, num - nums[idx]))
    #         if idx == len(nums) and num ==target:
    #             count +=1

    #     return count
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        stack = [(0, 0)]  # (index, current_sum)
        count = 0

        while stack:
            index, current_sum = stack.pop()

            if index == len(nums):
                if current_sum == target:
                    count += 1
            else:
                # Try adding the current number
                stack.append((index + 1, current_sum + nums[index]))
                # Try subtracting the current number
                stack.append((index + 1, current_sum - nums[index]))

        return count