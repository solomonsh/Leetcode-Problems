# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0 or len(preorder) == 0:
             return None
        root = TreeNode(preorder.pop(0))


        left  = self.buildTree(preorder,inorder[:inorder.index(root.val)])

        right = self.buildTree(preorder,inorder[inorder.index(root.val)+1:])

        root.left = left
        root.right = right

        return root

sol = Solution()

preorder = [3,9,20]
inorder =  [9,3,20]

print(sol.buildTree(preorder,inorder))