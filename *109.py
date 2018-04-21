'''
109. Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # def calHeight(left, right):
        #     h1 = DFS(left)
        #     h2 = DFS(right)
        #     return h1-h2

        # def DFS(node):
        #     if not node:
        #         return 0
        #     h1 = DFS(node.left)
        #     h2 = DFS(node.right)
        #     return 1+max(h1, h2)

        # def rotateLeft(rotRoot):
        #     newRoot = rotRoot.right    # 创建一个临时变量来跟踪子树的新根
        #     rotRoot.right = None  # 用新的左孩子替换旧根的右孩子
        #     newRoot.left = rotRoot
        #     return newRoot

        # def rotateRight(rotRoot):
        #     newRoot = rotRoot.left    # 创建一个临时变量来跟踪子树的新根
        #     rotRoot.left = None  # 用新的左孩子替换旧根的右孩子
        #     newRoot.right = rotRoot
        #     return newRoot

        # if not head:
        #     return
        # root = TreeNode(head.val)
        # r_node = root
        # while head.next:
        #     leaf = TreeNode(head.next.val)
        #     r_node.right=leaf
        #     r_node.left=None
        #     r_node = leaf
        #     # 计算左右子树的高度差，若超过1则重新调整
        #     diff = calHeight(root.left, root.right)
        #     if diff>1:
        #         # 向右重新调整BTS
        #         root = rotateRight(root)
        #     elif diff<-1:
        #         # 向左重新调整BTS
        #         root = rotateLeft(root)
        #     else:
        #         pass
        #     head = head.next
        # return root

        def build(start, end):
            if start==end:
                return
            fast = start
            slow = start
            while not fast==end and not fast.next==end:
                fast=fast.next.next
                slow=slow.next
            root = TreeNode(slow.val)
            root.left = build(start, slow)
            root.right = build(slow.next, end)
            return root

        if not head:
            return
        return build(head, None)




s = Solution()
root = ListNode(-10)
a = ListNode(-3)
b=ListNode(0)
c = ListNode(5)
d=ListNode(9)

root.next=a
a.next=b
b.next=c
c.next=d
root = s.sortedListToBST(root)
Q=[root]
while Q:
    a=Q[0]
    Q=Q[1:]
    print(a.val)
    if a.left:
        Q.append(a.left)
    if a.right:
        Q.append(a.right)