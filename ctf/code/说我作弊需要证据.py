from base64 import b64decode,b64encode
from libnum import n2s
from gmpy2 import invert
from Crypto.PublicKey import RSA
f=open('1.txt','r')
a=[]
b=[]
for i in f.readlines():
    a.append(i[:-1])
for i in a:
    b.append(b64decode(i))
Alice_n=0x53a121a11e36d7a84dde3f5d73cf
Bob_n=0x99122e61dc7bede74711185598c7
e=0x10001
n1=int(Alice_n)
n2=int(Bob_n)
p1=38456719616722997
q1=44106885765559411
p2=49662237675630289
q2=62515288803124247
d1=int(invert(e,(p1-1)*(q1-1)))
d2=int(invert(e,(p2-1)*(q2-1)))
A=RSA.construct((n1,e,d1))
B=RSA.construct((n2,e,d2))
flag={}
for i in b:
    i=str(i)
    seq=int(i.split(';')[0].split(' ')[2])
    data=int(i.split(';')[1].split('0x')[1].rstrip('L'),base=16)
    sig=int(i.split(';')[2].split('0x')[1].rstrip('L'),base=16)
    m=B.decrypt(data)
    signcheck=A.sign(m,'')[0]
    if signcheck==sig:
        flag[seq]=n2s(m)
dic=sorted(flag.items(),key = lambda item: item[0])
f=''
for i in dic:
    f+=i[1].decode()
print(f)