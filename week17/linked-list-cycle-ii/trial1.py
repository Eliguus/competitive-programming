# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked = head
        count = 0
        node_set = set()
        while linked and linked.next:
            if linked in node_set:
                return linked
            node_set.add(linked)
            count+=1
            linked = linked.next
        return None
