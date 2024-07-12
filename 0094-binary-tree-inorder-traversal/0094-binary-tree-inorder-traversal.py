# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder Traversal: left -> root -> right
class Solution(object):
    def run(self, root, result):
        if root:
            self.run(root.left, result)
            result.append(root.val)
            self.run(root.right, result)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        answer = []
        self.run(root, answer)

        return answer
