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
        if not head:
            return
        root = TreeNode(head.val)
        while head.next:
            root.right=head.next
            # 计算左右子树的高度差，若超过1则重新调整
            diff = calHeight(root.left, root.right)
            if diff>1:
                # 重新调整BTS
                root = retune(root)
            head = head.next

        

        
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
print(s.sortedListToBST(root))