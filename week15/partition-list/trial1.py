class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = less_dum = ListNode(0)
        more = more_dum = ListNode(0)
        while head:
            if head.val < x:
                less.next = head
                less = less.next 
            else:
                more.next = head
                more = more.next
            head = head.next
        more.next = None
        less.next = more_dum.next
        return less_dum.next
