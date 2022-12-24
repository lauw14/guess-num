import random
r = random.randint(1, 100)
while True:
	num = input('請猜1至100的其中一個數字： ')
	num = int(num)
	if num == r:
		print('你猜中了')
		break
	elif num > r:
		print('你的數字比答案大')
	elif num < r:
		print('你的數字比答案小')
		
	