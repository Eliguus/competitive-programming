class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def tracking(arr,path):
            if not arr and len(path) == 4:
                ans.append('.'.join(path))

            for i in range(1,len(arr)+1):
                if not (0<=int(arr[:i])<=255) or (len(arr[:i]) > 1 and arr[:i][0]=='0'):
                    continue
                tracking(arr[i:],path+[arr[:i]])
            
        tracking(s,[])

        return ans