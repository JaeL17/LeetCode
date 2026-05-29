class Solution:
    def minElement(self, nums: List[int]) -> int:
        answer: List[int] = []

        def digit_sum(num: int) -> int:
            num_str = str(num)
            digit_sum = 0
            for num_char in num_str:
                num_int = int(num_char)
                digit_sum += num_int % 10

            return digit_sum

        # O (n * m), n is the length of input list: nums, m is the length of total digits in the input list
        for num in nums:
            answer.append(digit_sum(num))

        return min(answer)
        