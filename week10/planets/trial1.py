from collections import Counter
num=int(input())
for i in range(num):
    n=list(map(int,input().split()))
    c=n[1]
    planets=list(map(int,input().split()))
    num_planets=Counter(planets)
    count=0
    for key in num_planets.keys():
        if c<num_planets[key]:
            count+=c
        else:
            count+=num_planets[key]
    print(count)
