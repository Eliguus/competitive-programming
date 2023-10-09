class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {
            1:[8,6],
            2:[7,9],
            3:[8,4],
            4:[9,0,3],
            6:[0,7,1],
            7:[2,6],
            8:[3,1],
            9:[2,4],
            0:[4,6]
        }

        memo = {}
        def dp(left,num):
            if left == 1:
                return 1
            temp = 0
            
            if (left,num) in memo:return memo[(left,num)]
            if num != 5:
                for i in moves[num]:
                    temp = temp + dp(left-1,i)
            memo[(left,num)] = temp
            return temp
        ans = 0
        for i in range(10):
            ans += dp(n,i)
        return ans % (10**9 + 7)