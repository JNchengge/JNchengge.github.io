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

# 工业协议分析2
- wireshark打开下载的文件
- 在UDP中找到几个长度很独特的报文：147、173、179
- 其中，147的报文中含有flag，而173和179的报文中含有许多16进制数
- 将16进制数取出
```
6c61677b37466f4d3253746b6865507a
666c61677b37466f4d3253746b6865507a7d
```
- 16进制转换之后就得到`flag{7FoM2StkhePz}`

# sherlock
- 打开txt后发现是完整的小说，仔细看发现其中有一些字母会很不正常的大写
- 用python把这些字母取下来
```python
with open('ctf/code/sherlock.txt','r') as f:
    text=f.read()
    s=''
    for i in text:
        if i>='A' and i<='Z':
            s+=i
    print(s)
```
- 得到
```
ZEROONEZEROZEROZEROZEROONEZEROZEROONEZEROZEROONEZEROZEROONEZEROONEZEROONEZEROONEZEROZEROZEROONEZEROONEZEROZEROONEONEZEROONEZEROZEROZEROZEROONEONEZEROONEZEROONEZEROONEZEROZEROZEROONEZEROZEROZEROONEONEZEROZEROONEONEONEONEZEROONEONEZEROONEONEZEROONEZEROZEROZEROZEROZEROONEONEZEROZEROZEROONEZEROONEONEZEROZEROONEZEROZEROZEROZEROONEONEZEROZEROONEONEZEROONEZEROONEONEONEONEONEZEROZEROONEONEZEROZEROZEROONEZEROONEONEZEROONEONEONEZEROZEROONEZEROONEONEONEONEONEZEROONEONEONEZEROZEROZEROZEROZEROONEONEZEROONEONEZEROZEROZEROZEROONEONEZEROONEZEROZEROZEROZEROONEONEZEROZEROZEROONEZEROONEONEZEROONEONEONEZEROZEROONEZEROONEONEONEONEONEZEROZEROONEONEZEROONEZEROONEZEROZEROONEONEZEROZEROZEROONEZEROZEROONEONEZEROONEONEONEZEROZEROONEONEZEROZEROONEONEZEROONEONEONEONEONEZEROONE
```
- 显然是二进制了，替换得到：
```
010000100100100101010100010100110100001101010100010001100111101101101000001100010110010000110011010111110011000101101110010111110111000001101100001101000011000101101110010111110011010100110001001101110011001101111101
```
- 每8bit对应一个字节，使用python代码跑一下
```python
with open('ctf/code/sherlock.txt','r') as f:
    text=f.read()
    s=''
    for i in text:
        if i>='A' and i<='Z':
            s+=i
    #print(s)
s='010000100100100101010100010100110100001101010100010001100111101101101000001100010110010000110011010111110011000101101110010111110111000001101100001101000011000101101110010111110011010100110001001101110011001101111101'
a=[s[i*8:i*8+8] for i in range(len(s)//8)]
flag=''
for i in a:
    flag+=chr(int(i,base=2))
print(flag)
```
- 得到flag`BITSCTF{h1d3_1n_pl41n_5173}`

# cr3-what-is-this-encryption
- 题目直接给出了p,q,e,c，就差直接把答案给出来了
- 当成是python解rsa的练习
```python
from gmpy2 import invert
import libnum
p=0xa6055ec186de51800ddd6fcbf0192384ff42d707a55f57af4fcfb0d1dc7bd97055e8275cd4b78ec63c5d592f567c66393a061324aa2e6a8d8fc2a910cbee1ed9 
q=0xfa0f9463ea0a93b929c099320d31c277e0b0dbc65b189ed76124f5a1218f5d91fd0102a4c8de11f28be5e4d0ae91ab319f4537e97ed74bc663e972a4a9119307 
e=0x6d1fdab4ce3217b3fc32c9ed480a31d067fd57d93a9ab52b472dc393ab7852fbcb11abbebfd6aaae8032db1316dc22d3f7c3d631e24df13ef23d3b381a1c3e04abcc745d402ee3a031ac2718fae63b240837b4f657f29ca4702da9af22a3a019d68904a969ddb01bcf941df70af042f4fae5cbeb9c2151b324f387e525094c41 
c=0x7fe1a4f743675d1987d25d38111fae0f78bbea6852cba5beda47db76d119a3efe24cb04b9449f53becd43b0b46e269826a983f832abb53b7a7e24a43ad15378344ed5c20f51e268186d24c76050c1e73647523bd5f91d9b6ad3e86bbf9126588b1dee21e6997372e36c3e74284734748891829665086e0dc523ed23c386bb520
p=int(p)
q=int(q)
n=p*q
phi_n=(p-1)*(q-1)
e=int(e)
c=int(c)
d=invert(e,phi_n)
m=pow(c,d,n)
print(libnum.n2s(m))
```
- 其中两个比较基本的函数`invert()`和`n2s()`一定要会用，另外libnum只支持python2
- 得到flag`ALEXCTF{RS4_I5_E55ENT1AL_T0_D0_BY_H4ND}`

# Decrypt-the-Message
- 诗文密码，原理极其复杂，直接跑别人的代码解`poemcode.py`
- 原理：http://wmbriggs.com/post/1001/
- 注意：使用poemcode的时候，`Note that the poem, msg and cipher has to be alphabetic letters only. No commatas, dots, whatgives.`
- 得到flag`ifyouthinkcryptographyistheanswertoyourproblemthenyoudonotknowwhatyourproblemisabcdefghijklmnopqrstu`

