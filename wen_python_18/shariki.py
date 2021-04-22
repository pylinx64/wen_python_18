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
    def __init__(self, x, y):
        # радиус Bubble
        self.r = random.uniform(3, 10)
    
    def update(self):
        pass
        
        
class App:
    def __init__(self):
        # создает экран
        pyxel.init(SCREEN[0], SCREEN[1])
        
        # запускает мышку
        pyxel.mouse(True)
        
        # запускает программу
        pyxel.run(self.update, self.draw)     
        
    def update(self):
        # проверяет нажата ли клавиша Q
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
    def draw(self):
        # очищает экран
        pyxel.cls(0)
        
        pyxel.text(SCREEN[0] / 2 - 30, SCREEN[1] / 2, "Hello Cyberpank 2088", pyxel.frame_count % 16)
     
# запускаем класс "Приложение"        
App()
