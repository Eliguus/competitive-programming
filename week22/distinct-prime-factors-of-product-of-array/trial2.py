class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def isPrime(num):
            if num<2:
                return False
            for i in range(1,int(num**0.5)+1):
                if num%i==0:
                    return False
            return True

        count = defaultdict(int)

        for num in nums:
            if isPrime(num):
                count[num]+=1
                continue

            d=2
            while d*d<=num:
                while num%d==0:
                    count[d]+=1
                    num//=d
                d+=1
            if num>1:
                count[num]+=1

        return len(count)
