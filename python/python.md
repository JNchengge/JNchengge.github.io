
# 

# 位运算符
<table class="reference", style="font-size:12px">
<tbody><tr>
<th>运算符</th><th>描述</th><th>实例<br>  a = 0011 1100 即60<br>  b = 0000 1101 即13
</th>
</tr>
<tr>
<td>&amp;</td><td>按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0</td><td> (a &amp; b) 输出结果 12 ，二进制解释： 0000 1100</td>
</tr>
<tr>
<td>|</td><td> 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。</td><td> (a | b) 输出结果 61 ，二进制解释： 0011 1101</td>
</tr>
<tr>
<td>^</td><td>按位异或运算符：当两对应的二进位相异时，结果为1 </td><td> (a ^ b) 输出结果 49 ，二进制解释： 0011 0001</td>
</tr>
<tr>
<td>~</td><td> 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。<span class="marked">~x</span> 类似于 <span class="marked">-x-1</span> </td><td> (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。</td>
</tr>
<tr>
<td>&lt;&lt;</td><td>左移动运算符：运算数的各二进位全部左移若干位，由"&lt;&lt;"右边的数指定移动的位数，高位丢弃，低位补0。</td><td> a &lt;&lt; 2 输出结果 240 ，二进制解释： 1111 0000</td>
</tr>
<tr>
<td>&gt;&gt;</td><td>右移动运算符：把"&gt;&gt;"左边的运算数的各二进位全部右移若干位，"&gt;&gt;"右边的数指定移动的位数 </td><td> a &gt;&gt; 2 输出结果 15 ，二进制解释： 0000 1111</td>
</tr>
</tbody></table>

# 列表
## 列表的复制
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/1.PNG)
- 可以看到，无论使用哪种切片方法，对象的id都是相同的
- 但是，我们再使用`is`来判断的时候，发现即使id相同，却返回的是false（这里使用了不同的例子，这是后期的修改）
```python
print(a[1:] is a[2:])
print(id(a[1:]))
print(id(a[2:]))
```

```
False
139713944826760
139713944826760
```
- `is`不是简单的判断id是否相同，而是判断对象是否相同
- 那很显然，a[1:]和a[2:]是不同的对象
- 他们id相同，但不是同一个对象，所以is返回false
## sort and sorted
### sort
- sort是列表和元组的一个方法
- sort将列表或元组对象中的元素进行排序，默认为递增
- 注意：sort是在原来的对象中进行改动
- sort有两个参数：
 1. key:指定带有一个参数的函数，用于从每个列表元素中提取比较键 (例如 key=str.lower)
 2. reverse:True or False

 ```python
a=['d','y','v']
a.sort(key=str.upper,reverse=True)
print(a)
 ```
 ```
['y', 'v', 'd']
 ```
### sorted
- 创建一个新的对象，复制旧对象的内容，改动新对象的内容
```python
a=['d','y','v']
b=sorted(a,key=str.upper,reverse=True)
print(b)
print(a is b)
```

```
['y', 'v', 'd']
False
```

- 显然a和b是不同的
## 切片对象的原理
- 不同的切片对象虽然使用同样的id，但是始终是不一样的对象
- 因为`切片对象`属于生存周期极短的对象，python将会把这些对象放在一个相同的id里面
- It simply sets certain values in the already existing object as specified by the slice notation to those given on the right hand side of the assignment——from stackoverflow
- 结合list.clear和del()可以更好地理解
```python
a=[1,2,3,4,5,6]
del a[:]
print(a)
```

```
[]
```

```python
a=[1,2,3,4,5,6]
a.clear()
print(a)
```

```
[]
```

- 所以可以看出来，切片只是将元素放在了一个已经存在的对象里面，当我们修改切片中的元素的时候，其实就是对原列表元素的修改

```python
a=[1,2,3,4,5,6]
print(a[1:][0] is a[1])
```

```
True
```
## 列表对象的方法
|方法|用途|参数|其他|
|:---:|:---:|:---:|:---:|
|list.append(x)|在列表的末尾添加一个元素||相当于a[len(a):]=[x]（这里做的是索引，所以可以直接更改list里面的元素）；无返回值|
|list.extend(iterable)|在列表的末尾添加一个可迭代对象||相当于a[len(a):]=[iterable]；无返回值|
|list.insert(i,x)|在列表的位置i插入x|i的范围为`[0,len(a)]`|无返回值|
|list.remove(x)|移除列表中第一个值为x的元素，如果找不到x则抛出ValueError异常||可以在嵌套的列表中移除元素，无返回值|
|list.pop([i])|删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中的最后一个元素||方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号|
|list.clear()|移除列表中的所有元素|无参数|等价于del(a[:])|
|list.count(x)|返回元素x在列表中出现的次数||注意这个方法是有返回值的|
|list.reverse()|翻转列表||无返回值|
|list.copy()|浅复制列表||相当于a[:]|

### list.extend
- 例子：
```python
a=[1,2,3,4,5,6]
b=[7,8,9]
c=(1,2,3)
a.extend(b)
print(a)
a.extend(c)
print(a)
```

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
```

- 但是
```python
a=[1,2,3,4,5,6]
b=[7,8,9]
c=(1,2,3)
print(a.extend(b))
print(a.extend(c))
```

```
None
None
```

- 当直接输出时，返回None
- 因为该方法没有返回值，只会在已存在的列表中添加新的列表内容（菜鸟教程）
- list.append也是同理

# 深复制和浅复制
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/2.PNG)
- 可以看出，当使用copy方法时，虽然copy和origin的id不同，但是更深层次的deeper还是原来的id，所以这里只是
- 对对象deeper做了一个引用并非复制
- 然后我们再创建一个新的列表对象[1,2,3,deeper]
- 可以发现，这个新的列表对象和origin虽然值相同但是id是不一样的，
- 但是deeper却还是引用原来的deeper！
- 若要做深复制，应该使用copy模块中的deepcopy()

# 不可变对象和可变对象
- Python中的大部分对象都是不可变对象，例如 int , str , complex 等。变量是指向某个对象的引用，多个变量可以指向同一个对象。给变量重新赋值，并不改变原始对象的值，只是创建一个新对象，并指向该变量
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/3.PNG)
- 虽然都是id(a)，但是因为int对象的不同，因此id也不同，变量a只是int对象的一个引用
- 再看b，b的id和25的id是一样的，说明是b引用了int(25)这个对象

# 一些好用的函数

## enumerate
- 可用于记录当前迭代次数
- 一般形式：`enumrate(_sequence_,[start=0])`,`start`是起始标号。
- 当迭代类型是有序序列，迭代标号等同于当前临时变量在序列中的索引。
```python
for i,name in enumerate(student_name):
    print("编号："+str(i).zfill(3)+"\t学生姓名："+name)
