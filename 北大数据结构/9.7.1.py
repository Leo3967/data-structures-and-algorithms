# -*- coding: UTF-8 -*-
# 树的遍历

# 前序遍历
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# 后序遍历
def postorder(tree):
    if tree != None :
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRootVal())

# 中序遍历
def inorder(tree):
    if tree != None:
        preorder(tree.getLeftChild())
        print(tree.getRootVal())
        preorder(tree.getRightChild())


