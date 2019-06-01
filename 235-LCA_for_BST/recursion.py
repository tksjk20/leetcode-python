# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return root
        p_path = self.find_path(root, p)
        q_path = self.find_path(root, q)
        p_set = set(p_path)
        for node in q_path[::-1]:
            if node in p_set:
                return node
            
    def find_path(self,root,target):
        path = [root]
        if root.val >target.val:
            path.extend(self.find_path(root.left,target))
        elif root.val < target.val:
            path.extend(self.find_path(root.right,target))
        return path