# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        left = right = head
        for _ in range(n):
            right = right.next
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head

a = Solution()
head = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
head.next = two
two.next = three
three.next = four
four.next = five
head = a.removeNthFromEnd(head,2)
while head.val:
    print(head.val)
    head = head.next
