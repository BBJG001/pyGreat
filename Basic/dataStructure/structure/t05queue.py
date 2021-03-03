class Queue(object):
    def __init__(self):
        '''初始化一个空队列'''
        self.__list = []

    def enqueue(self, item):
        '''入队列'''
        self.__list.append(item)

    def dequeue(self):
        '''出队列'''
        return self.__list.pop(0)   # 时间复杂度O(n)
    # 在使用list的情况下，enqueue 与 dequeue的时间复杂度总是一个O（1），一个O（n）
    # 应该视操作入队还是出队操作多而决定应用list的方法

    def is_empty(self):
        '''是否为空'''
        return not self.__list

    def size(self):
        '''队列中元素数量'''
        return len(self.__list)