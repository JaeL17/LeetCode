class Solution:
    def calculate(self, s: str) -> int:

        result: int = 0
        stack: List[int] = []
        sign: int = 1
        current_number: int = 0
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)

            elif char == "+":
                result += sign * current_number
                current_number = 0
                sign = 1

            elif char == "-":
                result += sign * current_number
                current_number = 0
                sign = -1

            elif char == "(":
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif char == ")":
                result += sign * current_number
                current_number = 0

                previous_sign = stack.pop()
                previous_result = stack.pop()

                result = previous_result + previous_sign * result

        result += sign * current_number
        return result