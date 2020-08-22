# N школьников делят K яблок поровну, не делящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику?
# ================================
# Формат ввода
#
# Программа получает на вход числа N и K — натуральные, не превышают 10000.
# ================================
# Формат вывода
#
# Выведите ответ на задачу.
# ================================
# Примеры
#
# Тест 1
# Входные данные:
# 3
# 14
#
#
# Вывод программы:
# 4

n = int(input("Количество школьников: "))
k = int(input("Количество яблок: "))

v = k // n
print(v)