# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_track: dict[int, Optional[TreeNode]] = {}
        child_nodes: set[int] = set()

        for des in descriptions:
            
            # check there is parent node
            if des[0] not in node_track:
                node_track[des[0]] = TreeNode(val = des[0])
              
            parent_node = node_track[des[0]]

            # check there is child node
            if des[1] not in node_track:
                node_track[des[1]] = TreeNode(val = des[1])
            
            child_node = node_track[des[1]]
            
            # check left or right
            if des[2] == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            node_track[des[0]] = parent_node
            child_nodes.add(des[1])
            
            # if not root_node or (root_node.val == child_node.val):
            #     root_node = parent_node


        for key in node_track.keys():
            if key not in child_nodes:
                return node_track[key]

        return None


        