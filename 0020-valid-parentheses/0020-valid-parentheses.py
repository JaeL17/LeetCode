from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # (), {}, []
        stack = deque()
        open_bracket = ["(", "[", "{"]
        close_bracket = [")", "]", "}"]
        check = {")": "(",
                 "}": "{",
                 "]": "["}
        for char in s:
            if char in open_bracket:
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

