'''
116. Populating Next Right Pointers in Each Node II
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?
'''
# Definition for binary tree with next pointer.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # if not root:
        #     return
        # # 层级遍历方法
        # Q=[root]
        # while Q:
        #     length=len(Q)
        #     while length:
        #         a = Q[0]
        #         Q=Q[1:]
        #         length-=1
        #         a.next = Q[0] if length else None
        #         if a.left:
        #             Q.append(a.left)
        #         if a.right:
        #             Q.append(a.right)

        
s = Solution()
root = TreeNode(1)
a = TreeNode(2)
b=TreeNode(3)
c = TreeNode(4)
d=TreeNode(5)
e = TreeNode(6)
f=TreeNode(7)

root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
print(s.connect(root))