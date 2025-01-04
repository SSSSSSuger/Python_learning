# 作者：朱志浩
# Mail：211283810@qq.com

my_list = "This is a test string from Andrew".split()
print(my_list)

student_tuples = [
    ('jane', 'B', 12),
    ('john', 'A', 15),
    ('dave', 'B', 10),
]

a = sorted(student_tuples, key=lambda x: x[2])
print(a)


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__来说，更方便，可以返回非字符串类型
        :return:
        """
        return repr((self.name, self.grade, self.age))


student = Student('john', 'A', 15)
print(student)
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print('-' * 50)
print(sorted(student_objects, key=lambda student:student.age))
