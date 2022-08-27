# 封装成类



class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()
    
    def gettop(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]