# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        maxS=0
        while slow and pre:
            maxS=max(maxS,slow.val+pre.val)
            pre=pre.next
            slow=slow.next
        return maxS
