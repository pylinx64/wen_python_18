import telebot
import requests
import bs4
import random

def elon_gif():
    '''Функция которая находит рандомную с gif'''
    # подключаемся к сайту
    res = requests.get('https://tenor.com/search/elon-gifs')
    # проверяем сайт
    res.raise_for_status()
    # анализируем сайт
    soup = bs4.BeautifulSoup(res.text)
    # ищем картинки
    gifElem = soup.select('img[src]')
    gif_list = []
    # скачиваем ссылки
    for i in gifElem:
        gifUrl = i.get('src')
        gif_list.append(gifUrl)
    # выбираем рандомную ссылку и сохраняем ее
    gif_random = random.choice(gif_list)
    return gif_random


bot = telebot.TeleBot('ваш бот') # сюда токен

@bot.message_handler(commands=['start'])
def start_message(message):
    '''Принимает команду и отвечает на нее'''
    bot.send_message(message.chat.id, 'Привет, я чат-бот с котиками!🐈')
    
    
@bot.message_handler(content_types=['text'])
def send_text(message):
	'''Принимает сообщение текст и отвечает на них'''
	#print(message)
	if 'привет' in message.text.lower():
		 bot.send_message(message.chat.id, 'Хай!')
		 bot.send_sticker(message.chat.id, '')
		 
   	elif 'шарк' in message.text.lower():
		 bot.send_message(message.chat.id, 'https://i.pinimg.com/originals/7d/d6/2f/7dd62ff2aaa072239d0810ae5c66a8aa.gif')
		 
	elif 'илон' in message.text.lower():
		 bot.send_message(message.chat.id, elon_gif())
	
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
	'''Ловит стикеры и отправляет их обратно'''	 
	print(message.sticker.file_id)
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    
    
print('> bot run...')
bot.polling()
