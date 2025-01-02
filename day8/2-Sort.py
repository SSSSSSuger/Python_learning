# 作者：朱志浩
# Mail：211283810@qq.com
import random


class Sort:
    def __init__(self, n):
        self.len = n
        self.arr = [0]*n

    def ramdom_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def quick_sort(self, left, right):



if __name__ == '__main__':
    my_sort = Sort(10)
    my_sort.ramdom_data()
    print(my_sort.arr)


