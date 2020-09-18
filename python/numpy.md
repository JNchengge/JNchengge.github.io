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
|copy|对象hi否需要复制|
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
