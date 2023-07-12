# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp_list = []

        for node in lists:
            while node:
                temp_list.append(node.val)
                node=node.next

        temp_list.sort()
        head = dummy = ListNode()

        for vals in temp_list:
            dummy.next = ListNode(vals)
            dummy = dummy.next

        return head.next