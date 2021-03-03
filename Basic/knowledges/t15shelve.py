import shelve

# 自定义class
class Student(object):
    def __init__(self, name, age, sno):
        self.name = name
        self.age = age
        self.sno = sno

    def __repr__(self):
        return 'Student [name: %s, age: %d, sno: %d]' % (self.name, self.age, self.sno)

# 保存数据
tom = Student('Tom', 19, 1)
jerry = Student('Jerry', 17, 2)

with shelve.open('../data/stu.db') as db:
    db['Tom'] = tom
    db['Jerry'] = jerry
    db['attr1'] = 1
    db['attr2'] = [3,5,7]

# 读取数据
with shelve.open('../data/stu.db') as db:
    a = db['Tom']
    b = db['Jerry']
    c = db['attr1']
    d = db['attr2']

print(type(a))  # <class '__main__.Student'>
print(a)        # Student [name: Tom, age: 19, sno: 1]
print(a.name)   # Tom
print(b)        # Student [name: Jerry, age: 17, sno: 2]
print(c)        # 1
print(d)        # [3, 5, 7]