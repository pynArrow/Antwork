'''
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列
'''
import random

def quick_sort(qlist):
    if qlist == []:
        return []
    else :
        q = qlist[0]
        bigger_list = quick_sort([num for num in qlist[1:] if num >= q])
        less_list = quick_sort([num for num in qlist[1:] if num < q])
    return less_list + [q] + bigger_list

if __name__ == '__main__':
    ls = [random.randint(0, 1000) for i in range(50)]
    print(ls)
    ls = quick_sort(ls)
    print(ls)