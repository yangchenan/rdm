import random
r = random.randint(1, 100)
count = 0
while True:
	count = count+1
	guess = input('請猜數字:')
	guess = int(guess)
	if guess == r:
		print('答對了')
		print('你玩了', count, '次')	
		break
	elif guess > r:
		print('太大')
	elif guess < r:
		print('太小')
	print('你玩了', count, '次')	


