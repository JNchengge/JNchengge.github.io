# easychallenge
- 下载文件，发现是一个pyc文件，正常来说是打不开的
- 查询资料发现，在命令行使用`uncompyle`可以将pyc文件反编译
- 参考https://www.cnblogs.com/ttyb/p/6741848.html
- pip安装后，在cmd中输入
```
uncompyle6 test.pyc > test1.py 
```

- 即可看到pyc文件的内容

```python
# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]
# Embedded file name: ans.py
# Compiled at: 2018-08-09 11:29:44
import base64

def encode1(ans):
    s = ''
    for i in ans:
        x = ord(i) ^ 36
        x = x + 25
        s += chr(x)

    return s


def encode2(ans):
    s = ''
    for i in ans:
        x = ord(i) + 36
        x = x ^ 36
        s += chr(x)

    return s


def encode3(ans):
    return base64.b32encode(ans)


flag = ' '
print('Please Input your flag:')
flag = input()
final = 'UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==='
if encode3(encode2(encode1(flag))) == final:
    print('correct')
else:
    print('wrong')
# okay decompiling C:\Users\13415\Downloads\42aa1a89e3ae48c38e8b713051557020.pyc

```

- 分析代码，得到解密思路
1. base32解码得到16进制byte序列
2. 16进制转10进制后，根据encode2和encode1反解

```
import base64
a=base64.b32decode('UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E===')
b=a.hex(' ')
b=b.split(' ')
c=[] #十六进制序列
for i in b:
    c.append('0x'+i)    
d=[] #十进制序列
for i in c:
    d.append(int(i,16))
e2=[] #第一次解密
for i in d:
    i=i^36
    i-=36
    e2.append(i)
e1=[] #第二次解密
for i in e2:
    i-=25
    i=i^36
    e1.append(chr(i))
print(e1)
flag=''
for i in e1:
    flag+=i
print(flag)

```

- 留意一下：
 - bytes.hex(),int(),^的内容

- python中多种进制的转换
- https://blog.csdn.net/u012063703/article/details/42609833

# normal_rsa
- 绝对的劝退题
- 按照以下几个方面来记录
 1. 思路
 2. 学习过程
 3. 配置过程

## 思路
1. 下载后解压缩我们得到两个文件：
     1. flag.enc
     2. pubkey.pem
2. 点击flag.enc，没什么反应，但是猜的出来应该是rsa解密后得到flag
3. 点击pubkey.pem，进firefox，看到
```
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAMJjauXD2OQ/+5erCQKPGqxsC/bNPXDr
yigb/+l/vjDdAgMBAAE=
-----END PUBLIC KEY-----
```
- 这个其实也很好明白，就是公钥e

4. 现在我们有密文，有公钥，要求私钥d，那么我们就需要找到pq两个素数；
5. 我们现在来回顾一下公钥e是怎么来的
     1. 选取pq
     2. n=pq
     3. φ(n)=(p-1)(q-1)
     4. 选取e,使得(e,n)=1
     5. 计算d,使得ed=1(mod φ(n))
6. 我们想要解密，就一定要私钥d，那么整道题的思路就是朝着解d的方向
7. 第一步，利用.pem文件找公钥(e,n)
8. 第二步，利用公钥求出私钥，这里需要大整数分解
9. 解密

## 学习过程
- 整体思路清晰了，接下来就是怎么实现了
- 通过提前查看writeup，我大致知道两个方向
     1. 利用openssl求n
     2. 利用rsatool求d
- openssl是linux自带的加密库，我在windows上也安装了openssl，用法是一样的
- openssl的教程：
     - openssl的基本原理及使用：https://blog.51cto.com/jyxnt/1590235
     - openssl的使用详解：https://www.itread01.com/articles/1476760884.html
- 在cmd中输入指令
```
openssl rsa -pubin -text -modulus -in warmup -in pubkey.pem
```
- openssl就会自动帮我们解出n的16进制
- 我们直接利用python，把n转为10进制，在python命令行下
```python
0xC2636AE5C3D8E43FFB97AB09028F1AAC6C0BF6CD3D70EBCA281BFFE97FBE30DD
```

```
87924348264132406875276140514499937145050893665602592992418171647042491658461
```

- 接下来分解整数，使用网站：http://www.factordb.com/

