class Stack(object):
    def __init__(self):
        self.__list = []    # 通过list来实现

    def push(self, value):
        '''压/入栈：从栈顶添加元素'''
        self.__list.append(value)   # 把list的尾部当做栈顶来用

    def pop(self):
        '''出栈，从栈顶取元素'''
        self.__list.pop()   # 把list的尾部当做栈顶

    def peek(self):
        '''返回栈顶元素'''
        if self.__list:
            return self.__list[-1]
        else:
            return

    def is_empty(self):
        return not self.__list

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    ss = Stack()
    print(ss.is_empty())
    ss.push(2)
    ss.push(3)
    ss.push(4)
    print(ss.size())
    print(ss.is_empty())
    ss.pop()
    print(ss.size())
    print(ss.is_empty())
    print(ss.peek())
