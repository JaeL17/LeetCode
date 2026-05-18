class MyStack:

    def __init__(self):
        self.input_queue = []
        self.output_queue = []
    # we need two queues because only one queue supports FIFO, but we need LIFO.

    def push(self, x: int) -> None:
        self.input_queue.append(x)

    def pop(self) -> int:
        
        while len(self.input_queue) > 1:
            self.output_queue.append(self.input_queue.pop(0))
        top_element = self.input_queue.pop(0)

        self.input_queue, self.output_queue = self.output_queue, self.input_queue
        return top_element

    def top(self) -> int:
        top_element = self.pop()
        self.input_queue.append(top_element)

        return top_element

    def empty(self) -> bool:
        return not self.input_queue and not self.output_queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()