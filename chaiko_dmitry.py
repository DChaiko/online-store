
# Текст
text = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'

# Колличество симлволов
textLenght = len(text)

# Развернутая строка
textBackwards = text[::-1]

# Заглавные буквы
textTitled = text.title()

# Прописные буквы
textBig = text.upper()

# Колличество "нд", "ам", "о"
nd = text.count('нд')
am = text.count('ам')
o = text.count('о')

# Сообственное упражнение
print (max(text.split(), key = len))

# Вывод
print(text)
print(textBackwards[:len(text)-4:], '\n', textTitled[:len(text)-4:], '\n', textBig[:len(text)-4:])
print(nd > text.count('ор'))
