# 掀桌子
- 本题使用ASCII扩展
- https://blog.csdn.net/mastergu2/article/details/106564450
```python
a='c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2'
flag=''
l=len(a)//2
for i in range(l):
    flag+=chr(int(a[i*2:(i+1)*2],16)%128)
print(flag)
```

# stegano
- 尝试复制pdf的内容，发现pdf内有隐藏的内容
- NoFlagHere! NoFlagHere! NoFlagHere! XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Close - but still not here !
BABA BBB BA BBA ABA AB B AAB ABAA AB B AA BBB BA AAA BBAABB AABA ABAA AB BBA BBBAAA ABBBB BA AAAB ABBBB AAAAA ABBBB BAAA ABAA AAABB BB AAABB AAAAA AAAAA AAAAB BBA AAABB
- 培根密码解密，不行
- 用txt打开，找到这样的内容
  - Producer(find mr.morse text)/Keywords(Could this be the flag? : Tm9wZSAsIG5vdCBoZXJlIDspCg==)
- 尝试使用base64解码，发现没有flag
- 但是这里有提示要使用摩斯电码，所以上面的AB猜测是点的横的组合
```python
a='BABA BBB BA BBA ABA AB B AAB ABAA AB B AA BBB BA AAA BBAABB AABA ABAA AB BBA BBBAAA ABBBB BA AAAB ABBBB AAAAA ABBBB BAAA ABAA AAABB BB AAABB AAAAA AAAAA AAAAB BBA AAABB'
b=''
for i in a:
    if i=='A':
        b+='.'
    if i=='B':
        b+='-'
    if i==' ':
        b+='/'
print(b)
```

- 翻译之后得`congratulations,flag:1nv151bl3m3554g3`