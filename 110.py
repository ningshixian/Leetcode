'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root)!=-1

        # Q = [root]
        # while Q:
        #     a = Q[0]
        #     Q=Q[1:]
        #     if a:
        #         h1=self.dfs(a.left)
        #         h2=self.dfs(a.right)
        #         if not abs(h1-h2)<=1:
        #             return False
        #     if a.left:
        #         Q.append(a.left)
        #     if a.right:
        #         Q.append(a.right)
        # return True

    def dfs(self, root):
        if not root:
            return 0
        h1=self.dfs(root.left)
        h2=self.dfs(root.right)
        if h1==-1 or h2==-1 or abs(h1-h2)>1:
            return -1
        return max(h1, h2)+1

        
                


s = Solution()
root = TreeNode(1)
a = TreeNode(2)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(3)
e=TreeNode(4)
f=TreeNode(4)

root.left=a
root.right = b
a.left = c
a.right=d
c.left=e
c.right=f
print(s.isBalanced(root))