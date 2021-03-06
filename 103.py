'''
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
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

        for i in range(len(result)):
            if not (i+1)%2==1:
                result[i] = result[i][::-1]
        return result


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
print(s.zigzagLevelOrder(root))
