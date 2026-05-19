class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node() # dummy head node with value of 0
        self.size = 0 # size of the linked list

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr_node = self.head.next

        for _ in range(index):
            curr_node = curr_node.next
        return curr_node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        if index < 0:
            index = 0

        prev_node = self.head

        # move prev to the node before index
        for _ in range(index):
            prev_node = prev_node.next

        new_node = Node(val)
        new_node.next = prev_node.next
        prev_node.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev_node = self.head
        
        for _ in range(index):
            prev_node = prev_node.next
        
        prev_node.next = prev_node.next.next
        self.size -=1

  

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)