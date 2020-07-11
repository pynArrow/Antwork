'''
每个数从低位往高位取，每次取一位数，并对所有数的同一位计数排序。
'''

import math
import random 

def radix_sort(mlist):   
    def get_bit(num, index):
        return num//(int(math.pow(10, index)))%10

    max_num = max(mlist)
    max_bit = int(math.log10(max_num))+1
    for i in range(0, max_bit):
        res = []
        radix = [[] for _ in range(10)]
        for num in mlist:
            radix[get_bit(num, i)].append(num)
        for j in range(10):
            res += radix[j]
        mlist = res
    return mlist


if __name__ == '__main__':
    ls = [random.randint(0, 1000) for i in range(50)]
    print(ls)
    ls = radix_sort(ls)
    print(ls)