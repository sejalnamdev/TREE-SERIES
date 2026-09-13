
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
    def sumNumbers(self, root):
        if not root:
            return 0

        return self.dfs(root, 0)

    def dfs(self, root, currentnumbers):
        if not root:
            return 0

        currentnumbers = currentnumbers*10 + root.val

        if root.left is None and root.right is None:
            return currentnumbers

        leftsidenumbers = self.dfs(root.left, currentnumbers)
        rightsidenumbers = self.dfs(root.right, currentnumbers)

        return leftsidenumbers + rightsidenumbers 

a = list(map(int,input().split()))
root = buildtree(a)
s = Solution()
print(s.sumNumbers(root))