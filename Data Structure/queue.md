### queue 队列

数据结构中队列的主要特点是“先进先出”。如下图所示，先进入队列的元素一定在后进入队列的元素前被取出。stack/queue都是封装了deque<T\>容器的适配器类模板,两者都没有迭代器，访问元素的唯一方式就是遍历内容器内容，同时移除访问过的每一个元素，应该说是想遍历是必须移除，或者考虑拷贝到另一个容器中。

![img](http://c.biancheng.net/uploads/allimg/180913/2-1P913113140553.jpg)

* 头文件

```cpp
#include<queue>
```

* 常用api

1. queue<type\> obj

与stack模板类很相似，queue模板类也需要两个模板参数，一个是元素类型，一个容器类型，元素类型是必要的，容器类型是可选的，默认为deque类型。

```cpp
//使用deque
queue<int> obj;
//使用vector
queue<int, vector<int>> obj;
```

2. obj.front()

返回第一个元素的引用。

3. obj.back()

返回最后一个元素的引用。

4. obj.push()

在队列尾部添加一个元素的副本。

5. obj.pop()

删除队列中第一个元素。

6. obj.size()

返回队列中元素的个数。

7. obj.empty()

判断队列是否为空。

8. obj.emplace()

用传给 emplace() 的参数调用 T 的构造函数，在 queue 的尾部生成对象。

9. obj.swap(queue<T\>& other_queue)

将当前 queue 中的元素和参数 queue 中的元素交换。

#### 程序演示

```cpp
#include<queue>
#include<iostream>

using namespace std;

int main()
{
    //使用deque声明queue
    deque<int> nums{1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    queue<int> obj(nums);

    //队列大小
    cout << "size: " << obj.size() << endl;

    //取出第一个元素和最后一个元素
    cout << "front: " << obj.front() << endl;
    cout << "back: " << obj.back() << endl;

    //压入队列，分别使用左值引用和右值引用
    obj.push(5);
    obj.push(5 + 1);
    
    //依次取出队列
    while(!obj.empty()){
        cout << "top: " << obj.front() << endl;
        obj.pop();
    }

    //自动生成对象，放入构造函数
    obj.emplace(5);
    cout << "emplace: " << obj.front() << endl;
    //交换栈
    queue<int> obj2;
    for (int i = 0; i < 10; i++){
        //元素入栈，右值引用
        obj2.push(10-i);
    }
    obj.swap(obj2);
    //取出所有元素
    while(!obj.empty()){
        cout << "top: " << obj.front() << endl;
        obj.pop();
    }

}
```

* 输出结果

```cpp
size: 10
front: 1
back: 0
top: 1
top: 2
top: 3
top: 4
top: 5
top: 6
top: 7
top: 8
top: 9
top: 0
top: 5
top: 6
emplace: 5
top: 10
top: 9
top: 8
top: 7
top: 6
top: 5
top: 4
top: 3
top: 2
top: 1
```

### 