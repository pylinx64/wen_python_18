def exp(a,b):
	s = a ** b
	return s
	
z=exp(2, 3)
#print(z)

import time, colorama
from colorama import Fore, Back, Style
# запуск движка
colorama.init()
def test1(a, b):
	print(Fore.RED + '---------#test1----------')
	et = time.time()
	res = exp(a, b)
	st = time.time()
	dt = st - et
	print(Fore.RED + '#time - ', dt)
	if dt > 5:
		print(Fore.RED + '##test1 failed')
	#print('#time - ', res)
	print(Fore.RED + '---------#test1----------')
	
	
#test1(100000, 100000)
try:
	x = int(input('Введите х: '))
	print(x+10)	
except:
	print('Введите пж число!')	
