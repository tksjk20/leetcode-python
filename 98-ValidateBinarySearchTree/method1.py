# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 中序遍历方法，直观但是 相对慢一些
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.inorder(root)
        return inorder == sorted(list(set(inorder)))
    
    def inorder(self, root):
        if root is None:
            return[]
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)