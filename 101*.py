'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # # 递归解法一
        # if not root:
        #     return True
        # 
        # def judge(left, right):
        #     if not left and not right:
        #         return True
        #     elif left==None or right==None:
        #         return False
        #     c1 = (left.val==right.val)
        #     c2 = judge(left.left, right.right)
        #     c3 = judge(left.right, right.left)
        #     return c1 and c2 and c3
        # return judge(root.left, root.right)

        # 循环解法二
        # 对于循环， 我们要满足对于每一层进行check， 使用FIFO的queue来作为临时空间存储变量
        # 我们用两个queue对于左右同时进行检查

        if not root:
            return True
        Q1 = [root.left]
        Q2 = [root.right]
        while Q1 and Q2:
            left = Q1[0]
            right = Q2[0]
            Q1 = Q1[1:]
            Q2 = Q2[1:]
            if (not left and right) or (left and not right):
                return False
            if left and right:
                if not left.val==right.val:
                    return False
                Q1.append(left.left)
                Q1.append(left.right)
                Q2.append(right.right)
                Q2.append(right.left)
        return True


s = Solution()
root = TreeNode(2)
a = TreeNode(3)
b=TreeNode(3)
c=TreeNode(4)
d=TreeNode(5)
e=TreeNode(5)
f=TreeNode(4)
root.left=a
root.right = b
a.left=c
a.right=d
b.left=e
b.right=f
print(s.isSymmetric(root))