```
```python    
for i,name in enumerate(student_name,start=1):
    print("编号："+str(i).zfill(3)+"\t学生姓名："+name)
```

- `zfill()`表示填充满三位数

## zip
- zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*号操作符有，可以将元组解压为列表
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/zip-1.PNG)
<br>
- 此例中，列表a和列表d,zip后其中元素被两两打包为一个元组
 - 列表a和列表c,zip后其中元素同样被打包为元组，但是因为a比c短，因此只返回3的长度
 - 列表zipped通过*解压后，将列表a和列表d的元素重新打包，并返回一个二维矩阵式
<br>

- zip三个列表:(以及解压)
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/zip-2.PNG)

- <font color=#AA0000>杨辉三角的实现</font>
- 利用zip的功能，来实现错位相加：
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/zip-3.PNG)
- [0]+a:在a的前面加一个[0]
- a+[0]:在a的后面加一个[0]
- 那么每次循环执行sum(i)的时候，i从两个元组之中各取一个并相加，
- 创建一个新的列表，归到生成器中
- 最后输出的时候，注意每两个数之间要有一个空格才能保持整齐

## eval()
- `eval()`函数可以将字符串当成代码执行
- `eval()`包含三个参数，字符串，`locals()`和`globals()`
 1. 若只含`locals()`，将操作局部变量
 2. 若只含`globals()`，将操作全局变量
 3. 若两者都含，若`eval()`函数所在位置有局部变量，且`locals()`函数在后面，则操作`eval()`函数当前位置的局部变量，否则操作全局变量（后面覆盖前面）
 ![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/eval-1.PNG)
 <img src="https://cdn.jsdelivr.net/gh/JNchengge/image@master/eval-2.PNG" width="2500" height="230"/>

## locals()和globals()

- locals()会以字典类型返回当前位置的全部局部变量
- globals()会以字典类型返回当前位置的全部全局变量

![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/locals&globals.PNG)

<img src="https://cdn.jsdelivr.net/gh/JNchengge/image@master/locals&globals-2.PNG" width="2000" height="90"/>

- 局部变量为函数fuction_1中的num1,a,b三项
- 全局变量为开头的a,b两项
- 所显示的都是该行代码之前的所有相应类型的变量

# 字典

- 刚开始学习字典应该从：<font color=#FF7F00>键值对的理解、添加键值对、删除键值对、创建字典、输出字典、循环遍历字典</font>开始

## 键值对
- 字典是python中的数据类型，和列表元组不同的地方是，字典是通过关键字索引的
- 在字典中，每一个关键字对应一个值value（value可以为None）
- 关键字一定是<font color=#FF7F00>不可变类型</font>，而值不一定

## 添加键值对
- 使用创建和添加的方法
- 创建是指：原本字典中没有关键字的情况下，直接进行索引，再进行赋值
```python
a={'foo':1,'bar':2}
a['foobar']=3
print(a)
```

```
{'foo': 1, 'bar': 2, 'foobar': 3}
```

- 当然，必须得赋值，python才会在字典对象中创建一个新的映射关系

## 删除键值对
- 直接使用`del()`语句即可
- 注意不可以使用不存在的关键字

## 创建字典
1. 使用{}的方式创建
2. 
 1. 使用`dict()`，直接从键值对序列里创建字典
 ```python
 a=[('foo',1),('bar',2),('foobar',3)]
 b=dict(a)
 print(type(b))
 print(b)
 ```

 ```
 <class 'dict'>
 {'foo': 1, 'bar': 2, 'foobar': 3}
 ```
 2. 直接使用`dict()`来创建字典
 ```python
 a=dict(foo=1,bar=2,foobar=3)
 print(a)
 ```
 ```
{'foo': 1, 'bar': 2, 'foobar': 3}
 ```
 
3. 使用表达式的方法创建字典
```python
a={x:x**2 for x in range(5)}
print(a)
```
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```


## 输出字典
1. 使用`list(dict)`的方式,可以将所有键以列表的形式输出
```python
a={'foo':1,'bar':2}
a['foobar']=None
print(list(a))
```

```
['foo', 'bar', 'foobar']
```

2. 使用`dict.keys()`和`dict.values()`方法输出键和值
```python
a=dict(foo=1,bar=2,foobar=3)
print(a.keys()) # 返回类型'dict_keys'
print(a.values()) # 返回类型'dict_values'
```

```
dict_keys(['foo', 'bar', 'foobar']) 
dict_values([1, 2, 3])
```

3. 使用循环的方式遍历字典
 1. 使用items()方法将关键字和值同时取出
 ```python
 a=dict(foo=1,bar=2,foobar=3)
 for k,v in a.items():
    print(k,v)
 print(a.items())
 print(type(a.items())) #返回a.items()类型————`dict_items`
 ```

 ```
 foo 1
 bar 2
 foobar 3
 dict_items([('foo', 1), ('bar', 2), ('foobar', 3)])
 <class 'dict_items'>
 ```
 
 2. 在序列中循环时，用`enumrate()`函数将其索引位置和对应的值取出
 ```python
 for i,v in enumerate(['foo','bar','foobar']):
    print(i,v)
 ```

 ```
 0 foo
 1 bar
 2 foobar
 ```

## get()

- `get()`函数用于检查字典中key是否存在，可以避免以键取值时，键不存在而报错
- `get()`有两个参数，一个是`key`，一个是返回值`fallback value`
- `fallback value`的用处是：当字典中没有要检查的关键字时，返回`fallback value`的值
```python
a={'1':'001'}
a.get('1')
a.get('2','002')
```

## setdefault()

- `setdefault()`函数同样用于检查字典中`key`是否存在
- 但是与`get()`不一样的地方是，若不存在，则在字典中添加相应的键值对
- 如果没有值，则赋`None`
```python
a={'1':'001','3':'003','2':'002'}
a={'1':'001','3':'003','2':'002'}
a.setdefault('4')
a.setdefault('5','005')
print(a)     
'001'
{'1': '001', '3': '003', '2': '002', '4': None}
{'1': '001', '3': '003', '2': '002', '4': None, '5': '005'}
 ```

## update()

- `update()`函数用于将一个字典的值更新到另一个字典中

```python
a={'1': '001', '3': '003', '2': '002', '4': None, '5': '005'}
a.update({'1':None})
a.update('6':'006')
print(a)   
{'1': None, '3': '003', '2': '002', '4': None, '5': '005', '6': '006'}
```
- 可以看到，`update`一个已存在的键时，会更新它的值；`update`一个不存在的键时，会插入一个新的键值对（字典）

