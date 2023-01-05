class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_list=num1.split('+')
        num2_list=num2.split('+')
        num1_list[1]=num1_list[1][:len(num1_list[1])-1]
        num2_list[1]=num2_list[1][:len(num2_list[1])-1]
        imaginary1=0
        real=0
        print(num2_list)
        
        real+=(int(num1_list[1])*int(num2_list[1]))*(-1)
        
        imaginary1+=(int(num1_list[1])*int(num2_list[0]))
        imaginary1+=int(num2_list[1])*int(num1_list[0])
        real+=(int(num1_list[0])*int(num2_list[0]))
        multiplied=str(real)+'+'+str(imaginary1)+'i'
        return multiplied
