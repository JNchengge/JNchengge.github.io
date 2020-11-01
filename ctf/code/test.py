from base64 import b64decode
b=[]
t=open('4.txt','w')
with open('3.txt','r') as f:
    content=f.readlines()
    for i in content:
        tmp=b64decode(i)
        b.append(tmp.decode('utf-8'))
        t.write(tmp.decode('utf-8')+'\n')
t.close()