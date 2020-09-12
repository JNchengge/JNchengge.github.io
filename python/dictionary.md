###### `get()`函数用于检查字典中key是否存在，可以避免以键取值时，键不存在而报错
###### `get()`有两个参数，一个是`key`，一个是返回值`fallback value`
###### `fallback value`的用处是：当字典中没有要检查的关键字时，返回`fallback value`的值
```python
a={'1':'001'}
a.get('1')
a.get('2','002')
```

###### `setdefault()`函数同样用于检查字典中`key`是否存在
###### 但是与`get()`不一样的地方是，若不存在，则在字典中添加相应的键值对
###### 如果没有值，则赋`None`
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

###### `update()`函数用于将一个字典的值更新到另一个字典中

```python
a={'1': '001', '3': '003', '2': '002', '4': None, '5': '005'}
a.update({'1':None})
a.update('6':'006')
print(a)
    
{'1': None, '3': '003', '2': '002', '4': None, '5': '005', '6': '006'}
```
###### 可以看到，`update`一个已存在的键时，会更新它的值；`update`一个不存在的键时，会插入一个新的键值对（字典）

###### import模块`pprint`,可以使用`pprint()`,以字典方式打印字典