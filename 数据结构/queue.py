class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0
    
    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('Queue is filled.')
    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.rear]
        else:
            raise IndexError('Queue is empty.')

    def is_empty(self):
        return self.rear == self.front
    
    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

# q = Queue(5)
# for i in range(4):
#     q.push(i)
# q.pop()
# print(q.queue)

from collections import deque

def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)  # maxsize满了队首自动出队
    return q
for line in tail(5):
    print(line, end='')