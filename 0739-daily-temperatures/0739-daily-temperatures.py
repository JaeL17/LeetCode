from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer: List[int] = [0] * len(temperatures)
        stack: List[int] = []


        # O(n) time and space complexity
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day

            stack.append(i)

        return answer