class Solution:
    def calculate(self, s: str) -> int:
        stack: List[int] = []
        operation = "+"
        current_num = 0

        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num*10 + int(char) # digit shifting to get number that is more than one digit

            if (not char.isdigit() and char != " ") or i == len(s) - 1:
                if operation == "+":
                    stack.append(int(current_num))
                elif operation == "-":
                    stack.append(-int(current_num))
                elif operation == "*":
                    prev_integer = stack.pop()
                    stack.append(prev_integer * int(current_num))
                elif operation == "/":
                    prev_integer = stack.pop()
                    stack.append(int(prev_integer / current_num))
                operation = char
                current_num = 0                
        return sum(stack)