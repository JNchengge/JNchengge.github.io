import base64
def decode(message):
    s=base64.b64decode(message)
    flag=''
    for i in s:
        x=ord(i)-16
        x=x^32
        flag+=chr(x)
    return flag
correct='XlNkVmtUI1MgXWBZXCFeKY+AaXNt'
flag=decode(correct)
print(flag)
