# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = deque()
        stack.append((root, False)) # push (root node, visited state) to the stack.
        while stack:
            curr, visited = stack.pop()
            if curr: # if the node exists
                if visited:
                    answer.append(curr.val)
                else:
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))
                    stack.append((curr, True))


        return answer
        