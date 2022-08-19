class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list=[]
        if n%3==0:
            list=list+["Fizz"]
        elif n%5:
            list=list+["buzz"]
        elif n%15:
            list=list+["FizzBuzz"]
        else:
            list=list+[n]

