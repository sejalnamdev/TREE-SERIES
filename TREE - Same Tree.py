class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class sol:
    def isSameTree(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        r1 =  self.isSameTree(p.left, q.left)
        r2 =  self.isSameTree(p.right, q.right)

        return r1 and r2

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)

s = sol()
print(s.isSameTree(t1, t2))
