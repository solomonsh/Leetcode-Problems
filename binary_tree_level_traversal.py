from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if root is None:
            return None
        result = []
        queue = deque([root])

        while queue:

            level_children = []
            for i in range(len(queue)):
                current = queue.popleft()
                level_children.append(current.val)
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
            result.append(level_children)
        return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


root1 = TreeNode(1)
root2 = None

sol = Solution()
print(sol.levelOrder(root2))
