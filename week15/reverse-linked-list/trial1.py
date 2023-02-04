class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        pre = head
        cur = head.next
        temp = head.next.next
        pre.next = None
        while temp:
            cur.next = pre
            pre = cur
            cur = temp
            temp = temp.next
        cur.next = pre
        return cur
