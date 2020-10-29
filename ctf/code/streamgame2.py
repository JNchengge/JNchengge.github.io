def lfsr(R,mask):
    output = (R << 1) & 0xffffff
    i=(R&mask)&0xffffff
    lastbit=0
    while i!=0:
        lastbit^=(i&1)
        i=i>>1
    output^=lastbit
    return (output,lastbit)

mask=0x100002

key=[]
f=open('ctf//code//key','rb')
content=f.read()
for i in content:
    key.append(int(i))

for flag in range(2**27):
    R=flag
    tmp=0
    judge=0
    for i in range(12):
        tmp=0
        for j in range(8):
            (R,out)=lfsr(R,mask)
            tmp=(tmp << 1)^out
        if tmp!=key[i]:
            judge=0
            break
        else:
            judge=1
    if judge:
        break
print('flag{'+bin(flag)[2:]+'}')