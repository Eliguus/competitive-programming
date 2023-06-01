class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def isPrime(num):
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    return False

            return True

        n1 = None
        n2 = None
        mini = 10**6+1
        for i in range(left,right+1):
            if i==1:
                continue
            if isPrime(i):
                if not n1:
                    n1=i
                else:
                    n2 = n1
                    n1 = i
                    if n1-n2<3:
                        return [n2,n1]
                    mini = min(mini,n1-n2)
                    res = [n2,n1]
        if mini>10**6:
            return [-1,-1]
        return res