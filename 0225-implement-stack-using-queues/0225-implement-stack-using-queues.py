class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        queue_temp = self.queue[::-1]
        x = queue_temp.pop(0)
        self.queue = queue_temp[::-1]
        return x

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()