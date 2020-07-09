# Linux常用指令整理

[toc]

## 概览

| 命令   | 含义                                           |
| ------ | ---------------------------------------------- |
| man    | manual，查询指令用法                           |
| cat    | concatenate，从第一行显示档案内容              |
| cd     | change directory，变换目录                     |
| pwd    | print working directory，显示当前目录          |
| mkdir  | make directory，建立一个新的目录               |
| rmdir  | remove directory，删除一个空的目录             |
| ls     | list，显示档案或目录的相关信息                 |
| export | export，将自定义变量转变成环境变量             |
| find   | find，在硬盘中搜索档案                         |
| grep   | 分析一行数据，如果其中有需要的信息，就提取该行 |
| kill   | 17                                             |
| cp     | copy，复制档案/目录                            |
| mv     | move， 移动档案/目录                           |
| rm     | remove，删除档案/目录                          |
| ps     | 将某个时间点的程序运作情况颉取下来             |
| chmod  | change mode，修改档案/目录权限                 |
| su     | 14                                             |
| tar    | tape achive，打包档案/目录                     |
| top    | 17                                             |
| ln     | link，文件/档案间添加链接                      |

## 查阅指令用法

* man

```
$ man [指令]
可以显示指令的相关用法和参数说明：

[指令](number)    #括号中的数字指指令的类别
NAME             #指令的名称和简单说明
SYNOPSIS         #基本语法
DESCRIPTION      #详细语法及参数说明！
ENVIRONMENT      #相关环境参数
AUTHOR           #作者
REPORTING BUGS   #联系方式
COPYRIGHT        #著作权说明
SEE ALSO         #介绍查看说明文件的方式

$ man -f 部分指令
可以搜索包含man命令的指令
$ man -k 关键字
通过搜索关键字，来获取指令信息
```

注：

1. 在查阅过程中而已使用【空格】向下翻页（也可以用PgUp、PgDn、Home和end）。

2. 在任何时候，都可以通过输入【/word】来查询关键字，如【/date】。

* info

可以将文件拆分成段落，段落间可以由超链接相互跳转。

## 档案权限

### 文件属性

先看一个例子：

```
-rw-r--r-- 1 root root 42304 Sep 4 18:26 install.log
    [1]   [2] [3]  [4]  [5]       [6]         [7]
```

分别解释上面7个字段的意思：

* [1]表示档案的类型与权限：$-rw-r--r--$

1. 第一个字符[-]表示档案类型：

[d]、[-]、[l]、[b]、[c]分别表示目录、档案、连结档、可随机存取装置、一次性读取装置

2. 接下来的字符以三个为一组。

每个个字符在[r,w,x,-]中选取，分别表示读、写、可执行、无权限。第一组三个表示User权限，第二组表示Group权限，第三个表示Others权限。

* [2]表示连结到inode的档名数量

* [3]表示档案的User账号
* [4]表示档案的所属Group
* [5]表示档案容量大小
* [6]建档日期/修改日期
* [7]档案的档名

### 修改文件属性与权限

* chgrp(chang group)

改变档案所属群组

```
$ chgrp [-R] dirname/filename
-R表示递归操作
```

* chown（change owner）

改变档案拥有者

```
$ chown [-R] 账号名称：组名 档案或目录
```

* chmod

修改权限设定的方法有两种，一种是通过数字设定，另一种是通过符号来进行权限的变更。

1. 数字类型

分别赋予r、w、x、- 一个“分数”：4、2、1、0。用三个符号位数字的和来表示权限。这样以来，任何权限的组合，都可以用不同的分数表示。比如rwx：4+2+1=7，rwxr--r--：744。

```
$ chmod [-R] xyz dirname/filename
```

2. 符号类型

```
$ chmod [ugoa] [+-=] [rwx] dirname/filename
```

[ugoa]：表示user、group、others、all

[+-=]：+表示加入，-表示除去，=表示设定

[rwx]：三种权限

## 档案档名的搜索

whereis和locate是在数据库中寻找，速度比在硬盘中寻找的find更快。

### 数据库搜索

* whereis

