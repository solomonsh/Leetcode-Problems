# Definition for a binary tree node.
from collections  import deque

# Definition for a binary tree node.
from collections  import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        queue = deque([p,q])
    
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

        
# DFS; Time: O(n); Space: O(n)
def is_same_tree_dfs(p, q):
    if p is None and q is None:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    left_nodes = is_same_tree_dfs(p.left, q.left)
    right_nodes = is_same_tree_dfs(p.right, q.right)

    return left_nodes and right_nodes


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)


root3 = TreeNode(1)
root3.left = TreeNode(2)

root4 = TreeNode(1)
root4.right = TreeNode(2)


root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.right = TreeNode(1)


root6 = TreeNode(1)
root6.left = TreeNode(1)
root6.right = TreeNode(2)

sol = Solution()

print(sol.isSameTree(root5, root6))
