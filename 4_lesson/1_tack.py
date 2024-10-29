# Задача 1
# Пользователь по команде p может узнать владельца документа по его номеру.

# Задача 2 (необязательная)
# Секретарь по команде s может по номеру документа узнать, на какой полке документ хранится.


documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
    {'type': 'invoice', 'number': '5-13', 'name': 'Василий Корунов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': ['5-13']
}


def show_owner(num):
    for i in documents:
        if i["number"] == num:
            return i["name"]
    return False


def find_shelf(num):
    for i in directories:
        if num in directories[i]:
            return i
    return False


while True:
    answer = input("Введите команду: ")
    if answer == "q":
        break
    elif answer == "p":
        result = show_owner(input("Введите номер документа: "))
        if result:
            print(f"Владелец документа: {result}")
        else:
            print("Владелец документа: владелец не найден")

    elif answer == "s":
        result = find_shelf(input("Введите номер документа: "))
        if result:
            print(f"Документ хранится на полке: {result}")
        else:
            print("Такого номера в базе нет")
    else:
        print("Введите команды p, s или q!")
