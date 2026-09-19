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
    def isValidBST(self, root) :
        
        ans = True
        prev = None

        def inorderTraversal(root):
            if not root:
                return

            nonlocal prev, ans

            inorderTraversal(root.left)

            if prev is not None and root.val <= prev:
                ans = False

            prev = root.val

            inorderTraversal(root.right)

        inorderTraversal(root)

        return ans



a = list(map(int, input().split()))
root = buildtree(a)
s = Solution()
print(s.isValidBST(root))