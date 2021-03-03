class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglLinkList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.head == None

    def length(self):
        '''返回链表长度'''
        cur = self.head  # 指针
        count = 0  # 计数器
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        cur = self.head  # 指针
        while cur != None:
            print(cur.value, end=' ')
            cur = cur.next
        print()

    def add(self, value):
        '''头部插入——头插法'''
        node = Node(value)
        node.next = self.head  # 把新节点夹在head之前
        self.head = node  # 链表的新头部编程node
        pass

    def append(self, value):
        '''尾部插入——尾插法'''
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, index, value):
        '''
        :param index: the position of insert(start from 0)
        :param value: node.value
        :return:
        '''
        node = Node(value)
        if index <= 0:
            self.add(node)
        elif index > self.length():
            self.append(node)
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        '''从链表中删除item'''
        # 如果空链表
        if self.head == None:
            return
        else:
            # 如果第一个就命中
            if self.head.value == item:
                self.head = self.head.next
            else:
                cur = self.head
                while True:
                    if cur.next != None:
                        if cur.next.value == item:
                            cur.next = cur.next.next
                            break
                        else:
                            cur = cur.next
                    else:
                        break

    def search(self, item):
        '''在链表中查找item，含有返回True，不含返回False（因为是链表，返回索引也没有意义）'''
        cur = self.head
        while cur != None:
            cur = cur.next
            if cur.value == item:
                return True
        return False


if __name__ == '__main__':
    sll1 = SinglLinkList()
    print(sll1.is_empty())
    print(sll1.length())
    sll1.append(6)
    print(sll1.is_empty())
    sll1.add(10)
    sll1.append(7)
    sll1.append(8)
    print(sll1.length())
    sll1.insert(4, 22)
    sll1.travel()
    sll1.remove(10)
    sll1.travel()
    sll1.remove(7)
    sll1.travel()
    sll1.remove(22)
    sll1.travel()
    sll1.remove(10)
    sll1.travel()
    # sll1.remove(8)
    # sll1.remove(8)
    # sll1.travel()
