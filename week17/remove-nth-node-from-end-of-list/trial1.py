# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ptr_d = dummy
        ptr_h = head
        for _ in range(n):
            ptr_h = ptr_h.next
        while ptr_h:
            ptr_d = ptr_d.next
            ptr_h = ptr_h.next
        ptr_d.next = ptr_d.next.next
        return dummy.next
