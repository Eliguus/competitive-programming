if __name__ == '__main__':
    N = int(input())
    instructions=[]
    for i in range(N):
        instruction=list(map(str,input().split()))
        instructions+=[instruction]
    the_list=[]
    for index in range(N):
        if instructions[index][0]=='insert':
            the_list.insert(int(instructions[index][1]),int(instructions[index][2]))
        elif instructions[index][0]=='print':
            print(the_list)
        elif instructions[index][0]=='remove':
            for i in range(len(the_list)):
                if the_list[i]==int(instructions[index][1]):
                    the_list.pop(i)
                    break
        elif instructions[index][0]=='append':
            the_list.append(int(instructions[index][1]))
        elif instructions[index][0]=='sort':
            the_list.sort()
        elif instructions[index][0]=='pop':
            the_list.pop()
        elif instructions[index][0]=='reverse':
            the_list=the_list[::-1]
