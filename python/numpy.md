# 
# Numpy Ndarray对象
```python
numpy.array(object,dtype=None,copy=True,order=None,subok=False,ndmin=0)
```
- 参数说明：
|名称|描述|
|:---:|:---:|
|object|数组或者嵌套的数列|
|dtype|数组元素的数据类型，可创建|
|copy|对象是否需要复制|
|order|创建数组的样式，C为行方向，F为列方向，A为任意方向|
|subok|默认返回一个与基类类型一致的数组|
|ndmin|指定生成数组的最小维度|

## 创建对象
```python
import numpy as np
a=np.array([1,2,3])
print(a)

[1,2,3]
```
```python
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

```python
a=np.array([[1,2,3],[4,5,6],[7,8]])
print(a)

[list([1, 2, 3]) list([4, 5, 6]) list([7, 8])]
```

## 最小维度
```python
a=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=2)
print(a)

[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

```python
a=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)
print(a)

[[[1 2 3]
  [4 5 6]
  [7 8 9]]]
```
- 区别：3维度的比2维度的多了一对括号

# Numpy数据类型
|名称|描述|范围|
|:---:|:---:|:---:|
|bool_|布尔类型||
|int_|默认的整数类型|类似于C中的long,int32,int64|
|intc|与C的int一样|一般是int32和int64|
|intp|用于索引的整数类型|一般情况下是int32和int64|
|int8|字节(-127~128)|-128~127|
|int16|整数16字节|-32678~32677|
|int32|整数32字节|-2147483648~2147483647|
|int64|整数64字节|-9223372036854775808~9223372036854775807|
|uint8|无符号整数|0~255|
|uint16|无符号整数|0~65535|
|uint32|无符号整数|0~4294967295|
|uint64|无符号整数|0~18446744073709551615|
|float_|默认的浮点类型|float64|
|float16|半精度浮点数|1个符号位。5个指数位，10个尾数位|
|float32|单精度浮点数|1个符号位，8个指数位，23个尾数位|
|float64|双精度浮点数|1个符号位，11个指数位，52个尾数位|
|complex_|128位复数||
|complex64|双32位复数||
|complex128|双64位复数||

## 类型字段名
- 使用类型字段名可以使ndarray形成一个类似C语言结构体的结构
```python
import numpy as np
dt=np.dtype([('foo',np.int8)])
a=np.array([(10,),(20,),(30,)],dtype=dt)
print(a)
print(a['foo'])
```
```
[(10,) (20,) (30,)]
[10 20 30]
```
- 注意：
- dtype格式：一个列表，列表中的“结构体”使用圆括号括起来,只能使用一个列表
- 如果单指元素的类型和大小，则直接写就好
```python
import numpy as np
dt=np.dtype([('foo',np.int8)],[('bar',np.int16)])
a=np.array([[(10,),(20,),(30,)],[(40,),(50,),(60,)]],dtype=dt)
print(a)
print(a['foo'])
print(a['bar'])
```
```
[[(10,) (20,) (30,)]
 [(40,) (50,) (60,)]]
[[10 20 30]
 [40 50 60]]
Traceback (most recent call last):
  File "/home/ch/docs/python/test.py", line 6, in <module>
    print(a['bar'])
ValueError: no field of name bar
```
### 使用多个内建类型
```python
import numpy as np
dt=np.dtype([('foo',np.int8),('bar',np.float_)])
a=np.array([[(10,40.0),(20,50.0),(30,60.0)]],dtype=dt)
print(a)
print(a['foo'])
print(a['bar'])
```
```
[[(10,  40.) (20,  50.) (30,  60.)]]
[[10 20 30]]
[[ 40.  50.  60.]]
```
### 每个内建类型都有一个唯一定义它的字符代码
|字符|对应类型|
|:---:|:---:|
|b|布尔|
|i|int|
|u|unsigned int|
|f|float|
|c|complex|
|m|timedelta（时间间隔）|
|M|datetime（日期时间）|
|O|（Python）对象|
|S,a|字符串|
|U|Unicode|
|v|原始数据(void)|

# numpy数组属性

## ndarray.ndim
- 返回数组的维数(形式上的，并没有化成最简)
```python
import numpy as np
a=np.array([[1,1,1],[0,0,0]])
print(a.ndim)
```

```
2
```

## ndarray.shape
- 返回一个元组，包含数组的行列数
```python
import numpy as np
a=np.array([[1,1,1],[0,0,0]])
print(a.shape)
```

```
(2,3)
```

- 也可用于调整数组
```python
import numpy as np
a=np.array([[1,1,1],[0,0,0]])
a.shape=(3,2)
print(a)
```
```
[[1 1]
 [1 0]
 [0 0]]
```

- 使用reshape方法改变数组
```python
import numpy as np
a=np.array([[1,1,1],[0,0,0]])
b=a.reshape(3,2)
print(b)
```

```
[[1 1]
 [1 0]
 [0 0]]
```

## ndarray.itemsize
- 以字节形式返回数组中每个元素的大小
```python
import numpy as np
a=np.array([[1,1,1],[0,0,0]])
dt=np.dtype(np.int32)
print(a.itemsize)
```

```
8
```

## ndarray.flags
- 返回ndarray对象的内存信息，包括下列：
|属性|描述|
|:---:|:---:|
|C_CONTIGUOUS(C)|数据是在一个单一的C风格的连续段中|
|F_CONTIGUOUS(F)|数据是在一个单一的Fortran风格的连续段中|
|OWNDATA(O)|数据拥有它所使用的内存或者从另一个对象中借用它|
|WRITEABLE(W)|数据区域可以被写入|
|ALIGNED(A)|数据和所有元素都适当的对齐到硬件上|
|UPDATEIFCOPY(U)|这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新|

```python
import numpy as np
a=np.array([[1,1,1],[0,0,0]])
print(a.flags)
```

```
  C_CONTIGUOUS : True
  F_CONTIGUOUS : False
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  UPDATEIFCOPY : False
```

# numpy创建数组

## numpy.empty
- 有参数`shape`,`dtype`,`order`
- 在大小范围内随机生成数组的数字
```python
import numpy as np
a=np.empty(shape=(2,3),dtype=(np.int8))
print(a)
```

```
[[  32   28 -109]
 [   2    0    0]]
```

## numpy.zeros
- 和numpy.empty差不多，使用0填充

## numpy.ones
- 使用1填充

```python
import numpy as np
a=np.zeros(shape=(2,3))
b=np.ones(shape=(3,2),dtype=int)
print(a)
print(b)
```

```
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
[[1 1]
 [1 1]
 [1 1]]
```

# numpy创建数组

## numpy.asarray
- 只有三个参数：`a`,`dtype`,`order`
|参数|描述|
|:---:|:---:|
|a|任意形式的输入参数，可以是：列表、列表的元组、元组、元组的元组、元组的列表，多维数组|
|dtype|数据类型|
|order|C、F|

```python
import numpy as np
x=[1,2,3]
y=([1,],[2,],[3,])
z=(1,2,3)
u=((1,),(2,),(3,))
v=[(1,),(2,),(3,)]
w=[[1,2,3]]
a=np.asarray(x)
b=np.asarray(y)
c=np.asarray(z)
d=np.asarray(u)
e=np.asarray(v)
f=np.asarray(w)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
```

```
[1 2 3]
[[1]
 [2]
 [3]]
[1 2 3]
[[1]
 [2]
 [3]]
[[1]
 [2]
 [3]]
[[1 2 3]]
```

## numpy.frombuffer
- 用于实现动态数组
- 接受buffer输入参数，以流的形式转换为ndarray对象
- 3以上的版本都会显示`AttributeError: 'str' object has no attribute '__buffer__'`

## numpy.fromiter
- 从可迭代对象中创建ndarray对象，返回一维数组
|参数|描述|
|:---:|:---:|
|iterable|可迭代对象|
|dtype|数据类型,<font color=#339900>必须要，否则报错!</font>|
|count|读取的数据数量，默认为-1（全部）|

```python
import numpy as np
a=range(5)
it=iter(a)
b=np.fromiter(it,dtype=int,count=3)
print(b)
```

```
[0 1 2]
```

# numpy从数值范围创建数组

## numpy.arange
- 使用arange函数创建数值范围并返回ndarray对象
|参数|描述|
|:---:|:---:|
|start|起始值，默认为0|
|stop|终止值|
|step|步长|
|dtype|数据类型|
```python
import numpy as np
a=np.arange(2,5,dtype=float)
print(a)
```

```
[ 2.  3.  4.]
```
- 注意：arange使用的是位置参数，位置为`numpy.arange(start,stop,step,dtype)`，其中`dtype`可以关键字参数

## numpy.linspace
- `numpy.linspace`用于创建一个等差一维数组
- numpy.linspace(start,stop,num,endpoint=True,restep=False,dtype=None)
|参数|描述|
|:---:|:---:|
|start|起始位置|
|stop|终点位置，若endpoint为True，则包含stop|
|num|样本数量|
|endpoint|是否包含stop，若为True则为闭区间，否则为左闭右开|
|restep|生成的数组显示间距|
|dtype|数据类型|

```python
import numpy as np
a=np.linspace(1,6,10,endpoint=False,retstep=True)
print(a)
```

```
(array([ 1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,  5.5]), 0.5)
```
- 注意：该等差数列的公差不是输入的，而是根据起始位置和样本数量num自动确定的
- 如果`restep`设置成了`True`，那么返回的对象就是一个元组，进行`reshape`操作的时候，就会报错：
```python
import numpy as np
a=np.linspace(1,6,10,endpoint=False,retstep=True).reshape(1,10)
print(a)
```

```
Traceback (most recent call last):
  File "/home/ch/docs/python/test.py", line 2, in <module>
    a=np.linspace(1,6,10,endpoint=False,retstep=True).reshape(1,10)
AttributeError: 'tuple' object has no attribute 'reshape'
```

- 若`restep=False`则可进行`reshape`操作,在后面加上即可

```python
import numpy as np
a=np.linspace(1,6,10,endpoint=False).reshape(10,1)
print(a)
```

```
[[ 1. ]
 [ 1.5]
 [ 2. ]
 [ 2.5]
 [ 3. ]
 [ 3.5]
 [ 4. ]
 [ 4.5]
 [ 5. ]
 [ 5.5]]
```
## numpy.logspace
- `numpy.logspace`用于创建一个等比数列：
- `numpy.logspace(start,stop,num,endpoint=True,base=10.0,dtype=None)`

|参数|描述|
|:---:|:---:|
|start|起始位置|
|stop|终点位置，若endpoint为True，则包含stop|
|num|样本数量|
|endpoint|是否包含stop，若为True则为闭区间，否则为左闭右开|
|base|取对数时log的下标|
|dtype|数据类型|

```python
import numpy as np
a=np.logspace(0,9,num=10)
b=np.logspace(0,9,num=10,base=2,dtype=int)
print(a)
print(b)
```
```
[  1.00000000e+00   1.00000000e+01   1.00000000e+02   1.00000000e+03
   1.00000000e+04   1.00000000e+05   1.00000000e+06   1.00000000e+07
   1.00000000e+08   1.00000000e+09]
[  1   2   4   8  16  32  64 128 256 512]
```

- 注意：远离其实是根据start,stop,num生成一个等差的空间，然后根据base来对base进行乘方，所以是等比的

# numpy切片和索引
## 切片
1. slice()函数
2. [::]方式
 - 可以包括省略号，以实现行切和列切的效果
 ```python
 import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[...,2]) #第三列元素
print(a[1,...]) #第二行元素
print(a[...,1:]) #第二列和第三列元素
print(a[:2,...]) #和下面一条语句是相同的效果
print(a[:2])     #前两行元素
```
```
[3 6 9]
[4 5 6]
[[2 3]
 [5 6]
 [8 9]]
[[1 2 3]
 [4 5 6]]
[[1 2 3]
 [4 5 6]]
```

# numpy高级索引
## 整数数组索引
- 使用两个列表，一个装行标，一个装列标
- 在两个列表的同一个位置，确定一个数
- 比如：
```python
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) #取四个角的元素
rows=np.array([[0,0],[3,3]]) #行索引为：0，0，3，3
cols=np.array([[0,2],[0,2]]) #列索引为：0，2，0，2
y=a[rows,cols] #组合为：(0,0),(0,2),(3,0),(3,2)
print(y)
```

```
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
[[ 1  3]
 [10 12]]
```

- 也可以借助切片:或...与索引数组组合
- 其实...切片方式也是一种索引

## 布尔索引
- 通过一个布尔数组来索引目标数组
- 比如：
```python
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a[a>5])
```

```
[ 6  7  8  9 10 11 12]
```

- 但是不可以`a[a>5 and a<10]`

- 使用`~`来过滤NaN
```python
import numpy as np
b=np.array([np.nan,1,2,3,np.nan,4,5])
print(b[~np.isnan(b)])
```

```
[ 1.  2.  3.  4.  5.]
```

- 过滤非复数元素
```python
import numpy as np
b=np.array([1+2j,1,2,3,4+5j,4,5])
print(b[np.iscomplex(b)])
```

```
[ 1.+2.j  4.+5.j]
```

## 花式索引
- 利用整数数组进行索引
- 根据索引数组的值来作为目标数组的某个轴来进行取值
- 如果目标是一维数组，那么就取对应位置的值
- 如果是二维数组，就取对应的行
- 支持负号逆取
```python
import numpy as np
a=np.arange(32).reshape(8,4)
print(a)
print()
print()
print(a[[1,2,4,7]]) #输出第2、3、5、8行
```

```
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]
 [24 25 26 27]
 [28 29 30 31]]


[[ 4  5  6  7]
 [ 8  9 10 11]
 [16 17 18 19]
 [28 29 30 31]]
```
- 倒序：
```python
import numpy as np
a=np.arange(32).reshape(8,4)
print(a)
print()
print()
print(a[[-1,-2,-4,-7]]) #输出倒数第1、2、4、7行
```

```
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]
 [24 25 26 27]
 [28 29 30 31]]


[[28 29 30 31]
 [24 25 26 27]
 [16 17 18 19]
 [ 4  5  6  7]]
```
## 使用numpy.ix_索引
- 举个例子：`numpy.ix_([1,5,7,2],[0,3,1,2])`
- 意思是，取：
|||||
|:---:|:---:|:---:|:---:|
|[1,0]|[1,3]|[1,1]|[1,2]|
|[5,0]|[5,3]|[5,1]|[5,2]|
|[7,0]|[7,3]|[7,1]|[7,2]|
|[2,0]|[2,3]|[2,1]|[2,2]|

# numpy广播(broadcast)
- `广播(broadcast)`是对不同`shape`的数组进行计算的方式
- 当运算中的两个数组形状不同时，numpy将自动启动广播机制
- 比如：
```python
import numpy as np
a=np.arange(32).reshape(8,4)
b=np.array([1,2,3,4])
print(a+b)
```

```
[[ 1  3  5  7]
 [ 5  7  9 11]
 [ 9 11 13 15]
 [13 15 17 19]
 [17 19 21 23]
 [21 23 25 27]
 [25 27 29 31]
 [29 31 33 35]]
```

- 即将b重复了8次

## 广播的规则
- 让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
- 输出数组的形状是输入数组形状的各个维度上的最大值。
- 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
- 当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。

# numpy迭代数组

## numpy.nditer
- 使用`nditer`可以灵活地将数组进行迭代
- 不使用`nditer`的情况：
```python
import numpy as np
a=np.arange(10).reshape(5,2)
for item in a:
    for b in item:
        print(b,end=",")
```

```
0,1,2,3,4,5,6,7,8,9,
```

- 使用`nditer`的情况：
```python
import numpy as np
a=np.arange(10).reshape(5,2)
for i in np.nditer(a):
    print(i,end=' ')
```

```
0 1 2 3 4 5 6 7 8 9
```

## 控制遍历顺序
- `for x in np.nditer(a, order='F'):`Fortran order，即是列序优先；
- `for x in np.nditer(a.T, order='C'):`C order，即是行序优先；


## 修改数组中元素的值
- `nditer`默认的模式为只读
- 如果想要修改元素的值，一定要将`op_flags`参数的值改为`readwrite`或`write-only`的模式
```python
import numpy as np
a=np.arange(10).reshape(5,2)
for i in np.nditer(a):
    i[...]=2*i
print(a)
```

```
Traceback (most recent call last):
  File "/home/ch/docs/python/test.py", line 5, in <module>
    i[...]=2*i
ValueError: assignment destination is read-only
```

```python
import numpy as np
a=np.arange(10).reshape(5,2)
for i in np.nditer(a,op_flags=['readwrite']):
    i[...]=2*i
print(a)
```

```
[[ 0  2]
 [ 4  6]
 [ 8 10]
 [12 14]
 [16 18]]
```

- 疑惑:
```python
import numpy as np
a=np.arange(10).reshape(5,2)
for i in np.nditer(a):
    a[...]=2*a
print(a)
```
- 为什么会这样输出？
```
[[   0 1024]
 [2048 3072]
 [4096 5120]
 [6144 7168]
 [8192 9216]]
```
- 解答
```
import numpy as np
a=np.arange(10).reshape(5,2)
print(a)
for i in np.nditer(a):
  print(a[...])
  a[...]=2*a
print(a)
```
- 检查过程

```
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
[[ 0  2]
 [ 4  6]
 [ 8 10]
 [12 14]
 [16 18]]
[[ 0  4]
 [ 8 12]
 [16 20]
 [24 28]
 [32 36]]
[[ 0  8]
 [16 24]
 [32 40]
 [48 56]
 [64 72]]
[[  0  16]
 [ 32  48]
 [ 64  80]
 [ 96 112]
 [128 144]]
[[  0  32]
 [ 64  96]
 [128 160]
 [192 224]
 [256 288]]
[[  0  64]
 [128 192]
 [256 320]
 [384 448]
 [512 576]]
[[   0  128]
 [ 256  384]
 [ 512  640]
 [ 768  896]
 [1024 1152]]
[[   0  256]
 [ 512  768]
 [1024 1280]
 [1536 1792]
 [2048 2304]]
[[   0  512]
 [1024 1536]
 [2048 2560]
 [3072 3584]
 [4096 4608]]
[[   0 1024]
 [2048 3072]
 [4096 5120]
 [6144 7168]
 [8192 9216]]
```
- 其实就是乘了10遍2
- 因为a[...]就是a的全部，每次都乘2

```python
import numpy as np
a=np.arange(10).reshape(5,2)
print(a)
print(a is a[...])
print(a[...])
b=a[...]  #对a[...]进行修改，看是否会修改原来的a的值
b[[0],[0]]=100
print(b)
print(a)  
c=a.copy()  #看a[...]和a.copy()返回的是否同一对象
print(b is c)
```

```
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
False
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
[[100   1]
 [  2   3]
 [  4   5]
 [  6   7]
 [  8   9]]
[[100   1]
 [  2   3]
 [  4   5]
 [  6   7]
 [  8   9]]
False
```

- 显然，对a[...]修改之后，原a的值也会发生改变


## 使用外部循环
- `nditer`类的构造器拥有`flags`参数，接受下列值：
|参数|描述|
|:---:|:---:|
|c_index|根据C顺序索引|
|f_index|根据F顺序索引|
|multi_index|每次迭代可以跟踪一种索引类型|
|external_loop|给出的值是具有多个值的一维数组，而不是零维数组|
```python
import numpy as np
a=np.arange(10).reshape(5,2)
print("原始数组是：")
print(a)
print("修改后的数组是：")
print()
print("列顺序：")
for x in np.nditer(a,flags=['external_loop'],order='F'):
    print(x)
print("行顺序：")
for x in np.nditer(a,flags=['external_loop'],order='C'):
    print(x)
```

```
原始数组是：
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
修改后的数组是：

列顺序：
[0 2 4 6 8]
[1 3 5 7 9]
行顺序：
[0 1 2 3 4 5 6 7 8 9]
```

```python
import numpy as np
a=np.arange(10).reshape(5,2)
print("原始数组是：")
print(a)
print("修改后的数组是：")
print()
print("列顺序：")
for x in np.nditer(a,flags=['external_loop'],order='F'):
    print(x)
print("行顺序：")
for x in np.nditer(a,flags=['c_index']):
    print(x,end=' ')
print()
```

```
原始数组是：
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
修改后的数组是：

列顺序：
[0 2 4 6 8]
[1 3 5 7 9]
行顺序：
0 1 2 3 4 5 6 7 8 9 
```

```python
import numpy as np
a=np.arange(0,10).reshape(5,2)
it=np.nditer(a,flags=['f_index'])
while not it.finished:
    print(it[0],"<",it.index,">")
    it.iternext()
```

```
0 < 0 >
1 < 5 >
2 < 1 >
3 < 6 >
4 < 2 >
5 < 7 >
6 < 3 >
7 < 8 >
8 < 4 >
9 < 9 >
```

```python
import numpy as np
a=np.arange(0,10).reshape(5,2)
it=np.nditer(a,flags=['c_index'])
while not it.finished:
    print(it[0],"<",it.index,">")
    it.iternext()
```
```
0 < 0 >
1 < 1 >
2 < 2 >
3 < 3 >
4 < 4 >
5 < 5 >
6 < 6 >
7 < 7 >
8 < 8 >
9 < 9 >
```
- 使用迭代器迭代的时候，输出元素的顺序是不变的，但是元素的位置会发生改变
- 比如上面两例，使用f_index和c_index输出元素都是一样的，但是他们在数组里面的位置发生了改变
- 应该是一种灵活遍历数组的方式，具体作用有待研究

## 广播迭代
- 如果两个数组是可广播的，那么`nditer`可以同时迭代它们
- 比如：
```python
import numpy as np
a=np.arange(10).reshape(5,2)
b=np.array([1,2])
print("原始数组是：")
print(a)
print(b)
print("修改后的数组是：")
for x,y in np.nditer([a,b]):
    print("%d:%d"%(x,y),end=' ')
print()
```

```
原始数组是：
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
[1 2]
修改后的数组是：
0:1 1:2 2:1 3:2 4:1 5:2 6:1 7:2 8:1 9:2 
```

- 注意，要使用中括号把需要遍历的数组括起来
```python
import numpy as np
a=np.arange(10).reshape(5,2)
b=np.array([1,2])
c=np.array([3,4])
print("原始数组是：")
print(a)
print(b)
print(c)
print("修改后的数组是：")
for x,y,z in np.nditer([a,b,c]):
    print("%d:%d:%d"%(x,y,z),end=' ')
print()
```

```
原始数组是：
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
[1 2]
[3 4]
修改后的数组是：
0:1:3 1:2:4 2:1:3 3:2:4 4:1:3 5:2:4 6:1:3 7:2:4 8:1:3 9:2:4 
```

# numpy数组操作

## 修改数组形状
|函数|描述|参数|
|:---:|:---:|:---:|
|reshape|不改变数据的情况下改变形状|reshape(row,col,order='C'),'C'--按行，'F'--按列，'A'--原顺序，'K'--元素在内存中出现的顺序|
|flat|数组元素迭代器|numpy.ndarray.flat|
|flatten|返回一份数组拷贝，对拷贝所做的修改不会影响原始数组|numpy.ndarray.flatten(order='C')|
|ravel|返回展开数组|numpy.ravel(array,order='C')|

### reshape
- `reshape`的原理是复制原来数组的数据，新建一个ndarray对象
- 比如：
```python
import numpy as np
a=np.arange(10).reshape(5,2)
np.reshape(a,(2,5))
print(a)
```

```
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
```

- 第二行，a引用这个`reshape(5,2)`
- 第三行，因为没有引用，所以a没有改变
- 加一句：
```python
print(a is np.reshape(a,(2,5))) #False
```

### flat
- `numpy.ndarray.flat`是一个数组元素迭代器
```python
import numpy as np
a=np.arange(10).reshape(5,2)
for i in a.flat:
    print(i,end=' ')
print()
```

```
0 1 2 3 4 5 6 7 8 9
```

### flatten
- `numpy.ndarray.flatten`返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
```python
import numpy as np
a=np.arange(10).reshape(5,2)
print(a.flatten())
print(a.flatten(order='F'))
```

```
[0 1 2 3 4 5 6 7 8 9]
[0 2 4 6 8 1 3 5 7 9]
```

### ravel
- 展平数组元素，返回的是数组视图，修改会影响原数组
```python
import numpy as np
a=np.arange(10).reshape(5,2)
print(np.ravel(a))
for i in np.ravel(a):
    a[...]=0
print(a)
```

```
[0 1 2 3 4 5 6 7 8 9]
[[0 0]
 [0 0]
 [0 0]
 [0 0]
 [0 0]]
```

## 翻转数组
|函数|描述|
|:---:|:---:|
|transpose|转置|
|ndarray.T|转置|
|rollaxis|向后滚动指定的轴|
|swapaxes|对换数组的两个轴|


### numpy.rollaxis


### numpy.rollaxis
- `axis`表示要向后滚动的轴的数量
- `start`表示滚动到特定的位置
- 例子：
```python
import numpy as np
a=np.arange(10).reshape(2,5)
b=np.rollaxis(a,1,0)
print(a)
print(b)
```

```
[[0 1 2 3 4]
 [5 6 7 8 9]]
[[0 5]
 [1 6]
 [2 7]
 [3 8]
 [4 9]]
```

```python
import numpy as np
 
# 创建了三维的 ndarray
a = np.arange(12).reshape(3,2,2)
 
print ('原数组：')
print (a)
print ('获取数组中一个值：')
print(np.where(a==10))   
print(a[2,1,0])  # 为 10
print ('\n')

# 将轴 2 滚动到轴 0（宽度到深度）
 
print ('调用 rollaxis 函数：rollaxis(a,2,0)')
b = np.rollaxis(a,2,0)
print (b)
# 查看元素 a[2,1,0]，即 10 的坐标，变成 [0, 2, 1]
print(np.where(b==10))   
print ('\n')
 
# 将轴 2 滚动到轴 1：（宽度到高度）
 
print ('调用 rollaxis 函数：rollaxis(a,2,1)')
c = np.rollaxis(a,2,1)
print (c)
# 查看元素 a[2,1,0]，即 10 的坐标，变成 [2, 0, 1]
print(np.where(c==10))   
print ('\n')

print ('调用 rollaxis 函数：rollaxis(a,0,2)')
d = np.rollaxis(a,0,2)
print (d)
# 查看元素 a[2,1,0]，即 10 的坐标，变成 [1, 2, 0]
print(np.where(d==10))   
print ('\n')
```
```
原数组：
[[[ 0  1]
  [ 2  3]]

 [[ 4  5]
  [ 6  7]]

 [[ 8  9]
  [10 11]]]
获取数组中一个值：
(array([2]), array([1]), array([0]))
10


调用 rollaxis 函数：rollaxis(a,2,0)
[[[ 0  2]
  [ 4  6]
  [ 8 10]]

 [[ 1  3]
  [ 5  7]
  [ 9 11]]]
(array([0]), array([2]), array([1]))


调用 rollaxis 函数：rollaxis(a,2,1)
[[[ 0  2]
  [ 1  3]]

 [[ 4  6]
  [ 5  7]]

 [[ 8 10]
  [ 9 11]]]
(array([2]), array([0]), array([1]))


调用 rollaxis 函数：rollaxis(a,0,2)
[[[ 0  1]
  [ 4  5]
  [ 8  9]]

 [[ 2  3]
  [ 6  7]
  [10 11]]]
(array([1]), array([2]), array([0]))

```

### numpy.swapaxes
- 交换轴

### numpy.transpose
- 转置

## 修改数组维度
|维度|描述|
|:---:|:---:|
|broadcast|产生模仿广播的对象|
|broadcast_to|将数组广播到新形状|
|expend_dims|扩展数组的形状|
|squeeze|从数组的形状中删除一维条目|

### numpy.broadcast
```python
import numpy as np
x=np.array([[1],[2],[3]])
y=np.array([4,5,6])
b=np.broadcast(x,y)
for i in b:
    print(i)
```

```
(1, 4)
(1, 5)
(1, 6)
(2, 4)
(2, 5)
(2, 6)
(3, 4)
(3, 5)
(3, 6)
```
- (3,1)的x和(1,3)的y，新组成了一个(3,3)的数组，每一项都是(x,y)的广播形式

### numpy.broadcast_to
- 直接广播到新形状
- 比如：
```python
import numpy as np
a=np.array([4,5,6])
b=np.broadcast_to(a,(4,3))
print(b)
```

```
[[4 5 6]
 [4 5 6]
 [4 5 6]
 [4 5 6]]
```

### numpy.expand_dims
- 通过在指定位置插入新的轴来扩展数组形状
```python
import numpy as np
a=np.array([4,5,6])
b=np.expand_dims(a,axis=0)
print(b)
print(a.shape,b.shape)
```

```
[[4 5 6]]
(3,) (1, 3)
```

- 原来一维的a，在它自己的0位置插入新的轴后，变成了二维的b

### numpy.squeeze
- 从给定的数组形状中删除一维的条目
```python
import numpy as np
a=np.array([4,5,6])
b=np.expand_dims(a,axis=0)
c=np.squeeze(b)
print(c)
```

```
[4 5 6]
```
