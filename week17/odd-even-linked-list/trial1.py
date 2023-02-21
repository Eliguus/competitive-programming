# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head):
            return head
        even=head.next
        odd=head
        evenL=even
        while even and odd:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next=evenL
        return head
