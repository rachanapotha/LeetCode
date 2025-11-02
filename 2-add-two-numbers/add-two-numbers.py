# Definition for singly-linked list.
#Two 
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry

            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next