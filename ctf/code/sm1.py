from Crypto.Util.number import getPrime,long_to_bytes,bytes_to_long
from Crypto.Cipher import AES
import hashlib
from random import randint
from base64 import b64decode
def tobinrev(s):
    return bin(int(s))[2:][::-1]
dic={}
dic_value=[0 for i in range(512)]
with open('ps','r') as lines:
    for i in range(512):
        for line in lines:
            line=line.strip()
            index=tobinrev(line).find('1')
            dic[index]=i
            dic_value[index]=tobinrev(line)
            break
with open('r','r') as r:
    r_rev=tobinrev(r.read())
    tmp_result=[0 for i in range(512)]
    for i in range(512):
        tmp=0
        for j in range(i):
            tmp^=(int(dic_value[j][i])*tmp_result[j])
        tmp_result[i]=int(r_rev[i])^tmp
ans=[0 for i in range(512)]
for i in range(512):
    ans[dic[i]]=tmp_result[i]
choose=''
for i in ans:
    choose+=str(i)
print(choose)
choose=int(choose,2)
key=long_to_bytes(int(hashlib.md5(long_to_bytes(choose)).hexdigest(),16))
aes_obj=AES.new(key,AES.MODE_ECB)
flag=open('ef','r').read()
ef=aes_obj.decrypt(flag.decode('base64'))
print(ef)