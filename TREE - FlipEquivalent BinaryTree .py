from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
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

        if a[i] is not -1:
            node.left = TreeNode(a[i])
            q.append(node.left)
        i += 1

        if i < len(a) and a[i] is not -1:
            node.right = TreeNode(a[i])
            q.append(node.right)
        i += 1

    return root

class sol:
    def flipequivalent(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val is not root2.val:
            return False

        Normal = (
            self.flipequivalent(root1.left, root2.left) and 
            self.flipequivalent(root1.right, root2.right)
            )

        Flipped = (
            self.flipequivalent(root1.left, root2.right) and
            self.flipequivalent(root1.right, root2.left)
            )

        return Normal or Flipped


a = list(map(int, input().split()))
b = list(map(int, input().split()))

root1 = buildtree(a)
root2 = buildtree(b)

s = sol()
print(s.flipequivalent(root1, root2))