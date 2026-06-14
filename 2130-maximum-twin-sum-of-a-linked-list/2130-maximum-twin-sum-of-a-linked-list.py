# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        counter: int = 0
        value_dict: dict[int, int] = {}
        node = head

        while node:
            value_dict[counter] = node.val
            node = node.next
            counter += 1

        max_sum = float("-inf")

        for i in range(counter // 2):
            max_sum = max(max_sum, value_dict[i] + value_dict[counter - 1 - i])

        return max_sum