- import模块`pprint`,可以使用`pprint()`,以字典方式打印字典


# 元组
<font size=3px>初始化只有1个元素的元组时，需在元素后加一个逗号，否则将看成是计算意义的括号;
**元组可以为空()，类型为tuple**</font>

- 修改元组变量
```python
dimentions=(200,50)
print(dimentions[0])
print(dimentions[1])
200
50
```
修改只能是创建一个新的元组对象，重新引用

```python
dimentions=(400,100)
```
- 如果需要存储的一组值在程序的整个生命周期内都不变, 可使用元组.






# 函数
1. 位置实参：按位置传递实参
2. 关键字实参：按关键字的值传递实参
3. 默认值：在编写函数时，赋给形参一个值
4. 传递任意数量的实参：使用*符号，让python创建一个元组，并将所有收到的值放进元组中,<font color=#AA0000>使用**符号，则是创建一个空字典</font>

5. 导入模块：`import+文件名`，导入模块后，使用“方法”的方式使用函数（文件名.函数名）
6.  `from+文件名+import+函数名[1],函数名[2],+……`，可以直接使用这些函数
7. `from+文件名+import+函数名[1]+as+别名`，也可以为模块起别名`import+文件名+as+别名`
8. `from+文件名+import+*`，导入全部函数

## 汉诺塔问题
### 实现一个普通的汉诺塔
- 汉诺塔问题可以分解为三个子问题：
 1. 把前n-1个圆盘从a移动到b上(a-->b)
 2. 把第n个圆盘从a移动到c上(a-->c)
 3. 把前n-1个圆盘从b移动到a上(b-->c)
- 使用递归可以很直接地表现：
```python
def Hanoi(a,b,c,n):
    if n==1:
        print(a+"->"+c)
    else:
        Hanoi(a,c,b,n-1)  #把前n-1个圆盘从a移动到b上(a-->b)
        Hanoi(a,b,c,1)    #把第n个圆盘从a移动到c上(a-->c)
        Hanoi(b,a,c,n-1)  #把前n-1个圆盘从b移动到a上(b-->c)
a,b,c='A','B','C'
Hanoi(a,b,c,3)
```

```
A->C
A->B
C->B
A->C
B->A
B->C
A->C
```

### 进阶
- 提供一个表示圆盘放置状态的字符串，利用这个字符串解决Hanoi问题
- 例子：`next_state_list("111")结果为：["113","123"]`
 - "111"表示：ABC三个圆盘都在1号柱子上
 - "113"表示：第二和第三个圆盘在1号柱子上，第一个圆盘在3号柱子上
- 和普通版的问题不同，这个问题涉及到了具体的圆盘的位置移动
- 而且，圆盘的表示顺序是倒过来的
- 思路：
 1. 首先确定只有一个盘的时候，要怎么操作：
  - 只有一个盘的时候，也就是考虑最后一个盘的情况，毫无疑问，一定是从a移到c，那我们就找到a的位置（不用担心找错，因为这个时候只有一个a），将它改为c
  - 为什么这里说a,b,c呢，实际上因为情况的不同，a,b,c的角色也会发生变化
  - 比如在做前n-1个圆盘从a移到b时：1号为a，2号为c，3号为b
  - 还需要注意的是，在做这一步之前，我们要先把列表倒序，转为我们普通情况的思路
  - 当然是需要还原的，在移动之后把顺序倒回来，递归的时候就可以实现复原了
 2. 那么接下来，我们递归实现就没问题了，这里可以多设置一个参数l；因为我们操作的是列表，那列表长度始终不变，设置一个l来隐式地表示列表的长度是在变化的
  - 代码如下：
```python
def next_state_list(state,a,b,c,l):
    if l==1:
        state=state[::-1]
        state[state.index(a)]=c
        state=state[::-1]
        print(state)
        return state
    else:
        state=next_state_list(state,a,c,b,l-1)
        state=next_state_list(state,a,b,c,1)
        state=next_state_list(state,b,a,c,l-1)
        return state  #这一步非常关键，如果不返回，那么再回到l=2的时候，就没有state返回了，state变成了Noneobject
a,b,c='1','2','3'
next_state_list(['1','1','1'],a,b,c,3)
```

```
['1', '1', '3']
['1', '2', '3']
['1', '2', '2']
['3', '2', '2']
['3', '2', '1']
['3', '3', '1']
['3', '3', '3']
```
### 思考题
- 思考题：完成next_state_list函数
- 举例：next_state_list("111")结果为：["112","113"]

- 思维方式：按位思考
 - 盘子分为三种，短盘、中盘、长盘，轮流考虑三个柱子：
     - 短盘是否可以移到柱子上
         - 取决于：
             1. 现在考虑的柱子是不是短盘当前位置
                 - 如果是，则不移动
                 - 如果不是，则移动到这个柱子
     - 中盘是否可以移到柱子上
         - 取决于：
             1. 现在考虑的柱子是不是中盘当前位置
             2. 短盘是否在中盘上面
             3. 现在考虑的柱子是不是短盘当前位置，因为如果是的话，中盘也不可以移到这根柱子上
                 - 同时满足这三个条件，则不移动
                 - 反之，移动到这个柱子
     - 长盘是否可以移到柱子上
         - 取决于：
             1. 现在考虑的柱子是否长盘当前位置
             2. 中盘和短盘是否在长盘当前位置 
             3. 中盘和短盘是否在现在考虑的柱子上
                 - 同时满足这三个条件，则不移动
                 - 否则，移动到该位置

```python
def next_state_list(state):
    loc_li = ['1','2','3']
    result_li = []
    short_loc = state[2]
    middle_loc = state[1]
    long_loc = state[0]    
    for loc in loc_li:
        # 不计入不移动的情况
        if loc != short_loc:             
            result_li.append(long_loc+middle_loc+loc)  
        # 不计入不移动的情况、不计入移动不了的情况、不计入放置不上的情况
        if loc != middle_loc and short_loc!=middle_loc and loc != short_loc:
            result_li.append(long_loc+loc+short_loc)
        # 不计入不移动的情况、不计入移动不了的情况、不计入放置不上的情况
        if loc != long_loc and (short_loc!=long_loc and middle_loc!=long_loc) and (loc != short_loc and loc != middle_loc):
            result_li.append(loc+middle_loc+short_loc)
    return result_li

print(next_state_list("321"))
print(next_state_list('111'))
```
```
['322', '323', '331']
['112', '113']

```

