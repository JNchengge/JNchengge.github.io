from pwn import unhex
import numpy as np
test='3c3c3c3c7474747414141414e0e0e0e0'
BLOCK=16
pad = lambda s: s+chr(BLOCK-len(s)%BLOCK)*(BLOCK-len(s)%BLOCK)
s=pad('dddd')
f=[]
for i in s:
    f.append(i)
test_unhex=unhex(test)
test_unhex_list=[i for i in test_unhex]
test_list=[ord(i) for i in f]
P=np.array(test_list).reshape(4,4)
C=np.array(test_unhex_list).reshape(4,4)
print(P)
print(C)
