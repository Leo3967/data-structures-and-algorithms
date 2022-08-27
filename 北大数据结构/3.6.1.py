# -*- coding: UTF-8 -*-
from pythonds.basic.stack import Stack
# 后缀表达式求值

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenlist = postfixExpr.split()

    for token in tokenlist:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()

def doMath(token, op1, op2):
    if token == "*":
        return op1 * op2
    elif token == "/":
        return op1 / op2
    elif token == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval("30 40 * 50 60 * +"))