import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": operator.add,
                     "-": operator.sub,
                     "*": operator.mul,
                     "/": operator.truediv}
        for char in tokens:
            if char in operators.keys():
                num1 = stack.pop()
                num2 = stack.pop()
                operation_result = operators[char](num2, num1)
                # print(num1, num2, char, int(operation_result))
                stack.append(int(operation_result))
            else:
                stack.append(int(char))

        return stack[0]
                     

        
        