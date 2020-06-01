'''
计数排序用待排序的数值作为计数数组（列表）的下标，统计每个数值的个数，然后依次输出即可。
'''


import random 

def count_sort(clist):
    clist_len = len(clist)
    cnt = [0]*(max(clist)+1)
    tmp = []*clist_len
    for i in range(clist_len):
        cnt[clist[i]] += 1
    for i in range(len(cnt)):
        for _ in range(cnt[i]):
            tmp.append(i)

    return tmp
                
if __name__ == '__main__':
    ls = [random.randint(0, 1000) for i in range(50)]
    print(ls)
    ls = count_sort(ls)
    print(ls)