from collections import defaultdict
num=int(input())
for i in range(num):
    num2=int(input())
    integers=list(map(int,input().split()))
    letters=input()
    dic=defaultdict(list)
    for idx,integer in enumerate(integers):
        dic[integer].append(idx)
    truth=True
    for list_of_integer in dic.values():
        temp=list_of_integer[0]
        for integers in list_of_integer:
            if letters[temp]!=letters[integers]:
                truth=False
                break
    if truth:
        print('YES')
    else:
        print('NO')
        
