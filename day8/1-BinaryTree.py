# 作者：朱志浩
# Mail：211283810@qq.com

class Node:
    def __init__(self, elem=None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:
    def __init__(self):
        self.root = Node()
        self.help_squeue = []

    def add(self, elem):
        node = Node(elem)

        if self.root.elem is None:
            self.root = node

        elif self.help_squeue[0].lchild is None:
            self.help_squeue[0].lchild = node

        else:
            self.help_squeue[0].rchild = node
            self.help_squeue.pop(0)

        self.help_squeue.append(node)

    def preorder(self, node1:Node):
        if node1:
            print(node1.elem)
            self.preorder(node1.lchild)
            self.preorder(node1.rchild)


    def midorder(self, node1:Node):
        if node1:
            self.preorder(node1.lchild)
            print(node1.elem)
            self.preorder(node1.rchild)

    def lastorder(self, node1: Node):
        if node1:
            self.preorder(node1.lchild)
            self.preorder(node1.rchild)
            print(node1.elem)

    def levelorder(self, node1: Node):
        list1 = [node1]
        while len(list1) > 0:
            print(list1[0].elem)
            if list1[0].lchild is None:
                pass
            else:
                list1.append(list1[0].lchild)
            if list1[0].rchild is None:
                pass
            else:
                list1.append(list1[0].rchild)
            list1.pop(0)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    tree = BinaryTree()
    for i in a:
        newnode = Node(i)
        tree.add(i)

    # tree.preorder(tree.root)
#
    tree.levelorder(tree.root)

