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
