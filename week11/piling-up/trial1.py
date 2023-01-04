# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases=int(input())
for cases in range(test_cases):
    size=int(input())
    blocks=list(map(int,input().split()))
    result='Yes'
    while len(blocks)>1:
        if blocks[-1]>=blocks[0]:
            large_num=blocks[-1]
            blocks.pop(-1)
        else:
            large_num=blocks[0]
            blocks.pop(0)
        if blocks[0]>large_num or blocks[-1]>large_num:
            result='No'
            break
    print(result)
