### MRO简介：
-  MRO即方法解析顺序，用于判断子类调用的属性来自于哪个父亲，python2.3之前是基于深度优先算法的，自2.3开始使用C3算法，定义类时需要继承object，这样的类称为新式类，否则为旧式类，新式类是广度优先搜索

<img src="https://cdn.jsdelivr.net/gh/JNchengge/image@master/super.PNG" wdith="600" height="700"/>