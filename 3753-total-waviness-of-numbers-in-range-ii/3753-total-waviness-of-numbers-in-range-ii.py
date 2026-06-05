from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count_up_to(num: int) -> int:
            if num <= 0:
                return 0

            digits = list(map(int, str(num)))
            n = len(digits)

            @lru_cache(None)
            def dfs(
                index: int,
                tight: bool,
                started: bool,
                prev_prev: int,
                prev: int
            ) -> tuple[int, int]:
                """
                Return:
                (count_numbers, total_waviness)

                count_numbers = how many valid numbers can be formed
                total_waviness = total waviness from those numbers
                """

                if index == n:
                    return 1, 0

                limit = digits[index] if tight else 9

                total_count = 0
                total_wave = 0

                for digit in range(limit + 1):
                    next_tight = tight and digit == limit

                    # Still skipping leading zeros
                    if not started and digit == 0:
                        count, wave = dfs(
                            index + 1,
                            next_tight,
                            False,
                            -1,
                            -1
                        )
                        total_count += count
                        total_wave += wave
                        continue

                    # First real digit
                    if not started:
                        count, wave = dfs(
                            index + 1,
                            next_tight,
                            True,
                            -1,
                            digit
                        )
                        total_count += count
                        total_wave += wave
                        continue

                    # We already have at least one digit.
                    # Add current digit and maybe evaluate prev.
                    extra_wave = 0

                    if prev_prev != -1:
                        if prev > prev_prev and prev > digit:
                            extra_wave = 1
                        elif prev < prev_prev and prev < digit:
                            extra_wave = 1

                    count, wave = dfs(
                        index + 1,
                        next_tight,
                        True,
                        prev,
                        digit
                    )

                    total_count += count
                    total_wave += wave + extra_wave * count

                return total_count, total_wave

            return dfs(0, True, False, -1, -1)[1]

        return count_up_to(num2) - count_up_to(num1 - 1)