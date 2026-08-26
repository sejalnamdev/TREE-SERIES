from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(a):
    if not a or a[0] == -1:
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


class sol:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)


a = list(map(int, input("Tree 1: ").split()))
b = list(map(int, input("Tree 2: ").split()))

t1 = buildTree(a)
t2 = buildTree(b)

s = sol()
print(s.isSameTree(t1, t2))