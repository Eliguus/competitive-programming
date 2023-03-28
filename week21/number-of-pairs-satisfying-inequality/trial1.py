class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        dif=[nums1[i]-nums2[i] for i in range(len(nums1))]
        ans=0
        def merge_sort(arr):
            nonlocal ans
            if len(arr)==1:
                return arr
            
            
            x=merge_sort(arr[:len(arr)//2])
            y=merge_sort(arr[len(arr)//2:])
            
            for i in x:
                ans+=len(y)-bisect_left(y,i-diff)
            return sorted(x+y)
        merge_sort(dif)
        return ans
        
