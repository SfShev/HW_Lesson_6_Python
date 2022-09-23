# 16. Задать список из n чисел последовательности (1+1/n)^n 
# и вывести на экран их сумму 

# from msilib import sequence

# n = int(input('Введите число: ')) 

# def squerence(n):
#     return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

# nums = squerence(n)
# print(nums)
# print(round(sum(nums), 5))




n = int(input('Введите число: ')) 
sq = lambda i: ((1 + 1 / i) ** i)
lst = [sq(n) for n in range(1, n + 1)]
lst = [round(lst[item],5) for item in range(len(lst)) ]
print(f"{lst}\n{round(sum(lst[i] for i in range(len(lst))),5)}")

