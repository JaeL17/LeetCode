# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        counter: dict[int, List[int]] = dict()
        

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
        answer = [1] * len(counter)
        for idx, vals in counter.items():
            answer[idx] = vals
        return answer