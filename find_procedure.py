
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os.path

# Получает список файлов
def get_files():
	migrations = 'Advanced Migrations'
	return glob.glob(os.path.join(migrations, "*.sql"))

# Проверяет и выводит результат 
def check_result(suitable_files):
	if len(suitable_files) > 7:
		print('... большой список файлов ...')
	else:
		for file in suitable_files:
			print(file)
	print('Всего: {}'.format(len(suitable_files)))

# Ищет среди файло (files) те, которые содержат в себе строку (string)
def make_a_selection(files, string):
	suitable_files = []
	for file in files:
		open_file = open(file, 'r')
		if open_file.read().find(string) != -1:
			suitable_files.append(file)
		open_file.close()
	check_result(suitable_files)
	return suitable_files

files = get_files()
check_result(files)

while True:
	string = input('Введите строку: ')
	files = make_a_selection(files, string)

