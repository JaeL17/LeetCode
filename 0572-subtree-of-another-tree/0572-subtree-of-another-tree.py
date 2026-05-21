# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True

            if tree1 is None or tree2 is None:
                return False

            if tree1.val != tree2.val:
                return False
            
            return is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)

        target_val = subRoot.val
        def dfs(node):
            if node is None:
                return False

            if is_same_tree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
    

        return dfs(root)

        