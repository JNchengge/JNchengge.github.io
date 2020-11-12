# 基础
## 图片头
1. JPEG
 - 文件头标识 (2 bytes): $ff, $d8 (SOI) (JPEG 文件标识) 
 - 文件结束标识 (2 bytes): $ff, $d9 (EOI)
2. TGA
 - 未压缩的前5字节    00 00 02 00 00
 - RLE压缩的前5字节   00 00 10 00 00
3. PNG
 - 文件头标识 (8 bytes)   89 50 4E 47 0D 0A 1A 0A
4. GIF
 - 文件头标识 (6 bytes)   47 49 46 38 39(37) 61
 -                       G    I    F     8    9 (7)     a
5. BMP
 - 文件头标识 (2 bytes)   42 4D
 -                        B    M
6. PCX
 - 文件头标识 (1 bytes)   0A
7. TIFF
 - 文件头标识 (2 bytes)   4D 4D 或 49 49
8. ICO
 - 文件头标识 (8 bytes)   00 00 01 00 01 00 20 20
9. CUR
 - 文件头标识 (8 bytes)   00 00 02 00 01 00 20 20
10. IFF
 - 文件头标识 (4 bytes)   46 4F 52 4D
 -                        F   O  R  M
11. ANI
 - 文件头标识 (4 bytes)   52 49 46 46
 -                        R  I  F   F

# 神奇的Modbus
- 工业设备消息传输使用modbus协议
- 这种工控协议有一些列的操作码，数据藏在这里面不太靠谱，而是藏在了可靠通信的TCP中
- 追踪TCP流可以获得flag
- Modbus学习：https://www.jianshu.com/p/f7fd49a51f23

# somthing_in_image
- 直接记事本查找就好了
- 没什么难的，收获了常用图片头

# pure_color
- 直接stegsolve

