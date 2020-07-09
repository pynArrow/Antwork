# cmake

## 内部构建

**CMakeLists.txt**

```cmake
PROJECT (HELLO)
SET(SRC_LIST main.c)
MESSAGE(STATUS "This is BINARY dir " ${HELLO_BINARY_DIR})
MESSAGE(STATUS "This is SOURCE dir "${HELLO_SOURCE_DIR})
ADD_EXECUTABLE(hello ${SRC_LIST})
```

1. PORJECT (projectname)

用于定义工程名称。这个指令隐式地定义了两个cmake变量，分别是，projectname_BINARY_DIR和projectname_SOURCE_DIR指向工程的路径。用时cmake也会预定义PROJECT_BINARY_DIR和PROJECT_SOURCE_DIR，与上述两个指向路径的变量分别相同。

2. SET(VAR [VALUE])

用于显示定义变量，VALUE可以使用双引号括起来（在文件名中含有空格时是必要的）。

3. MESSAGE([SEND_ERROR | STATUS | FATAL_ERROR] "message to display")

用于向终端输出用户定义的信息，包含三种：

1）SEND_ERROR，产生错误，跳过生成过程。

2）STATUS，输出前缀为-的信息。

3）FATAL_ERROR，终止所有cmake过程。

4. ADD_EXECUTABLE(hello ${SRC_LIST})

定义了工程生成的可执行文件名为hello

5. ${VAR}

表示引用变量。需要特别注意，在IF语句中需要直接使用变量名，而不需要${VAR}引用方法。

6. 指令大小写无关。

* 内部编译

```
$ cmake .
```

* 外部编译

```
$ cmake PATH
```

在外部编译时，HELLO_BINARY_DIR指代编译路径（即执行cmake命令时所在的目录），HELLO_SOURCE_DIR指代工程目录。

## 外部构建

* 添加源文件目录

1. ADD_SUBDIRECTORY(source_sir [binary_dir])

向当前工程添加存放源文件的子目录，可以指定中间二进制和目标二进制存放的位置（如果不指定则存放在当前目录的src目录下）。

2. ADD_SUBDIRS(dir1, dir2 ...)

向工程中添加多个子目录

* 设置输出保存位置

1. SET(EXECUTABLE_OUTPUT_PATH ${PORJECT_BINARY_DIR}/bin)

定义二进制文件的输出路径

2. SET(LIBRARY_OUTPUT_PATH ${PORJECT_BINARY_DIR}/lib)

定义库文件的输出路径（共享库和静态库）。

* 安装

1. makefile版本：make install DESTDIR=...
2. cmake版本：cmake -DCMAKE_INSTALL_PREFIX=...

**安装目标文件**

* INSTALL(TARGETS targets ... [[ARCHIVE|LIBRARY|RUNTIME]

  ​															    [DESTINATION \<dir\>] 

  ​																[PERMISSIONS permissions ...] 			       																[CONFIGURATIONS [Debug|Release|...]] 																[COMPONENT \<component\>]

  ​																[OPTIONAL]

  ​																] [...])

（参数真的太多了）

1. TARGETS后面的targets是通过ADD_EXECUTABLE定义的目标文件。二进制、静态库、动态库等。分别对应后面的三种指令RUNTIME, ARCHIVE, LIBRARY。
2. DESTINATION定义了安装路径。
3. PERMISSIONS定义访问权限，默认为644。

**安装普通文件**

```cmake
INSTALL(FILES files... DESTINATION <dir>
 [PERMISSIONS permissions...]
 [CONFIGURATIONS [Debug|Release|...]]
 [COMPONENT <component>]
 [RENAME <name>] [OPTIONAL])
```

**安装可执行文件**

```cmake
INSTALL(PROGRAMS files... DESTINATION <dir>
 [PERMISSIONS permissions...]
 [CONFIGURATIONS [Debug|Release|...]]
 [COMPONENT <component>]
 [RENAME <name>] [OPTIONAL])
```

**安装目录文件**

```cmake
INSTALL(DIRECTORY dirs... DESTINATION <dir>
	[FILE_PERMISSIONS permissions...]
	[DIRECTORY_PERMISSIONS permissions...]
	[USE_SOURCE_PERMISSIONS]
	[CONFIGURATIONS [Debug|Release|...]]
	[COMPONENT <component>]
	[[PATTERN <pattern> | REGEX <regex>]
	[EXCLUDE] [PERMISSIONS permissions...]] [...])
```

## 静态库与动态库的构建

* ADD_LIBRARY(hello SHARED ${LIBHELLO_SRC})

添加共享库。只需要填写库名【hello】，cmake会自动生成libhello.so。

SHARED:动态库

STATIC:静态库

MODULE:使用dyld系统有效，否则当做SHARED

