### pair

pair是一种模板类型，其中包含两个元素，可以是不同的数据类型。pair可以配合关联容器使用，当函数需要返回两个值时，可以使用pair构造。pair的底层是一个struct。

* 头文件

~~~cpp
#include<utility>
~~~

* 常用api

1. pair<type1, type2\>obj(value1, value2)

声明一个pair

2. pair.first

返回pair中第一个value

3. pair.second

返回pair中第二个value

4. make_pair( elem1, elem2 )

使用make_pair对已经存在的两个数据构造一个新的pair类型。两个数据可以是常量，也可以是已经初始化的变量。

#### 程序演示

```cpp
#include<iostream>
#include<utility>

using namespace std;

void pair_example(){
    //直接初始化
    pair<string, double> obj("zhiyu", 111);

    cout << "first:" << obj.first << " second:" << obj.second << endl;
    obj.first = "ZhiYu";
    obj.second = 222;
    cout << "first:" << obj.first << " second:" << obj.second << endl;

    //声明后在程序内初始化
    pair<string, double> new_obj;
    string name = "Zhi Yu";
    double age = 18;
    new_obj = make_pair(name, age);

    cout << "first:" << new_obj.first << " second:" << new_obj.second << endl;

}

int main(){
    pair_example();
}
```

* 输出结果

```cpp
first:zhiyu second:111
first:ZhiYu second:222
first:Zhi Yu second:18
```

