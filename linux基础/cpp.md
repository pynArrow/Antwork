## 引用变量

### 左值引用

C语言和C++均使用&符号表示变量的地址。而C++赋予了&一个引得含义，即将其用来声明引用。

```cpp
int & num1  = num2;
```

上例即是一个”引用“，表示num1和num2指向相同的值和内存单元。这一点可以和指针对比来看。int*是指向int的指针，int&是指向int的引用，区别在于指针分配的内存和源变量不同。

```cpp
#include<iostream>

using namespace std;

int main(){
    int num1 = 5;
    int &num2 = num1;
    cout << num1 << " " << num2 << endl;
    num2++;
    cout << num1 << " " << num2 << endl;
    cout << &num1 << " " << &num2 << endl;
}
```

输出结果

```cpp
5 5
6 6
0x62fe0c 0x62fe0c
```

### 右值引用

在左值引用中，引用变量不能是表达式等“右值”。C++11中新增了一种引用——右值引用。这种引用可以指向右值，使用&&声明：

```cpp
include<iostream>
#include<cmath>

using namespace std;

int main(){
    double num = 3;
    double &&num1 = sqrt(36);
    double &&num2 = num * 5 + 1;
    cout << num1 << " " << num2 << endl;
}
```

输出结果

```cpp
6 16
6 17
0x62fe10 0x62fe18
```

