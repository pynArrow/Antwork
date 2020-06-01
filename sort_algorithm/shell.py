'''
将数组列在一个表中并对列分别进行插入排序，重复这过程，
每次用更长的列（步长更长了，列数更少了）来进行。最后整个表就只有一列了。
'''

import random 

def shell_sort(slist):
    list_len = len(slist)
    gap = list_len // 2
    while gap:
        for i in range(gap, list_len):
            tmp = i
            for j in range(i, -1, -gap):
                if slist[tmp] < slist[j]:
                    slist[tmp], slist[j] = slist[j], slist[tmp]
                    tmp = j
        gap = gap // 2
                
if __name__ == '__main__':
    ls = [random.randint(0, 1000) for i in range(50)]
    print(ls)
    shell_sort(ls)
    print(ls)