# -*- coding: UTF-8 -*-
# 树的应用：解析树（语法树）,表达式解析
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator

def buildTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild() # 下降到左子树
        elif i not in ["+", '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ["+", '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight("")
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")":
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

t = buildTree('( ( 3 * 5 ) + ( 5 * 7 ) )')
print(t)
print(evaluate(t))