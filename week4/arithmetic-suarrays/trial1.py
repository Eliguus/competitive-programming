class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans=[]
        for i in range(len(l)):
            temp=nums[l[i]:r[i]+1]
            temp=sorted(temp)
            count=0
            for j in range(len(temp)-1):
                if temp[j+1]-temp[j]==temp[1]-temp[0]:
                    count+=1
                else:
                    ans+=[False]
                    break
                if count==len(temp)-1:
                    ans+=[True]
                
        return ans      
        
