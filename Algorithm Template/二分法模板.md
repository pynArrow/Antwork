二分法是一种思路很简单，但是写起来很容易错的算法。对于小白（比如我）来说，刚开始接触二分法的时候很容易怀疑人生，直呼“玄学”：为什么提示整型溢出？while里面到底加不加=？mid后面要不要+1-1？诸如此类。

有鉴于此，博主在力扣上刷了30题后，试图总结二分法的模板（并附有相应力扣题目链接）。一方面加深印象，以期对二分法有更直观、深入的理解。另一方面可以帮助暂时对二分法不甚了解的读者。

此文纯c。

## 基本思想

二分法的思想可以说是很”朴素“：当我们在一个（有序）区间内搜索某个target时，不断地选取“中间值”来缩小存在target的区间的大小，直到找到target或者退出。

## 二分法模板

二分法的框架其实不难，这个框架其实就是将刚才提到的【基本思想】用C语言翻译了一下。至于不同问题中可能的变数，都暂且先用...代替，留待后续分析。

```python
int binarySearch(int* nums, int numsSize, int target){
    int left, right, mid;
    left = 0;
    right = ...;
    
    while( ... ){
        mid = left + (right - left) / 2;
        if( nums[mid] == target ){
            ...;
        }
        else if( nums[mid] > target ){
            ...;
        }
        else{
            ...;
        }
    }
    return ...;
}
```

值得一提的是其中计算mid时的写法：$mid=left+(right-left)/2$。这种写法等价于$mid=(right+left)/2$，并且有效防止了整数溢出情况的出现。这两种写法都是【向下取整】的，对应的区间边界时【左偏】的，与之对应的写法是$mid=left+(right-left+1)/2$、$mid=(right+left+1)/2$。具体区别在后文中介绍。

在上述模板中以...代替的地方，有两个非常纠结的细节。在开篇中“玄学问题”之列。

**第一个是while中间取不取等。**

**第二个是三个条件判断中区间改变时是否需要+1-1。**

这两点将在以下问题中着重分析。简单来说while解决的是有没有能力“取遍”整个区间的问题，条件判断中的处理解决的是区间怎样收缩的问题。

## 有序数组中查找某个值

这是因为二分查找中最简单的情形：在有序数组中查找某个值。找到了返回索引值，未找到返回-1。

```python
int binarySearch(int* nums, int numsSize, int target) {
    int left = 0; 
    int right = numsSize - 1; 

    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target){
            return mid; 
        }
        else if (nums[mid] < target){
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }
    return -1;
}
```

在这种情况中，最开始的区间为$[0,numsSize-1]$，也就是整个数组。这也就要求我们在二分搜索时需要使mid“能够”取遍整个区间。我们不妨考虑数组中只有两个数的情况（这可以对应一个更大的 区间的中间状态）。如果while中不取等，则显然mid是取不到索引为1的值的。为了使二分法能够取到该值，我们需要让left和right有可能取等，也就是while中要取等。

接下来再考虑当mid不是我们期望的索引值时，怎样收缩区间。以nums[mid]<target为例，target在【右区间】中，此时我们需要移动【左边界】。那么到底是移动到mid还是移动到mid+1呢？由之前的分析可知，搜索是在左右都闭的区间上进行的，并且可以取到区间内的所有数，所以left设置为mid+1即可。

