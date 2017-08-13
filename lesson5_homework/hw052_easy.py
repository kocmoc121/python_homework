# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

def make_dir(name_dir):
	new_dir = os.path.join(os.getcwd(), name_dir)
	try:
		os.mkdir(new_dir)
	except FileExistsError:
		print('Папки уже созданы')
	print(new_dir)


def del_dir(name_dir):
	new_dir2 = os.path.join(os.getcwd(), name_dir)
	print(new_dir2)
	os.rmdir(new_dir2)
	



# Задача-2:
# Напишите скрипт отображающий папки текущей директории
def list_this_dir():
	list_dir = os.listdir()
	print (list_dir)
	only_dir = []

	for f in list_dir:
		if os.path.isdir(f):
			only_dir.append(f)

	print (only_dir)		


if __name__ == '__main__':
	for i in range(9):
		new_dir = os.path.join(os.getcwd(), 'dir_'+str(i+1))
		try:
			os.mkdir(new_dir)
		except FileExistsError:
			print('Папки уже созданы')
		print(new_dir)

	for i in range(9):
		new_dir2 = os.path.join(os.getcwd(), 'dir_'+str(i+1))
		print(new_dir2)
		os.rmdir(new_dir2)
	
	list_dir = os.listdir()
	print (list_dir)
	only_dir = []

	for f in list_dir:
		if os.path.isdir(f):
			only_dir.append(f)

	print (only_dir)		





	# Задача-3:
	# Напишите скрипт создающий копию файла, из которого запущен данный скрипт
	print ('---------------3--------------')
	name_script = sys.argv[0]
	new_name = name_script[0:-3] + '_copy.py'
	print (name_script)
	print(new_name)
	shutil.copy(name_script, new_name)