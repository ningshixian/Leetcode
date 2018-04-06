'''
104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         depth = 0
#         queue = [root]
#         while queue:
#             lenth = len(queue)  # 记录当前层的宽度
#             while lenth:
#                 head = queue[0]
#                 queue = queue[1:]
#                 lenth-=1
#                 if head.left:
#                     queue.append(head.left)
#                 if head.right:
#                     queue.append(head.right)
#             depth+=1
#         return depth


class Solution(object):
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

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
print(s.maxDepth(root))