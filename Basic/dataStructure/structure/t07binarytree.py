class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        '''向二叉树中追加元素'''
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]  # 相当于直接用队列的内部实现机理来处理
        # 直到出现第一个空位置，（这是一个完全二叉树）
        while queue:
            cur_node = queue.pop(0)  # 把低位当做队列的出口
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)  # 层次遍历，如果不为空，加进去
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)  # 层次遍历，如果不为空，加进去

    def breadth_travel(self):
        '''广度优先遍历'''
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if not cur_node.lchild is None:
                queue.append(cur_node.lchild)
            if not cur_node.rchild is None:
                queue.append(cur_node.rchild)

    def preorder(self, rootnode):
        '''先序遍历'''
        if rootnode is None:
            return
        print(rootnode.elem, end=' ')
        self.preorder(rootnode.lchild)
        self.preorder(rootnode.rchild)

    def inorder(self, rootnode):
        '''中序遍历'''
        if rootnode is None:
            return
        self.inorder(rootnode.lchild)
        print(rootnode.elem, end=' ')
        self.inorder(rootnode.rchild)

    def postorder(self, rootnode):
        '''后续遍历'''
        if rootnode is None:
            return
        self.postorder(rootnode.lchild)
        self.postorder(rootnode.rchild)
        print(rootnode.elem, end=' ')


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print()
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()
