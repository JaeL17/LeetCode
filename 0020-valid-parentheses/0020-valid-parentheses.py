class Solution:
    def isValid(self, s: str) -> bool:
        pare_dict: dict = {")" : "(", 
                           "}" : "{",
                           "]" : "["}
        stack: List[str] = []

        # for loop: O(n)
        for par in s:
            if par in pare_dict and stack: # if par is a closing parentheses
                last_par = stack.pop() # O(1)
                if last_par != pare_dict[par]:
                    return False
            else:
                stack.append(par) # O(1)
        
        return True if len(stack) == 0 else False
        