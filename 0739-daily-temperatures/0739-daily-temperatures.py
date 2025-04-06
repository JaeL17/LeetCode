from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = [] # store indicies

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx

            stack.append(i)

        return answer
   