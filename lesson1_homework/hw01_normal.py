# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа
print ("----------1 зачада----------")
number = int(input("Введите число: "))
a = 0
if number == 0:
    a = number
elif number < 10:
    a = number
else:
    while number > 0:
        N = number % 10
        number = number // 10
        if N > a:
            a = N
print ("Максимальная цифра", a)

print ("----------второй забавный способ----------")
number = input("Введите число: ")
if '9' in number:
    print ("Максимальная цифра 9")
elif '8' in number:
    print ("Максимальная цифра 8")
elif '7' in number:
    print ("Максимальная цифра 7")
elif '6' in number:
    print ("Максимальная цифра 6")
elif '5' in number:
    print ("Максимальная цифра 5")
elif '4' in number:
    print ("Максимальная цифра 4")
elif '3' in number:
    print ("Максимальная цифра 3")
elif '2' in number:
    print ("Максимальная цифра 2")
elif '1' in number:
    print ("Максимальная цифра 1")
else:
    print ("Максимальная цифра 0")

    
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные
print ("----------2 задача----------")
a = int(input("Введите число: "))
b =int(input("Введите число: "))

a = a + b
b = a - b
a = a - b
print (a)
print (b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
# import math
# math.sqrt(4) - вычисляет корень числа 4

print ("----------3 задача----------")
import math
print ("Необходимо ввести данные для уравнения ax2 + bx + c = 0")
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
x = 0
if a == 0:
    x = -c / b
    print ("x = ", x)

D = b**2 - (4 * a * c)
if D == 0:
    x = -b /(2 * a)
    print ("x = ", x)
elif D > 0:
    x = (-b - math.sqrt(D))/(2 * a)
    print ("x1 = ", x)
    x = (-b + math.sqrt(D))/(2 * a)
    print ("x2 = ", x)
elif D < 0:
    print ("оба корня являются комплексными числами")
