class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        temp=[]
        for i in range(len(nums)):
            temp=temp+[int(nums[i])]
        temp.sort(reverse=True)
        return str(temp[k-1])
        
