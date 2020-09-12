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

# 其它ArgumentParse参数：
## prog
- 默认情况下，ArgumentParser对象使用sys.argv[0]来确定如何在帮助消息中显示程序的名称，比如一个myprogram.py的文件
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
```
- 该程序的帮助信息将显示文件名作为程序名称：
```
$ python myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]
optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
$ cd ..
$ python subdir/myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]
optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
 ```
- 使用prog参数来改变这样的默认行为：
```python
parser = argparse.ArgumentParser(prog=myprogram)
parser.add_argument('--foo', help='foo help')
parser.print_help()
```
- 输出：

```
usage: myprogram [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program
```

## usage
- 默认情况下，ArgumentParser 根据它包含的参数来构建用法消息：
- 可以通过 usage= 关键字参数覆盖这一默认消息：

```python
parser = argparse.ArgumentParser(prog=PROG,usage='%(prog)s[options]')
parser.print_help()
```
```
usage: PROG [options]
```
- 可以通过`%(prog)s`来输出prog的信息
## parents
- parents使用ArgumentParser对象的列表，从ArgumentParser列表中手机所有位置和可选的行为，然后将这些行为添加到正在构建的ArgumentParser对象中去，比如：
```python
parent_parser=argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent',type=int)
```
```python
foo_parser=argparse.ArgumentParser(parents=[parent_parser])
foo_parser.add_argument('foo')
foo_parser.parse_args(['--parent','2','XXX'])
```
```
Namespace(foo='XXX',parent=2)
```
- 解析：
 1. 这里有两个`ArgumentParser`对象，一个是作为父的`parent_parser`,另一个是作为当前对象的`foo_parser`
 2. 需要在创建`parent_parser`把`add_help=`参数设为False，否则在对`foo_parser`使用help时会看到`parent_parser`和`foo_parser`的help，并且报错
 3. 在创建`foo_parser`时，将`parents=`参数设置为[parent_parser]，这是一个`ArgumentParser`的列表
 4. 对`foo_parser`进行参数解析的时候，可以看到，`foo_parser`有两个参数，分别为：`--parent`和`foo`,所以在解析参数的时候，看到两个参数都被赋值
   - 虽然`--parent`参数被设置为`int`类型，但是在命令行参数中，默认接受字符串，所以`2`应该是字符串类型

```python
bar_parser=argparse.ArgumentParser(parents=[parent_parser])
bar_parser.add_argument('--bar')
bar_parser.parse_args(['--bar','YYY'])
```
```
Namespace(bar=YYY,parent=None)
```
- 解析：
1. `bar_parser`以`parent_parser`作为父对象，同样被添加了`--parent`参数
2. 但是在解析参数时，没有添加`--parent `的参数
3. 所以最后的结果是`--parent`的值为None
## formatter_class
   - class argparse.RawDescriptionHelpFormatter
     - 表示 description 和 epilog 已经被正确的格式化了，不能在命令行中被自动换行:(默认自动换行)
   - class argparse.RawTextHelpFormatter
     - 保留所有种类文字的空格，包括参数的描述。然而，多重的新行会被替换成一行。如果你想保留多重的空白行，可以在新行之间加空格。
   - class argparse.ArgumentDefaultsHelpFormatter
     - 自动添加默认的值的信息到每一个帮助信息的参数中
   - class argparse.MetavarTypeHelpFormatter
     - 为它的值在每一个参数中使用 type 的参数名当作它的显示名（而不是使用通常的格式 dest )
## prefix_chars
- 许多命令行会使用 `-` 当作前缀，比如 `-f/--foo`。如果解析器需要支持不同的或者额外的字符，比如像 `+f` 或者 `/foo` 的选项，可以在参数解析构建器中使用 `prefix_chars=` 参数。
```python
parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
parser.add_argument('+f')
parser.add_argument('++bar')
parser.parse_args('+f X ++bar Y'.split())
```
- `prefix_chars=` 参数默认使用 '-'. 支持一系列字符，但是不包括 `-` ，这样会产生不被允许的 `-f/--foo` 选项。
## fromfile_prefix_chars
- 可以通过文件输入参数。比如：
```python
with open('args.txt','w') as fp:
    fp.write('-f\nbar')
parser=argparse.ArgumentParser(fromfile_prefix_chars='@')
parse.add_argument('-f')
parse.parse_argument(['-f','foo','@args.txt'])
```
```
Namespace(f='bar')
```
- 解析：
 - 其实['-f','foo','@args.txt']相当于['-f','foo','-f','bar'],后面覆盖了前面

## conflict_handler

- ArgumentParser 对象不允许在相同选项字符串下有两种行为。默认情况下， ArgumentParser 对象会产生一个异常如果去创建一个正在使用的选项字符串参数。

```python
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--foo', help='old foo help')
parser.add_argument('--foo', help='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo
```

- 有些时候（例如：使用 parents），重写旧的有相同选项字符串的参数会更有用。为了产生这种行为， 'resolve' 值可以提供给 ArgumentParser 的 conflict_handler= 参数:

```python
parser = argparse.ArgumentParser(prog='PROG',conflict_handler='resolve')
parser.add_argument('-f','--foo',help='old foo help')
parser.add_argument('--foo',help='new foo help')
parser.print_help()
usage: PROG [-h] [-f FOO] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 -f FOO      old foo help
 --foo FOO   new foo help
```

# add_argument方法：
- 定义单个的命令行参数该如何解析。
- 有以下参数：
  - name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。

  - action - 当参数在命令行中出现时使用的动作基本类型。

  - nargs - 命令行参数应当消耗的数目。

  - const - 被一些 action 和 nargs 选择所需求的常数。

  - default - 当参数未在命令行中出现时使用的值。

  - type - 命令行参数应当被转换成的类型。

  - choices - 可用的参数的容器。

  - required - 此命令行选项是否可省略 （仅选项可用）。

  - help - 一个此选项作用的简单描述。

  - metavar - 在使用方法消息中使用的参数值示例。

  - dest - 被添加到 parse_args() 所返回对象上的属性名。

## action
