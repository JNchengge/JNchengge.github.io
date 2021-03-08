# 14个寄存器
|名字|英文全称|意义|
|:---:|:---:|:---:|
|ax|accumulate register|累加器|
|bx|based register|基地址寄存器|
|cx|count register|计数器|
|dx|data register|数据寄存器|
|cs|code segment|代码段|
|ds|data segment|数据段|
|ss|stack segment|栈段|
|es|extra segment|附加段|
|ip|instructor point|指令指针|
|sp|stack point|堆栈指针|
|bp|base point|基础指针|
|si|source index|原变址寄存器|
|di|destination index|目的变址寄存器|
|psw|program state word|程序状态字|

# DOSBOX debug命令
1. r——查看寄存器数据，也可以修改CS，IP等寄存器的数据
```bash
r
r ax
r cs
r ip
```

2. a——将代码写入当前地址，可以在后面指定写入地址
```bash
a 2000:0
```

3. t——执行一次代码

4. u——将机器码翻译回汇编语言

5. d——查看指定地址的内容，可以指定查看的数量
```bash
d 2000:0 1f
```

6. e——修改指定位置的内容


# 第一章
## 地址总线
- CPU通过地址总线来指定存储器单元
- 每一根导线可以传输0或者1两个数字，若一共有N根导线，那么寻址能力为：
<center>2^n bit</center>

## 数据总线
- CPU通过数据总线与其他器件进行数据传输
- 每一根导线同样只可以传输0或者1，和寻址不同，数据传输的意义在于**“一次可以传多大的数据”**，若一共有N根导线，那么数据传输能力为
<center>N bit</center>

## 控制总线
- CPU对外部器件的控制是通过控制总线来进行的
- 控制总线是一些不同控制线的集合，有多少根控制总线，就意味着CPU对外部器件的控制种数

```mermaid
graph LR
    CPU->RAM（主存储器）
    CPU->ROM（装有系统BIOS）
    CPU->内存条    
    CPU->显卡（ROM装有显卡BIOS）
    显卡->显示器
    CPU->网卡（ROM装有网卡BIOS）
```

```mermaid
graph LR
    CPU->|0~9FFFH|主随机存储器
    CPU->|A000H~BFFFH|显存地址空间（修改数据会使得屏幕上的显示有变化）
    CPU->|C000H~FFFFH|各个ROM的地址空间（只读，无法修改）
```

# 第二章——寄存器
## CS:IP
1. 注意概念不要混淆：段地址是不乘16的，代码段首地址是乘过16的
2. IP的更改方式：在取完代码之后马上自加一次，无论这条代码是不是jmp，jmp一定改一次
## 代码执行顺序
1. CS:IP送入地址加法器
2. 把CSx16+IP的计算结果送入“输入输出控制电路”
3. 将地址送入地址总线
4. 在内存中找到数据，将数据从数据总线传入“输入输出控制电路”
5. 将代码送入指令缓冲器
6. **IP自加**（这一步非常关键）
7. 执行代码
## jmp指令
```bash
jmp 2000:0 #跳到指定地址
jmp ax     #相当于mov ip,ax ，但是不可以这么用
```



