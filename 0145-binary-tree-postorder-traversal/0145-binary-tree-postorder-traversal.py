# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result= []
        
        def dfs(node):
            if node is None:
                return
            dfs(node.left) # go as left as possible
            dfs(node.right) # go as right as possible
            result.append(node.val) # root
        dfs(root)
        return result
        