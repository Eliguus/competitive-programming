class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dou_nums=nums+nums
        ans=[]
        for i   in  range(len(nums)):
            count=0
            for j in range(i+1,len(dou_nums)):
                count+=1
                if nums[i]<dou_nums[j]:
                    
                    ans=ans+[dou_nums[j]]
                    
                    break
                if count==len(dou_nums)-i-1:
                    ans=ans+[-1]
                    break
              
        return  ans
                    
        
        
