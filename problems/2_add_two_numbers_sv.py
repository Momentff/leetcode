# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n, m = l1, l2
        list_node = []
        extra = 0
        while True:
            curr = n.val + m.val + extra
            if curr < 10:
                S = ListNode(n.val + m.val + extra)
                extra = 0
            else:
                S = ListNode(curr - 10)
                extra = 1
            if list_node:                                                   
                list_node.pop().next = S
            else:
                list_node.append(S)
            list_node.append(S)
            if n.next is None or m.next is None:
                break
            n = n.next
            m = m.next

        if n.next is None and m.next is not None:
            m = m.next
            while True:
                curr = m.val + extra
                if curr < 10:
                    S = ListNode(m.val + extra)
                    extra = 0
                else:
                    S = ListNode(curr - 10)
                    extra = 1
                if list_node:
                    list_node.pop().next = S
                else:
                    list_node.append(S)
                list_node.append(S)
                if m.next is None:
                    break
                m = m.next

        if m.next is None and n.next is not None:
            n = n.next
            while True:
                curr = n.val + extra
                if curr < 10:
                    S = ListNode(n.val + extra)
                    extra = 0
                else:
                    S = ListNode(curr - 10)
                    extra = 1
                if list_node:
                    list_node.pop().next = S
                else:
                    list_node.append(S)
                list_node.append(S)
                if n.next is None:
                    break
                n = n.next

        if n.next is None and extra == 1 and m.next is None:
            list_node.pop().next = ListNode(1)
        return list_node[0]
