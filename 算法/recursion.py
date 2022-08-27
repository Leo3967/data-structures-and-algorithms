# 汉诺塔问题
def move(n, a, b, c):
	# n表示有几个圆盘
	if n == 0:
		return
	else:
		move(n-1, a, c, b)
		print('moving from %s to %s'%(a, c))
		move(n-1, b, a, c)
	return


if __name__ == '__main__':
	# 初始化三个塔
	move(6, 'a', 'b', 'c')
