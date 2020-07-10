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

注意这种方法会覆盖原链表

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

19. obj.erase(iterator)

删除一个或某区域的元素

20. obj.splice(iterator, list)

将其他list容器储存的多个元素添加到当前list的指定位置

```cpp
obj.splice(pos, list);				//将list插入到pos位置
obj.splice(pos, list, it);			//将list中it位置元素插入到pos位置
obj.splice(pos, list, first, last);	//将list中[first, last)中的元素插入到pos位置
```

#### 程序演示

```cpp
#include<iostream>
#include<list>

using namespace std;

//顺序遍历输出
void sequentail_output(list<int> obj){
    list<int>::iterator it;
    cout << "list:";
    for (it = obj.begin(); it != obj.end(); it++){
        cout << *it << " ";
    }
    cout << endl;
}

//逆序遍历输出
void reverse_output(list<int> obj){
    list<int>::reverse_iterator it;
    cout << "reverse:";
    for (it = obj.rbegin(); it != obj.rend(); it++){
        cout << *it << " ";
    }
    cout << endl;
}

int main()
{
    //声明链表
    list<int> obj(6, 3);
    
    //插入元素
    obj.push_back(1);
    obj.push_front(5);
    
    //输出链表长度
    cout << "size: " << obj.size() << endl;
    //改变链表长度
    //obj.resize(0)
    
    //顺序遍历输出
    sequentail_output(obj);
    //逆序遍历输出
    reverse_output(obj);

    //删除元素
    obj.pop_back();
    obj.pop_front();
    sequentail_output(obj);

    //给链表元素赋值
    obj.assign(2, 10);
    sequentail_output(obj);

    //插入元素
    obj.insert(++obj.begin(), 9);
    sequentail_output(obj);
    //删除元素
    obj.erase(--obj.end());
    reverse_output(obj);
    //中间生成元素
    obj.emplace(--obj.end(), 2);
    sequentail_output(obj);

    //取出头部元素
    cout << "front: " << obj.front() << endl;
    //取出尾部元素
    cout << " back: " << obj.back() << endl;

    //将其他list插入到指定位置
    list<int> obj2(3, 7);
    obj.splice(obj.begin(), obj2);
    sequentail_output(obj);


}
```

* 运行结果

```cpp
size: 8
list:5 3 3 3 3 3 3 1
reverse:1 3 3 3 3 3 3 5
list:3 3 3 3 3 3
list:10 10
list:10 9 10
reverse:9 10
list:10 2 9
front: 10
 back: 9
list:7 7 7 10 2 9
```

