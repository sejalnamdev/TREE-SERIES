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
    def lowestcountancestor(self, root, p, q):
        if root is None or root.val == p or root.val == q:
            return root

        left = self.lowestcountancestor(root.left, p, q)
        right = self.lowestcountancestor(root.right, p, q)

        if left and right:
            return root
        
        return left or right

        


a = list(map(int, input().split()))
root = buildtree(a)
p = int(input())
q = int(input())


s = sol()
ans = s.lowestcountancestor(root, p, q)

if ans:
    print(ans.val)
else:
    print(None)

    