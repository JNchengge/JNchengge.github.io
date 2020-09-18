# 
# class property(fget=None,fset=None,fdel=None,doc=None)
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

# @property装饰器
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
