# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # space complexity : O(n), store n values
        counter: dict[int, List[int]] = dict()
        
        # time complexity: O(n). there are n nodes to visit.
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return

            if depth in counter:
                counter[depth].append(node.val)
            else:
                counter[depth] = [node.val]

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root,0)

        # Time: O(h), where h is number of levels.
        answer = [1] * len(counter)

        # Time: O(h), where h is number of levels.
        for idx, vals in counter.items():
            answer[idx] = vals
        return answer