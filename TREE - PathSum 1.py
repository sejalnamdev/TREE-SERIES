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


class Sol:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True

        remaining = targetSum - root.val

        rightSum = self.hasPathSum(root.right, remaining)
        leftSum = self.hasPathSum(root.left, remaining)

        if leftSum or rightSum:
            return True

        return False


a = list(map(int,input().split()))
targetSum = int(input())
root = buildtree(a)
s = Sol()
print(s.hasPathSum(root, targetSum))

            