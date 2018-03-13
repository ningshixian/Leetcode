# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val <= l2.val:
            l3 = l1
            l1=l1.next
        else:
            l3=l2
            l2=l2.next
        temp = l3
        while l1 and l2:
            a = l1.val
            b = l2.val
            c = temp.val
            if a<=b:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        while l1:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        while l2:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        return l3

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
# while l1:
#     print(l1.val)
#     l1 = l1.next
# print('--------------')
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4) 
l3 = s.mergeTwoLists(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next
