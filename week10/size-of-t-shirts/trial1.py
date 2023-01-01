test_cases=int(input())
for i in range(test_cases):
    sizes=list(map(str,input().split()))
    if sizes[0]==sizes[1]:
        print('=')
    elif 'M' in sizes[0] or 'M' in sizes[1]:
        if 'M' in sizes[0] and 'S' in sizes[1]:
            print('>')
        elif 'M' in sizes[0] and 'L' in sizes[1]:
            print('<')
        elif 'M' in sizes[1] and 'L' in sizes[0]:
            print('>')
        elif 'M' in sizes[1] and 'S' in sizes[0]:
            print('<')
    elif 'S' in sizes[0] and 'S' in sizes[1]:
        if len(sizes[0])>len(sizes[1]):
            print('<')
        elif len(sizes[0])<len(sizes[1]):
            print('>')
    elif 'L' in sizes[0] and 'L' in sizes[1]:
        if len(sizes[0])>len(sizes[1]):
            print('>')
        elif len(sizes[0])<len(sizes[1]):
            print('<')
    elif ('S' in sizes[1] and 'L' in sizes[0]) or ('S' in sizes[0] and 'L' in sizes[1]):
        if 'S' in sizes[0] and 'L' in sizes[1]:
            print('<')
        elif 'S' in sizes[1] and 'L' in sizes[0]:
            print('>')
    
