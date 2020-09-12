- 可用于记录当前迭代次数
- 一般形式：`enumrate(_sequence_,[start=0])`,`start`是起始标号。
- 当迭代类型是有序序列，迭代标号等同于当前临时变量在序列中的索引。
    ```ruby
    for i,name in enumerate(student_name):
        print("编号："+str(i).zfill(3)+"\t学生姓名："+name)
    
    for i,name in enumerate(student_name,start=1):
        print("编号："+str(i).zfill(3)+"\t学生姓名："+name)
    ```

- `zfill()`表示填充满三位数