# OldDriver
- Linux`unzip`解压缩得到一个enc.txt文件，打开看到
```
[{"c": 7366067574741171461722065133242916080495505913663250330082747465383676893970411476550748394841437418105312353971095003424322679616940371123028982189502042, "e": 10, "n": 25162507052339714421839688873734596177751124036723831003300959761137811490715205742941738406548150240861779301784133652165908227917415483137585388986274803},
{"c": 21962825323300469151795920289886886562790942771546858500842179806566435767103803978885148772139305484319688249368999503784441507383476095946258011317951461, "e": 10, "n": 23976859589904419798320812097681858652325473791891232710431997202897819580634937070900625213218095330766877190212418023297341732808839488308551126409983193},
{"c": 6569689420274066957835983390583585286570087619048110141187700584193792695235405077811544355169290382357149374107076406086154103351897890793598997687053983, "e": 10, "n": 18503782836858540043974558035601654610948915505645219820150251062305120148745545906567548650191832090823482852604346478335353784501076761922605361848703623},
{"c": 4508246168044513518452493882713536390636741541551805821790338973797615971271867248584379813114125478195284692695928668946553625483179633266057122967547052, "e": 10, "n": 23383087478545512218713157932934746110721706819077423418060220083657713428503582801909807142802647367994289775015595100541168367083097506193809451365010723},
{"c": 22966105670291282335588843018244161552764486373117942865966904076191122337435542553276743938817686729554714315494818922753880198945897222422137268427611672, "e": 10, "n": 31775649089861428671057909076144152870796722528112580479442073365053916012507273433028451755436987054722496057749731758475958301164082755003195632005308493},
{"c": 17963313063405045742968136916219838352135561785389534381262979264585397896844470879023686508540355160998533122970239261072020689217153126649390825646712087, "e": 10, "n": 22246342022943432820696190444155665289928378653841172632283227888174495402248633061010615572642126584591103750338919213945646074833823905521643025879053949},
{"c": 1652417534709029450380570653973705320986117679597563873022683140800507482560482948310131540948227797045505390333146191586749269249548168247316404074014639, "e": 10, "n": 25395461142670631268156106136028325744393358436617528677967249347353524924655001151849544022201772500033280822372661344352607434738696051779095736547813043},
{"c": 15585771734488351039456631394040497759568679429510619219766191780807675361741859290490732451112648776648126779759368428205194684721516497026290981786239352, "e": 10, "n": 32056508892744184901289413287728039891303832311548608141088227876326753674154124775132776928481935378184756756785107540781632570295330486738268173167809047},
{"c": 8965123421637694050044216844523379163347478029124815032832813225050732558524239660648746284884140746788823681886010577342254841014594570067467905682359797, "e": 10, "n": 52849766269541827474228189428820648574162539595985395992261649809907435742263020551050064268890333392877173572811691599841253150460219986817964461970736553},
{"c": 13560945756543023008529388108446940847137853038437095244573035888531288577370829065666320069397898394848484847030321018915638381833935580958342719988978247, "e": 10, "n": 30415984800307578932946399987559088968355638354344823359397204419191241802721772499486615661699080998502439901585573950889047918537906687840725005496238621}]
```
- 有很多密文，n，以及他们都通用一个e
- 尝试分解n，发现都不可以分解
- 结合rsa加密原理我们可以知道，m^e=c(mod n)，且因为n无法分解，都是素数，所以所有n两两互素
- 也就是说，m^e可以使用中国剩余定理解出来
- python代码实现,注意开头加一个`# -*- coding: UTF-8 -*-`不然python2识别不出中文

