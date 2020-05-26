# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n, m = l1, l2
        temp = None
        extra = 0
        val1 = False
        val2 = False

        while True:
            s1 = 0 if val1 else n.val
            s2 = 0 if val2 else m.val
            total = s1 + s2 + extra
            extra = 1 if total >= 10 else 0
            S = ListNode(total%10)
            if temp:
                temp.next = S
                temp = S
            else:
                temp = S
                output = S
            if n.next is None and m.next is None and extra == 1:
                S = ListNode(1)
                temp.next = S
                break
            elif n.next is None and m.next is None:
                break
            if n.next is None:
                val1 = True
            else:
                n = n.next
            if m.next is None:
                val2 = True
            else:
                m = m.next
        return output
