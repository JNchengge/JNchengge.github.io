from base64 import b64decode
fw=open('2','w')
with open('1','r') as f:
    for line in f:
        fw.write(str(b64decode(line)))
fw.close()