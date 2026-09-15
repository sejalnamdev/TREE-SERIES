from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildtree(a):
    if a is None or a[0] == -1:
        return None

    root = TreeNode(a[0])
    q = deque([root])
    i = 1

    while q and i < len(a):
        node = q.popleft()

        if a[i] != -1:
            node.left = TreeNode(a[i])
            q.append(node.left)

        i += 1

        if i < len(a) and a[i] != -1:
            node.right = TreeNode(a[i])
            q.append(node.right)

        i += 1

    return root


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = [0]

        def fun(root):
            if not root:
                return 0

            left = fun(root.left)
            right = fun(root.right)

            res[0] = max(res[0], left + right)

            return 1 + max(left, right)

        fun(root)
        return res[0]


a = list(map(int,input().split()))
root = buildtree(a)
s = Solution()
print(s.diameterOfBinaryTree(root))


            