'''
将序列分为已排序序列和未排序序列，
每次从未排序序列中取出一个数，插入到已排序的序列中。
也就是从后往前遍历，已排序的数大，就交换。
'''
import random

def insert_sort(ilist):
    list_len = len(ilist)
    for i in range(1, list_len):
        num = ilist.pop(i)
        for j in range(i-1, -1, -1):
            if num > ilist[j]:
                ilist.insert(j+1, num)
                break
            if j == 0:
                ilist.insert(0, num)

if __name__ == '__main__':
    ls = [random.randint(0, 1000) for i in range(50)]
    print(ls)
    insert_sort(ls)
    print(ls)
