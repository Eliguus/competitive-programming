def swap_case(s):
    string=''
    dic={'q':'Q','w':'W','e':'E','r':'R','t':'T','y':'Y','u':'U','i':'I','o':'O','p':'P','a':'A','s':'S','d':'D','f':'F','g':'G','h':'H','j':'J','k':'K','l':'L','z':'Z','x':'X','c':'C','v':'V','n':'N','m':'M','b':'B'}
    for letter in s:
        if letter in dic.values():
            string+=list(dic.keys())[list(dic.values()).index(letter)]
        elif letter in dic.keys():
            string+=dic[letter]
        else:
            string+=letter
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
