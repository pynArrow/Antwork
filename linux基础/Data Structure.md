# C++ STL

[toc]

## Data Structure

### array数组

### vector 向量

vector是一个能够存放任意类型的动态数组，能够增加和压缩数据。

* 头文件

```cpp
#include <vector>
```

* 常用api

1. vector\<type\>obj

向量储存容器的声明

```cpp
vector<int> obj;								//声明int型向量obj
vector<int> obj(10);							//声明size为10的向量
vector<int> obj(10, 1);							//size为10，初值为1
vector<int> obj2(obj);							//用obj初始化obj2
vector<int> obj2(obj.begin(), obj.begin()+1)	//用obj前两个数初始化obj2
```

需要注意的是，用一个向量（或数组）初始化另一个向量时，使用的参数为指针。

2. obj.push_back(elem)

在容器最后插入数据，无返回值

```cpp
test.push_back(1) //把1压入vector；test[0]=1
```

3. obj.pop_back()

在容器最后移除数据，无返回值

4. obj.size()

返回容器中数据个数

5. obj.capacity()

返回obj在内存中可以容纳的元素个数

6. obj.resize(num, [elem])

将obj中的元素size调整为num个，初始化为elem，缺省则随机

7. obj.clear()

清除容器中的所有数据

8. obj.front()

返回obj中的首元素

9. obj.back()

返回obj中最后一个元素

10. obj.erase(pos)

删除pos位置的元素。如果给出第二个参数，则可以删除区间内的元素。注意pos为指针。可以用obj.begin()+index删除对应索引位置的值。

11. obj.begin()

返回首位置的指针

12. obj.end()

返回末位置的指针的下一位

13. obj.empty()

判断obj是否为空，空则返回true，否则返回false

14. obj.insert(p, elem)

向对应位置插入elem，p为位置的指针

* 使用迭代器访问容器

```cpp
vector<int>::iterator t;
for(t=obj.begin(); t!=obj.end(); t++){
    cout<<*t;
}
```

* 向量间复制

```cpp
//有一个已经初始化的obj
vector<int> obj2;
obj2 = obj；					//把obj复制给obj2
```

* 向量间交换

```cpp
//交换两个向量变量，obj2已经初始化了
vector<int> obj(1);
obj.swap(obj);
```

* 二维向量

obj的每个元素是一个vector。

```cpp
vector<vector<int>>obj(10, vector<int>(5));
```

#### 程序演示

```cpp
#include<iostream>
#include<vector>

using namespace std;

int main(){
    //初始化容器
    vector<int> obj(10, 1);

    //取出首尾和末尾元素
    cout << "front:" << obj.front() << " back:" << obj.back() << endl;

    //观察obj的大小
    cout << "size:" << obj.size() << endl;
    //观察内存最大容量
    cout << "capacity:" << obj.capacity() << endl;

    //将元素压入容器末端，无返回值
    obj.push_back(0);

    //观察obj的大小
    cout << "size:" << obj.size() << endl;
    //观察内存最大容量
    cout << "capacity:" << obj.capacity() << endl;

    //使用迭代器遍历容器
    vector<int>::iterator t;
    cout << "obj:";
    for (t = obj.begin(); t != obj.end(); t++){
        cout << *t << " ";
    }
    cout << endl;

    //判断是否为空
    vector<int> emp(0);
    cout << "empty? " << emp.empty() << endl;

    
    //移除最后一位，不会返回值
    obj.pop_back();
    //插入值，位置参数用指针
    obj.insert(obj.begin(), 8);
    cout << "front:" << obj.front() << endl;
    //删除任意位置元素
    obj.erase(obj.begin() + 3);

    //改变容器大小
    obj.resize(5);
    cout << "size:" << obj.size() << endl;
    
    //交换两个向量变量
    vector<int> obj2(6, 3);
    obj.swap(obj2);
    cout << "obj:";
    for (size_t i = 0; i < obj.size(); i++){
        cout << obj[i] << " ";
    }
    cout << endl;

    //二维向量
    vector<vector<int>> obj3(5, vector<int>(5));
    for (int i = 0; i < 5; i++){
        //可以直接调整大小
        //obj3[i].resize(5);
        for (int j = 0; j < 5; j++){
            cout << obj3[i][j] << " ";
        }
        cout << endl;
    }
}
```

* 输出结果

```cpp
front:1 back:1
size:10
capacity:10
size:11
capacity:20
obj:1 1 1 1 1 1 1 1 1 1 0
empty? 1
front:8
size:5
obj:3 3 3 3 3 3
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

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

### deque 双端队列

deque是双向队列容器，由一段一段的定量连续空间构成，可以向两端发展，因此在头尾安插元素十分方便、迅速。 在中间部分安插元素则比较费时，因为必须移动其它元素。

* 头文件

```cpp
#include<deque>
```

* 常用api

1. deque<type\>obj

声明deque

```cpp
deque<int> obj;									//声明int类型双端队列
deque<int> obj(10);								//声明双端队列初始大小为10
deque<int> obj(10, 1);							//初始值为1
deque<int> obj(obj2);							//用双端队列obj2初始化obj
deque<int> obj(obj2.begin(), obj2.end()-1);		//用obj2初始化obj
```

2. obj.size()

返回容器大小

3. obj.max_size()

容器最大容量，有点像vector里面的capacity。

4. obj.resize(num)

调整队列大小

5. obj.empty()

判断容器是否为空

6. obj.push_front(elem)

头部添加元素

7. obj.push_back(elem)

尾部添加元素

8. obj.insert(iterator it, elem)

```cpp
deque<int> obj;
obj.insert(iterrator it, const T& x);						//在指定位置插入元素
obj.insert(iterrator it,int n, const T& x);					//插入n个元素
obj.insert(iterrator it,iterator first, iterator last);     //插入另一个队列某区间的元素
```

9. obj.pop_front()

头部删除元素

10. obj.pop_back()

尾部删除元素

11. obj.erase(iterator it)

```cpp
obj.erase(iterator it)						//删除it位置元素
obj.erase(iterator first, iterator last)	//删除first，last区间内元素
```

12. obj.clear()

清空所有元素

13. obj[index]

注意下标访问不会检查是否越界

14. obj.at(index)

at方法会检查是否越界，是则抛出out ofrange异常

15. obj.front()

访问第一个元素

16. obj.back()

访问最后一个元素 

17. obj.assign(int nSize, const T& x)

为多个元素赋值

18. obj.begin()

开始迭代器指针

19. obj.end()

末尾迭代器指针

#### 程序演示

```cpp
#include <iostream>
#include <deque>

