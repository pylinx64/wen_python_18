# -*- coding: utf-8 -*-

import socket
import time
import threading


def receving (name, sock, switch):
	while not switch:
		try:
			while True:
				# data - сообщение, addr - ip человека
				data, addr = sock.recvfrom(1024) 
				# декодирует сообщение и печатает в ВАШУ консоль
				print('\n'+data.decode("utf-8"))
				time.sleep(0.2)
		except:
			pass	

	
# коробка для выключения, для подключение	
shutdown = False
join = False

# ваш ip, порт
host = socket.gethostbyname(socket.gethostname())
port = 0

# сервера ip, порт
server = ('192.168.31.17', 11719)

# сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

name = input('name > ')
# отправляет сообщение
s.sendto(("["+name+"] => join chat ").encode("utf-8"), server)
time.sleep(0.2)

# запускает сбор сообщений с сервера
rT = threading.Thread(target = receving, args = ("RecvThread", s, shutdown))
rT.start()

# запускает отправку сообщений
while shutdown == False:
	try:
		message = input("["+name+"] > ")
		s.sendto(("["+name+"] > " + message).encode("utf-8"), server)
		time.sleep(0.2)
	except:
		s.sendto(("["+name+"] <= left chat ").encode("utf-8"), server)
		shutdown = True

# прекращает сбор сообщений с сервера, закрывает сооединение
rT.join()
s.close()
