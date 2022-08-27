import numpy as np
import random

def bubble_sort(li):
	temp = None
	for i in range(len(li)-1):
		flag_change = False
		for j in range(len(li)-1-i):
			if li[j] > li[j+1]:
				temp = li[j]
				li[j] = li[j+1]
				li[j+1] = temp
				flag_change = True
		if flag_change == False:
			break
		print(li)	
	return
a = [9,8,7,1,2,3,4,5,6]
bubble_sort(a)
				
				
