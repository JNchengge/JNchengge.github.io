s=":\"AL_RT^L*.?+6/46"
key=[i for i in s]
a='harambe'
flag=''
for i in range(len(s)):
    flag+=chr(ord(a[i%7])^ord(s[i]))
print(flag)