- 得到p=275127860351348928173285174381581152299，q=319576316814478949870590164193048041239

- 接下来，求私钥d

- 如果不使用工具的话将会特别困难，并且即使计算出了d也没办法进行解密因为不可以将d转换为pem。但是使用rsatool的话就会变得容易很多

- 安装完rsatool之后，我们在Ubuntu上的rsatool文件夹内运行：
```
python rsatool.py -f PEM -o private.pem -e 65537 -p 275127860351348928173285174381581152299 -q 319576316814478949870590164193048041239
```
- 得到
```
Using (p, q) to initialise RSA instance

n =
c2636ae5c3d8e43ffb97ab09028f1aac6c0bf6cd3d70ebca281bffe97fbe30dd

e = 65537 (0x10001)

d =
1806799bd44ce649122b78b43060c786f8b77fb1593e0842da063ba0d8728bf1

p = 275127860351348928173285174381581152299 (0xcefbb2cf7e18a98ebedc36e3e7c3b02b)

q = 319576316814478949870590164193048041239 (0xf06c28e91c8922b9c236e23560c09717)

Saving PEM as private.pem
```

- 我们尝试cat一下private.pem

```
-----BEGIN RSA PRIVATE KEY-----
MIGqAgEAAiEAwmNq5cPY5D/7l6sJAo8arGwL9s09cOvKKBv/6X++MN0CAwEAAQIgGAZ5m9RM5kkS
K3i0MGDHhvi3f7FZPghC2gY7oNhyi/ECEQDO+7LPfhipjr7cNuPnw7ArAhEA8Gwo6RyJIrnCNuI1
YMCXFwIRAJulRkclqWIHx5pNZIAp9VUCEGjeJLIZek+lSut5m+LJ3p0CEDRBEd7C622/wt1+58xO
IfE=
-----END RSA PRIVATE KEY-----
```

- 现在就是最后一步解密了

- 解密，我们需要用到openssl，在终端中输入
```
openssl rsautl -decrypt -in flag.enc -inkey private.pem 
```
- 得到flag

```
PCTF{256b_i5_m3dium}
```

## 配置过程
- 接下来就是最操蛋的安装过程

### windows安装openssl
- 这个很简单，直接在 https://slproweb.com/products/Win32OpenSSL.html 下载安装就好

### Linux安装rsatool
- 这个才是最恶心的
- 先在git上面克隆
```
git clone https://github.com/ius/rsatool
```
- 克隆下来之后，运行setup.py install
```
python setup.py install
```

- 安装完之后我尝试求私钥，却总是报错
![](https://img2020.cnblogs.com/q/2131225/202009/2131225-20200915121051186-588566330.jpg)

- 然后我按照 https://blog.csdn.net/jcbx_/article/details/97250664 的操作全部做了一遍，还是不行

- 最后才知道 参考：https://q.cnblogs.com/q/129227/ 
- 依赖环境安装完成后rsatool.py运行后也出现Attempted "iter" operation on ASN.1 schema object错误。经过一段时间的搜索终于找到问题原因，根本原因是pyasn1库的bug(其他的开源项目中有人提过这个错误的issue)，可采用的解决办法是降低pyasn1库版本来解决报错。
 1. 卸载已安装的pyasn1模块
       pip uninstall pyasn1
 2. 安装低版本的pyasn1模块
       pip install pyasn1==0.4.5

- 然后就可以成功运行了

# easy_ECC
- 原理：椭圆曲线加密原理
- 使用ECCtool可以很快速地解出问题
- 我们先来看题目给的条件
```
已知椭圆曲线加密Ep(a,b)参数为

p = 15424654874903

a = 16546484

b = 4548674875

G(6478678675,5636379357093)

私钥为

k = 546768

求公钥K(x,y)
```

- p表示素数域内点的个数，a和b是其中的两个大数，这三个数都和椭圆曲线本身是有密切联系的
- G表示基点
- k表示私钥
- 原理：公钥K=k*G，这里的乘法不是数乘，所以需要一些方法解出K
- 在ECCtool中，我们先配置椭圆曲线
1. 首先，这里给的都是10进制数，我们需要先在`Numberbase`处设置10进制
2. 输入p，A，B的数据
3. 输入k，Gx，Gy的数据
4. 点击`CALC R`计算出公钥