import csv

purchases = {
    '1840e0b9d4': 'Продукты',
    '4e4f90fcfb': 'Электроника',
    '5b7c6c3fb8': 'Бытовая техника',
    'e557b6d27d': 'Одежда',
    'd94b6f7a54': 'Спорттовары',
    '68d3f7a3f4': 'Книги'
}

with open('visit_log.csv', 'r', encoding='utf-8') as visit_log, \
        open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel_file:
    reader = csv.reader(visit_log)
    writer = csv.writer(funnel_file)

    writer.writerow(['user_id', 'source', 'category'])

    for row in reader:
        if len(row) < 2:
            continue

        user_id, source = row[:2]
        if user_id in purchases:
            writer.writerow([user_id, source, purchases[user_id]])

print("Файл funnel.csv создан.")
