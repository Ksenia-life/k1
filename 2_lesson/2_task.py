boys = ["Peter", "Alex", "John", "Arthur", "Richard"]
girls = ["Kate", "Liza", "Kira", "Emma", "Trisha"]
# girls = ["Kate", "Liza", "Kira", "Emma"]

boys.sort()
girls.sort()

if len(boys) == len(girls):
    for i in range(len(boys)):
        print(f"{boys[i]} и {girls[i]}")