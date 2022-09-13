class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i   in  range(len(nums1)):
            m=1
            for j   in  range(nums2.index(nums1[i])+1,len(nums2)):
                if  nums1[i]<nums2[j]:
                    ans=ans+[nums2[j]]
                    m=0
                    break
                else:
                    m=1
                    continue
            if  m==1:
                ans=ans+[-1]
        return  ans
                    
                    
        
