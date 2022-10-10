class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        mountain=0
        p=0
        while p<=len(arr)-2:
            count=0
            while p<len(arr)-2 and arr[p]<arr[p+1]:
                if count==0:
                    count=1
                p+=1
                count+=1
            while p<len(arr)-1 and count>0 and arr[p]>arr[p+1]:
                p+=1
                count+=1
                mountain=max(mountain,count)
            if count==0:
                p+=1
        return mountain
