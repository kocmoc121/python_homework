# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1
print ('----------------1------------')

def fibonacci(n, m):
    a = 0
    b = 1
    str_fib = ''
    for __ in range(m-1):
        a, b = b, a + b
        str_fib += str(a)

    return str_fib[n-1:m-1]

print(fibonacci(5,17))

# Задача-2:
# Напишите функцию сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()
print ('----------------------2------------')

def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list)-n):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
        n += 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter
print ('-----------------3------------')


def fil_manual(num, l_list):
    new_list = []
    for i in l_list:
        if num(l_list[i]) == 1:
            new_list.append(l_list[i])
    return new_list

A = [1, 2, -3, 3, -4, 5, 6, -7, 7, 9]

print (fil_manual(lambda x: x>0, A))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма
print ('-----------------4------------')

def par_s(A1, A2, A3, A4):
    if (A1[1] == A4[1]) and (A2[1] == A3[1]) and (abs(A1[0] - A2[0]) == abs(A3[0] - A4[0])):
        print('Точки являются вершинами параллелограмма')
    else:
        print('Точки не являются вершинами параллелограмма');
    pass

A1 = [0, 0]
A2 = [0, 1]
A3 = [1, 1]
A4 = [1, 0]
par_s (A1, A2, A3, A4)
#par_s (0, 0, 0, 1, 1, 1, 1, 0)
