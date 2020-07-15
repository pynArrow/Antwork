### map

map是stl中的一种关联容器，提供key-value方式的储存，每个关键字在map中出现一次。

* 头文件

```cpp
#include<map>
```

* 常用api

1. map<int, string> obj

声明map容器。

2. obj.insert(elem)

```cpp
obj.insert(pair<int, string>(key, value));				//直接插入pair数据 
obj.insert(map<int, string>::value_type (key, value))	//插入value_type数据
obj[key] = value;										//数组方法插入元素
```

注意：前两种方法插入时，如果key存在则插入失败。而第三种方法则会覆盖value。

```cpp
pair<map<int, string>::iterator, bool> obj;
Insert_Pair = obj.insert(map<int, string>::value_type (key, value));
```

这种方法获取Insert_Pair.second可以得到数据是否插入成功的bool值。

3. map<int, string>::iterator it;

声明迭代器

4. obj.size()

返回map的大小

5. obj.count(key)

返回key出现的次数。只有0和1两种情况，代表存在与否。

6. obj.find(key)

返回一个迭代器。如果找到key了就返回对应的位置，否则返回obj.end()。

7. obj.lower_bound(key)

返回一个pair，first是key，second是第一个大于等于key的iterator

8. obj.upper_bound(key)

返回一个pair，first是key，second是第一个大于key的iterator

9. obj.erase(iterator)

删除迭代器指向位置的元素

10. obj.clear()

清空map

11. obj.equal_range(key)

返回一个pair（其中元素为迭代器），可以用first和second取出。分别表示第一个大于等于key的元素和第一个大于key的元素。

* 自定义排序

有重载小于号和仿函数两种方法，和set类似。

#### 程序演示

```cpp
#include<map>
#include<iostream>
#include<string>

using namespace std;

void map_example(){
    map<int, string> obj;
    //插入元素
    obj.insert(pair<int, string>(1, "a"));
    obj.insert(map<int, string>::value_type(2, "b"));
    for (int i = 3; i < 11; i++){
        obj[i] = 'a' + i - 1;
    }

    //遍历map
    map<int, string>::iterator it;
    for (it = obj.begin(); it != obj.end(); it++){
        cout << it->first << ":" << it->second << endl;
    }

    //map大小
    cout << "size:" << obj.size() << endl;
    
    //查找元素
    cout << "find 5:" << endl;
    if(obj.find(5) != obj.end())
        cout << "5 is in the set." << endl;
    else
        cout << "5 does not exist." << endl;
    
    cout << "find 20:" << endl;
    if(obj.find(20) != obj.end())
        cout << "20 is in the set." << endl;
    else
        cout << "20 does not exist." << endl;

    //查找大于数
    cout << "find 3's bound:" << endl;
    cout << "lower bound:" << obj.lower_bound(3)->first << endl;
    cout << "upper bound:" << obj.upper_bound(3)->first << endl;

    pair<map<int, string>::iterator, map<int, string>::iterator> bound;
    //bound是含有两个iterator的pair
    bound = obj.equal_range(3);
    cout << "lower bound:" << (bound.first)->first << endl;
    cout << "upper bound:" << (bound.second)->first << endl;

    //根据key删除元素
    obj.erase(5);
    //遍历map
    for (it = obj.begin(); it != obj.end(); it++){
        cout << (*it).first << ": "<< it->second << endl;
    }

    //清空map
    cout << "empty? " << obj.empty() << endl;
    obj.clear();
    cout << "empty? " << obj.empty() << endl;
    
}

int main(){
    map_example();
}
```

* 输出结果

```cpp
1:a
2:b
3:c
4:d
5:e
6:f
7:g
8:h
9:i
10:j
size:10
find 5:
5 is in the set.
find 20:
20 does not exist.
find 3's bound:
lower bound:3
upper bound:4
lower bound:3
upper bound:4
1: a
2: b
3: c
4: d
6: f
7: g
8: h
9: i
10: j
empty? 0
empty? 1
```
