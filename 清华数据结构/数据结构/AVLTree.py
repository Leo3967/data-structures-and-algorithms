from bst import BiTreeNode, BST

class AVLNode(BiTreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.bf = 0  # balance factor

class AVLTree(BST):
    def __init__(self, li) -> None:
        super().__init__(li)

    def rotate_left(self, p, c):
        # 左旋; p, c 对应图上的P和C
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c
        # 需要更新balance factor
        p.bf = 0
        c.bf = 0
        return c
    
    def rotate_right(self, p, c):
        # 右旋
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.right = p
        p.parent = c
        p.bf = 0
        c.bf = 0
        return c
    
    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g
        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        else:  
            p.bf = 0
            c.bf = 1
        g.bf = 0
        return g
    
    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g
        # 更新bf
        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        else: 
            p.bf = 0
            c.bf = -1
        g.bf = 0
        return g
    
    def insert_no_rec(self, val):
        # 1. 和BST一样，插入， 非递归
        p = self.root
        if not p:
            # 空树的情况
            self.root = AVLNode(val)
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左子树不存在
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # node存储的是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:  # 右子树不存在
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:
                return
        # 2. 更新balance factor
        while node.parent:  # 保证node父亲节点有值
            if node.parent.lchild == node:  # 2.1 传递是从左子树来的，左子树更沉了
                # 目的是更新node.parent的balance factor -= 1
                if node.parent.bf < 0:  # 原来node.parent的bf=-1，更新之后变成-2
                    # 看node哪边沉，进行旋转
                    g = node.parent.parent  # 为了旋转后的连接
                    x = node.parent  # 旋转前子树的根
                    if node.bf > 0:  # 右边沉，左旋右旋
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得把g和n连起来
                elif node.parent.bf > 0:  # 原来node.parent的bf=1，更新之后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent的bf=0，更新之后变成-1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:  # 2.2 传递是从右子树来的，右子树更沉了
                # 更新node.parent.bf += 1
                if node.parent.bf > 0:  # 原来node.parent的bf=1，更新之后变成2
                    # 看node哪边沉，进行旋转
                    g = node.parent.parent  # 为了旋转后的连接
                    x = node.parent  # 旋转前子树的根
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                elif node.parent.bf < 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue
            
            # 连接旋转后的子树
            n.parent = g
            if g:
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


            
tree = AVLTree([9,8,7,6,5,4,3,2,1])
tree.pre_order(tree.root)
print('')
tree.in_order(tree.root)