# property装饰器
## class property(fget=None,fset=None,fdel=None,doc=None)
- 返回`property`属性
- `fget`是获取属性值的函数，`fset`是修改属性值的函数，`fdel`是删除属性值的函数。并且`doc`为`property`对象创建文档字符串
- 一个典型的用法是定义一个托管属性x
```python
class C:
    def __init__(self):
        self._x=None
    
    def getx(self):
        return self._x

    def setx(self,value):
        self._x=value
    
    def delx(self):
        del self._x

    x=property(getx,setx,delx,"I'm the 'x' property")
```
```python
c=C()
print(c.x)
c.x=True
print(c.x)
del c.x
print(c.x)
```
```
None
True
Traceback (most recent call last):
  File "/home/ch/docs/python/test.py", line 21, in <module>
    print(c.x)
  File "/home/ch/docs/python/test.py", line 6, in getx
    return self._x
AttributeError: 'C' object has no attribute '_x'
```
- 解析：
 - `c.x`调用`getx(getter)`
 - `c.x=Ture`调用`setx(setter)`
 - `del c.x`调用`delx(deleter)`
 - 如果给出`doc`，则`doc`将成为`property`的文档字符串，否则将拷贝`fget`的文档字符串

## @property装饰器
- 特征属性对象具有 getter, setter 以及 deleter 方法，它们可用作装饰器来创建该特征属性的副本，并将相应的访问函数设为所装饰的函数。 这最好是用一个例子来解释:
```python
class C:
    def __init__(self):
        self._x=None
    
    @property
    def x(self):
        """I'm the 'x' property"""
        return self._x
    
    @x.setter
    def x(self,value):
        self._x=value
    
    @x.deleter
    def x(self):
        del self._x
```
```python
c=C()
print(c.x)
c.x=True
print(c.x)
del c.x
print(c.x)
```

```
None
True
Traceback (most recent call last):
  File "/home/ch/docs/python/test.py", line 24, in <module>
    print(c.x)
  File "/home/ch/docs/python/test.py", line 8, in x
    return self._x
AttributeError: 'C' object has no attribute '_x'
```

- 解析：
 1. 使用装饰器后，要将原来的函数名字都改为设置装饰器那里的名字，比如这里从`x`开始，那么后面的`setter`和`deleter`都要使用`x`作为函数名
 2. 和之前所用例子的效果是一样的
 3. `doc`应该放在第一次设置`@property`的位置，即`getter`的位置

# partial()

## functools.partial(func,/,*args,**keywords)
- 返回一个新的`partial`对象，当被调用时其行为类似于`func`附带位置参数`args`和关键字参数`keywords`被调用
- 如果为调用提供了更多的参数，它们会被附加到`args`。 如果提供了额外的关键字参数，它们会扩展并重载`keywords`
- 偏函数是将所要承载的函数作为`partial()`函数的第一个参数，原函数的各个参数依次作为`partial()`函数后续的参数，除非使用关键字参数
- 例如：
```python
from functools import partial
basetwo=partial(int,base=2)
print(basetwo('10010'))
```

```
18
```
- 解析：
 1. 首先，`partial`的`func`是`int`
 2. `base=2`说明`int`的`base`参数被设置成了`2`,即从二进制转换为整型
 3. `basetwo`是`partial`对象的一个引用
 4. 最后再调用`basetwo`时，再添加一个参数`10010`，即完成了`int('10010',base=2)`的效果

## class functools.partialmethod(func,/,*args,**keywords)
- 返回一个新的`partialmethod`描述器，其行为类似`partial`但它被设计用作方法定义而非直接用作可调用对象
- `func`必须是一个`descriptor`或可调用对象（同属两者的对象例如普通函数会被当作描述器来处理）
 - descriptor -- 描述器
  - 任何定义了 __get__(), __set__() 或 __delete__() 方法的对象。当一个类属性为描述器时，它的特殊绑定行为就会在属性查找时被触发。通常情况下，使用 a.b 来获取、设置或删除一个属性时会在 a 的类字典中查找名称为 b 的对象，但如果 b 是一个描述器，则会调用对应的描述器方法。理解描述器的概念是更深层次理解 Python 的关键，因为这是许多重要特性的基础，包括函数、方法、属性、类方法、静态方法以及对超类的引用等等。
 - 当 `func` 是一个描述器（例如普通 Python 函数, `classmethod()`, `staticmethod()`, `abstractmethod()` 或其他 `partialmethod` 的实例）时, 对 `__get__` 的调用会被委托给底层的描述器，并会返回一个适当的`partial`对象作为结果
 - 当`func`是一个非描述器类可调用对象时，则会动态创建一个适当的绑定方法。 当用作方法时其行为类似普通 Python 函数：将会插入`self`参数作为第一个位置参数，其位置甚至会处于提供给`partialmethod`构造器的`args`和`keywords`之前

 ```python
 from functools import partialmethod
class Cell(object):
    def __init__(self):
        self._alive=False
    @property
    def alive(self):
        return self._alive
    def set_state(self,state):
        self._alive=bool(state)
    set_alive=partialmethod(set_state,True)
    set_death=partialmethod(set_state,False)
c=Cell()
print(c.alive)
c.set_alive()
print(c.alive)
```
```
False
True
```



# 生成器
- 和列表解析式用法差不多，只是将方括号改为圆括号，例如：

```python
g=（x*x for x in range(10)）
```

- python将会自动生成一个列表，但不会输出
- 访问时可以通过next(g)访问，每执行一次就跳至下一项
- 或者使用for循环访问：
```python
for num in g:    
```

## 生成器函数
- 和常规函数一样定义，但是返回值用yield
- 每次返回一个数后挂起，然后从挂起处继续执行

# 迭代器
## **iterator**
- 可以直接用for循环的对象都是可迭代的（iterable）
- 常见的可迭代对象：`list,tuple,dict,set,str`; 文件对象 ; 在类中定义了`__iter__`方法的对象
- 可以被`next()`函数调用并且不断返回下一个值的对象成为迭代器
- **生成器**都是<font color=#AA0000><i>iterator对象</i></font>，但是`list,dict,str`虽然都是可迭代的但是不是迭代器
- 可以使用`iter()`函数将他们变为<font color=#AA0000><i>iterator</i></font>
- 可以使用`isinstance()`函数判断对象是否可以迭代
 - 用法：isinstance(对象,iterator/iterable)

### 定义可迭代对象的方法：
    
    class Iter_obj:
    """简单定义一个可迭代对象"""
        def __iter__(self):
            return self #简单返回自身，但实际可能不会这么用

- 这里实现了__iter__()方法
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/iterator-1.PNG)

### 使用hasattr()函数检验对象中是否含有属性：hasattr(对象，name))

![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/iterator-2.PNG)

