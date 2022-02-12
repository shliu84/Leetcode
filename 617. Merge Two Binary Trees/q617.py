# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # https://www.youtube.com/watch?v=QHH6rIK3dDQ ######
        if  not root1 and not root2:
            return None
        
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        
        root = TreeNode(v1 + v2)
        root.left = self.mergeTrees(root1.left if root1 else 0, root2.left if root2 else 0)
        root.right = self.mergeTrees(root1.right if root1 else 0, root2.right if root2 else 0)
        
        return root
        ####################################################

#         def addNodesVal(node1, node2):
#             node3 = TreeNode()
#             if node1.val != None:
#                 if node2.val != None:
#                     node3.val = node1.val + node2.val
#                 else:
#                     node3.val = node1.val
#             elif node2.val !=none:
#                 node3.val = node2.val
#             else:
#                 return None
#             return node3
        
#         def addNodes(node1, node2):
#             if node1 == None and node2 == None:
#                 return None
#             if node1 == None:
#                 return node2
#             if node2 == None:
#                 return node1
            
#             node3 = TreeNode(addNodesVal(node1,node2), addNodes(node1.left,node2.left), addNodes(node1.right,node2.right))
            

            
#             return node3
        
#         return addNodes(root1, root2)
    