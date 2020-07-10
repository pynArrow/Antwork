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
