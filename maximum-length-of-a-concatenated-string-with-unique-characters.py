class Solution:
    def maxLength(self, arr: List[str]) -> int:
        length = 0
        def tracking(idx,string):
            nonlocal length

            if len(string)!=len(set(string)):
                return

            length = max(length,len(string))

            for i in range(idx,len(arr)):
                tracking(i+1,string+arr[i])

        tracking(0,'')

        return length