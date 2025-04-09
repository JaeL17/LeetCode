# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # post oroder traversal: left -> right -> middle
        answer = []
        stack = deque()
        stack.append((root, False)) # push (root node, visited_state) to the stack

        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    answer.append(curr.val)
                else:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))


        return answer

        