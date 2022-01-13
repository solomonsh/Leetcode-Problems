from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def get_parents(self, root, node):
        if root.val == node:
            return [root.val]

        if root.val < node:
            return [root.val] + self.get_parents(root.right, node)
        if root.val > node:
            return [root.val] + self.get_parents(root.left, node)

    def lowestCommonAncestor(self, root, p, q):
       
        pparents = self.get_parents(root, p)
        qparents = self.get_parents(root, q)

        if len(pparents) < len(qparents):

            smallest = pparents
            largest = qparents
        else:

            smallest = qparents
            largest = pparents

        for i in range(len(smallest)-1, -1, -1):
            if smallest[i] in largest:
                return TreeNode(smallest[i])

# Optimized
# def lowest_common_ancestor(root, p, q):
#     queue = deque([root])

#     while queue:
#         current = queue.popleft()

#         if p.val < current.val and q.val < current.val:
#             if current.left:
#                 queue.append(current.left)
#         elif p.val > current.val and q.val > current.val:
#             if current.right:
#                 queue.append(current.right)
#         else:
#             return current.val 

sol = Solution()

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


print(sol.lowestCommonAncestor(root, 2, 8))
