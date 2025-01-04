# 作者：朱志浩
# Mail：211283810@qq.com

import copy


def use_list_copy():
    list1 = [1, 2, 3]
    list2 = list1.copy()
    list3 = [1, 2, [1, 3]]
    list4 = list3.copy()
    list4[2][1] = 4
    print(list1)
    print(list2)
    print(list3)
    print(list4)

# list自带的copy是浅copy，只复制第一层，其余层仍然是引用


def use_copy():
    c = [[1, 3], 2, 3]
    d = copy.copy(c)
    d[0][0] = 99
    print(id(c))
    print(id(d))
    print(c)
    print(d)
# 浅copy

def use_deepcopy():
    c = [[1, 3], 2, 3]
    d = copy.deepcopy(c)
    d[0][0] = 99
    print(id(c))
    print(id(d))
    print(c)
    print(d)

if __name__ == '__main__':
    # use_list_copy()
    # use_copy()
    use_deepcopy()