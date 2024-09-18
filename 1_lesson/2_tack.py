# Дана переменная, в которой хранится шестизначное число — номер проездного
# билета. Напишите программу, которая будет определять, является ли этот билет
# счастливым. Билет считается счастливым, если сумма первых трёх цифр совпадает с
# суммой последних трёх цифр номера.

num = input("Напишите номер: ")

n_1 = int(num[0]) + int(num[1]) + int(num[2])
n_2 = int(num[5]) + int(num[4]) + int(num[3])

if n_1 == n_2:
    print("Счастливый билет")
else:
    print("Обычный билет")