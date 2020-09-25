### MRO简介：
-  MRO即方法解析顺序，用于判断子类调用的属性来自于哪个父亲，python2.3之前是基于深度优先算法的，自2.3开始使用C3算法，定义类时需要继承object，这样的类称为新式类，否则为旧式类，新式类是广度优先搜索

<img src="https://cdn.jsdelivr.net/gh/JNchengge/image@master/super.PNG" wdith="600" height="700"/>

# 类的私有属性和方法
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



