from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # (), {}, []
        stack = deque()
        check = {")": "(",
                 "}": "{",
                 "]": "["}
        for char in s:
            if char not in check.keys():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                bracket = stack.pop()
                if bracket != check[char]:
                    return False
        
        if len(stack) ==0:
            return True
        else:
            return False

