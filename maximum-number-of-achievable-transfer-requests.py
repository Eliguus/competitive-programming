class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        array = [0]*n

        def tracking(i):
            if i == len(requests):
                if min(array)==max(array)==0:
                    return 0
                return -400
            v,w = requests[i]

            array[v]-=1
            array[w]+=1
            res = 1 + tracking(i+1)
            array[v]+=1
            array[w]-=1

            return max(res,tracking(i+1))

        return tracking(0)