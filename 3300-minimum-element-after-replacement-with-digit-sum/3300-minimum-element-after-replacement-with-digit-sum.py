class Solution:
    def minElement(self, nums: List[int]) -> int:
        answer = float('inf')

        def digit_sum(num: int) -> int:
            # num_str = str(num)
            # digit_sum = 0
            # for num_char in num_str:
            #     num_int = int(num_char)
            #     digit_sum += num_int % 10

            # at most 5 because 1 <= nums[i] <= 104
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        # O (n), n is the length of input list.
        for num in nums:
            answer = min(answer, digit_sum(num))

        return answer
        