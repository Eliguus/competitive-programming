class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        max_digit=len(num1)+len(num2)
        first_num=num1[::-1]
        second_num=num2[::-1]
        multiple=[0]*max_digit
        for place1,digit1 in enumerate(first_num):
            for place2,digit2 in enumerate(second_num):
                num_zero=place1+place2
                carry=multiple[num_zero]
                multiply=int(digit1)*int(digit2)+carry
                multiple[num_zero]=multiply%10
                multiple[num_zero+1]+=multiply//10
        ans=[]
        if multiple[-1]==0:
            multiple.pop()
        for num in multiple[::-1]:
            ans.append(str(num))
        return ''.join(ans)