```
$ whereis dirname/filename
用完整名称查找档案
$ whereis -b dirname/filename
只找二进制格式的档案
$ whereis -m dirname/filename
只找说明文件在manual路径下的档案
$ whereis -s dirname/filename
只找source来源档案
$ whereis -u dirname/filename
寻找上述三种方法之外的档案
```

* locate

```
$ locate keyword
用部分名称查找档案
$ locate -i keyword
忽略大小写的差异
$ locate -r keyword
可以用正则表达式查找
```

### 硬盘搜索

* find

```
$ find [PATH] [option] [action]
```

1. 与使用者或组名相关的参数（对应option栏、action栏）

-uid n：n为用户id（数字）

-gid n：n为组名id

-user name：name为用户名

-group name：name为组名

-nouser：寻找拥有者不存在的档案

-nogroup：寻找群组不存在的档案

2. 与档案权限相关

-name filename：依据名称搜索

-size [+-]SIZE：依据大小搜索

-type TYPE：依据类型搜索

-perm mode：搜索权限是mode的档案

-perm -mode：搜索权限包括mode的档案

## 档案与目录管理

相关操作：

1. 检视：ls
2. 处理：cd, pwd, mkdir, rmdir
3. 复制、删除、移动：cp, rm, mv
4. 查询：cat，nl，more，less

### 目录结构

| 目录名 | 功能                                                         |
| ------ | ------------------------------------------------------------ |
| /home  | 普通用户默认目录，在此目录下每个用户都有一个以用户名命名的文件夹 |
| /root  | 超级用户的根目录                                             |
| /bin   | 储存一些二进制可执行文件                                     |
| /etc   | 保存系统管理所需的配置文件和目录                             |
| /lib   | 保存系统运行所需的库文件                                     |
| /usr   | 包括与系统用户直接有关的文件和目录                           |
| /var   | 储存一些不断变化的文件，如日志                               |
| /tmp   | 系统和用户的临时文件，对所有用户提供读写权限                 |
| /sys   | 系统设备和文件层次结构，包括内核数据信息                     |
| /dev   | 存放设备文件 ，比如linux驱动                                 |
| /boot  | 存放系统内核和启动文件                                       |
| /sbin  | 储存了很多系统命令                                           |

### 特殊目录

| 目录符号 | 含义                     |
| -------- | ------------------------ |
| .        | 此层目录                 |
| ..       | 上一级目录               |
| -        | 前一个工作目录           |
| ~        | 目前用户身份所在的家目录 |
| ~account | account用户的家目录      |

> 注：根目录的上层目录仍然是根目录

### 检视

* ls

```
$ ls -a 目录名
显示所有档案（包括隐藏档）
$ ls -d 目录名
仅列出目录，而不列出档案数据
$ ls -l 目录名
以长数据串行出，包括属性和权限
```

### 处理目录

* cd（change directory）

```
$ cd 相对路径或绝对路径
表示去到该路径
绝对路径：cd /var/spool/mail
相对路径：cd ../mqueue #上级目录相同的时候可以这么写
$ cd ~
回到自己的家目录（root）
$ cd 
同样是回到家目录
$ cd ..
返回上级目录
$ cd -
返回之前的目录
```

* pwd(Print Working Directory)

```
$ pwd 
显示当前所在目录的路径
$ pwd -P
显示完整路径，包括连结档
```

* mkdir（make directory）

```
$ mkdir 目录名
建立新目录(只能建立单层)，也就是说目录名中只有最后一个目录名是不存在、待建的。
建立多层目录时会报错，eg. $ mkdir test1/test2/test3
$ mkdir -p 目录名
可以递归建立多层目录
$ mkdir -m 目录名
配置文件案的权限
```

* rmdir

```
$ rmdir 目录名
删除空目录（有内容则无法删除）
$ rmdir -p 目录名
同时删除该目录上层所有空目录
```

### 复制、删除、移动

* cp（copy）

```
$ cp source destination
将档案从source位置移动到destination位置，只能复制档案
如$ cp ~/source destination 就只复制source
$ cp -i source destination
如果destination已经存在，会询问是否复制档案
$ cp source .
复制source到当前目录（某些属性、权限可能会改变，比如建档时间）
$ cp -a source destination
复制目录，同时复制所有属性，相当于同时含有-pdr的功能。
$ cp -r source destination
递归持续复制，可以直接复制目录
$ cp -p source destination
连同档案的属性一起复制过去，而不是用默认属性。
$ cp -d source destination
如果source的属性是link file，则复制link file的属性而不是复制档案本身。
```

