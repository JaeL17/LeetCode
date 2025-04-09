
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x) # push in stack

    def pop(self) -> int:
        stack_temp = self.stack[::-1]
        x = stack_temp.pop()
        self.stack = stack_temp[::-1]
        return x
        
    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()