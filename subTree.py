from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        queue = deque([p, q])

        while queue:
            current1 = queue.popleft()
            current2 = queue.popleft()
            if current1 and current2:
                if current1.val != current2.val:
                    return False

                queue.append(current1.left)

                queue.append(current2.left)

                queue.append(current1.right)

                queue.append(current2.right)

            elif current1 != current2:
                return False

        return True

    def isSubtree(self, root, subRoot):
        if self.isSameTree(root, subRoot):
            return True
        else:
            queue = deque([root])

            while queue:
                current = queue.popleft()

                if current.val == subRoot.val:
                    if self.isSameTree(subRoot, current):
                        return True

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
            return False

# Test case 1
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(2)


subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

# Test case 2
root1 = TreeNode(3)
root1.left = TreeNode(4)
root1.right = TreeNode(5)

root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(0)


sol = Solution()

print(sol.isSubtree(root1, subRoot))
