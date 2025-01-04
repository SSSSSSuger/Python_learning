# 作者：朱志浩
# Mail：211283810@qq.com

import re


def simple():
    result = re.match("abc", "abc.b")
    if result:
        print(result.group())


def single():
    """
    匹配单个字符
    :return:
    """
    ret = re.match('.', 'nM')
    print(ret.group())

    ret = re.match('n.m', 'nMm')
    print(ret.group())
    print('-' * 50)

    ret = re.match('[hH]', 'Hmmm')
    print(ret.group())

#   匹配0-99
    ret = re.match('[1-9]?[0-9]', '0')
    print(ret.group())

    ret = re.match(r"嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())


def more_alp():
    """
    多字符
    :return:
    """
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())

    print('*'*50)

    names = ["name1", "_name", "2_name", "__name__"]

    for name in names:
        ret = re.match(r'^[a-zA-Z_]+\w*', name)
        if ret:
            print(f'{name}符合要求')
        else:
            print(f'{name}不符合要求')
    print('-' * 50)

    print('-' * 50)
    ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
    print(ret.group())
    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455%ff66")
    print(ret.group())


def start_end():
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for email in email_list:
        ret = re.match(r'^[a-zA-z0-9]{4,20}@163\.com$', email)
        if ret:
            print(f'{email}符合要求')
            print()
        else:
            print(f'{email}不符合要求')


def split_group():
    """
    分组
    :return:
    """
    # 匹配0-100
    ret = re.match('[1-9]?[0-9]$|100$', '1000')
    # ret = re.match('[1-9]?[0-9]$|100', '1000')
    if ret:
        print(ret.group())
    else:
        print('buzai 0-100')

    ret = re.match(r"([^-]+)-(\d+)", "010-12345678")
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))

    ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmla>")
    print(ret.group())
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
    print(ret.group())
    print('-' * 50)

    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]
    for label in labels:
        # ret = re.match(r"<(\w*)><(\w*)>.*</\2/></\1>", label)
        ret = re.match(r'<(\w+)><(\w+)>(.*)</\2></\1>', label)
        if ret:
            print(label)
        else:
            print("false")


def add(x):
    result = x.group()
    return str(int(result) + 100)


def other_fun():
    ret = re.search(r"\d+", "阅读次数为 9999,点赞888")
    # search只找第一个
    print(ret.group())
    print('-' * 50)

    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)
    print('-' * 50)
    # findall找所有

    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)
    # sub 将匹配字符串替换成repl

    ret = re.sub(r"\d+", lambda x: str(int(x.group()) + 100), "python = 997")
    print(ret)
    # x.group()是匹配字符串 转int 后加100 再转字符串 替换掉原来的str

    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)
    print('-' * 50)
    # 通过调用add函数 实现原匿名函数作用

    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"

    new_text = re.sub(pattern, replacement, text, count=2)
    print(new_text)



if __name__ == '__main__':
    # simple()
    # single()
    # more_alp()
    # start_end()
    # split_group()
    other_fun()