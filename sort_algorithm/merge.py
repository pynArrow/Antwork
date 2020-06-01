'''
归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，取较小的数，
取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
'''

import random 

def merge_sort(mlist):
    def merge_divide(mlist, left, right):
        if left >= right:
            return
        mid = (left+right)//2
        merge_divide(mlist, left, mid)
        merge_divide(mlist, mid+1, right)
        merge_conquer(mlist, left, mid, right)

    def merge_conquer(mlist, left, mid, right):
        res = []
        left_pos = left
        right_pos = mid+1
        while left_pos <= mid and right_pos <= right:
            if mlist[left_pos] <= mlist[right_pos]:
                res.append(mlist[left_pos])
                left_pos += 1
            else:
                res.append(mlist[right_pos])
                right_pos += 1             
        while left_pos <= mid:
            res.append(mlist[left_pos])
            left_pos += 1
        while right_pos <= right:
            res.append(mlist[right_pos])
            right_pos += 1
        for i in range(left, right+1):
            mlist[i] = res[i-left]
    merge_divide(mlist, 0, len(mlist)-1)
                
if __name__ == '__main__':
    ls = [random.randint(0, 1000) for i in range(50)]
    print(ls)
    merge_sort(ls)
    print(ls)