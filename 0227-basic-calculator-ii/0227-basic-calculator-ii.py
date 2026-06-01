class Solution:
    def calculate(self, s: str) -> int:
        stack : List[int] = []
        current_num = 0
        operation = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            if (not char.isdigit() and char != " ") or i == len(s) - 1:
                if operation == "+":
                    stack.append(current_num)
                elif operation == "-":
                    stack.append(-current_num)
                elif operation == "*":
                    prev_num = stack.pop()
                    stack.append(prev_num * current_num)
                elif operation == "/":
                    prev_num = stack.pop()
                    stack.append(int(prev_num / current_num))

                current_num = 0
                operation = char

        return sum(stack)