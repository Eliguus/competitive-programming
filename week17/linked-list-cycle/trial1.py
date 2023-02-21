# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        linked = head
        count = 0
        node_set = set()
        while linked and linked.next:
            if linked in node_set:
                return True
            node_set.add(linked)
            count+=1
            linked = linked.next
        return False



