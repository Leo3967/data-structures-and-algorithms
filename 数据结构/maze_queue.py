# 迷宫问题
from collections import deque
from ntpath import realpath
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y-1),
    lambda x, y: (x, y+1)
]

def print_r(path):
    curNode = path[-1]
    real_path = []
    while curNode[2] != -1:
        real_path.append(curNode[0: 2])
        curNode = path[curNode[2]]
    real_path.append(curNode[0: 2])
    real_path.reverse()
    for i in real_path:
        print(i)

def maze_path_queue(x1, y1, x2, y2):
    q = deque()
    q.append((x1, y1, -1))  # 第三个位置记录这个点是由哪个点来的
    path = []
    while len(q) > 0:
        curNode = q.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 到达重点
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                q.append((nextNode[0], nextNode[1], len(path)-1))  # 后续节点进队
                maze[nextNode[0]][nextNode[1]] = 2  # 标记为已经走过
    else:
        print('没有路')
        return False
maze_path_queue(1, 1, 8, 8)