注意：此种方法中静态库和动态库不能重名。

* SET(LIBRARY_OUTPUT_PATH ...)

指定库文件输出路径。

* SET_TARGET_PROPERTIES(hello_static PROPERTIES OUTPUT_NAME "hello")

添加这条指令后，可以“人为”将静态库的名字改成与动态库相同。

OUTPUT_NAME 用于设置输出名的参数

CLEAN_DIRECT_OUTPUT 设为1时可以防止cmake清除使用相同名字的库

VERSION 动态库的版本号

SOVERSION API版本

* GET_TARGET_PROPERTY（VAR target property）

用于获取target的属性

* 安装

```cmake
INSTALL(TARGETS hello hello_static
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib)
INSTALL(FILES hello.h DESTINATION include/hello)
```

## 使用外部共享库和头文件

* INCLUDE_DIRECTORIES( ... )

添加对头文件的路径支持

* LINK_DIRECTORIES(directory1 directory2 ...)

添加非标准（自己写的）共享库的搜索路径。

* TARGET_LINK_LIBRARIES（target library1 <debug | optimized> library2 ...)

为target添加需要链接的共享库

**环境变量**

CMAKE_INCLUDE_PATH、CMAKE_LIBRARY_PATH

## cmake常用变量和常用环境变量

* 引用变量

一般情况：${ }

IF等语句中：直接使用变量名

* 自定义变量

隐式定义：比如PROJECT指令生成的\<projectname\>_BINARY_DIR。

显示定义：SET指令

* 常用变量

1. CMAKE_BINARY_DIR, PROJECT_BINARY_DIR, \<projectname>_BINARY_DIR：

内部编译指向工程顶层目录

外部编译指向编译发生的目录（执行make指令的目录）

2. CMAKE_SOURCE_DIR, PROJECT_SOURCE_DIR, \<projectname>_SOURCE_DIR：

永远指向工程顶层目录

3. CMAKE_CURRENT_SOURCE_DIR

值向当前处理的CMakeLists.txt路径

4. CMAKE_CURRENT_BINARY_DIR

内部编译指向CMakeLists.txt路径

外部编译指向target编译路径

5. CMAKE_CURRENT_LIST_FILE

指向的调用时这个变量的CMakeLists.txt完整路径

6. CMAKE_CURRENT_LIST_LINE

输出变量所在的行

7. EXECUTABLE_OUTPUT_PATH, LIBRARY_OUTPUT_PATH

定义最终结果的存放目录

* 环境变量

${ENV}调用系统的环境变量

1. CMAKE_INCLUDE_CURRENT_DIR

自动添加CMAKE_CURRENT_BINARY_DIR和CMAKE_CURRENT_SOURCE_DIR到当前处理的CMakeLists.txt

2. CMAKE_INCLUDE_DIRECTORIES_PROJECT_BEFORE

将工程头文件目录置于系统头文件目录的前面

## cmake常用指令

* 基本指令

1. ADD_DEFINITIONS

2. ADD_DEPENDENCE

定义target的依赖target

3. ADD_LIST, ENABLE_TESTING

ENTABLE_TESTING()

用来控制Makefile是否构建test目标

ADD_TEST(testname Exename arg1 arg2 ...)

用自定义的test测试，最后需要加上ENABLE_TESTING

4. AUX_SOURCE_SIRECTORY(dir VARIABLE)

用于发现dir目录下的所有源代码文件并将列表储存在变量中

```cmake
AUX_SOURCE_DIRECTORY(. SRC_LIST)
ADD_EXECUTABLE(main ${SRC_LIST})
```

5. CMAKE_MINIMUM_REQUIRED( VERSION versionNumber [FATAL_ERROR])

设置cmake最低版本

6. EXEC_PORGRAM

用于在指定的目录运行某个程序，通过 ARGS 添加参数，如果要获取输出和返回值，可通过

OUTPUT_VARIABLE 和 RETURN_VALUE 分别定义两个变量。

* 控制指令

1. IF指令

```cmake
IF(expression)
 # THEN section.
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
 ELSE(expression)
 # ELSE section.
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
 ENDIF(expression)
```

2. WHILE指令

```cmake
WHILE(condition)
     COMMAND1(ARGS ...)
     COMMAND2(ARGS ...)
     ...
     ENDWHILE(condition)
```

3. FOREACH

处理列表

```cmake
FOREACH(loop_var arg1 arg2 ...)
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
 ENDFOREACH(loop_var)
```

处理范围

```cmake
FOREACH(loop_var RANGE total)
ENDFOREACH(loop_var)
```

范围中设置步长

```cmake
FOREACH(loop_var RANGE start stop [step])
ENDFOREACH(loop_var)
```





## 模块的使用与自定义模块

