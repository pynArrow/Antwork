### set 集合

set是关联容器的一种，是已排序的集合。set和multiset的区别在于set中的元素不能重复，而multiset中允许存在重复的元素。

需要注意的是，set中的元素最好不要直接修改。因为直接修改元素，并不会引起容器的重新排序，所以容器中的有序性被破坏。如果一定要修改，可以先删除该元素，然后插入新元素。

* 头文件

```cpp
#include<set>
template < class Key,
			class Pred = less<Key>,
			class A = allocator<Key> >
class set {...}
```

* 常用api

1. set<type\> obj

```cpp
set<int> obj;
```

2. obj.begin()

返回容器的第一个元素

3. obj.end()

返回容器的最后一个元素的下一位

4. obj.clear()

删除容器中的所有元素

5. obj.empty()

判断容器是否为空

6. obj.max_size()

返回容器可能包含的元素最大个数

7. obj.size()

返回当前容器中元素个数

8. obj,insert(elem)

向容器中插入元素

9. obj.count(elem)

返回elem在元素中出现的次数，可以用来判断元素是否存在

10. obj.equal_range(elem)

返回一个pair（其中元素为迭代器），可以用first和second取出。分别表示第一个大于等于elem的元素和第一个大于elem的元素。

11. obj.erase(iterator)

删除iterator位置的元素

```cpp
obj.erase(iterator);			//删除iterator指向的值
obj.erase(first, second);		//删除first和second之间的值
obj.erase(key_value);			//删除键值key_value的元素
```

12. obj.find(elem)

返回给定值的iterator，如果没找到返回obj.end()

13. obj.lower_bound(elem)

返回第一个大于等于elem的iterator

14. obj.upper_bound(elem)

返回第一个大于elem的iterator

* 自定义排序

一、重载()运算符

```cpp
struct cmp{
    bool operator()(const data_type &a, const data_type &b){
        return a.x-b.x;
    }
}
```

二、重载<运算符

```cpp
struct cmp{
    int x;
    bool operator < (const cmp &a) const{
        return a.x<x; 
```

#### 程序演示

```cpp
#include<set>
#include<iostream>

using namespace std;

void set_example(){
    set<int> obj;

    for (int i = 1; i < 11; i++){
        //插入元素
        obj.insert(i);
    }

    cout << "size: " << obj.size() << endl;
    cout << "max_size: " << obj.max_size() << endl;

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
    cout << "lower bound:" << *obj.lower_bound(3) << endl;
    cout << "upper bound:" << *obj.upper_bound(3) << endl;

    pair<set<int>::iterator, set<int>::iterator> bound;
    bound = obj.equal_range(3);
    cout << "lower bound:" << *bound.first << endl;
    cout << "upper bound:" << *bound.second << endl;

    //删除元素
    obj.erase(5);

    //遍历set
    set<int>::iterator it;
    cout << "set: ";
    for (it = obj.begin(); it != obj.end(); it++){
        cout << " " << *it;
    }
    cout << endl;

    //元素出现次数
    for (int i = 1; i < 11; i++){
        cout << i << " counts " << obj.count(i) << endl;
    }

    //清空set
    cout << "Is empty? " << obj.empty() << endl;
    obj.clear();
    cout << "Is empty? " << obj.empty() << endl;
}

int main(){
    set_example();
}
```

* 程序输出

```cpp
size: 10
max_size: 461168601842738790
find 5:
5 is in the set.
find 20:
20 does not exist.
find 3's bound:
lower bound:3
upper bound:4
lower bound:3
upper bound:4
set:  1 2 3 4 6 7 8 9 10
1 counts 1
2 counts 1
3 counts 1
4 counts 1
5 counts 0
6 counts 1
7 counts 1
8 counts 1
9 counts 1
10 counts 1
Is empty? 0
Is empty? 1
```
