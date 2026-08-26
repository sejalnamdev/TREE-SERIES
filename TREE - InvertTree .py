from collections import deque
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right 

def buildtree(a):
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
    def InvertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.InvertTree(root.left)
        self.InvertTree(root.right)

        return root

def printtree(root):
    if not root:
        return

    q = deque([root])

    while q:
        node = q.popleft()
        print(node.val, end=" ")

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

a = list(map(int, input().split()))
root = buildtree(a)

s = sol()
root = s.InvertTree(root)

printtree(root)