- 显然，<font color=#AA0000><i>it</i></font>是<font color=#AA0000><i>Iterable</i></font>且是含有`__iter__`属性的实例
但是在使用`iter()`函数将其转换为<font color=#AA0000><i>Iterator</i></font>的时候出现了类型错误，因为`iter()`返回了一个非<font color=#AA0000><i>Iterator</i></font>的对象
- 如果把<font color=#AA0000><i>Iter_obj</i></font>的返回对象修改一下，比如将其改为<font color=#AA0000><i>Iterable</i></font>但却不是<font color=#AA0000><i>Iterator</i></font>的列表
- 这里要先在`__init__()`里面给`self`加一个列表对象
- 然后再在`__iter__()`里面把这个列表用`iter()`函数转换为<font color=#AA0000><i>Iterator</i></font>

![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/iterator-3.PNG)
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/iterator-4.PNG)

1. 首先，it这个实例它不是Iterator
2. 第二，it它包含__iter__这个属性
3. 第三，使用iter()函数的时候，python成功将it转换为了Iterator，但是后续使用isinstance()函数验证时，却发现it不是Iterator

![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/iterator-5.PNG)

- 根据上面这个实验可以知道，iter()函数其实是将Iterable的对象重新开了一个Iterator（相当于强制类型转换），但是不改变原来对象

- 所以，通过这次实验可以发现，在创建类的时候，含有__iter__()方法说明后续在实用类的时候，iter()函数可以调用该类的数据（也就是说iter()可以调用含__iter__()方法的类），但是__iter__()必须返回一个可迭代的对象（反例为return self的例子）

- 最后一点，如果一个类中不含__iter__()方法，且这个类中含有__getitem__()方法时，使用isinstance()函数检测时，它不是Iterable的

![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/iterator-6.PNG)
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/iterator-9.PNG)

- 可以猜测：像list,dict,tuple,set这种Iterable，可以getitem，也可以被iter()函数调用的对象，都是有__iter__()方法以及__getitem__()方法的

![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/iterator-7.PNG)

- 可以做出总结：
1. 一个可迭代的对象一定是实现了__iter__和__next__方法的对象（可以被next()调用）
2. 可以直接用for循环的对象不一定可迭代，比如没有实现__iter__方法但是实现了__getitem__方法的对象
3. 实现了__getitem__但是不可迭代的对象，可以使用iter()函数将其转换为Iterator，可以使用next()函数

## itertools

### itertools.combinations
- 选取组合数，无顺序
```python
form itertools import combinations
list(combinations([1,2,3],2))
```

```
[(1, 2), (1, 3), (2, 3)]
```
- 参数解释：
 - 第一个参数提供需要组合的元素的列表
 - 第二个参数提供选择组合元素的数量，等效于数学中的C组合数


### itertools.permutations
- 排列组合，有顺序
```python
form itertools import permutations
list(permutations([1,2,3],3))
```

```
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

- 等效于数学中的A组合数

# 类
## MRO简介
-  MRO即方法解析顺序，用于判断子类调用的属性来自于哪个父亲，python2.3之前是基于深度优先算法的，自2.3开始使用C3算法，定义类时需要继承object，这样的类称为新式类，否则为旧式类，新式类是广度优先搜索

<img src="https://cdn.jsdelivr.net/gh/JNchengge/image@master/super.PNG" wdith="600" height="700"/>

## 类的私有属性和方法
- 类的私有属性和方法只能在类内部访问
- 当在类外部调用时，将会报错：`No Attribute`
```python
class Foo:
    def __init__(self):
        self.__name='Foo'
    def info(self):
        print(self.__name)
a=Foo()
a.info()
a.__name
```

```
Foo
Traceback (most recent call last):
  File "/home/ch/docs/python/test.py", line 8, in <module>
    a.__name
AttributeError: 'Foo' object has no attribute '__name'
```

- 因为在定义私有属性或者方法时，会将名字改为`_classname__name`的形式
- 在类的外部，是可以通过这种名字来访问变量或者方法的
```python
class Foo:
    def __init__(self):
        self.__name='Foo'
    def info(self):
        print(self.__name)
a=Foo()
a.info()
print(a._Foo__name)
```
```
Foo
Foo
```

- 还可以在外部为类添加属性或者方法
- 比如：
```python
class Foo:
    def __init__(self):
        self.__name='Foo'
    def info(self):
        print(self.__name)
a=Foo()
a.info()
a.__n='bar'
print(a.__n)
```

```
Foo
bar
```

- 注意：虽然这里为a添加的是私有类型的写法`__n`，但是却可以直接外部调用
- 可见。在外部添加的属性，都不属于私有属性

- 添加方法的例子，需要导入`MethodType`模块
```python
from types import MethodType
class Foo:
    def __init__(self):
        self.__name='Foo'
    def info(self):
        print(self.__name)
def bar(self,x):
    self.x=x
Foo.bar=MethodType(bar,Foo)
f=Foo()
f.bar(123)
print(f.x)
```
```
123
```
- 但是会出现两个问题
 1. f.bar is not callable
 2. instance of 'Foo' has no 'x' member

- 暂时猜测：MethodType只是暂时地添加了方法
- 有待进一步学习

# argparse模块和命令行参数解析
 
## sys.argv
- 命令行参数是用户在命令行中python程序之后的参数，在程序中可以通过sys.argv访问命令行参数。
- argv[0]为Python脚本名，argv[1]为第一个参数，argv[2]为第二个参数，以此类推
- argv[1]、argv[2]等参数按惯例为字符串，所以实际使用时要记住类型转换

![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/sys.PNG)

## 1.导入模块：
```python
import argparse
```
## 2.创建ArgumentsParser对象：
```python
parser=argparse.ArgumentParser()
```
## 3.调用parser对象方法add_argument()增加要解析的命令参数信息：
```python
parser.add_argument('--length',default=10,type=int,help='长度')
parser.add_argument('--width',default=5,type=int,help='宽度')
```
## 4.调用parser对象方法parse_args()解析命令行参数，生成对应的列表
```python
args=parser.parse_args()
```
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/argparse.PNG)

## 其它ArgumentParse参数：
### prog
- 默认情况下，ArgumentParser对象使用sys.argv[0]来确定如何在帮助消息中显示程序的名称，比如一个myprogram.py的文件
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
```
- 该程序的帮助信息将显示文件名作为程序名称：
```
$ python myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]
optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
$ cd ..
$ python subdir/myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]
optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
 ```
- 使用prog参数来改变这样的默认行为：
```python
parser = argparse.ArgumentParser(prog=myprogram)
parser.add_argument('--foo', help='foo help')
parser.print_help()
```
- 输出：

```
usage: myprogram [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program
```

### usage
- 默认情况下，ArgumentParser 根据它包含的参数来构建用法消息：
- 可以通过 usage= 关键字参数覆盖这一默认消息：

