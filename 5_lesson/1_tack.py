# Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой
# газеты из списка напишите формат указанной даты для перевода в объект datetime:
# The Moscow Times — Wednesday, October 2, 2002
# The Guardian — Friday, 11.10.13
# Daily News — Thursday, 18 August 1977

from datetime import datetime


def recognize_date(some_date):
    all_form = {
        "%A, %B %d, %Y": "The Moscow Times",
        "%A, %d.%m.%y": "The Guardian",
        "%A, %d %B %Y": "Daily News"
    }

    for fmt in all_form:
        try:
            obj = datetime.strptime(some_date, fmt)
            return obj, all_form[fmt]
        except ValueError:
            continue
    return None


while True:
    answer = input("Введите дату вида:\n\tWednesday, October 2, 2002\n\tFriday, 11.10.13\n\tThursday, 18 August 1977"
                   " \n'q' для выхода: ")

    if answer.lower() == "q":
        print("Пока!")
        break

    date_obj, f_type = recognize_date(answer)
    if date_obj:
        print(f"Дата типа '{f_type}' - {date_obj}\n")
    else:
        print("Неверный формат даты.\n")
