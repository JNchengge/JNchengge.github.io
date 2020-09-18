# 
# functools.partial(func,/,*args,**keywords)
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

# class functools.partialmethod(func,/,*args,**keywords)
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
