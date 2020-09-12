#  
# 1.导入模块：
```python
import argparse
```
# 2.创建ArgumentsParser对象：
```python
parser=argparse.ArgumentParser()
```
# 3.调用parser对象方法add_argument()增加要解析的命令参数信息：
```python
parser.add_argument('--length',default=10,type=int,help='长度')
parser.add_argument('--width',default=5,type=int,help='宽度')
```
# 4.调用parser对象方法parse_args()解析命令行参数，生成对应的列表
```python
args=parser.parse_args()
```
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/argparse.PNG)
