import string
import libnum
def tobin(data):
    data=str(data)
    base64table=string.ascii_uppercase+string.ascii_lowercase+string.digits+'+/'
    index=base64table.find(data)
    return format(index,'06b')
def toStr(mybin):
    binlen=len(mybin)
    out=''
    for i in range(0,binlen,8):
        out+=chr(int('0b'+bin(mybin[i,i+8],2)))
    return out
flag=''
f=open('3.txt','rb')
for line in f:
    line=line.decode('utf-8').strip()
    if line[-2:] == '==':
        tmp=line[-3]
        tmp_bin=tobin(tmp)
        print(tmp_bin)
        flag+=tmp_bin[-4:]
    elif line[-1:]== '=':
        tmp=line[-2]
        tmp_bin=tobin(tmp)
        print(tmp_bin)
        flag+=tmp_bin[-2:]
print(flag)
print(libnum.n2s(int(flag,base=2)))
f.close()
