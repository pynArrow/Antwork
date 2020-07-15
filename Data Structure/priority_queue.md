### priority_queue 优先队列

以前已经提到过队列（queue）了，队列是一种”先进先出“的数据结构，即元素在队列尾部增加，在队列头部删除（也就是平常所说的“排队”）。

在现实生活中，【为了参与建设和谐美好的现代化社会】，我们在排队时会被道义约束而去让某些人群“优先”。比如说公交车上的老弱病残专座，亦或是讲台旁边的为某些学生提供的“专座”，不一而足。

总之，优先队列的思想由此而来。通过设立一种比较结构，确立优先级，在优先队列中具有最高优先级的元素先出。

* 头文件

```cpp
#include<queue>

template <class T, 
		class Container = vector<T>, 
		class Compare = less<typename Container::value_type> >
class priority_queue;
```

* 常用api

1. priority_queue<type\> obj

声明最大优先队列，这是因为默认的compare是less。

```cpp
priority_queue<int> obj;							//声明最大优先队列
priority_queue<int, vector<int>, greater<int>> obj;	//声明最小优先队列
```

有关自定义的compare将在后文说明。

2. obj.empty()

判断队列是否为空

3. obj.size()

返回优先队列的长度

4. obj.top()

返回优先队列中有最高优先级的元素

5. obj.pop()

删除第一个元素

6. obj.push(elem)

插入一个元素

7. obj.back()

返回优先队列的末尾元素

* 自定义compare方法

一、重载小于运算符

二、使用仿函数

和set的类似。

#### 程序演示

```cpp
#include<queue>
#include<iostream>

using namespace std;

void priority_queue_example(){
    priority_queue<int> obj1;
    priority_queue<int, vector<int>, greater<int>> obj2;
    //插入元素
    for (int i = 0; i < 10; i++){
        obj1.push(i);
        obj2.push(i);
    }
    //输出队列大小
    cout << "size: " << obj1.size() << endl;
    //输出最大优先队列
    cout << "priority queue: " << endl;
    while(!obj1.empty()){
        cout << "top: " << obj1.top() << " " << endl;
        //删除最高优先级元素
        obj1.pop();
    }
    //输出最小优先队列
    cout << "priority queue: " << endl;
    while(!obj2.empty()){
        cout << "top: " << obj2.top() << " " << endl;
        //删除最高优先级元素
        obj2.pop();
    }
    cout << endl;
}

int main(){
    priority_queue_example();
}
```

* 输出结果

```cpp
size: 10
priority queue:
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
priority queue:
top: 0
top: 1
top: 2
top: 3
top: 4
top: 5
top: 6
top: 7
top: 8
top: 9
```
