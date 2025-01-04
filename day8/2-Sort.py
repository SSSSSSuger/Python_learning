# 作者：朱志浩
# Mail：211283810@qq.com
import random


class Sort:
    def __init__(self, n):
        self.len = n
        self.arr = [0]*n
        self.random_data()

    def ramdom_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, left, right):
        list1 = self.arr

        i = left
        k = left
        key = list1[right]
        while i < right:
            if list1[k]<key:
                list1[k],list1[i] = list1[i],list1[k]
                i += 1
                k += 1
            else:
                i += 1


    def quick_sort(self, list1):
        i = partition





if __name__ == '__main__':
    my_sort = Sort(10)
    my_sort.ramdom_data()
    print(my_sort.arr)


