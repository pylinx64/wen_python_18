def say():
	print('Hello')

def sum2(a, b):
	s = a + b
	return s

def sum3(a, b, c):
	s = sum2(a, sum2(b, c))
	return s

def sumList(a=[]):
	s = a[0]
	for elem in a:
		s = s + elem
	return s
	
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sumList(numbers))

# процедура
say()

#функция с вых данными
z=sum2(1, 2)
print(z)

print(sum2(1, 2))