* rm（remove）

```
$ rm source
删除文件，如果档案以-开头（可能会误判为选项），可以使用./source
$ rm -f source
force，忽略不存在的档案
$ rm -i source
删除前会询问是否执行
$ rm -r source
递归删除目录下所有档案
```

* mv（move）

```
$ mv source destination
将目录从source移动到destination
$ mv -f source destination
force，如果destination存在，之间覆盖
$ mv -i source destination
如果destination存在，询问是否覆盖
$ mv -u source destination
如果档案已经存在，且source比较新的时候，会更新（update）
```

### 查询

* cat

```
$ cat 档案名
从第一行开始显示档案内容
$ cat -n 档案名
打印行号（空白行也有）
$ cat -b 档案名
打印行号，空白行不标行号
$ cat -A 档案名
可以列出特殊字符，相当于vET操作
```

* more、less

一页一页显示档案内容

* tac

从最后一行开始显示

* nl

添加行号

## 磁盘与文件管理

### 实体链接与符号链接

Linux下的连结档有两种：第一种类似windows的快捷方式，能够快速连接到目标档案或目录，称为符号链接（Symbolic Link）；另一种通过inode产生新档名，称为实体链接（Hard Link）。

1. Hard Link

在Linux中，档案内容是由inode的记录来指向的。如果需要有多个档名指向同一个内容，则就需要对应相同的inode号码，这就是hard link。所以hard link是档名与inode的链接。

2. Symbolic Link

相当于windows中的快捷方式，这个链接会让数据的读取直接指向link的档案的档名。当该档案被删除后，Symbolic Link也会失效。

****

无论是实体链接还是符号链接，都会用到指令ln。

* ln

```
$ ln source destination
source和destination建立实体链接
$ ln -s source destination
source和destination建立符号链接
$ ln -f source destination
移除目标文件，再建立链接
```

## 压缩与打包

### 压缩档案

1. compress
2. gzip
3. bzip2、bzcat

### 打包目录

tar指令可以将多个档案或目录打包成一个大档案，然后通过gzip/bzip2压缩。

```
$ tar [-j|-z][cv] [-f 建立的档名] filename
打包、压缩filename到[建立的档名]
-j 表示bzip2压缩
-z 表示gzip压缩
-c 建立打包档案
-v 压缩过程中显示档名
-f 后接处理的档名
$ tar [-j|-z][tv] [-f 建立的档名]
查看档名
-t 查看打包档案的档名
$ tar [-j|-z][xv] [-f 建立的档名] [-C 目录]
解压缩
-x 解打包、解压缩
-C 用在指定目录前
```

## 其他指令

### 更改变量属性

* export

父程序的自定义变量不能直接被继承到子程序，需要使用export指令将自定义变量变成环境变量才能传递到子程序。

```
$ export 自定义变量
```

### 颉取命令

* grep

```
$ grep [-acinv] [--color=auto] “字符串” filename
```

-v：反向选择，没有【字符串】的一行输出

-i：忽略大小写

-n：输出行号

-c：计算找到字符串的次数

-a：将binary以text的方式搜索

--color=auto：将关键字加上颜色显示

### 切换身份

* su

```
$ su [-lm] [-c 指令] [username]
```

### 管理工作

* kill

```
$ kill -I
列出kill能使用的signal
$ kill -1
重新读取一次参数的配置文件
$ kill -2
Ctrl-c
$ kill -9
立即强制删除一个工作
$ kill -15
以正常的方式终止工作
```

### 程序的观察

* ps

```
$ ps aux
观察系统所有程序数据
$ ps -IA
观察所有系统的数据
$ ps axjf
联通部分程序书的状态
```

* top

持续侦测程序的运作状态

```
$ top [-d 数字] | top [-bnp]
```

-d 数字：程序更新的秒数

-b：批次执行top

-n：与-b搭配，表示需要进行几次top的输出结果

-p：指定某个PID进行观察