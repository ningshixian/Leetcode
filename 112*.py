'''
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.dfs(root, sum, 0)

    def dfs(self, root, target, sum):
        if not root:
            return False
        sum+=root.val
        if not root.left and not root.right:
            if sum==target:
                return True
            else:
                return False
        l = self.dfs(root.left, target, sum)
        r = self.dfs(root.right, target, sum)
        return l or r


s = Solution()
root = TreeNode(5)
a = TreeNode(4)
b=TreeNode(8)
c=TreeNode(11)
d=TreeNode(13)
e=TreeNode(4)
f=TreeNode(7)
g=TreeNode(2)
h=TreeNode(1)

root.left=a
root.right = b
a.left = c
b.left = d
b.right = e
c.left=f
c.right=g
e.right=h

sum = 22
print(s.hasPathSum(root, sum))