# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val != subRoot.val:
            return False

        r1 = self.sameTree(root.left, subRoot.left)
        r2 = self.sameTree(root.right, subRoot.right)

        return r1 and r2

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False

        if subRoot is None:
            return True

        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True

        r1 = self.isSubtree(root.left, subRoot)
        r2 = self.isSubtree(root.right, subRoot)

        return r1 or r2
            

        