```python
# -*- coding: UTF-8 -*-
import libnum
a=[{"c": 7366067574741171461722065133242916080495505913663250330082747465383676893970411476550748394841437418105312353971095003424322679616940371123028982189502042, "e": 10, "n": 25162507052339714421839688873734596177751124036723831003300959761137811490715205742941738406548150240861779301784133652165908227917415483137585388986274803},
{"c": 21962825323300469151795920289886886562790942771546858500842179806566435767103803978885148772139305484319688249368999503784441507383476095946258011317951461, "e": 10, "n": 23976859589904419798320812097681858652325473791891232710431997202897819580634937070900625213218095330766877190212418023297341732808839488308551126409983193},
{"c": 6569689420274066957835983390583585286570087619048110141187700584193792695235405077811544355169290382357149374107076406086154103351897890793598997687053983, "e": 10, "n": 18503782836858540043974558035601654610948915505645219820150251062305120148745545906567548650191832090823482852604346478335353784501076761922605361848703623},
{"c": 4508246168044513518452493882713536390636741541551805821790338973797615971271867248584379813114125478195284692695928668946553625483179633266057122967547052, "e": 10, "n": 23383087478545512218713157932934746110721706819077423418060220083657713428503582801909807142802647367994289775015595100541168367083097506193809451365010723},
{"c": 22966105670291282335588843018244161552764486373117942865966904076191122337435542553276743938817686729554714315494818922753880198945897222422137268427611672, "e": 10, "n": 31775649089861428671057909076144152870796722528112580479442073365053916012507273433028451755436987054722496057749731758475958301164082755003195632005308493},
{"c": 17963313063405045742968136916219838352135561785389534381262979264585397896844470879023686508540355160998533122970239261072020689217153126649390825646712087, "e": 10, "n": 22246342022943432820696190444155665289928378653841172632283227888174495402248633061010615572642126584591103750338919213945646074833823905521643025879053949},
{"c": 1652417534709029450380570653973705320986117679597563873022683140800507482560482948310131540948227797045505390333146191586749269249548168247316404074014639, "e": 10, "n": 25395461142670631268156106136028325744393358436617528677967249347353524924655001151849544022201772500033280822372661344352607434738696051779095736547813043},
{"c": 15585771734488351039456631394040497759568679429510619219766191780807675361741859290490732451112648776648126779759368428205194684721516497026290981786239352, "e": 10, "n": 32056508892744184901289413287728039891303832311548608141088227876326753674154124775132776928481935378184756756785107540781632570295330486738268173167809047},
{"c": 8965123421637694050044216844523379163347478029124815032832813225050732558524239660648746284884140746788823681886010577342254841014594570067467905682359797, "e": 10, "n": 52849766269541827474228189428820648574162539595985395992261649809907435742263020551050064268890333392877173572811691599841253150460219986817964461970736553},
{"c": 13560945756543023008529388108446940847137853038437095244573035888531288577370829065666320069397898394848484847030321018915638381833935580958342719988978247, "e": 10, "n": 30415984800307578932946399987559088968355638354344823359397204419191241802721772499486615661699080998502439901585573950889047918537906687840725005496238621}]
N=[item['n'] for item in a]
C=[item['c'] for item in a]
M=1
Mi=[]
Mi_=[]
for i in N:
    M*=i
for i in N:
    Mi.append(M//i)
for i in range(10):
    Mi_.append(libnum.modular.invmod(Mi[i],N[i]))
m_pow_10=0
for i in range(10):
    m_pow_10+=C[i]*Mi[i]*Mi_[i]
m=854589733786598088127099154138504953368140761371523704656865879247874533963639770706597129057405
print(libnum.n2s(m))
```
```python
import gmpy2
m=207767069011310615382005496956699939002724661123322994221751166142695274160861910347361276996042799742560876960023725026707962638166575129135440766865100701316764816670483379054343205951075808999752703332882348125629896107658067054751367722901224219091040510838592389076377332778179355096997243543295505018634634561572451967022510155507636716076240560673569886607358154881030549395513906366427051905370416043155267775715988736634788617468194185922049327782963634886497288418641621769381790420751978088082773658829633825745189702805012204673024347719875566559379781189582566329675268632721978707602317933712815171019007700996700182017336704427281863111341960851776549837229695668747526286721345451749979009955616040973254276606709769043027544927251024901061553394041775684108915439050273468693088021984899729089503269397596389715537835361719103933892287450966618345853058411623620115907347761036477799240200802958348678085348640790171222722538999911355478515625
a=gmpy2.iroot(m,10)
print(a)
```
- 这个m是用gmpy2的iroot()解出来的，最后使用n2s()，得到flag`flag{wo0_th3_tr4in_i5_leav1ng_g3t_on_it}`

# 你猜猜
- 学会识别文件头`504B`，是zip的文件头
- 把16进制复制带HxD中，另存为zip文件
- 打开zip文件，猜密码为123456
- 得到flag`daczcasdqwdcsdzasd`

# wtc_rsa_bbq
- 学会使用RsaCtfTool和wsl的文件移动
- 使用WinHex打开cry300文件，发现zip头`504B`
- wsl移动文件到RsaCtfTool目录下
- 直接使用RsaCtfTool解密发现不行，可能是n太大了，使用openssl查看n的信息
```
openssl rsa -pubin -in key.pem -text -modulus
```
- 得到
```
RSA Public-Key: (8587 bit)
```
- 太大了，尝试使用费马攻击
```
python3 RsaCtfTool.py --publickey key.pem --uncipherfile cipher.bin --attack fermat
```
- 得到
```
flag{how_d0_you_7urn_this_0n?}
```

# ecb_is_easy_as_123
- 学会位图文件的基础
- 位图文件包含头和数据两部分
- 位图文件的头是固定的，数据则不同，但是因为加密之后，头被破坏，导致无法查看位图文件
- 所以给它接一个新的头上去
```python
from Crypto.Util.number import long_to_bytes
f=open('ctf/code/ecb.bmp','rb')
data=f.read()
pre=0x424d76483f00000000007600000028000000000f000070080000010004000000000000483f00000000000000000000000000000000000000000000008000008000000080800080000000800080008080000080808000c0c0c0000000ff0000ff000000ffff00ff000000ff00ff00ffff0000ffffff00ffffffffffffffffffffL
out=long_to_bytes(pre)+data[128:]
f.close()
with open('out.bmp','w') as o:
    o.write(out)
```
- 注意这里要python2
- 打开out.bmp，就可以看到flag了
- `flag{no_penguin_here}`

# fanfie
- 脑洞题，先看题目
```
MZYVMIWLGBL7CIJOGJQVOA3IN5BLYC3NHI
```
- 没什么头绪，但是感觉跟base32有关
- 将`bitsctf`base32加密一下
```
MJUXI43DORTA====
```
- 两者开头比对，发现有共同之处，而且有些字母对是相同的，所以猜测是单表代换或者仿射密码
- 试试仿射密码，把(a,b)对爆出来发现是(13,4)
- 因为是base32的仿射，所以我们的字母表要用base32的字母表，即`A~Z,2~7`
```python
from base64 import b32decode,b32encode
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
```
- 得到`IJEVIU2DKRDHWUZSKZ4VSMTUN5RDEWTNPU`
- 再base32解码一下，注意补充=
```
BITSCTF{S2VyY2tob2Zm}
```

# cr4-poor-rsa
- 直接使用RsaCtfTool工具解不了
- 那就根据公钥解出私钥文件然后在线解就好了
- 两个基础指令
```
openssl rsa -pubin -text -modulus -in warmup -in key.pub
```

