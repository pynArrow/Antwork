'''
相邻的两个元素进行比较，然后把较大的元素放到后面（正向排序），
在一轮比较完后最大的元素就放在了最后一个位置，
因为这一点像鱼儿在水中吐的气泡在上升的过程中不断变大，所以得名冒泡排序。
'''
import random

def bubble_sort(blist):
    list_len = len(blist)
    print(list_len)
    for i in range(list_len):
        for j in range(list_len - 1):
            if blist[j] > blist[j+1]:
                blist[j], blist[j+1] = blist[j+1], blist[j]

if __name__ == '__main__':
    ls = [random.randint(0, 1000) for i in range(50)]
    print(ls)
    bubble_sort(ls)
    print(ls)
