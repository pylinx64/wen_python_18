import pyxel 
import math
import random

# Глобальные переменные
SCREEN = [256, 256]
MAX_SPEED_BUBBLE = 1.8

# создаем класс вектор
class Vec2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

'''
# vectorA - это экземпляр класса
# Vec() - класс
vectorA = Vec2(2, 3)
print(vectorA.__dict__)    
'''

class Bubble:
	def __init__(self):
		# радиус Bubble
		self.radius = random.uniform(3, 10)
		
		# рандомная позиция
		self.position = Vec2(
		random.uniform(self.radius, SCREEN[0] - self.radius),
		random.uniform(self.radius, SCREEN[1] - self.radius)
		)
		
		# цвет
		self.color = random.randint(0, 15)
		
		# скорость шариков
		self.vel = Vec2(
		random.uniform(-MAX_SPEED_BUBBLE, MAX_SPEED_BUBBLE), 
		random.uniform(-MAX_SPEED_BUBBLE, MAX_SPEED_BUBBLE)
		)
	
	def update(self):
		pass
		
		
class App:
	def __init__(self):
		# создает экран
		pyxel.init(SCREEN[0], SCREEN[1])
		
		# запускает мышку
		pyxel.mouse(True)
		
		# создаем список из объектов Bubble
		self.bubble_list = []
		for x in range(10):
			self.bubble_list.append(Bubble())
		
		# запускает программу
		pyxel.run(self.update, self.draw)     
		
	def update(self):
		# проверяет нажата ли клавиша Q
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
		
	def draw(self):
		# очищает экран
		pyxel.cls(0)
		
		# x, y, радиус, цвет
		#pyxel.circ(100, 100, 20, 6)
		
		for bubble in self.bubble_list:
			pyxel.circ(bubble.position.x, bubble.position.y, bubble.radius, bubble.color)
		
		pyxel.text(SCREEN[0] / 2 - 30, SCREEN[1] / 2, "Hello Cyberpank 2088", pyxel.frame_count % 16)
	 
# запускаем класс "Приложение"        
App()
