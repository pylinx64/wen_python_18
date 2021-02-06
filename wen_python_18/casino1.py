import random

print("-> Приветствую тебя в нашем казино! ")

number_random = random.randint(1, 10)
number_player = input("-> Введите число от 1 до 10: ")
number_player = int(number_player)

if number_random == number_player:
	print("-> You WIN $$$")
if number_random == number_player:
	print("-> Game over :((")
	print(number_random)