using namespace std;

int main(int argc, char* argv[])
{
	deque<int> deq;
    //初始化
    deq.assign(6, 3);

    //计算大小
    cout << "size: " << deq.size() << endl;
    //最大容量
    cout << "max size: " << deq.max_size() << endl;
    //调整大小
    deq.resize(0);
	cout << "size: " << deq.size() << endl;

	// 头部增加元素
	deq.push_front(4);
	// 末尾添加元素
	deq.push_back(5);
	// 任意位置插入一个元素
	deque<int>::iterator it = deq.begin();
	deq.insert(it, 2);
	// 任意位置插入n个相同元素
    it = deq.begin();
    deq.insert(it, 3, 9);
	// 插入另一个向量的[forst,last]间的数据
	deque<int> deq2(5,8);
    it = deq.begin();
	deq.insert(it, deq2.end() - 1, deq2.end());

	// 遍历显示
	for (it = deq.begin(); it != deq.end(); it++)
		cout << *it << " ";
	cout << endl;

    // 头部删除元素
	deq.pop_front();
	// 末尾删除元素
	deq.pop_back();
	// 任意位置删除一个元素
    it = deq.begin();
    deq.erase(it);
	// 删除[first,last]之间的元素
	deq.erase(deq.begin(), deq.begin()+1);

	// 遍历显示
	for (it = deq.begin(); it != deq.end(); it++)
		cout << *it << " ";
	cout << endl;

	// 清空所有元素
	//deq.clear();

    // 下标访问
	cout << deq[0] << endl;
	// at方法访问
	cout << deq.at(0) << endl;
	// 访问第一个元素
	cout << deq.front() << endl;
	// 访问最后一个元素
	cout << deq.back() << endl;
}
```

* 输出结果

```cpp
size: 6
max size: 4611686018427387903
size: 0
8 9 9 9 2 4 5
9 2 4
9
9
9
4
```

### list 双向循环列表

list也就是我们通常所说的双向链表容器。与vector相比，list可以快速地插入和删除，但是不能根据索引来随机读取。

* 头文件

```cpp
#include<list>
```

* 常用api

1. list<type\>obj

```cpp
list<int> obj;								//声明空的list
list<int> obj(10);							//声明包含十个结点的list，初始值为0
list<int> obj(10, 5);						//初始值为5
list<int> obj(obj2);						//用obj2声明obj，要求obj2是list
list<int> obj(obj2.begin(), obj2.end());	//这里的obj2可以是数组、array、list
```

2. obj.begin()

返回指向容器中第一个元素的双向迭代器

3. obj.end()

返回指向容器最后一个元素下一位的双向迭代器

4. obj.rbegin()

reverse版本的begin，即返回指向最后一个元素的反向双向迭代器

5. obj.rend()

reverse版本的end，即返回指向第一个元素的前一位

> 注：在上述四个函数名前增加”c“，即cbegin,crbegin,cend,crend，表示增加const属性，对应的迭代器将不能用于修改元素。

6. obj.empty()

判断容器内是否有元素

7. obj.size()

返回当前容器实际包含的元素个数

8. obj.max_size()

返回容器能包含的元素个数的最大值

9. obj.resize(num)

改变链表长度

10. obj.front()

返回第一个元素的引用

11. obj.back()

返回最后一个元素的引用

12. obj.assign(n, elem)

```cpp
int a[]={1,2,3,4,5};
obj.assign(2,10);					//将2个10赋给链表
obj.assign(a,a+5);					//用指针的方法赋值
```

13. obj.push_front(elem)

在链表头部插入一个元素

14. obj.pop_front()

在链表尾部删除一个元素

15. obj.push_back(elem)

在链表尾部插入一个元素

16. obj.pop_back()

在链表尾部深处一个元素

17. obj.emplace()

在指定位置直接生成新元素，注意当前位置原来的数直接移动到下一位

18. obj.insert(iterator , elem)

在指定位置插入元素

```cpp
obj.insert(pos, elem);				//在pos（迭代器）位置插入元素
obj.insert(pos, n, elem);			//在pos位置之前插入n个elem
obj.insert(pos, left, right);		//在pos位置插入其他容器区间内的元素
obj.insert(pos, list);				//在pos位置插入初始化list
```

19. obj.erase(interator)

删除一个或某区域的元素

20. obj.splice()

将其他list容器储存的多个元素 添加到当前list的指定位置



#### 程序演示



### forward_list  单链表



### priority_queue 优先队列



### pair 



### set集合



