class Solution:
    def countArrangement(self, n: int) -> int:

        arr = [False]*(n+1)
        count = 0
        def tracking(n,idx):
            nonlocal count
            if idx>n:
                count+=1
                return

            for i in range(1,n+1):
                if not arr[i] and (idx%i==0 or i%idx==0):
                    arr[i]=True
                    tracking(n,idx+1)
                    arr[i] = False
        tracking(n,1)
        return count