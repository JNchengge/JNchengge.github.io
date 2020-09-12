###### zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*号操作符有，可以将元组解压为列表
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/zip-1.PNG)
<br>
- 此例中，列表a和列表d,zip后其中元素被两两打包为一个元组
 - 列表a和列表c,zip后其中元素同样被打包为元组，但是因为a比c短，因此只返回3的长度
 - 列表zipped通过*解压后，将列表a和列表d的元素重新打包，并返回一个二维矩阵式
<br>

###### zip三个列表:(以及解压)
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/zip-2.PNG)

###### <font color=#AA0000>杨辉三角的实现</font>
###### 利用zip的功能，来实现错位相加：
![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/zip-3.PNG)
- [0]+a:在a的前面加一个[0]
- a+[0]:在a的后面加一个[0]
- 那么每次循环执行sum(i)的时候，i从两个元组之中各取一个并相加，
- 创建一个新的列表，归到生成器中
- 最后输出的时候，注意每两个数之间要有一个空格才能保持整齐
