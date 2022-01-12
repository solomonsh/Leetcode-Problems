from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inOdrder_traversal(self, root):
        if root is None:
            return []

        return self.inOdrder_traversal(root.left)+[root.val]+self.inOdrder_traversal(root.right)
       

    def kthSmallest(self, root, k):
        return self.inOdrder_traversal(root)[k-1]


sol = Solution()

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.right = TreeNode(2)


root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(6)

root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)

root1.left.left.left = TreeNode(1)

root2 = TreeNode(4)

print(sol.kthSmallest(root, 1))
