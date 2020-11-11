s='c61b68366edeb7bdce3c6820314b7498'
t=['0' for i in range(32)]
v=0
while(v<len(s)):
    if v&1:
        v3=1
    else:
        v3=-1
    t[v]=chr(ord(s[v])+v3)
    v+=1
print(''.join(t))