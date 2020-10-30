f1=open('msg001.enc','r')
f2=open('msg002.enc','r')
cipher1=f1.read()
cipher2=f2.read()
n=0
t=0
input_="Hi! This is only test message"
key='VeryLongKeyYouWillNeverGuess'*1000
for j,p in zip(cipher1,input_): #求解密钥
    for k in range(256):
        c=(ord(p)+(k^t)+n*n)&0xff
        if chr(c)==j:
            t=ord(p)
            n+=1
            key+=chr(k)
            break
print(key)
n=0
t=0
flag=''
for i in cipher2:  #解密
    for p in range(256):
        c=(p+(ord(key[n])^t)+n*n)&0xff
        if i==chr(c):
            t=p
            n+=1
            flag+=chr(p%128)
            break
print(flag)
f1.close()
f2.close()