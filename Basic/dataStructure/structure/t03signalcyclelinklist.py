class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglCycleLinkList(object):
    def __init__(self, node=None):
        self.head = None
        if node:    # 每加入一个节点，就是一个指向自己的循环链表？
            node.next = node

    def is_empty(self):
        '''判断链表是否为空'''
        return self.head == None

    def length(self):
        '''返回链表长度'''
        if self.is_empty(): # 如果链表为空
            return 0
        cur = self.head  # 指针
        count = 1  # 计数器
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        if self.is_empty():
            return
        cur = self.head  # 指针
        while cur.next != self.head:
            print(cur.value, end=' ')
            cur = cur.next
        print(cur.value)

    def add(self, value):
        '''头部插入——头插法'''
        node = Node(value)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head  # 把新节点夹在head之前
            self.head = node       # 链表的新头部编程node
            cur.next = self.head   # 尾部指向新头部


    def append(self, value):
        '''尾部插入——尾插法'''
        node = Node(value)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def insert(self, index, value):
        '''
        :param index: the position of insert(start from 0)
        :param value: node.value
        :return:
        '''
        node = Node(value)
        if index <= 0:
            self.add(value)
        elif index > self.length():
            self.append(value)
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
        # 如果为空
        if self.head == None:
            return
        # 如果第一个命中
        if self.head.value == item:
            # 如果只有一个元素
            if self.length() == 1:
                self.head = None
                return
            else:
                rear = self.head    # 用这个索引去找尾
                while rear.next != self.head:
                    rear = rear.next
                self.head = self.head.next
                rear.next = self.head
        else:
            cur = self.head
            while cur.next != self.head and cur.next.value != item:
                cur = cur.next
            if cur.next.value == item:
                cur.next = cur.next.next

    def search(self, item):
        '''在链表中查找item，含有返回True，不含返回False（因为是链表，返回索引也没有意义）'''
        if self.is_empty():
            return False
        cur = self.head
        if cur.value == item:
            return True
        else:
            while cur != self.head:
                cur = cur.next
                if cur.value == item:
                    return True
            return False


if __name__ == '__main__':
    sll1 = SinglCycleLinkList()
    print(sll1.is_empty())
    sll1.append(6)
    print(sll1.length())
    sll1.travel()
    print(sll1.is_empty())
    sll1.add(10)
    sll1.travel()
    sll1.append(7)
    sll1.append(8)
    print(sll1.length())
    sll1.insert(4, 22)
    sll1.travel()
    sll1.remove(10)
    sll1.travel()
    sll1.remove(22)
    sll1.travel()
    sll1.remove(10)
    sll1.travel()
    # sll1.remove(7)
    # sll1.travel()
    # sll1.remove(8)
    # sll1.travel()