```
python rsatool,py -f PEM -o private.pem -p XXX -q XXX
```
- 最后得到private.pem文件就把flag.b64的内容丢去网站解密就好了
- ALEXCTF{SMALL_PRIMES_ARE_BAD}

# banana-princess
- 很好的一题学习题
- 首先先下载pdf，发现是打不开的，很正常，因为加了密
- 然后分析一下加密方式，一般的PDF开头都会有`%PDF-版本号`
- 而加密后的pdf是`%CQS-1.5`
- P->C,13个;D->Q,13个;F->S,13个，所以猜测是ROT13
- Linux中使用tr将文件中的匹配字符串替换
```
cat 9e45191069704531accd66f1ee1d5b2b.pdf | tr 'A-Za-z' 'N-ZA-Mn-za-m' > new.pdf
```
- tr后面第一个字符串为搜索，后面的字符串则是用来和前面的字符串一一替换，这里的两个字符串替换规则符合ROT13，`>`表示输出到一个新的文件
- 把new弄到windows中查看，发现flag被遮挡了
- 这个时候，就需要`pdf to html`了，在网站上整一整，得到flag
- `BITSCTF{save_the_kid}`

# shanghai
- 根据维吉尼亚密码的分析方法，使用python尝试找密钥长度
```python
f=re.finditer('bju',t2)
for i in f:
    print(i)
```
- 找到最大公因数为22
- 尝试11和22的密钥长度
- 直接在网站上解决
- 解出明文

the quick brown fox jumps over 13 lazy dogs. history
the first well-documented description of a polyalphabetic cipher was formulated by leon battista alberti around 1467 and used a metal cipher disc to switch between cipher alphabets. alberti's system only switched alphabets after several words, and switches were indicated by writing the letter of the corresponding alphabet in the ciphertext. later, in 1508, johannes trithemius, in his work poligraphia, invented the tabula recta, a critical component of the vigenère cipher. the trithemius cipher, however, only provided a progressive, rigid and predictable system for switching between cipher alphabets.[citation needed]

what is now known as the vigenère cipher was originally described by giovan battista bellaso in his 1553 book la cifra del sig. giovan battista bellaso.[4] he built upon the tabula recta of trithemius but added a repeating "countersign" (a key) to switch cipher alphabets every letter. whereas alberti and trithemius used a fixed pattern of substitutions, bellaso's scheme meant the pattern of substitutions could be easily changed, simply by selecting a new key. keys were typically single words or short phrases, known to both parties in advance, or transmitted "out of band" along with the message. bellaso's method thus required strong security for only the key. as it is relatively easy to secure a short key phrase, such as by a previous private conversation, bellaso's system was considerably more secure.[citation needed]

blaise de vigenère published his description of a similar but stronger autokey cipher before the court of henry iii of france, in 1586.[5] later, in the 19th century, the invention of bellaso's cipher was misattributed to vigenère. david kahn, in his book, the codebreakers lamented the misattribution by saying that history had "ignored this important contribution and instead named a regressive and elementary cipher for him [vigenère] though he had nothing to do with it".[6]

the vigenère cipher gained a reputation for being exceptionally strong. noted author and mathematician charles lutwidge dodgson (lewis carroll) called the vigenère cipher unbreakable in his 1868 piece "the alphabet cipher" in a children's magazine. in 1917, scientific american described the vigenère cipher as "impossible of translation".[7][8] that reputation was not deserved. charles babbage is known to have broken a variant of the cipher as early as 1854 but failed to publish his work.[9] kasiski entirely broke the cipher and published the technique in the 19th century, but even earlier, some skilled cryptanalysts could occasionally break the cipher in the 16th century.[6]


cryptographic slide rule used as a calculation aid by the swiss army between 1914 and 1940.
the vigenère cipher is simple enough to be a field cipher if it is used in conjunction with cipher disks.[10] the confederate states of america, for example, used a brass cipher disk to implement the vigenère cipher during the american civil war. the confederacy's messages were far from secret, and the union regularly cracked its messages. throughout the war, the confederate leadership primarily relied upon three key phrases: "manchester bluff", "complete victory" and, as the war came to a close, "come retribution".[11]

gilbert vernam tried to repair the broken cipher (creating the vernam–vigenère cipher in 1918), but no matter what he did, the cipher was still vulnerable to cryptanalysis. vernam's work, however, eventually led to the one-time pad, a theoretically-unbreakable cipher.[12]

description

the vigenère square or vigenère table, also known as the tabula recta, can be used for encryption and decryption.
in a caesar cipher, each letter of the alphabet is shifted along some number of places. for example, in a caesar cipher of shift 3, a would become d, b would become e, y would become b and so on. the vigenère cipher has several caesar ciphers in sequence with different shift values.

to encrypt, a table of alphabets can be used, termed a tabula recta, vigenère square or vigenère table. it has the alphabet written out 26 times in different rows, each alphabet shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible caesar ciphers. at different points in the encryption process, the cipher uses a different alphabet from one of the rows. the alphabet used at each point depends on a repeating keyword.[citation needed]

for example, suppose that the plaintext to be encrypted is

attackatdawn.
the person sending the message chooses a keyword and repeats it until it matches the length of the plaintext, for example, the keyword "lemon":

