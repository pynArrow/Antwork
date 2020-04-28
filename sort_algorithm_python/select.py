'''
第一轮的时候，所有的元素都和第一个元素进行比较，如果比第一个元素小，就和第一个元素进行交换，在这轮比较完后，就找到了最小的元素；
第二轮的时候所有的元素都和第二个元素进行比较找出第二个位置的元素，以此类推。
'''
import random

def select_sort(slist):
    list_len = len(slist)
    print(list_len)
    for i in range(list_len):
        for j in range(i + 1, list_len):
            if slist[i] > slist[j]:
                slist[i], slist[j] = slist[j], slist[i]
                

if __name__ == '__main__':
    ls = [random.randint(0, 1000) for i in range(50)]
    print(ls)
    select_sort(ls)
    print(ls)
