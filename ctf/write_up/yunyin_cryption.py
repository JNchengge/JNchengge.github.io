a="8842101220480224404014224202480122"
a=a.split("0")
flag=''
"""print(a)"""
for item in a:
   temp=0
   for i in item:
      temp+=int(i)
   flag+=(chr(temp+64))
print(flag)
