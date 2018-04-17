'''
144. Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    #     if not root:
    #         return []
    #     result = []
    #     return self.preorder(root, result)

    # def preorder(self, root, result):
    #     result.append(root.val)
    #     if root.left:
    #         self.preorder(root.left, result)
    #     if root.right:
    #         self.preorder(root.right, result)
    #     return result
    
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            a=stack.pop()
            result.append(a.val)
            if a.right:
                stack.append(a.right)
            if a.left:
                stack.append(a.left)
        return result       


s = Solution()
root = TreeNode(1)
a = TreeNode(2)
b=TreeNode(3)

root.right = a
a.left = b
print(s.preorderTraversal(root))