lemonlemonle
each row starts with a key letter. the rest of the row holds the letters a to z (in shifted order). although there are 26 key rows shown, a code will use only as many keys (different alphabets) as there are unique letters in the key string, here just 5 keys: {l, e, m, o, n}. flag, '{' and 'vigenereisveryeasyhuh' and '}' for successive letters of the message, successive letters of the key string will be taken and each message letter enciphered by using its corresponding key row. the next letter of the key is chosen, and that row is gone along to find the column heading that matches the message character. the letter at the intersection of [key-row, msg-col] is the enciphered letter.

for example, the first letter of the plaintext, a, is paired with l, the first letter of the key. therefore, row l and column a of the vigenère square are used, namely l. similarly, for the second letter of the plaintext, the second letter of the key is used. the letter at row e and column t is x. the rest of the plaintext is enciphered in a similar fashion:

plaintext:	attackatdawn
key:	lemonlemonle
ciphertext:	lxfopvefrnhr
decryption is performed by going to the row in the table corresponding to the key, finding the position of the ciphertext letter in that row and then using the column's label as the plaintext. for example, in row l (from lemon), the ciphertext l appears in column a, which is the first plaintext letter. next, row e (from lemon) is gone to, the ciphertext x is located that is found in column t. thus t is the second plaintext letter.

- 找到flag{vigenereisveryeasyhuh}

 # equation-2
- 离谱题目，数学原理有待提升
```python
from gmpy2 import invert
s1="""3acf6684e41176a5b673056b9cd23bd832dc017a57509d471b"""
s2="""00D5A225C0D41B16699C4471570EECD3DD7759736D5781AA7710B31B4A46E441D386DA1345BC97D1AA913F853F850F6D4684A80E6067FB71CF213B276C2CBAED59"""
s3="""1338C593D3B5428CE978BED7A553527155B3D138AEAC084020C0C67F54B953015E55F60A5D31386505E02E6122DAD7DB0A05ECB552E448B347ADC2C9170FA2F3"""
s4="""00d5c8d6dc583ecdf3c321663ba32ae4ab1c9a2ded6702691993184209e93914f0d5adf415634788d5919d84a8d77429959d40fba47b29cf70b943124217c9a431"""
dp=int(s2,base=16)
dq=int(s3,base=16)
qinv=int(s4,base=16)
e=65537
for j in range(1,10000):
    q=((e*dq-1)//j)+1
    if s1 in str(hex(q)):
        break
for i in range(1,100000):
    p=((e*dp-1)//i)+1
    if invert(q,p)==qinv:
        break
print(p)
print(q)
```
- 数学原理：CRT-RSA参数：dp,dq,coefficient
- 还有PEM文件的一般格式，可以在RFC中查看，也可以在我的一堆书签中查看，有待整理
- 首先记住三个重要关系
```
e*dp=1 mod(p-1) dp=d mod(p-1)
e*dq=1 mod(q-1) dq=d mod(q-1)
qi=q^-1 mod(p) qi*q=1 mod(p)
```
- 那么，就有
```
p=((e*dp-1)//k)+1
q=((e*dq-1)//k)+1
qi*q-1=k*p
```
- 根据对PEM16进制的解析，我们得到，注意我们要取02开头的数据，02后面的一位是长度，也要找长度对应的
```
q="""3acf6684e41176a5b673056b9cd23bd832dc017a57509d471b"""
dp="""00D5A225C0D41B16699C4471570EECD3DD7759736D5781AA7710B31B4A46E441D386DA1345BC97D1AA913F853F850F6D4684A80E6067FB71CF213B276C2CBAED59"""
dq="""1338C593D3B5428CE978BED7A553527155B3D138AEAC084020C0C67F54B953015E55F60A5D31386505E02E6122DAD7DB0A05ECB552E448B347ADC2C9170FA2F3"""
qi="""00d5c8d6dc583ecdf3c321663ba32ae4ab1c9a2ded6702691993184209e93914f0d5adf415634788d5919d84a8d77429959d40fba47b29cf70b943124217c9a431"""
```
- 这里q是不完整的，需要还原，就根据上面的三个方程
- 利用字符串匹配可以找到q，然后再根据qi算p
```python
from gmpy2 import invert
s1="""3acf6684e41176a5b673056b9cd23bd832dc017a57509d471b"""
s2="""00D5A225C0D41B16699C4471570EECD3DD7759736D5781AA7710B31B4A46E441D386DA1345BC97D1AA913F853F850F6D4684A80E6067FB71CF213B276C2CBAED59"""
s3="""1338C593D3B5428CE978BED7A553527155B3D138AEAC084020C0C67F54B953015E55F60A5D31386505E02E6122DAD7DB0A05ECB552E448B347ADC2C9170FA2F3"""
s4="""00d5c8d6dc583ecdf3c321663ba32ae4ab1c9a2ded6702691993184209e93914f0d5adf415634788d5919d84a8d77429959d40fba47b29cf70b943124217c9a431"""
dp=int(s2,base=16)
dq=int(s3,base=16)
qinv=int(s4,base=16)
e=65537
for j in range(1,10000):
    q=((e*dq-1)//j)+1
    if s1 in str(hex(q)):
        break
for i in range(1,100000):
    p=((e*dp-1)//i)+1
    if invert(q,p)==qinv:
        break
print(p)
print(q)
```
- 最后得到
```
p=12883429939639100479003058518523248493821688207697138417834631218638027564562306620214863988447681300666538212918572472128732943784711527013224777474072569
q=12502893634923161599824465146407069882228513776947707295476805997311776855879024002289593598657949783937041929668443115224477369136089557911464046118127387
```

- 丢到rsatool里面生成私钥PEM文件