```python
parser = argparse.ArgumentParser(prog=PROG,usage='%(prog)s[options]')
parser.print_help()
```
```
usage: PROG [options]
```
- 可以通过`%(prog)s`来输出prog的信息
### parents
- parents使用ArgumentParser对象的列表，从ArgumentParser列表中手机所有位置和可选的行为，然后将这些行为添加到正在构建的ArgumentParser对象中去，比如：
```python
parent_parser=argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent',type=int)
```
```python
foo_parser=argparse.ArgumentParser(parents=[parent_parser])
foo_parser.add_argument('foo')
foo_parser.parse_args(['--parent','2','XXX'])
```
```
Namespace(foo='XXX',parent=2)
```
- 解析：
 1. 这里有两个`ArgumentParser`对象，一个是作为父的`parent_parser`,另一个是作为当前对象的`foo_parser`
 2. 需要在创建`parent_parser`把`add_help=`参数设为False，否则在对`foo_parser`使用help时会看到`parent_parser`和`foo_parser`的help，并且报错
 3. 在创建`foo_parser`时，将`parents=`参数设置为[parent_parser]，这是一个`ArgumentParser`的列表
 4. 对`foo_parser`进行参数解析的时候，可以看到，`foo_parser`有两个参数，分别为：`--parent`和`foo`,所以在解析参数的时候，看到两个参数都被赋值
   - 虽然`--parent`参数被设置为`int`类型，但是在命令行参数中，默认接受字符串，所以`2`应该是字符串类型

```python
bar_parser=argparse.ArgumentParser(parents=[parent_parser])
bar_parser.add_argument('--bar')
bar_parser.parse_args(['--bar','YYY'])
```
```
Namespace(bar=YYY,parent=None)
```
- 解析：
1. `bar_parser`以`parent_parser`作为父对象，同样被添加了`--parent`参数
2. 但是在解析参数时，没有添加`--parent `的参数
3. 所以最后的结果是`--parent`的值为None
### formatter_class
   - class argparse.RawDescriptionHelpFormatter
     - 表示 description 和 epilog 已经被正确的格式化了，不能在命令行中被自动换行:(默认自动换行)
   - class argparse.RawTextHelpFormatter
     - 保留所有种类文字的空格，包括参数的描述。然而，多重的新行会被替换成一行。如果你想保留多重的空白行，可以在新行之间加空格。
   - class argparse.ArgumentDefaultsHelpFormatter
     - 自动添加默认的值的信息到每一个帮助信息的参数中
   - class argparse.MetavarTypeHelpFormatter
     - 为它的值在每一个参数中使用 type 的参数名当作它的显示名（而不是使用通常的格式 dest )
### prefix_chars
- 许多命令行会使用 `-` 当作前缀，比如 `-f/--foo`。如果解析器需要支持不同的或者额外的字符，比如像 `+f` 或者 `/foo` 的选项，可以在参数解析构建器中使用 `prefix_chars=` 参数。
```python
parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
parser.add_argument('+f')
parser.add_argument('++bar')
parser.parse_args('+f X ++bar Y'.split())
```
- `prefix_chars=` 参数默认使用 '-'. 支持一系列字符，但是不包括 `-` ，这样会产生不被允许的 `-f/--foo` 选项。
### fromfile_prefix_chars
- 可以通过文件输入参数。比如：
```python
with open('args.txt','w') as fp:
    fp.write('-f\nbar')
parser=argparse.ArgumentParser(fromfile_prefix_chars='@')
parse.add_argument('-f')
parse.parse_argument(['-f','foo','@args.txt'])
```
```
Namespace(f='bar')
```
- 解析：
 - 其实['-f','foo','@args.txt']相当于['-f','foo','-f','bar'],后面覆盖了前面

### conflict_handler

- ArgumentParser 对象不允许在相同选项字符串下有两种行为。默认情况下， ArgumentParser 对象会产生一个异常如果去创建一个正在使用的选项字符串参数。

```python
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--foo', help='old foo help')
parser.add_argument('--foo', help='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo
```

- 有些时候（例如：使用 parents），重写旧的有相同选项字符串的参数会更有用。为了产生这种行为， 'resolve' 值可以提供给 ArgumentParser 的 conflict_handler= 参数:

```python
parser = argparse.ArgumentParser(prog='PROG',conflict_handler='resolve')
parser.add_argument('-f','--foo',help='old foo help')
parser.add_argument('--foo',help='new foo help')
parser.print_help()
usage: PROG [-h] [-f FOO] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 -f FOO      old foo help
 --foo FOO   new foo help
```

## add_argument方法：
- 定义单个的命令行参数该如何解析。
- 有以下参数：
  - name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。

  - action - 当参数在命令行中出现时使用的动作基本类型。

  - nargs - 命令行参数应当消耗的数目。

  - const - 被一些 action 和 nargs 选择所需求的常数。

  - default - 当参数未在命令行中出现时使用的值。

  - type - 命令行参数应当被转换成的类型。

  - choices - 可用的参数的容器。

  - required - 此命令行选项是否可省略 （仅选项可用）。

  - help - 一个此选项作用的简单描述。

  - metavar - 在使用方法消息中使用的参数值示例。

  - dest - 被添加到 parse_args() 所返回对象上的属性名。

### action

#### store
- 存储参数的值，默认动作

#### store_const
- 存储被const命名参数的值，例如
```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',action='store_const',const=100)
print(parser.parse_args(['--foo']))
```
```
Namespace(foo=100)
```
1. 要注意的点有：`parse_args`操作的是列表对象
2. 此例`--foo`参数的动作是存储`const=100`的值

#### store_true和store_false
- 用于存储True和False
```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',action='store_true')
parser.add_argument('--bar',action='store_false')
args=parser.parse_args(['--foo --bar'.split()])
```
```
Namesapce(foo=True,bar=False)
```

#### append
- 用于存储一个列表，并且将每个参数的值追加到列表中
```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',action='append')
args=parser.parse_args('--foo 1 --foo 2'.split())
print(args)
```
```
Namespace(foo=['1', '2'])
```

#### count
- 用于计算参数出现的次数
```python
parser=argparse.ArgumentParser()
parser.add_argument('-v',action='count',default=0)
args=parser.parse_args(['-vvv'])
print(args)
```
```
Namespace(v=3)
```
- `default`是将`-v`的值设置成了默认0

#### extend
- 存储一个列表，并将每个参数值加到列表中，例如：
```python
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--foo',action='extend',nargs='+',type=str)
args=parser.parse_args(['--foo','1','--foo','2','3','4'])
print(args)
```
```
Namespace(foo=['1', '2', '3', '4'])
```
- python3.6.9没有`extend`这个动作

