# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        pre = None
        for _ in range(left-1):
            pre=node
            node=node.next
        tail=node
        con=pre
        for _ in range(right-left+1):
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        if con:
            con.next=pre
        else:
            head=pre
        tail.next=node
        return head
