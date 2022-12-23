class Solution:
    def interpret(self, command: str) -> str:
        goal=''
        for index,char in enumerate(command):
            if char=='(' and command[index+1]==')':
                goal+='o'
            elif char=='(' and command[index+1]=='a':
                goal+='al'
            elif char=='G':
                goal+='G'
        return goal
