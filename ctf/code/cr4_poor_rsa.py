import base64
from Crypto.PublicKey import RSA
import rsa
from gmpy2 import invert
p=863653476616376575308866344984576466644942572246900013156919
q=965445304326998194798282228842484732438457170595999523426901
n=p*q
e=65537
d=int(invert(e,(p-1)*(q-1)))
cipher=open('flag.b64','r').read()
cipher=base64.b64decode(cipher)
privatekey=rsa.PrivateKey(n,e,d,p,q)
flag=rsa.decrypt(cipher,privatekey)
print(flag)