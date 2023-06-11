# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        
        ans = [0]*len(nums)
        stack = []
        for i,num in enumerate(nums):
            while stack and nums[stack[-1]]<num:
                temp = stack.pop()
                ans[temp] = num
            stack.append(i)
        
        return ans