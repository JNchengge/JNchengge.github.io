# AES
- AES为分组密码，AES有不同的分组规范，这里讨论128bit

|AES|密钥长度(32位比特字)|分组长度(32位比特字)|加密轮数|
|:---:|:---:|:---:|:---:|
|AES-128|4|4|10|
|AES-192|6|4|12|
|AES-256|8|4|14|

- AES的大概步骤如下，分为两个大块：
  - 明文加密 
  - 轮密钥产生
- AES算法的基本是分组思想。AES中，基本结构以4*4的矩阵为主，以每一列为一个分组，称为W，明文记为P，密钥记为K
![AES基本结构](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjE5MTMyNTQ4OTA2?x-oss-process=image/format,png "AES基本结构")
-----------------------------
## 密钥扩展
- 首先我们来讨论密钥扩展
- 以AES的基本结构为基础，将128bit的Key化为矩阵形式
![AES密钥扩展](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjIwMDgyMzE2NzM2?x-oss-process=image/format,png "AES密钥扩展")
- 以图片为例，每四个K组成一个W，每四个W组成一轮密钥
- 现讨论W[i]
 - 如果`i%4 != 0`，那么W[i]由以下等式确定
  - W[i]=W[i-4]xorW[i-1]
 - 如果i是4的倍数，那么W[i]由以下等式确定
  - W[i]=W[i-4]xorT(W[i-1]) 
    - T()是轮函数，包括以下三个过程：
      - a.字循环移位：将一个字4byte向左循环移1位
      - b.字节代换：对字循环的结果做S盒替换
      - c.轮常量异或：将前两步的结果盒Rcon[j]进行异或，其中j表示轮数
  |j|1|2|3|4|5|
  |:---:|:---:|:---:|:---:|:---:|:---:|
  |Rcon[j]|01 00 00 00|02 00 00 00 |04 00 00 00|08 00 00 00 |10 00 00 00|
  |j|6|7|8|9|10|
  |Rcon[j]|20 00 00 00|40 00 00 00|80 00 00 00|1B 00 00 00|36 00 00 00|

 - S盒：
 <table><thead><tr><th>行/列</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th></tr></thead><tbody><tr><td>0</td><td>0x63</td><td>0x7c</td><td>0x77</td><td>0x7b</td><td>0xf2</td><td>0x6b</td><td>0x6f</td><td>0xc5</td><td>0x30</td><td>0x01</td><td>0x67</td><td>0x2b</td><td>0xfe</td><td>0xd7</td><td>0xab</td><td>0x76</td></tr><tr><td>1</td><td>0xca</td><td>0x82</td><td>0xc9</td><td>0x7d</td><td>0xfa</td><td>0x59</td><td>0x47</td><td>0xf0</td><td>0xad</td><td>0xd4</td><td>0xa2</td><td>0xaf</td><td>0x9c</td><td>0xa4</td><td>0x72</td><td>0xc0</td></tr><tr><td>2</td><td>0xb7</td><td>0xfd</td><td>0x93</td><td>0x26</td><td>0x36</td><td>0x3f</td><td>0xf7</td><td>0xcc</td><td>0x34</td><td>0xa5</td><td>0xe5</td><td>0xf1</td><td>0x71</td><td>0xd8</td><td>0x31</td><td>0x15</td></tr><tr><td>3</td><td>0x04</td><td>0xc7</td><td>0x23</td><td>0xc3</td><td>0x18</td><td>0x96</td><td>0x05</td><td>0x9a</td><td>0x07</td><td>0x12</td><td>0x80</td><td>0xe2</td><td>0xeb</td><td>0x27</td><td>0xb2</td><td>0x75</td></tr><tr><td>4</td><td>0x09</td><td>0x83</td><td>0x2c</td><td>0x1a</td><td>0x1b</td><td>0x6e</td><td>0x5a</td><td>0xa0</td><td>0x52</td><td>0x3b</td><td>0xd6</td><td>0xb3</td><td>0x29</td><td>0xe3</td><td>0x2f</td><td>0x84</td></tr><tr><td>5</td><td>0x53</td><td>0xd1</td><td>0x00</td><td>0xed</td><td>0x20</td><td>0xfc</td><td>0xb1</td><td>0x5b</td><td>0x6a</td><td>0xcb</td><td>0xbe</td><td>0x39</td><td>0x4a</td><td>0x4c</td><td>0x58</td><td>0xcf</td></tr><tr><td>6</td><td>0xd0</td><td>0xef</td><td>0xaa</td><td>0xfb</td><td>0x43</td><td>0x4d</td><td>0x33</td><td>0x85</td><td>0x45</td><td>0xf9</td><td>0x02</td><td>0x7f</td><td>0x50</td><td>0x3c</td><td>0x9f</td><td>0xa8</td></tr><tr><td>7</td><td>0x51</td><td>0xa3</td><td>0x40</td><td>0x8f</td><td>0x92</td><td>0x9d</td><td>0x38</td><td>0xf5</td><td>0xbc</td><td>0xb6</td><td>0xda</td><td>0x21</td><td>0x10</td><td>0xff</td><td>0xf3</td><td>0xd2</td></tr><tr><td>8</td><td>0xcd</td><td>0x0c</td><td>0x13</td><td>0xec</td><td>0x5f</td><td>0x97</td><td>0x44</td><td>0x17</td><td>0xc4</td><td>0xa7</td><td>0x7e</td><td>0x3d</td><td>0x64</td><td>0x5d</td><td>0x19</td><td>0x73</td></tr><tr><td>9</td><td>0x60</td><td>0x81</td><td>0x4f</td><td>0xdc</td><td>0x22</td><td>0x2a</td><td>0x90</td><td>0x88</td><td>0x46</td><td>0xee</td><td>0xb8</td><td>0x14</td><td>0xde</td><td>0x5e</td><td>0x0b</td><td>0xdb</td></tr><tr><td>A</td><td>0xe0</td><td>0x32</td><td>0x3a</td><td>0x0a</td><td>0x49</td><td>0x06</td><td>0x24</td><td>0x5c</td><td>0xc2</td><td>0xd3</td><td>0xac</td><td>0x62</td><td>0x91</td><td>0x95</td><td>0xe4</td><td>0x79</td></tr><tr><td>B</td><td>0xe7</td><td>0xc8</td><td>0x37</td><td>0x6d</td><td>0x8d</td><td>0xd5</td><td>0x4e</td><td>0xa9</td><td>0x6c</td><td>0x56</td><td>0xf4</td><td>0xea</td><td>0x65</td><td>0x7a</td><td>0xae</td><td>0x08</td></tr><tr><td>C</td><td>0xba</td><td>0x78</td><td>0x25</td><td>0x2e</td><td>0x1c</td><td>0xa6</td><td>0xb4</td><td>0xc6</td><td>0xe8</td><td>0xdd</td><td>0x74</td><td>0x1f</td><td>0x4b</td><td>0xbd</td><td>0x8b</td><td>0x8a</td></tr><tr><td>D</td><td>0x70</td><td>0x3e</td><td>0xb5</td><td>0x66</td><td>0x48</td><td>0x03</td><td>0xf6</td><td>0x0e</td><td>0x61</td><td>0x35</td><td>0x57</td><td>0xb9</td><td>0x86</td><td>0xc1</td><td>0x1d</td><td>0x9e</td></tr><tr><td>E</td><td>0xe1</td><td>0xf8</td><td>0x98</td><td>0x11</td><td>0x69</td><td>0xd9</td><td>0x8e</td><td>0x94</td><td>0x9b</td><td>0x1e</td><td>0x87</td><td>0xe9</td><td>0xce</td><td>0x55</td><td>0x28</td><td>0xdf</td></tr><tr><td>F</td><td>0x8c</td><td>0xa1</td><td>0x89</td><td>0x0d</td><td>0xbf</td><td>0xe6</td><td>0x42</td><td>0x68</td><td>0x41</td><td>0x99</td><td>0x2d</td><td>0x0f</td><td>0xb0</td><td>0x54</td><td>0xbb</td><td>0x16</td></tr></tbody></table>
 
 - 下面举个例子：
 - 设初始的128位密钥为：
   - 3C A1 0B 21 57 F0 19 16 90 2E 13 80 AC C1 07 BD
 - 分为四组：
   - W[0]=3C A1 0B 21 
   - W[1]=57 F0 19 16
   - W[2]=90 2E 13 80
   - W[3]=AC C1 07 BD
 - 第一步，做字循环移位：
   - W[0]=A1 0B 21 3C
   - W[1]=F0 19 16 57
   - W[2]=2E 13 80 90
   - W[3]=C1 07 BD AC
 - 先计算W[4]，4是4的倍数，因此W[4]=w[0]xorT(W[3])
 - 第二步，对W[3]做字节代换：
   - 比如：替换C1，在S盒中找到第C行，第1列
   - S盒第C行，第1列的值为0x78
   - 把C1替换为78
   - 最后的结果为：W[3]=78 C5 7A 91
 - 第三步，对W[3]和Rcon[1]进行xor运算
   - 得到79 C5 7A 91
 - 因此，得到T(W[3])=79 C5 7A 91
 - 最后，再将得到的`T(W[3])=79 C5 7A 91`和W[0]进行xor运算，得到
   - W[4]=45 64 71 B0
 -其余的3个子密钥段的计算如下：
   - W[5] = W[1] ⨁ W[4] = 57 F0 19 16 ⨁ 45 64 71 B0 = 12 94 68 A6
   - W[6] = W[2] ⨁ W[5] =90 2E 13 80 ⨁ 12 94 68 A6 = 82 BA 7B 26
   - W[7] = W[3] ⨁ W[6] = AC C1 07 BD ⨁ 82 BA 7B 26 = 2E 7B 7C 9B
 - 所以，第一轮的密钥为 45 64 71 B0 12 94 68 A6 82 BA 7B 26 2E 7B 7C 9B

