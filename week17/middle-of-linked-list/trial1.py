# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare=head
        tortorise=head
        while hare and hare.next:
            tortorise=tortorise.next
            hare=hare.next.next
        return tortorise
