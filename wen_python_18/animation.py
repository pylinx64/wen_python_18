import pygame

# инициализируем движок
pygame.init()

# цвета
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# размеры экрана
size = [1280, 800]
screen = pygame.display.set_mode(size)

# заголовок окна
pygame.display.set_caption("Cool ITFriends Game")

# Используется для FPS
clock = pygame.time.Clock()

#------------------------ОСНОВНОЙ ЦИКЛ------------------------
done = True
while True == done:
	# СОБЫТИЯ
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = False
	# СОБЫТИЯ КОНЕЦ		
	
	
	# РИСОВАНИЕ
	# линия (экран, цвет, точка1, точка2, толщина)
	pygame.draw.line(screen, white, [10, 30], [290, 15], 10)
	# РИСОВАНИЕ КОНЕЦ
	
	
	# ЛОГИКА
	# ЛОГИКА КОНЕЦ
	
	# обновляем экран
	pygame.display.flip()
	
	# с какой скоростью обновляется єкран (FPS)
	clock.tick(20)
	
pygame.quit()
	

