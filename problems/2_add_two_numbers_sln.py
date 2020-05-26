# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rem = 0
        head = None
        tail = None
        while l1 is not None or l2 is not None:
            s = rem
            if l1 is not None:
                s += l1.val
                l1 = l1.next
            if l2 is not None:
                s += l2.val
                l2 = l2.next            
            if s >= 10:
                rem = 1
                next_node = ListNode(s - 10)
            else:
                rem = 0
                next_node = ListNode(s)
            
            if head is None:
                head = next_node
                tail = next_node
            else:
                tail.next = next_node
                tail = next_node
        if rem > 0:
            tail.next = ListNode(rem)
        return head
