import random
from winreg import DeleteValue
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self, li) -> None:
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)
    
    def insert(self, node, val):
        # 递归定义
        if node == None:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchid, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchid, val)
            node.rchild.parent = node
        else:  # 认为没有等于的情况
            pass
        return node
    
    def insert_no_rec(self, val):
        # 非递归
        p = self.root
        if not p:
            # 空树的情况
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左子树不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:  # 右子树不存在
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def query(self, node, val):
        # 递归，要有node
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchlid, val)
        elif node.data > val:
            return self.query(node.lchlid, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)
    
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')
    
    def __remove_node_1(self, node):
        # 情况1： node是叶子节点
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = None
            node.parent = None
        else:
            node.parent.rchild = None
            node.parent = None

    def __remove_node_21(self, node):
        # 情况2.1： node只有一个左孩子，将其父亲节点与孩子连接
        if not node.parent:  # 是根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:  # 该node是父亲的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2.2： node只有一个右孩子，将其父亲节点与孩子连接
        if not node.parent:  # 是根节点
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:  # 该node是父亲的右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:  # 1. node是叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:  # 2.1 只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:  # 2.2 只有一个右孩子
                self.__remove_node_22(node)
            else:
                # 3. 两个孩子都有
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删min_node,判读属于哪种情况，肯定是没有左节点的，所以是1 or 2.2
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

li = list(range(1, 10)) 
random.shuffle(li)       
tree = BST(li)
tree.in_order(tree.root)
print('')
tree.delete(4)
tree.delete(1)
tree.in_order(tree.root)