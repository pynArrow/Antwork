# Makefile

在windows系统中，很多集成开发环境（intergrated development environment, IDE）会帮我们完成编译到运行的所有步骤。但是在Linux系统中，这些都需要我们自己来实现，这也是Makefile的主要用途。

## 编译和链接

在windows中，我们完成了一个.c/.cpp文件，直接通过IDE的“编译且运行”功能就可以直接获取程序运行结果。其过程是隐式的，不需要coders操心。然而，如果我们需要使用Makefile，就需要对.c/.cpp文件到.exe文件的过程有一个总体的了解。大致来说，此过程分为两步：1. 编译。2. 链接。

1. 编译（compile）：把源文件（.c/.cpp文件）转化成中间代码文件（.o文件）的过程。
2. 链接（link）：把工程中大量的object file打包成.a文件，再生成可执行文件（.exe）的过程。

## Makefile简介

先简单介绍一下，makefile的流程：

1. 生成makefile（Makefile）文件。

2. 打开Makefile文件所在目录，执行make命令。或是在任意目录下增加$-I\ [PATH]$参数。

3. make clean清除.o和可执行文件。

我们可以发现：

1. make指令很像IDE中的“编译并运行”的按钮，完成了从编译到生成可执行文件的过程。

2. 第三步是非必须的，只是为了保持文件的清洁。

### makefile文件名

一般情况下，make指令会在当前目录搜索文件名为makefile/Makefile的文件。如果你想使用别的文件名的话也可以使用-f参数，如

```
$ make -f xxxx.xxxx
```

### makefile规则

先给出一个简单的例子：

```makefile
edit : main.o
	cc -o edit main.o
	
main.o : main.c main.h
	cc -c main.c
```

可以发现，makefile的规则为：

```makefile
target : prerequisites
	command
```

1. 目标文件（target）是”待生成文件“，可以是.o/.exe文件，分别对应编译和链接过程。
2. 依赖文件（prerequisites）是“源文件”，可以是.o/.c/.h文件。依赖文件说明了目标文件是由哪一些文件更新得到的。
3. command必须以Tab键作为开头。
4. 当依赖文件的更新时间比目标文件要新，或者目标文件不存在时，make指令会执行，生成/更新目标文件。

### 自动推导

在实际工程中，经常有多个c文件需要编译，所以会遇到很多类似于

```makefile
xxxx.o : xxxx.c xyz.h
	cc -c xxxx.c
```

我们发现，在很多情况下，规则中xxxx.o/xxxx.c的前缀名是一样的、command命令也是类似的。现在有一个问题：既然这么多文件名是一样的，那么能否只输入一处，然后“自动填充”其他位置？

答案是可以。这也就是makefile的自动推导功能，上面的模式可以直接改写成：

```makefile
xxxx.o : xyz.h
```

其余部分可由makefile自动补充。

### 使用变量

在多文件编译的情景下，edit后面跟着的依赖文件会是一长串.o文件，而且这一长串将会在makefile文件中多次出现。那么如果我们对工程进行了修改，增减了.c文件，就会使得我们需要多次在相同的地方修改.o的文件串。这对于一个大工程是及其麻烦且易错的。

所以makefile提供了【变量】用法。类似于c语言中的宏定义，将之前提到的文件串用一个变量代替，执行make指令时将变量对应内容在指定位置进行替换。这样一来如果需要修改就只用修改变量指代的值。

```makefile
objects = main.o xxxx.o ...

edit = $(objects)              #<-注意这里的使用格式
	cc -o edit $(objects)
```

### make clean

每个 Makefile 中都应该写一个清空目标文件（.o 和执行文件）的规则，这不仅便于重编译，也很利于保持文件的清洁。一般来说，写成以下格式即可

```makefile
clean :
	rm edit $(objects)
```

当然，更好地写法是增加"伪目标"：

```makefile
.PHONY : clean
clean :
	-rm edit $(objects)
```

### 引用其他makefile

类似于C语言include方法，makefile可以用include关键字将其他的makefile包含进来，即将include后的文件完整地展开在include的位置。一般格式为

```makefile
include [filename]
```

注意这里的filename支持绝对路径、相对路径、正则表达式通配符。 