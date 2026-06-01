from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer: List[int] = [0] * len(temperatures)
        stack: List[int] = []

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                previous_day = stack.pop()
                answer[previous_day] = i - previous_day

            stack.append(i)

        return answer