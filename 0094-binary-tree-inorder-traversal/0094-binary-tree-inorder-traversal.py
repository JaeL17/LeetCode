from collections import deque
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer= []
        stack = deque()
        stack.append((root, False)) # push (root node, visited) to the stack
        
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    answer.append(curr.val)
                else:
                    stack.append((curr.right, False)) # push right node to the stack
                    stack.append((curr, True)) # push current node to the stack
                    stack.append((curr.left, False)) # push left note to the stack

        return answer
        