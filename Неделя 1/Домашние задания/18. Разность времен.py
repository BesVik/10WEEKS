# Даны два момента времени в пределах одних и тех же суток. Для каждого момента указан час, минута и секунда.
# Известно, что второй момент времени наступил не раньше первого.
#
# Определите сколько секунд прошло между двумя моментами времени.
# =============================
# Формат ввода
#
# Программа на вход получает шесть целых чисел через перевод строки. Первые три целых числа соответствуют часам,
# минутам и секундам первого момента, следующие три числа соответствуют второму моменту.
#
# Часы задаются числом от 0 до 23 включительно. Минуты и секунды — от 0 до 59.
# =============================
# Формат вывода
#
# Выведите число секунд между этими моментами времени.
# =============================
# Примеры
#
# Тест 1
# Входные данные:
# 1
# 1
# 1
# 2
# 2
# 2
#
# Вывод программы:
# 3661

hours1 = int(input("Кол-во часов в 1 момент: "))
minutes1 = int(input("Кол-во минут в 1 момент: "))
seconds1 = int(input("Кол-во секунд в 1 момент: "))

hours2 = int(input("Кол-во часов в 2 момент: "))
minutes2 = int(input("Кол-во минут в 2 момент: "))
seconds2 = int(input("Кол-во секунд в 2 момент: "))

print("Между двумя моментами времени прошло:",
      ((hours2 - hours1) * 3600) + ((minutes2 - minutes1) * 60) + (seconds2 - seconds1), "секунд")
