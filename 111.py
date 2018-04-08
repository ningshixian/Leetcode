'''
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        Q=[root]
        depth=0
        while Q:
            lenth = len(Q)
            while lenth:
                a=Q[0]
                Q=Q[1:]
                if a.left:
                    Q.append(a.left)
                if a.right:
                    Q.append(a.right)
                if not a.left and a.right:
                    return depth+1
                lenth-=1
            depth+=1
        return depth
                

s = Solution()
root = TreeNode(3)
a = TreeNode(9)
b=TreeNode(20)
c=TreeNode(15)
d=TreeNode(7)
root.left=a
root.right = b
# b.left=c
b.right=d
print(s.minDepth(root))