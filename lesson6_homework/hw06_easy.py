# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определть методы позволяющие вычислить: Площадь, высоту и периметр фигуры
import math


class fig_triangle:

	def __init__ (self, x1, y1, x2, y2, x3, y3):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.x3 = x3
		self.y3 = y3
		self.s_A = math.sqrt ((x2-x1)**2 + (y2-y1)**2)
		self.s_B = math.sqrt ((x3-x2)**2 + (y3-y2)**2)
		self.s_C = math.sqrt ((x1-x3)**2 + (y1-y3)**2)
		
	def sq_tr (self):
		p = (self.s_A+self.s_B+self.s_C)/2
		sq = math.sqrt (p*(p-self.s_A)*(p-self.s_B)*(p-self.s_C))
		return sq

	def h_tr(self):
		t = self.sq_tr() 
		h = t*2
		return h/self.s_A

	def p_tr(self):
		per=self.s_A+self.s_B+self.s_C
		return per


res_1 = fig_triangle(0, 0, 0, 1, 2, 0)

print (res_1.p_tr())
print (res_1.sq_tr())
print (res_1.h_tr())

# Задача-2: Написать Класс Равнобочная трапеция, заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.



class fig_trapezium:

	def __init__ (self, x1, y1, x2, y2, x3, y3, x4, y4):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.x3 = x3
		self.y3 = y3
		self.x4 = x4
		self.y5 = y4
		a1 = math.sqrt ((x2-x1)**2 + (y2-y1)**2)
		a2 = math.sqrt ((x3-x2)**2 + (y3-y2)**2)
		a3 = math.sqrt ((x4-x3)**2 + (y4-y3)**2)
		a4 = math.sqrt ((x1-x4)**2 + (y1-y4)**2)
		if a1 == a2:
			self.c = a1
			self.a = a3
			self.b = a4
		elif a1 == a3:
			self.c = a1
			self.a = a2
			self.b = a4
		elif a1 == a4:
			self.c = a1
			self.a = a2
			self.b = a3
		elif a2 == a3:			
			self.c = a2
			self.a = a1
			self.b = a4
		elif a2 == a4:
			self.c = a2
			self.a = a1
			self.b = a3
		elif a3 == a4:
			self.c = a3
			self.a = a1
			self.b = a2
		else:
			print ('Не ок')

	def check_tz(self):
		pass

	def len_tz (self):
		return [self.a, self.b, self.c]

	def sq_tz(self):
		S = ((self.a + self.b)/2) * math.sqrt(self.c**2 - ((self.a - self.b)**2)/4)
		return S

	def p_tz(self):
		p = self.a + self.b + 2*self.c
		return p

res_2 = fig_trapezium(0, 0, 2, 2, 4, 2, 4, 0)

print (res_2.len_tz())
print (res_2.sq_tz())
print (res_2.p_tz())