- 现在，我们得到了一个44列的轮密钥，一共11组，记为W[i]

## 明文加密

### 初始工作
- 首先将明文128bit/16byte同样化为一个4*4的矩阵
|P0|P4|P8|P12|
|:---:|:---:|:---:|:---:|
|P1|P5|P9|P13|
|P2|P6|P10|P14|
|P3|P7|P11|P15|

- 和密钥的扩展一样，做S盒替换

![S盒替换](https://img-blog.csdnimg.cn/20181213112210707.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI4MjA1MTUz,size_16,color_FFFFFF,t_70)


### 行移位
- 明文加密中的行移位
![行移位](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjE5MTc0MDE1MTY3?x-oss-process=image/format,png)
- 这里的行移位，是在矩阵中，对每一行的操作，和密钥扩展中的字循环移位不同。密钥扩展中的字循环移位是针对每一个W，对字节进行左移一位的操作

### 列混淆

- 所谓的列混淆是通过矩阵相乘来实现的

![列混淆的矩阵相乘](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjE5MjAzMzQ2NDM2?x-oss-process=image/format,png)

- 运算的过程为：

![矩阵相乘](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjE5MjAzNzQyNTE2?x-oss-process=image/format,png)

- 其中，矩阵元素的乘法和加法都是定义在基于GF(2^8)上的二元运算,并不是通常意义上的乘法和加法。这里涉及到一些信息安全上的数学知识，不过不懂这些知识也行。其实这种二元运算的加法等价于两个字节的异或，乘法则复杂一点。对于一个8位的二进制数来说，使用域上的乘法乘以(00000010)等价于左移1位(低位补0)后，再根据情况同(00011011)进行异或运算，设S1 = (a7 a6 a5 a4 a3 a2 a1 a0)，刚0x02 * S1如下图所示：

![二进制乘法](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjE5MjA0ODIyNTE3?x-oss-process=image/format,png)

- 也就是说，如果a7为1，则进行异或运算，否则不进行。
- 类似地，乘以(00000100)可以拆分成两次乘以(00000010)的运算：

![](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjE5MjA1NjAxNjgz?x-oss-process=image/format,png)

- 乘以(0000 0011)可以拆分成先分别乘以(0000 0001)和(0000 0010)，再将两个乘积异或：

![](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjE5MjEwNTU0MTMz?x-oss-process=image/format,png)

### 轮密钥相加

- 现在，将操作好的矩阵和对应轮次的密钥做xor运算

![](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjIwMDgwNTEyMDg2?x-oss-process=image/format,png)

- 然后我们将得到的结果丢到下一轮中去

# 总体操作

- 现在通过一张图来总结一下AES算法

![AES](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTcwMjE5MTYxMjAyNDg1?x-oss-process=image/format,png)


# AES解密

（参考https://blog.csdn.net/qq_28205153/article/details/55798628）