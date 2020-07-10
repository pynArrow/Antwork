### stack 栈

数据结构中栈的主要特点是“先入后出”。如下图所示，先进入栈的元素必须等到后进栈的元素取出后，才能被取出。stack/queue都是封装了deque<T\>容器的适配器类模板,两者都没有迭代器，访问元素的唯一方式就是遍历内容器内容，同时移除访问过的每一个元素，应该说是想遍历是必须移除，或者考虑拷贝到另一个容器中。

![img](http://c.biancheng.net/uploads/allimg/180913/2-1P913101Q4T2.jpg)

* 头文件

```cpp
#include<stack>
```

* 常见api

1. stack<type\>obj

class<stack\>定义如下：

```cpp
namespace std {
       template <class T,
                 class Container = deque<T> >
       class stack;
   }
```

也就是说stack的模板默认使用deque作为容器，实际上也可以使用vector。

```cpp
//使用deque
stack<int> obj;
//使用vector
stack<int, vector<int>> obj;
```

2. obj.top()

返回栈顶元素。

3. obj.push(elem)

将一个元素放入栈顶。

4. obj.pop()

移除栈顶元素，无返回值。

5. obj.size()

返回stack大小

6. obj.empty()

判断stack是否为空

7. obj.emplace()

用传入的参数调用构造函数，在栈顶生成对象。emplace在接受新对象的时候，自己会调用其构造函数生成对象然后放在容器内。而push，只能让其构造函数构造好了对象之后，再使用复制构造函数。

8. obj.swap(stack<T\> & other_stack)

将当前栈中的元素和参数中栈的元素交换。要求二者的数据类型相同。

#### 程序演示

```cpp
#include<stack>
#include<iostream>

using namespace std;

int main()
{
    stack<int> obj;
    for (int i = 0; i < 10; i++){
        //元素入栈，左值引用
        obj.push(i);
    }
    //stack大小
    cout << "size: " << obj.size() << endl;
    //取出所有元素
    while(!obj.empty()){
        cout << "top: " << obj.top() << endl;
        obj.pop();
    }
    //自动生成对象，放入构造函数
    obj.emplace(5);
    cout << "emplace: " << obj.top() << endl;
    //交换栈
    stack<int> obj2;
    for (int i = 0; i < 10; i++){
        //元素入栈，右值引用
        obj2.push(10-i);
    }
    obj.swap(obj2);
    //取出所有元素
    while(!obj.empty()){
        cout << "top: " << obj.top() << endl;
        obj.pop();
    }
}
```

* 输出结果

```cpp
size: 10
top: 9
top: 8
top: 7
top: 6
top: 5
top: 4
top: 3
top: 2
top: 1
top: 0
emplace: 5
top: 1
top: 2
top: 3
top: 4
top: 5
top: 6
top: 7
top: 8
top: 9
top: 10
```
