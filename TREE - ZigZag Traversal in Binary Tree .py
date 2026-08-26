# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([root])

        lefttoright = True

        while q:
            temp = []
            n = len(q)

            for i in range(n):
                node = q.popleft()
                temp.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if not lefttoright:
                temp.reverse()

            ans.append(temp)
            lefttoright = not lefttoright

        return ans

            
            
        
                