```
python rsatool.py -f PEM -o private.pem -p 12883429939639100479003058518523248493821688207697138417834631218638027564562306620214863988447681300666538212918572472128732943784711527013224777474072569
-q 12502893634923161599824465146407069882228513776947707295476805997311776855879024002289593598657949783937041929668443115224477369136089557911464046118127387
```

- 生成私钥，利用openssl求解

```
openssl rsautl -decrypt -in flag.enc -inkey private.pem
```
- 得到flag`0ctf{Keep_ca1m_and_s01ve_the_RSA_Eeeequati0n!!!}`

# RSA256
- 简单题
- 下载gz文件，解压
```
gzip -d 1.gz
```
- 解压得到两个文件
  - flllllag.txt
  - gy.key
- gy.key可以直接查看
```
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAKm9THp3YzcKBC/mvsfdyEFgLblCx6Ni
0bXTcqTQiRLZAgMBAAE=
-----END PUBLIC KEY-----
```
- 原来是公钥，openssl解析
```
openssl rsa -pubin -text -modulus -in warmup -in gy.key
```
- 得到：A9BD4C7A7763370A042FE6BEC7DDC841602DB942C7A362D1B5D372A4D08912D9
- python int一下，分解
```
p=273821108020968288372911424519201044333
q=280385007186315115828483000867559983517
```
- rsatool生成私钥
- openssl解密之后flag`flag{_2o!9_CTF_ECUN_}`不对，要去掉下划线

# streamgame2
- 和srteamgame1一样爆破得到答案
```python
def lfsr(R,mask):
    output = (R << 1) & 0xffffff
    i=(R&mask)&0xffffff
    lastbit=0
    while i!=0:
        lastbit^=(i&1)
        i=i>>1
    output^=lastbit
    return (output,lastbit)
mask=0x100002
key=[]
f=open('ctf//code//key','rb')
content=f.read()
for i in content:
    key.append(int(i))
for flag in range(2**27):
    R=flag
    tmp=0
    judge=0
    for i in range(12):
        tmp=0
        for j in range(8):
            (R,out)=lfsr(R,mask)
            tmp=(tmp << 1)^out
        if tmp!=key[i]:
            judge=0
            break
        else:
            judge=1
    if judge:
        break
print('flag{'+bin(flag)[2:]+'}')
```

# best_rsa
- 解析publickey1.pem 和 publickey2.pem可得到e1=117,e2=65537且模数为2047位不可分解
- 使用共模攻击
- https://xz.aliyun.com/t/2446
- 原理：
  - 当使用同一个模数，e不同的时候，收到两个密文则可以不需要私钥解出原文
  - 由广义欧几里得除法可知：当gdc(e1,e2)=1,存在s1,s2,使得e1*s1+e2*s2=1
  - 那么，又有方程组：
     - m^e=c1 mod(n)
     - m^e=c2 mod(n)
  - 就有：
     - c1^s1=m^(e*s1) mod(n)
     - c2^s2=m^(e*s2) mod(n)
     - c1^s1*c2^s2=m(e*s1+e*s2) mod (n)
     - c1^s1*c2^s2=m mod (n)
  - 其中，s1,s2不同号，为负数的那个数，需要对应得密文取n的逆元
- 我的代码
```python
from libnum import n2s,s2n
from gmpy2 import invert,gcdext,powmod
from math import pow
n=int(0x67755F890795644EC27E68892B94042C78334C34F9A6D8B6AA488D9B424D64A8B9B2DCC91B1D098A09D7AC4F9A06A4B5267F88F8968B4BAD29235D9A80330845F126B9A865F44C7A77DF72F763F553E99020745F40C8D97F0AB906154FBB1020B588F441F712B2377505B644FE36A78743EE4995B42C7B17B8DF4782EBB595097EE1BE74143261893C4EE2C140DC469E32B17F8AB30E25F07164506B4E79C6B4E3AF5BEA0268427FFB1134FB90A5122729C4EEF17B6D0B12CFBA4E7F14E27AA3C2B4F978E75163242EBD5CBD73829336F9A120E86E25D69CAE0229FDCCEB5B35DC630187B0EEF1532EEC546F4037A6EAB0D0207199B9566011A52F8E9ACD7261)
e1=117
e2=65537
f1=open('cipher1.txt','r')
f2=open('cipher2.txt','r')
c1=s2n(f1.read())
c2=s2n(f2.read())
_,s1,s2=gcdext(e1,e2)
s1=30808
s2=55
c2_=invert(c2,n)
m=(powmod(c1,s1,n)*powmod(c2_,s2,n))%n
print(n2s(m))
f1.close()
f2.close()
```
- 别人的代码
```python
def common_modulus(n, e1, e2, c1, c2):
    """
    ref: https://crypto.stackexchange.com/questions/16283/how-to-use-common-modulus-attack
    ∵gcd(e1,e2)==1,∴由扩展欧几里得算法，存在e1*s1+e2*s2==1
    ∴m==m^1==m^(e1*s1+e2*s2)==((m^e1)^s1)*((m^e2)^s2)==(c1^s1)*(c2^s2)
    """
    assert (libnum.gcd(e1, e2) == 1)
    _, s1, s2 = gmpy2.gcdext(e1, e2)
    # 若s1<0，则c1^s1==(c1^-1)^(-s1)，其中c1^-1为c1模n的逆元。
    m = pow(c1, s1, n) if s1 > 0 else pow(gmpy2.invert(c1, n), -s1, n)
    m *= pow(c2, s2, n) if s2 > 0 else pow(gmpy2.invert(c2, n), -s2, n)
    return m % n
```
- 解得flag`flag{interesting_rsa}`

