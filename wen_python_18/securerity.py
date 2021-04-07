from cryptography.fernet import Fernet

# коробка с АНГЛИЙСКИМ текстом
a = b'Hello world'
#print(a)

# ключ
key = Fernet.generate_key()
#print(key)

# шифровальщик
cript = Fernet(key)

# шифруем сообщения
secure_a = cript.encrypt(a)
print(secure_a)

# расшифровка
unsecure_a = cript.decrypt(secure_a)
print(unsecure_a)


#-------------------------------------
# создаем файл через пайтон
text = 'python 2077'
with open('message.txt', 'w') as f: # write
    f.write(text)

# читаем файл через пайтон
text_doc = open('message.txt', 'r').read() # read
print(text_doc)
