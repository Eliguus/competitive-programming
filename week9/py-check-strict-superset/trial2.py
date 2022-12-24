# Enter your code here. Read input from STDIN. Print output to STDOUT
setA=list(map(int,input().split()))
n=int(input())
setC=[]
for i in range(n):
    setC+=[list(map(int,input().split()))]
count=0
for sets in setC:
    count1=0
    if len(sets)!=len(setA):
        for nums in sets:
            if nums in setA:
                count1+=1
    if count1==len(sets):
        count+=1
        
if count==len(setC):
    print(True)
else:
    print(False)
