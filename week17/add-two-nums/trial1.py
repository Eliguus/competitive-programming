# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        main = ListNode(0)
        cur = main
        carry = 0
        while l1!=None or l2!=None or carry!=0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            summ = val1+val2+carry
            carry = summ//10
            temp = summ%10
            cur.next = ListNode(temp)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return main.next
