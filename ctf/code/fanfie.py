from base64 import b32decode,b32encode,b64decode
from gmpy2 import invert
#print(b32encode('BITSCTF'))
cipher="MZYVMIWLGBL7CIJOGJQVOA3IN5BLYC3NHI"
"""for i in range(27): #暴力破解a,b
    for j in range(27):
        if gcd(i,32)==1:
            if (i*21+j)%32==21 and (i*3+j)%32==11 and (i*9+j)%32==25 and (i*4+j)%32==24:
                print(i,j)"""
a=13
b=4
s="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 2 3 4 5 6 7"
alphabet=s.split(' ')
flag=''
for ch in cipher:
    flag+=alphabet[((alphabet.index(ch)-b)*invert(a,32))%32]
print(flag)