# md5 collision
- 首先这道题完全是不会的，在经过一段时间的对php和MD5的初步学习，希望对之后的题目有所帮助

- 先讨论MD5

- MD5，全称<font color=#FF7F00>Message Digest Algorithm 5，消息摘要算法版本5</font>，用于检查文件是否被更改
- MD5通过一系列复杂的计算，将无论多大的明文，都转换成一个128bit的哈希串
- 因为其高度离散的性质，即使是只改变一个字母，都会造成hash的很大的不同
- MD5一般用作“数字指纹”，也就是：
 - 发送方发送文件时同时发送一个hash
 - 接收方收到时，对明文进行md5计算，得到hash值
 - 比对，相同则没被篡改


- 对于MD5，可以先了解那么多，日后有需要再进行学习

- 再来讨论PHP

- 首先题目直接把php源码给了出来
```php
$md51 = md5('QNKCDZO');
$a = @$_GET['a'];
$md52 = @md5($a);
if(isset($a)){
if ($a != 'QNKCDZO' && $md51 == $md52) {
    echo "nctf{*****************}";
} else {
    echo "false!!!";
}}
else{echo "please input a";}
```

- php还是不难理解的，这里很明显，只要输入的a不等于'QNKCDZO'，且md51==md52时，给出flag
- 但问题是，既然MD5算法离散性特别强，那为什么a不同的时候，md51还可以等于md52？
- 这显然不科学
- 但是这是在不理解php'=='运算符的情况下的认识
- 的确，仅仅只是改变一点，不同a的hash会很不一样
- 但是，根据题目'md5 collision'，联想到可能是跟冲突有关
- 明眼人一眼就知道，这题跟<font color=#FF7F00>php弱类型比较</font>
- PHP 是弱类型语言，在使用 == 号时，如果比较一个数字和字符串或者比较涉及到数字内容的字符串，则字符串会被转换为数值并且比较按照数值来进行
- 也就是说，实际上，这里的md51和md52，比较的是前两个字母`0e`
- 我们只要上网找一个md5 hash开头为0e的字符串就好
- 这里给a=s878926199a
- OK，还差一步，怎么把a输进去
- 这里我突发奇想，试着把?a=s878926199a输入浏览器网址那一行
- 真的就可以了，得到了flag
- 盲猜?的作用是传参数，有待验证

- 对一个新手而言，这题真的不容易，即使是摸着桥过河也很难

# 签到2
1. 尝试输入`zhimakaimen`，发现只能输入10个字符
2. 打开网页源码，发现`maxlength=10`
3. 修改后再次输入，得到flag

# 这题不是web
1. 打开网页后发现是一张图片
2. 下载后尝试使用`base64`，无结果
3. 尝试直接使用文本编辑器打开，找到flag在最后一行

# 层层递进
1. 直接打开源码，展开部分文件夹后，发现有很多重复的html文件
2. 全部打开后发现有1个404网页是独特的
3. flag藏在注释中，用vscode取出并去掉空格获得flag

# AAencode
1. 打开网页，发现是一堆乱码，但是又有规律
2. 用txt转成Unicode编码后，发现是一堆颜文字
3. 根据提示aaencode，推测颜文字是使用aaencode加密后的js
4. 直接在chrome里的console中跑，得到flag

# 单身二十年
- 不用说这题肯定得抓包，这题教会了我怎么使用wireshark好吧
- 点击链接，可以发现浏览器连跳了两个网页
- 所以我猜测是在中间的网页找flag
- 使用wireshark，设置过滤器：`tcp src port 80`
- 为什么设置端口80呢，因为http常用的端口是80
- 常见的服务器软件（应用程序）分配端口如下：
 - FTP：21
 - SSH：22
 - MYSQL：3306
 - DNS：53
 - HTTP：80
 - POP3：109
 - Https：443
- 在里面找到HTTP的包，点击查看，就可以找到了


# php decode
- 题目有问题，最后一行应该用`echo`而不是`eval`
- 可以直接在WAMPSERVER上运行代码，直接得到结果
- 这里做一些对代码的解释
```php
<?php
function CLsI($ZzvSWE) {
 
    $ZzvSWE = gzinflate(base64_decode($ZzvSWE));
 
    for ($i = 0; $i < strlen($ZzvSWE); $i++) {
 
        $ZzvSWE[$i] = chr(ord($ZzvSWE[$i]) - 1);
 
    }
 
    return $ZzvSWE;
 
}
echo CLsI("+7DnQGFmYVZ+eoGmlg0fd3puUoZ1fkppek1GdVZhQnJSSZq5aUImGNQBAA==");
?>
```

- 首先定义了一个函数`CLsI()`
- 声明一个变量`$ZzvSWE`，将其使用`base64`解码并且使用`gzinflate()`对字符串进行解压缩后，重新赋值给`$ZzvSWE`
 - `gzinflate()`对gzip压缩进行解压
- 在循环中，对每个字符做：
 - ord()：取字符的ASCII值
 - ord()取值后-1
 - chr()：将其转换为字符
- 最后返回`$ZzvSWE`

- 所以直接使用echo就好了，为什么要用eval呢，还要报错`Parse error: syntax error, unexpected '{' in C:\wamp\www\new1.php(15) : eval()'d code on line 2`

- 这不就是代码执行不了吗，看到左括号还不猜这就是flag吗

- 注意这里我尝试一步步解码，发现使用ord()的时候，ACSII码竟然超过了128，使用chr()转换为字符的时候，全部都是`'-'`


