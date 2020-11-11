from gmpy2 import invert,powmod
from Crypto.Util.number import long_to_bytes
n=0xc3d945bc033ff7dd932ba62d8ef506cb37f5fe8e45abdac07660c7ac2af97d3ce723710384046c1bd967e92b0e03666d7c0bcbd4043b39ee128e5a1c98b5367044a4e72a4868fdc4824e8f0f3074da2857a414c9dfd7bf208d41caefeac144a45a6ca225975b0fced05d85d6e95dc7c2fa303c8a69185b75b8b3fd7f3fe0b9b5
p=0xdfe9dd9c9e9987e2fdb230fb346cefa87893afed5d1b4240872ec5b2dfc3b397ecbbf9b54ae6e9b7be150cdc79de1e87d2d674352b857ae4e000000000000000
c=0xe1ea04df467b48a7fa372d9374959571a084341041ec71f57e661cedfb517dbf1cc05a305edeb56ce0d2e29a98790a1cd538b31203a8ff7ea79aee1b3ad8629eac19607dce66f9138e3b376a8e915e24d209a23cb8e1a02c6030d840ceb4203
p=11727303544673695770693932646789704596383672272449098298200981935026553791519437864191858652198792482263288749913991072332028605113900194946640937749763897
q=11727303544673695770693932646789704596383672272449098298200981935026553791519437864191858652198792482263288749913991072332028605113900194946640937749764701
phi_n=(p-1)*(q-1)
for e in range(1000001,100000000):
    try:
        d=invert(e,phi_n)
    except ZeroDivisionError:
        pass
    m=powmod(c,d,n)
    m=long_to_bytes(m)
    flag1=[]
    for i in m:
        flag1.append(i%128)
    flag2=''
    for i in flag1:
        flag2+=chr(i)
    if 'ctf{' in flag2:
        print(str(e)+':'+flag2)