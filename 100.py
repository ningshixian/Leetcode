'''
100. Same Tree

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False

        Q1 = [p]
        Q2 = [q]
        while Q1 and Q2:
            if set(Q1)=={None} and set(Q2)=={None}:
                return True
            left = Q1[0]
            right = Q2[0]
            Q1 = Q1[1:]
            Q2 = Q2[1:]
            if not left and not right:
                continue
            if (not left and right) or (left and not right):
                return False
            if left and right:
                if not left.val==right.val:
                    return False
            Q1.append(left.left)
            Q1.append(left.right)
            Q2.append(right.left)
            Q2.append(right.right)
        return True


s = Solution()
root1 = TreeNode(1)
a = TreeNode(2)
b=TreeNode(3)
root1.left=a
root1.right = b

root2 = TreeNode(1)
c=TreeNode(2)
d=TreeNode(3)
root2.left=c
root2.right = d
print(s.isSameTree(root1, root2))