# safer_than_rot_13
- https://quipqiup.com/

# 工控安全取证
- 学习到了很多东西
- 首先，按照题目描述，下载下来的内容应该再wireshark中查看，把log文件改成pcapng
- 查看后发现是一堆TCP协议文件，且192.168.0.9是被攻击的
- 但是仔细看发现每次扫描攻击前，黑客都会发一个ICMP的请求，结合计算机网络的知识，大概猜出这个人每次扫描的时候都PING了一下靶机
- 那么直接查看ICMP的报文
- 发现刚刚好4组
- 那就第四组一个个试咯，没办法，毕竟靶机没回复了
- 得到flag`flag{155989}`

# cr2-many-time-secrets
- 掌握多字节异或异或加密方式的破解方法，这题是已知部分明文攻击
- 异或加密的原理就是：
  - m xor key =c
  - c xor key =m
- https://www.meiwen.com.cn/subject/plhwzftx.html
- https://www.cnblogs.com/Jlay/p/Xor.html
- 这里使用cribdrag工具可解
- 得到flag`ALEXCTF{HERE_GOES_THE_KEY}`

# 工业协议分析一
- 两种方式进行分析
## 普通做法
- wireshark打开文件，发现有很多MMS、COTP、TCP协议
- 对协议进行分类，在TCP中找到一个长度很离谱的报文
- 点开后发现里面竟然有base64编码的图片
- 取出之后丢到网站上解出flag
## 标准做法
- Linux下wget下载数据包，使用greg指令找flag的内容
```
grep -a "flag" 1.pcap
```
- 找到很多txt，但是都没有用
- 试试其他类型，比如：`jpg,png,zip,rar,flag`
- 找到有png的内容，是base64编码的
- python解码恢复图片
```python
from base64 import b64decode
a="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"
f=open('flag.png','wb')
f.write(b64decode(a))
f.close()
```
- VSCode中查看不到，复制到windows中查看
- 得到flag

# enc
- 打开就是一堆二进制
- 二进制借出来之后看到最后有等号，base64解码
- 解码后得到摩斯电码，再解码得到flag

# 说我作弊需要证据
- 最难的题目之一，需要搞懂TCP协议的内容
- https://blog.csdn.net/zz_Caleb/article/details/89316034
1. SEQ是最后的字符顺序 
2. DATA是需要解密的密文 
3. SIG是RSA的签名，利用Alice的公钥对数据进行一次签名验证 DATA是发送给Bob的实际密文,使用Bob的公钥对DATA进行了加密。所以先使用factor-db并解出私钥来解密数据。
- 流程：
  1. Alice发出报文，并且生成验证
  2. Bob收到报文，用私钥解密
  3. 解密后的数据需要验证，验证通过则留下，不通过则丢弃
```python
from base64 import b64decode,b64encode
from libnum import n2s
from gmpy2 import invert
from Crypto.PublicKey import RSA
f=open('1.txt','r')
a=[]
b=[]
for i in f.readlines():
    a.append(i[:-1])
for i in a:
    b.append(b64decode(i))
Alice_n=0x53a121a11e36d7a84dde3f5d73cf
Bob_n=0x99122e61dc7bede74711185598c7
e=0x10001
n1=int(Alice_n)
n2=int(Bob_n)
p1=38456719616722997
q1=44106885765559411
p2=49662237675630289
q2=62515288803124247
d1=int(invert(e,(p1-1)*(q1-1)))
d2=int(invert(e,(p2-1)*(q2-1)))
A=RSA.construct((n1,e,d1))
B=RSA.construct((n2,e,d2))
flag={}
for i in b:
    i=str(i)
    seq=int(i.split(';')[0].split(' ')[2])
    data=int(i.split(';')[1].split('0x')[1].rstrip('L'),base=16)
    sig=int(i.split(';')[2].split('0x')[1].rstrip('L'),base=16)
    m=B.decrypt(data)
    signcheck=A.sign(m,'')[0]
    if signcheck==sig:
        flag[seq]=n2s(m)
dic=sorted(flag.items(),key = lambda item: item[0])
f=''
for i in dic:
    f+=i[1].decode()
print(f)
```
- 学会使用RSA模块的：
  1. construct
  2. sign：用于验证数据
- 程序分为几个流程（包括前期操作的流程）
  1. 首先打开wireshark，都是TCP的报文，开启追踪流保存数据
  2. 打开文件读写，把内容base64解密
  3. 对每一行的内容（大概长这样`'SEQ = 27; DATA = 0x3cda4bf9b498a68d4cb65bff6fc0L; SIG = 0x1cc712adfa8e3895148458fad2c1L;'`）进行分出
  4. 分出之后，解密data，验证sig，可行则把seq和m加入flag
  5. 对字典进行排序，关键字取seq
  6. 输出字典
  7. 注意使用RSA模块的话很多结果都是byte类型的，需要转形式才可以继续操作
- 最后得到flag`flag{n0th1ng_t0_533_h3r3_m0v3_0n}`

