'''
107 Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        Q = []
        Q.append(root)
        result = []
        while Q:
            temp = []
            lenth = len(Q)
            while lenth:
                a = Q[0]
                Q = Q[1:]
                temp.append(a.val)
                lenth-=1
                if a.left:
                    Q.append(a.left)
                if a.right:
                    Q.append(a.right)
                
            result.append(temp)
        return result[::-1]


s = Solution()
root = TreeNode(3)
a = TreeNode(9)
b=TreeNode(20)
c=TreeNode(15)
d=TreeNode(7)
root.left=a
root.right = b
b.left=c
b.right=d
print(s.levelOrderBottom(root))
