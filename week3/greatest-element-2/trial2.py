class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        stack=[]
        for i in range(2*len(nums)-1,-1,-1):
            index=i%len(nums)
            while stack and stack[-1]<=nums[index]:
                stack.pop()
            if stack==[]:
                ans=ans+[-1]
            else:
                ans=ans+[stack[-1]]
            stack.append(nums[index])
        
        return  ans[:len(nums)-1:-1]
                    
        
        
