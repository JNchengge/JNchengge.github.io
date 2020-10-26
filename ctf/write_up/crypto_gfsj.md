# 

# 云影密码
- 题目给出了一串数字
```
8842101220480224404014224202480122
```
- 这里使用的是云影密码，原理为：
  1. 以0为分界，把数字集分开几组，每组对应一个字符
  2. 求和，发现每组的和都不超过26，所以猜测可能是每组的和对应字母的顺序
- 写代码跑一下
```
a="8842101220480224404014224202480122"
a=a.split("0")
flag=''
for item in a:
   temp=0
   for i in item:
      temp+=int(i)
   flag+=(chr(temp+64))
print(flag)

```
- 得到flag `WELLDONE`

# Railfence
- 栅栏密码，直接在线解密就好
- http://rumkin.com/tools/cipher/railfence.php
- 当Rails=5时，flag为：`cyberpeace{railfence_cipher_gogogo}`

# 不仅仅是Morse
- 先摩斯电码解密
```
may be have another decodehhhhaaaaabaabbbaabbaaaaaaaabaababaaaaaaabbabaaabbaaabbaabaaaababaabaaabbabaaabaaabaababbaabbbabaaabababbaaabbabaaabaabaabaaaabbabbaabbaabaabaaabaabaabaababaabbabaaaabbabaabba
```
- 典型的培根密码
- 直接在线解密，得到flag`cyberpeace{attackanddefenceworldisinteresting}`

# 混合编码
- base64解码得到
```
&#76;&#122;&#69;&#120;&#79;&#83;&#56;&#120;&#77;&#68;&#69;&#118;&#77;&#84;&#65;&#52;&#76;&#122;&#107;&#53;&#76;&#122;&#69;&#120;&#77;&#83;&#56;&#120;&#77;&#68;&#107;&#118;&#77;&#84;&#65;&#120;&#76;&#122;&#69;&#120;&#78;&#105;&#56;&#120;&#77;&#84;&#69;&#118;&#79;&#84;&#99;&#118;&#77;&#84;&#69;&#50;&#76;&#122;&#69;&#120;&#78;&#105;&#56;&#53;&#78;&#121;&#56;&#53;&#79;&#83;&#56;&#120;&#77;&#68;&#99;&#118;&#79;&#84;&#99;&#118;&#77;&#84;&#69;&#119;&#76;&#122;&#69;&#119;&#77;&#67;&#56;&#120;&#77;&#68;&#65;&#118;&#77;&#84;&#65;&#120;&#76;&#122;&#69;&#119;&#77;&#105;&#56;&#120;&#77;&#68;&#69;&#118;&#77;&#84;&#69;&#119;&#76;&#122;&#107;&#53;&#76;&#122;&#69;&#119;&#77;&#83;&#56;&#120;&#77;&#84;&#107;&#118;&#77;&#84;&#69;&#120;&#76;&#122;&#69;&#120;&#78;&#67;&#56;&#120;&#77;&#68;&#103;&#118;&#77;&#84;&#65;&#119;
```
- 可能是ASCII编码，python跑代码试试
```
a='76;&#122;&#69;&#120;&#79;&#83;&#56;&#120;&#77;&#68;&#69;&#118;&#77;&#84;&#65;&#52;&#76;&#122;&#107;&#53;&#76;&#122;&#69;&#120;&#77;&#83;&#56;&#120;&#77;&#68;&#107;&#118;&#77;&#84;&#65;&#120;&#76;&#122;&#69;&#120;&#78;&#105;&#56;&#120;&#77;&#84;&#69;&#118;&#79;&#84;&#99;&#118;&#77;&#84;&#69;&#50;&#76;&#122;&#69;&#120;&#78;&#105;&#56;&#53;&#78;&#121;&#56;&#53;&#79;&#83;&#56;&#120;&#77;&#68;&#99;&#118;&#79;&#84;&#99;&#118;&#77;&#84;&#69;&#119;&#76;&#122;&#69;&#119;&#77;&#67;&#56;&#120;&#77;&#68;&#65;&#118;&#77;&#84;&#65;&#120;&#76;&#122;&#69;&#119;&#77;&#105;&#56;&#120;&#77;&#68;&#69;&#118;&#77;&#84;&#69;&#119;&#76;&#122;&#107;&#53;&#76;&#122;&#69;&#119;&#77;&#83;&#56;&#120;&#77;&#84;&#107;&#118;&#77;&#84;&#69;&#120;&#76;&#122;&#69;&#120;&#78;&#67;&#56;&#120;&#77;&#68;&#103;&#118;&#77;&#84;&#65;&#119'
b=a.split(';&#')
flag=''
for i in b:
    flag+=chr(int(i))
flag2='119/101/108/99/111/109/101/116/111/97/116/116/97/99/107/97/110/100/100/101/102/101/110/99/101/119/111/114/108/100'
c=flag2.split('/')
flag=''
for i in c:
    flag+=chr(int(i))
print(flag)

```
- 因为是直接得到了flag2的序列，所以ASCII码转一下就好了
- 得到flag`welcometoattackanddefenceworld`

