class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list=[]
        for i in range(n):
            
            if (i+1)%15==0:
                list=list+["FizzBuzz"]
            elif (i+1)%5==0:
                list=list+["Buzz"]
            elif (i+1)%3==0:
                list=list+["Fizz"]
            else:
                list=list+[str(i+1)]
        return list

