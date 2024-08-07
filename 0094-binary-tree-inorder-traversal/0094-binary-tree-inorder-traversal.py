# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder Traversal: left -> root -> right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(root, answer):
            if root:
                traverse(root.left, answer)
                answer.append(root.val)
                traverse(root.right, answer)
        answer = []
        traverse(root, answer)
        return answer