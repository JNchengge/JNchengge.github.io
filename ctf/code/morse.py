a='11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110'
b=a.split(' ')
d=''
for item in b:
    for c in item:
        if c=='1':
            d+='-'
        else:
            d+='.'
    d+='/'
print(d)
