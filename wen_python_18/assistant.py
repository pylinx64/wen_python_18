import pyttsx3
import webbrowser


tts = pyttsx3.init()			# подключаем голосовой движок
tts.setProperty('rate', 200)

def say_bot(msg):
	print(msg)
	tts.say(msg)				# собирает фразы
	tts.runAndWait()			# запускает голос

say_bot('Приветсвую. Я ассистент версия 2.0')
command = input('Введите команду: ')
if command == 'Привет':			# Работает если True (Привет есть в command)
	say_bot('Ну привет')
elif command == 'Как дела':			# Работает если True (Привет есть в command)
	say_bot('Норм')
elif command == 'открой браузер':			
	webbrowser.open('youtube.com')
	say_bot('Сайт открыт')
else:							# Работает если False (Привет нету в command)
	say_bot('Я тебя не понимаю')
	
