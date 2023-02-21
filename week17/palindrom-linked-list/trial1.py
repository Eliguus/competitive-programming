class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        arrN = []
        arrR = []
        temp = head
        while slow:
            arrN.append(temp.val)
            arrR.append(slow.val)
            slow = slow.next
            temp = temp.next
        return arrN==arrR[::-1]
