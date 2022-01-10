# class TreeNode:
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:

# Solution using BFS1
# def maxDepth(root):

#     if root is None:
#         return 0

#     queue = deque()
#     queue.append(root)

#     depth_count = 0
#     while queue:

#         for i in range(len(queue)):

#             current = queue.popleft()

#             if current.left is not None:
#                 queue.append(current.left)

#             if current.right is not None:
#                 queue.append(current.right)

#         depth_count += 1

#     return depth_count


# Solution using DFS

def maxDepth(root):

    if root is None:
        return 0

    depth = max(maxDepth(root.left), maxDepth(root.right))+1

    return depth

# Solution using BFS2
# def max_depth_bfs(root):
#     if not root:
#         return 0

#     queue = deque([root, None])
#     depth = 0

#     while queue:
#         current = queue.popleft()

#         if current is None:
#             depth += 1

#         if current:
#             if current.left:
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)
#         elif queue:
#             queue.append(None)

#     return depth

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root.right.right.right = TreeNode(12)


print(maxDepth(root))
