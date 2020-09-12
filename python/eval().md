#### `eval()`函数可以将字符串当成代码执行
- `eval()`包含三个参数，字符串，`locals()`和`globals()`
 1. 若只含`locals()`，将操作局部变量
 2. 若只含`globals()`，将操作全局变量
 3. 若两者都含，若`eval()`函数所在位置有局部变量，且`locals()`函数在后面，则操作`eval()`函数当前位置的局部变量，否则操作全局变量（后面覆盖前面）
 ![](https://cdn.jsdelivr.net/gh/JNchengge/image@master/eval-1.PNG)
 <img src="https://cdn.jsdelivr.net/gh/JNchengge/image@master/eval-2.PNG" width="2500" height="230"/>