class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix_sum = 0 # sum from the beginning up to the current point

        prefix_count = {0 : 1} # stores how many times each prefix sum has appeared before.

        for num in nums:
            prefix_sum += num
            needed = prefix_sum - k

            if needed in prefix_count:
                answer += prefix_count[needed]
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1
        return answer