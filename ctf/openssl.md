#
# 对称加密
```
openssl enc -ciphername [-in filename] [-out filename] [-pass arg] [-e] [-d] [-a/-base64]
       [-A] [-k password] [-kfile filename] [-K key] [-iv IV] [-S salt] [-salt] [-nosalt] [-z] [-md]
       [-p] [-P] [-bufsize number] [-nopad] [-debug] [-none] [-engine id]
```
- -e:加密，可以指明一种加密算法，不指明则使用默认
- -d：解密，可以指定一种解密算法，不指明则使用默认
- -a/-base64：使用base64编码

- 示例：
```
加密：]# openssl enc -e -des3 -a -salt -in fstab -out jiami
解密：]# openssl enc -d -des3 -a -salt -in fstab -out jiami
```


# 单向加密
```
openssl dgst [-md5|-md4|-md2|-sha1|-sha|-mdc2|-ripemd160|-dss1] [-c] [-d] [-hex] [-binary]
       [-out filename] [-sign filename] [-keyform arg] [-passin arg] [-verify filename] [-prverify
       filename] [-signature filename] [-hmac key] [file...]
```
- 示例
```
echo "test" | openssl dgst -md5
```

- 單向加密除了 openssl dgst 工具還有：md5sum，sha1sum，sha224sum，sha256sum ，sha384sum，sha512sum

# 生成密码
```
openssl passwd [-crypt] [-1] [-apr1] [-salt string] [-in file] [-stdin] [-noverify] [-quiet] [-table] {password}
```

- 常用選項有：

  1.  -1：使用md5加密算法

  2.  -salt string：加入隨機數，最多8位隨機數

  3.  -in file：對輸入的文件內容進行加密

  4.  -stdion：對標準輸入的內容進行加密

# 生成随机数
```
openssl rand [-out file] [-rand file(s)] [-base64] [-hex] num
```
- 常用選項有：

  1.  -out file：將生成的隨機數保存至指定文件中

  2.  -base64：使用base64 編碼格式

  3.  -hex：使用16進制編碼格式

# 生成密钥对
```
openssl genrsa [-out filename] [-passout arg] [-des] [-des3] [-idea] [-f4] [-3] [-rand file(s)] [-engine id] [numbits]
```
- 常用選項有：

  1.  -out filename：將生成的私鑰保存至指定的文件中

  2.   -des|-des3|-idea：不同的加密算法

  3.  numbits：指定生成私鑰的大小，默認是512

# RSA
```
openssl rsa [-inform PEM|NET|DER] [-outform PEM|NET|DER] [-in filename] [-passin arg] [-out filename] [-passout arg]
       [-sgckey] [-des] [-des3] [-idea] [-text] [-noout] [-modulus] [-check] [-pubin] [-pubout] [-engine id]
```
- 常用選項：

  1.  -in filename：指明私鑰文件

  2.  -out filename：指明將提取出的公鑰保存至指定文件中

  3.  -pubout：根據私鑰提取出公鑰
