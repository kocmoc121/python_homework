#!/usr/bin/python3

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Ticket:
	
	def __init__ (self):
		pass

	def ticket_create(self):
		x = 0
		self.ticket = []
		tmp_ticket = []
		counter = 90
		for r in range(3): 
			self.ticket.append([]) 
			for c in range(5): 
				
				while True:
					ch = False
					x = random.randint(1,90)
					for df in range(len(self.ticket)):
						for df2 in range(len(self.ticket[df])):
							if x == self.ticket[df][df2]:
								ch = True
					if ch:
						continue
					else:
						break
			
				self.ticket[r].append(x) 
		for i in range(3):
			self.ticket[i].sort()


	def del_number(self, number):
		self.number = number
		x = 0
		for i in range(len(self.ticket)):
			for j in range(len(self.ticket[i])):
				if  self.ticket[i][j] == self.number:
					self.ticket[i][j] = '-'
					x = 1
		return x

	def print_ticket(self):
		
		for i in range(len(self.ticket)):
			for j in range(len(self.ticket[i])):
				if self.ticket[i][j] == '-' and j != (len(self.ticket[i])-1):
					print(self.ticket[i][j] , end='...')
				elif self.ticket[i][j] == '-' and j == (len(self.ticket[i])-1):
					print(self.ticket[i][j] , end=' ')
				elif self.ticket[i][j]<10:
					print(self.ticket[i][j] , end='...')
				elif j == (len(self.ticket[i])-1):
					print(self.ticket[i][j] , end=' ')
				else:
					print(self.ticket[i][j] , end='..')

			print()

#функция печатает билеты (пока для игрок-комп)
def print_players(a, b):
	print('Игрок')
	a.print_ticket()
	print()
	print('Компьютер')
	b.print_ticket()
	print()


numbers = []

#создаем 2 билета - игрок и комп, в дальнейшем будет функция где выбирается - игрок-игрок, игрок-комп, комп-комп
t = Ticket()
t.ticket_create()
comp = Ticket()
comp.ticket_create()

print_players(t, comp)


while True:
	c = 2	
	p = 2
	d = 2
	tmp = 0
	check_number = ''

	#рандом для бочонка
	num = random.randint(1,90)
	for i in range(len(numbers)):
		if num == numbers[i]:
			tmp = 1
	if tmp == 1:
		continue
	numbers.append(num)
	
	#отображаем выбранный бочонок
	lenth = 90-len(numbers)
	print ('Бочонок номер ' + str(num) + ' (в игре осталось {} бочонов)'.format(lenth))
	
	#проверка игрока
	check_number = input ('Зачеркнуть цифру? (y/n) ')
	if check_number == 'y':
		c = t.del_number(num)
	elif check_number == 'n':
		p = t.del_number(num)
	if c == 0 or p == 1:
		print ('Игрок проиграл')
		break
	
	#проверка компа
	d = comp.del_number(num)
	if d == 0:
		print ('Компьютер проиграл')
		break	
	
	print_players(t, comp)



