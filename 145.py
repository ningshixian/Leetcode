'''
145. Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3
 

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    #     if not root:
    #         return []
    #     result = []
    #     return self.postorder(root, result)

    # def postorder(self, root, result):
    #     if root.left:
    #         self.postorder(root.left, result)
    #     if root.right:
    #         self.postorder(root.right, result)
    #     result.append(root.val)
    #     return result
    
            


s = Solution()
root = TreeNode(1)
a = TreeNode(2)
b=TreeNode(3)

root.right = a
a.left = b
print(s.postorderTraversal(root))