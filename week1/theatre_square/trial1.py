m,n,a=map(int,input().split())
if  m%a==0:
    part1=m//a
else:
    part1=(m//a)+1
if  n%a==0:
    part2=n//a
else:
    part2=(n//a)+1
print(part1+part2)
