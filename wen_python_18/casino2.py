import random
import time

print("-> Приветствие: ")


money = input('Введите кол-во сало: ')
money = int(money)

list_win = ['сало', 'фиалка', 'кирпич', 'баклажан', '1000$']
while True:
	if money >= 11:
		win = random.choice(list_win)
		money = money - 10

		print('-> -10 сало')
		print('-> Вы выиграли:')
		print(win)

	elif money < 11:
		print('-> Game over, сало...')
		break
	print('------------------------------')
	time.sleep(1)
