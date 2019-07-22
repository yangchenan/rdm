import random
r = random.randint(1, 100)
while True:
	guess = input('請猜數字:')
	guess = int(guess)
	if guess == r:
		print('答對了')
		break
	elif guess > r:
		print('太大')
	elif guess < r:
		print('太小')