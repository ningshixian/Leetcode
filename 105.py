'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder[0])
        preorder = preorder[1:]
        root_idx = inorder.index(root.val)
        # print(root.val)

        root.left = self.buildTree(preorder[:root_idx], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx:], inorder[root_idx+1:])
        
        return root


s = Solution()
preorder = [1,2,3,4]
inorder = [1,2,3,4]
root = s.buildTree(preorder, inorder)
Q = [root]
while Q:
    a = Q[0]
    Q = Q[1:]
    print(a.val)
    if a.left:
        Q.append(a.left)
    if a.right:
        Q.append(a.right)
