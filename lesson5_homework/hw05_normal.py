# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов: 1, 3,4, программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/прейти"

# Для решения данной задачи используйте алоритмы из задания easy,
# оформленныйе в виде соответствующих функций, и импортированные в данный файл из easy.py

import os
import sys
import hw052_easy

def print_help():
    print('help - получить справку')
    print('mkdir <dir_name> - создать папку')
    print('rmdir <dir_name> - удалить папку')
    print('goto <dir_name> - перейти в папку')
    print('listdir  - просмотр содержимого папки')


while True:
	print ('print command "print_help" for help :)')
	name_input = input ("Введите команду: ")
	if name_input == 'mkdir':
		dir_name = input ('Название папки: ')
		hw052_easy.make_dir(dir_name)
	elif name_input == 'rmdir':
		dir_name = input ('Название папки: ')
		hw052_easy.del_dir(dir_name)
	elif name_input == 'listdir':
		hw052_easy.list_this_dir()
	elif name_input == 'goto':
		dir_name = input ('Полное название папки: ')
		try:
			
			os.chdir(dir_name)
			print('Действие успешно')
			print('Текущая папка' + str(os.getcwd())
		except FileNotFoundError:
			print('Указанной дирректории не существует')
	else:
		break