# easy_RSA
- 题目描述：在一次RSA密钥对生成中，假设p=473398607161，q=4511491，e=17，求解出d
- 可以使用rsatool解
```
python rsatool.py -p 473398607161 -q 4511491 -e 17
```
- 得到
```
Using (p, q) to initialise RSA instance

n = 2135733555619387051 (0x1da3a65a6d9356ab)

e = 17 (0x11)

d = 125631357777427553 (0x1be550de4f93c61)

p = 473398607161 (0x6e38c17d39)

q = 4511491 (0x44d703)
```
- 也可以使用gmpy2的invert求逆元
```
from gmpy2 import invert
p=473398607161
q=4511491
e=17
d=invert(e,(p-1)*(q-1))
print(d)
```
- 得到flag`125631357777427553`

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

# 转轮机加密
- 结合题目提示托马斯杰斐逊，搜索得到转轮机加密的原理
- https://blog.csdn.net/BigRingKing/article/details/100991878
- 可以手算，也可以python代码实现(懒得写了)


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

已知椭圆曲线加密Ep(a,b)参数为

p = 15424654874903

a = 16546484

b = 4548674875

G(6478678675,5636379357093)

私钥为

k = 546768

求公钥K(x,y)

- p表示素数域内点的个数，a和b是其中的两个大数，这三个数都和椭圆曲线本身是有密切联系的
- G表示基点
- k表示私钥
- 原理：公钥K=k*G，这里的乘法不是数乘，所以需要一些方法解出K
- 在ECCtool中，我们先配置椭圆曲线
1. 首先，这里给的都是10进制数，我们需要先在`Numberbase`处设置10进制
2. 输入p，A，B的数据
3. 输入k，Gx，Gy的数据
4. 点击`CALC R`计算出公钥`13957031351290+5520194834100`

# Broadcast
- 简单题，打开py文件直接得到`flag{fa0f8335-ae80-448e-a329-6fb69048aae4}`
- 题目原来的意思应该是RSA的广播攻击

# Flag_in_your_hand
- 需要一点小操作，先尝试读懂js代码
- 看到有一个很奇怪的函数ck
```javascript
a = ff(a, b, c, d, x[i + 0], 7, -680876936);
        d = ff(d, a, b, c, x[i + 1], 12, -389564586);
        c = ff(c, d, a, b, x[i + 2], 17, 606105819);
        b = ff(b, c, d, a, x[i + 3], 22, -1044525330);
        a = ff(a, b, c, d, x[i + 4], 7, -176418897);
        d = ff(d, a, b, c, x[i + 5], 12, 1200080426);
        c = ff(c, d, a, b, x[i + 6], 17, -1473231341);
        b = ff(b, c, d, a, x[i + 7], 22, -45705983);
        a = ff(a, b, c, d, x[i + 8], 7, 1770035416);
        d = ff(d, a, b, c, x[i + 9], 12, -1958414417);
        c = ff(c, d, a, b, x[i + 10], 17, -42063);
        b = ff(b, c, d, a, x[i + 11], 22, -1990404162);
        a = ff(a, b, c, d, x[i + 12], 7, 1804603682);
        d = ff(d, a, b, c, x[i + 13], 12, -40341101);
        c = ff(c, d, a, b, x[i + 14], 17, -1502002290);
        b = ff(b, c, d, a, x[i + 15], 22, 1236535329);
        ck(s);
        a = gg(a, b, c, d, x[i + 1], 5, -165796510);
        d = gg(d, a, b, c, x[i + 6], 9, -1069501632);
        c = gg(c, d, a, b, x[i + 11], 14, 643717713);
        b = gg(b, c, d, a, x[i + 0], 20, -373897302);
        a = gg(a, b, c, d, x[i + 5], 5, -701558691);
        d = gg(d, a, b, c, x[i + 10], 9, 38016083);
        c = gg(c, d, a, b, x[i + 15], 14, -660478335);
        b = gg(b, c, d, a, x[i + 4], 20, -405537848);
```
- 藏在一堆代码中间
- 查看ck
```javascript
function ck(s) {
    try {
        ic
    } catch (e) {
        return;
    }
    var a = [118, 104, 102, 120, 117, 108, 119, 124, 48,123,101,120];
    if (s.length == a.length) {
        for (i = 0; i < s.length; i++) {
            if (a[i] - s.charCodeAt(i) != 3)
                return ic = false;
        }
        return ic = true;
    }
    return ic = false;
}
```
- charCodeAt()函数的意思为：返回一个字符的Unicode值
- 所以分析一下，前面那个try得在`ic==True`的时候才不会catch以及退出
- 写个python试试s是什么东西
```python
a = [118, 104, 102, 120, 117, 108, 119, 124, 48,123,101,120]
for i in range(len(a)):
    a[i]-=3
b=''
for j in a:
    b+=chr(j)
print(b)
```
- 得到b是这个东西`security-xbu`
- 在网页上输入这个东西，得到`RenIbyd8Fgg5hawvQm7TDQ`

# 告诉你个秘密
- 打开后看到
```
636A56355279427363446C4A49454A7154534230526D6843
56445A31614342354E326C4B4946467A5769426961453067
```
- 盲猜16进制
- 解码后得到
```
cjV5RyBscDlJIEJqTSB0RmhCVDZ1aCB5N2lKIFFzWiBiaE0g
```
- 有1，盲猜base64
- 解码后得到
```
r5yG lp9I BjM tFhBT6uh y7iJ QsZ bhM
```
- 这个东西，就很神奇，因为，这个是键盘密码，一般3~5个一组，在键盘上围住的那个字母就是答案
- 最后找到：TONGYUAN
