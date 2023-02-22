# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 1
        node = head
        while node.next:
            node=node.next
            length+=1
        node.next=head
        for _ in range(length-(k%length)):
            node=node.next
        final = node.next
        node.next=None
        return final
