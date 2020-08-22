# Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей и копеек нужно заплатить за N пирожков.
# ========================================
# Формат ввода
#
# Программа получает на вход три числа: A, B, N — целые, неотрицательные, не превышают 10000.
# ========================================
# Формат вывода
#
# Программа должна вывести два числа: стоимость покупки в рублях и копейках.
# ========================================
# Примеры
#
# Тест 1
# Входные данные:
# 10
# 15
# 2
#
# Вывод программы:
# 20 30
#
#
#
# Тест 2
# Входные данные:
# 2
# 50
# 4
#
# Вывод программы:
# 10 0
rubles = int(input("Пирожок стоит рублей "))
copeyky = int(input("Пирожок стоит копеек "))
bulochki = int(input("Сколько пирожков куплено "))

print((rubles * bulochki) + (copeyky * bulochki) / 100)
