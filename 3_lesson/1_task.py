# Необходимо написать программу, которая сформирует словарь данных на основании
# заданных критериев (ключ = ключ в исходной структуре, значение = True — если
# количество ниже 20, False — остальные случаи). При разработке использовать
# dict comprehension.

items = {
    'milk15': {'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
    'cheese': {'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
    'sausage': {'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}

price_less_20 = {k: v['count'] < 20 for k, v in items.items()}

for i, k in price_less_20.items():
    print(f"{i} - {k}")
