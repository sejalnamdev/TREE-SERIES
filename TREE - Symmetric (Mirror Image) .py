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
    q =  deque([root])
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
    def symmetric( self,node1, node2):

        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False

        r1 = self.symmetric(node1.left, node2.right)
        r2 = self.symmetric(node1.right, node2.left)

        return r1 and r2

    #def isSymmetric(self, root):
    #    return self.symmetric(root.left, root.right)


a = list(map(int, input().split()))
root = buildtree(a)

s = sol()

#print(s.isSymmetric(root))
print(s.symmetric(root.left, root.right))
    


        


