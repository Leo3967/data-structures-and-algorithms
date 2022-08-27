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
    def is_empty(self):
        return len(self.stack) == 0

def brace_match(s):
    match = {'}': '{', ')':'(', ']': '['}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:  # 集合的in比列表的快
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.gettop() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else: 
        return False


s1 = '[][{[()}]'
s2 = '[([{}])]'

print(brace_match(s1))
print(brace_match(s2))