### nargs
- ArgumentParser 对象通常关联一个单独的命令行参数到一个单独的被执行的动作。 nargs 命名参数关联不同数目的命令行参数到单一动作。支持的值有：

#### N(一个整数)
- 命令行的N个参数会被添加到一个列表之中
```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',nargs=2,type=int)
parser.add_argument('--bar',nargs=3,type=str)
args=parser.parse_args('--bar 111 222 333 --foo 1 2'.split())
print(args)
```
```
Namespace(bar=['111', '222', '333'], foo=[1, 2])
```
- 解析：读入`bar`的三个参数和`foo`的两个参数，并且存储在对应的列表中
- 注意：nargs指定了几个参数，就需要几个参数，少了会报错，多了会识别不出来属于谁

```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',nargs=2,type=int)
parser.add_argument('--bar',nargs=3,type=str)
args=parser.parse_args('--bar 111 222 333 444 --foo 1 2'.split())
print(args)
```
```
usage: test.py [-h] [--foo FOO FOO] [--bar BAR BAR BAR]
test.py: error: unrecognized arguments: 444
```

```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',nargs=2,type=int)
parser.add_argument('--bar',nargs=3,type=str)
args=parser.parse_args('--bar 111 --foo 1 2'.split())
print(args)
```
```
usage: test.py [-h] [--foo FOO FOO] [--bar BAR BAR BAR]
test.py: error: argument --bar: expected 3 arguments
```

#### ?
- 如果可以的话，从命令行消耗一个参数，并产生一个与之对应的单一项。
- 如果当前没有命令行参数，则产生`default`值
- 如果字符串出现但是没有跟随参数，则产生`const`值
```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',nargs='?',const='c',default='d')
parser.add_argument('--bar',nargs='?',default='d')
args=parser.parse_args(['--bar','XX','--foo','YY'])
print(args)
args=parser.parse_args(['--bar','XX','--foo'])
print(args)
args=parser.parse_args([])
print(args)
```
```
Namespace(bar='XX', foo='YY')
Namespace(bar='XX', foo='c')
Namespace(bar='d', foo='d')
```

- nargs='?' 的一个更普遍用法是允许可选的输入或输出文件:
```python
parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),default=sys.stdout)
parser.parse_args(['input.txt', 'output.txt'])
parser.parse_args([])
```
```
Namespace(infile=<_io.TextIOWrapper name='input.txt' encoding='UTF-8'>,outfile=<_io.TextIOWrapper name='output.txt' encoding='UTF-8'>)
Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>,outfile=<_io.TextIOWrapper name='<stdout>' encoding='UTF-8'>)
```

#### *
- 所有当前命令行参数被聚集到一个列表中

```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',nargs='*')
parser.add_argument('--bar',nargs='*')
args=parser.parse_args(['--bar','XX','1','2','3','--foo','YY','4','5','6'])
print(args)
```

```
Namespace(bar=['XX', '1', '2', '3'], foo=['YY', '4', '5', '6'])
```

- 没有参数时，产生`default=None`
```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',nargs='*')
parser.add_argument('--bar',nargs='*')
args=parser.parse_args(['--bar','XX','1','2','3'])
print(args)
```

```
Namespace(bar=['XX', '1', '2', '3'], foo=None)
```

#### +
- 和 '*' 类似，所有当前命令行参数被聚集到一个列表中。另外，当前没有至少一个命令行参数时会产生一个错误信息。例如:

```python
parser=argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo',nargs='+')
args=parser.parse_args(['XX','1','2','3'])
print(args)
args=parser.parse_args([])
print(args)
```

```
Namespace(foo=['XX', '1', '2', '3'])
usage: PROG [-h] foo [foo ...]
PROG: error: the following arguments are required: foo
```

### metavar
- 当 ArgumentParser 生成帮助消息时，它需要用某种方式来引用每个预期的参数。 默认情况下，ArgumentParser 对象使用 dest 值作为每个对象的 "name"。 默认情况下，对于位置参数动作，dest 值将被直接使用，而对于可选参数动作，dest 值将被转为大写形式。 因此，一个位置参数 dest='bar' 的引用形式将为 bar。 一个带有单独命令行参数的可选参数 --foo 的引用形式将为 FOO。 示例如下:
```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('bar')
parser.print_help()
```

```
usage: test.py [-h] [--foo FOO] bar

positional arguments:
  bar

optional arguments:
  -h, --help  show this help message and exit
  --foo FOO
```

- 解析：help信息中，有两个参数名字，**可选参数**`--foo`和**位置参数**`bar`，`--foo`被转换成大写形式，`bar`不变

```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',metavar="XXX")
parser.add_argument('bar',metavar="YYY")
parser.print_help()
```

```
usage: test.py [-h] [--foo XXX] YYY

positional arguments:
  YYY

optional arguments:
  -h, --help  show this help message and exit
  --foo XXX
```

- 解析：使用`metavar`后，`XXX`代替了`FOO`，`YYY`代替了`bar`

- 不同的`nargs`值可能导致`metavar`被多次使用。 提供一个<font color=#AA0000>元组</font>给`metavar`即为每个参数指定不同的显示信息:

```python
parser=argparse.ArgumentParser()
parser.add_argument('--foo',nargs=3)
parser.add_argument('-x',nargs=2,metavar=('bar','baz'))
parser.print_help()
```

```
usage: test.py [-h] [--foo FOO FOO FOO] [-x bar baz]

optional arguments:
  -h, --help         show this help message and exit
  --foo FOO FOO FOO
  -x bar baz
```

### dest
- 对于可选参数动作，dest 的值通常取自选项字符串。 ArgumentParser 会通过接受第一个长选项字符串并去掉开头的 -- 字符串来生成 dest 的值。 如果没有提供长选项字符串，则 dest 将通过接受第一个短选项字符串并去掉开头的 - 字符来获得。 任何内部的 - 字符都将被转换为 _ 字符以确保字符串是有效的属性名称。 下面的例子显示了这种行为:

```python
parser=argparse.ArgumentParser()
parser.add_argument('-f','--foo-bar','--foo')
parser.add_argument('-x','-y')
parser.print_help()
```

```
usage: test.py [-h] [-f FOO_BAR] [-x X]

optional arguments:
  -h, --help            show this help message and exit
  -f FOO_BAR, --foo-bar FOO_BAR, --foo FOO_BAR
  -x X, -y X
```

- 解析：`dest`取`FOO_BAR`作为全部字符串的名字，因为`--foo-bar`是第一个长选项字符串（由--开头，中间的-被转换为'_'）
- 第二行`dest`取`X`作为全部字符串的名字，因为没有长选项字符串且`-x`为第一个短选字符串

