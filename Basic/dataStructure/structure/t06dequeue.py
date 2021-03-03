class Dequeue(object):
    def __init__(self):
        '''初始化一个空队列'''
        self.__list = []

    def add_front(self, item):
        '''从队列首添加'''
        self.__list.insert(0, item)

    def add_rear(self, item):
        '''从队列尾添加'''
        self.__list.append(item)

    def pop_front(self):
        '''从队列首删除'''
        return self.__list.pop(0)   # 时间复杂度O(n)

    def pop_rear(self):
        '''从队列尾删除'''
        return self.__list.pop()

    def is_empty(self):
        '''是否空'''
        return not self.__list

    def size(self):
        '''元素数量'''
        return len(self.__list)

if __name__ == '__main__':
    dq = Dequeue()
    dq.add_front(4)
    dq.add_front(5)
    dq.add_rear(6)
    print(dq.size())
    print(dq.pop_front())
    print(dq.size())
    print(dq.pop_rear())
    print(dq.size())
