# 1 . Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("Введите № дня недели: "))
check_day = (lambda day: "выходной" if day == 6 or day == 7 else "будний день")

print(check_day(day))