# RSA_gcd
- 这题还是有公因数的题，计算出公因数就很好求两个数的p,q了
```python
from gmpy2 import invert,powmod
from libnum import n2s
n1=23220619839642624127208804329329079289273497927351564011985292026254914394833691542552890810511751239656361686073628273309390314881604580204429708461587512500636158161303419916259271078173864800267063540526943181173708108324471815782985626723198144643256432774984884880698594364583949485749575467318173034467846143380574145455195152793742611717169602237969286580028662721065495380192815175057945420182742366791661416822623915523868590710387635935179876275147056396018527260488459333051132720558953142984038635223793992651637708150494964785475065404568844039983381403909341302098773533325080910057845573898984314246089
n2=22642739016943309717184794898017950186520467348317322177556419830195164079827782890660385734113396507640392461790899249329899658620250506845740531699023854206947331021605746078358967885852989786535093914459120629747240179425838485974008209140597947135295304382318570454491064938082423309363452665886141604328435366646426917928023608108470382196753292656828513681562077468846105122812084765257799070754405638149508107463233633350462138751758913036373169668828888213323429656344812014480962916088695910177763839393954730732312224100718431146133548897031060554005592930347226526561939922660855047026581292571487960929911
p1=138376604533530412400239558340424700312412702699022481119357799054715877829291635290832719835033140580690053865677079316241919169166375123691917675235979462772103681398725285808551041924624882840901583892858174270714471366531758975241868470938138238307005782651296179579961869801841395682782645916848523771439
q1=167807411649676462546661119644113081915542378755778327057156191284453150887662343414908916953154897183613548083558919410359642450001343644814021159828724844730881111955050992398535063409828169462180970629537792676998647880110463527555034040871485964361418080481113059959410616446772218038141157051007091689351
p2=138376604533530412400239558340424700312412702699022481119357799054715877829291635290832719835033140580690053865677079316241919169166375123691917675235979462772103681398725285808551041924624882840901583892858174270714471366531758975241868470938138238307005782651296179579961869801841395682782645916848523771439
q2=163631266233712837481823088378337134151021871060275887871338250274359922218053543333532579728777813509956261662615493179160669715503833949420308311581736674332268131534602581626817039237393599222688271607325131529790640375765697832746614700483681658911753936520482383592478743093233261371451718844275762094649
e=65537
d1=int(invert(e,(p1-1)*(q1-1)))
d2=int(invert(e,(p2-1)*(q2-1)))
c1=9700614748413503291260966231863562117502096284616216707445276355274869086619796527618473213422509996843430296526594113572675840559345077344419098900818709577642324900405582499683604786981144099878021784567540654040833912063141709913653416394888766281465200682852378794478801329251224801006820925858507273130504236563822120838520746270280731121442839412258397191963036040553539697846535038841541209050503061001070909725806574230090246041891486506980939294245537252610944799573920844235221096956391095716111629998594075762507345430945523492775915790828078000453705320783486744734994213028476446922815870053311973844961
c2=20513108670823938405207629835395350087127287494963553421797351726233221750526355985253069487753150978011340115173042210284965521215128799369083065796356395285905154260709263197195828765397189267866348946188652752076472172155755940282615212228370367042435203584159326078238921502151083768908742480756781277358357734545694917591921150127540286087770229112383605858821811640935475859936319249757754722093551370392083736485637225052738864742947137890363135709796410008845576985297696922681043649916650599349320818901512835007050425460872675857974069927846620905981374869166202896905600343223640296138423898703137236463508
m1=powmod(c1,d1,n1)
m2=powmod(c2,d2,n2)
m1=n2s(m1)
m2=n2s(m2)
print(m1)
print(m2)
```
- 得到

```
flag{336BB5172ADE227
FE68BAA44FDA73F3B}
```

# Easy-one（已知明文和密文攻击）
- 一道十分基础的密码题，是已知明文和密文攻击，需要求解密钥再进行解密
- 首先题目给出的密钥是`k[]="CENSORED"`，尝试使用该密钥解密，解不出来
- 查看提示后发现，密钥是不对的，msg001.enc是用题目给的示例加密的，也就是说可以把密钥找出来
- 找到密钥之后破解密文就很容易了，都是使用爆破的方法
- 两步操作合在一起的代码如下
```python
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
```
- 最后得到
```
The known-plaintext attack (KPA) is an attack model for cryptanalysis where the attacker has samples of both the plaintext (called a crib), and its encrypted version (ciphertext). These can be used to reveal further secret information such as secret keys and code books. The term "crib" originated at Bletchley Park, the British World War II decryption operation. 
The flag is CTF{6d5eba48508efb13dc87220879306619}
```
# 简单流量分析
- 打开之后，发现全是ICMP报文，其中有`no respones found`的内容，查询之后猜测可能是ICMP重定向攻击
- https://blog.csdn.net/wuyou1995/article/details/105186240
- 但是仔细一想没有中间人，检查了一下所有报文都是192.168.7.73和54.199.175.227之间的报文
- 查询之后发现，原来flag藏在了ICMP报文的长度里面（淦，谁想得到）
- 甚至还附带对pcap文件神器pyshark（数据包不可以爬的时候我人要气死了）
- OK上代码
```python
from base64 import b64decode
import pyshark
flag=[]
packets=pyshark.FileCapture('fetus_pcap.pcap')
for packet in packets:
    for pk in packet:
        if pk.layer_name=='icmp':
            if int(pk.type)!=0:
                flag.append(int(pk.data_len))
for i in range(len(flag)):
    flag[i]=chr(flag[i])
print(b64decode('Ojpcbm1vbmdvZGI6IToxNzg0MzowOjk5OTk5Ojc6OjpcbnVidW50dTokNiRMaEhSb21URSRNN0M0bjg0VWNGTEFHe3h4MmI4YV82bW02NGNfZnNvY2lldHl9Ojo='))
```
- 注意Linux下和VScode中都不可以跑，但是在命令行python中可以执行
- 解出来base64编码
- 解码得到flag`flag{xx2b8a_6mm64c_fsociety}`