- `dest`也可以自定义属性名称

# 数据模型
- 有些对象包含对外部对象的引用，例如打开文件或者窗口
 - 这些对象最好显式地关闭，比如使用close函数

- 有些对象包含对其他对象的引用，这些对象称为<font colo#3399FF>容器</font>，比如元组、字典、列表，这些引用是组成容器对象值的一部分
 - 当讨论容器的值的时候，指的是所包含的所有引用的值
 - 当讨论容器的可变性时，则仅指其直接包含的对象的编号
  - 因此，如果一个不可变容器对象（比如元组），内含一个可变对象的引用（比如列表），那么在修改列表的值的时候，元组的值也会发生变化
  - 但是，即使是元组的”值“发生了改变，元组还是不可变对象，因为元组的值实际上是对象的引用，也就是一些id，这些id没有发生改变，所以元组没有变
  - 若id指向的是可变对象，是可以改变该对象的值的

- 对于不可变类型，得出新值的运算实际上会返回对相同类型的已存在的对象的引用
 - 比如：
 ```python
 a=1
 b=1
 ```
 就是a指向1，b指向1
- 对于可变类型，绝对不会出现这种i情况
 - 比如：
 ```python
 a=[]
 b=[]
 ```
 就是创建了两个不同的列表对象
 但是：
 ```python
 a=b=[]
 ```
 就是a和b指向同一个列表

## numbers.Integral
- 此类对象包括数学中整数集合的成员
 - 整型(int)：
  - 表示一个任意大小的整数，在变换和掩码的时候使用二进制，复数会以2的补码表示
  - 2的补码：先全部取反，再加1

 - 布尔型(bool)
  - 此类对象表示逻辑值True和False

## numbers.Real(float)
 - 此类对象表示双精度浮点数

## numbers.Complex(complex)
- 此类对象以一对双精度浮点数来表示复数值
- 使用z.real和z.imag来获取实部和虚部
```python
a=complex(1,2)
print(a.real)
print(a.imag)
```

## 序列

### 不可变序列
- 一旦创建就不能再改变
 - 字符串(str)
 - 元组(tuple)
 - 字节串(bytes)

### 可变序列
- 创建后仍可被改变
 - 列表(list)
 - 字节数组(bytearray)

## 集合类型
- 此类对象表示由不重复且不可变对象组成的无序且有限的集合
- 不可通过下标访问
- 可以迭代，属于迭代器
- 常用于去重
- 可以进行交、并、差、对称差的运算

### 可变的集合
- 通过`set()`创建的集合，创建之后可以通过方法修改
- 比如
```python
a=set([1,1,2,3,45,4,64,6])
c=set("asgf")
b=a.difference(c)  #求差集
print(b)
a.add(10)          #添加值
print(a)
b.clear()          #清空集合
print(b)
print(a.copy() is a)    #复制
a.discard(1)        #丢弃元素
print(a)
b=set([1,2,3])
c=a.intersection(b)   #求交集
print(c)
```

```
{64, 1, 2, 3, 4, 6, 45}
{64, 1, 2, 3, 4, 6, 10, 45}
set()
False
{64, 2, 3, 4, 6, 10, 45}
{2, 3}
```
### 不可变集合
- 通过`fronzenset()`创建的集合
- 没有`add`、`discard`、`clear`等方法
```python
a=frozenset([1,1,2,3,45,4,64,6])
c=set("asgf")
b=a.difference(c)  #求差集
print(b)
print(a.copy() is a)    #复制
b=set([1,2,3])
c=a.intersection(b)   #求交集
print(c)
```
```
frozenset({64, 1, 2, 3, 4, 6, 45})
True
frozenset({1, 2, 3})
```
- 在复制的时候，体现了不可变对象的特性，即指向一个现存的不可变对象

- 由于不可变对象不可变且hashable，因此可以作为另一个集合的值或者字典的值
```python
import pprint
a=frozenset([1,1,2,3,45,4,64,6])
b=set([a,1,2,3,"asf"])
print(b)
d={'1':a,'2':'002'}
pprint.pprint(d)
```

```
{1, 2, 3, 'asf', frozenset({64, 1, 2, 3, 4, 6, 45})}
{'1': frozenset({64, 1, 2, 3, 4, 6, 45}), '2': '002'}
```

## 字典
- 字典会保留插入顺序，这意味着键将以它们被添加的顺序在字典中依次产生。 替换某个现有的键不会改变其顺序，但是移除某个键再重新插入则会将其添加到末尾而不会保留其原有位置

## 可调用类型
### 用户自定函数
#### 特殊属性
|属性|含义||
|:---:|:---:|:---:|
|__doc__|该函数的文档字符串，没有则为None|可写|
|__name__|该函数的名称|可写|
|__qualname__|该函数的qualified name|可写|
|__module__|该函数所属模块的名称|可写|
|__defaults__|由具有默认值的参数默认参数值组城的元组，无默认值则为None|可写|
|__code__|表示编译后的函数体的代码对象|可写|
|__globals__|对存放该函数中全局变量的字典的引用|只读|
|__dict__|命名空间支持的函数属性|可写|
|__closure__|None 或包含该函数可用变量的绑定的单元的元组|只读|
|__annotations__|包含参数标注的字典。字典的键是参数名，如存在返回标注则为 'return'|可写|
|__kwdefaults__|仅包含关键字参数默认值的字典|可写|

- __qualname__
 - 一个以点号分隔的名称，显示从模块的全局作用域到该模块中定义的某个类
 ```python
class C:
    class D:
        def foo(self):
            pass
print(C.__qualname__)
print(C.D.__qualname__)
print(C.D.foo.__qualname__)
print(C.D.foo.__name__)
print(C.D.__name__)
print(C.__name__)
 ```

 ```
C
C.D
C.D.foo
foo
D
C
 ```

 - 和`__name__`的区别在于，`__name__`表示的是当前所在定义的名字





# 其他
## Linux终端上直接运行python脚本
1. python文件开头加上解释器路径
    ```
    #!/usr/bin/python3
    ```    
2. 在终端上开启权限：
    ```
    chmod +x test.py
    ```
   
3. 输入文件路径即可运行
4. 根目录：`/`
5. 访问目录：`cd`
6. 得到子目录： `ls`

## r&u&b
- 字符串前面加`u`，该字符串以unicode格式进行编码（python2可以在开头加上<font color=008800>#encoding:utf-8</font>）
- 字符串前面加`r`，该字符串中的转义字符全部失效，变为一般的字符串
- 字符串前面加`b`，该字符串的类型转换为`byte`，网络编程中，服务器和浏览器只认`byte`类型的数据
