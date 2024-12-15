import csv


def get_data(name):
    with open(name, "r") as file:
        data = csv.DictReader(file)
        data_list = save_info(data)
        write_info(data_list)


def save_info(all_info):
    data_list = []

    for i in all_info:
        sex = "женского" if i["sex"] == 'female' else "мужского"
        device_type = {
            "mobile": "мобильного браузера",
            "tablet": "браузера на планшете",
            "laptop": "браузера на ноутбуке",
            "desktop": "браузера на компьютере"
        }
        region = i['region'] if i['region'] != "-" else "Неизвестен"
        data_list.append(
            f"Пользователь {i['name']} {sex} пола, {i['age']} лет совершила покупку на {i['bill']} у.е."
            f" с {device_type[i['device_type']]} {i['browser']}."
            f" Регион, из которого совершалась покупка: {region}.\n")

    return data_list


def write_info(data_list):
    with open("web_clients_correct.txt", "w", encoding="utf-8") as file_txt:
        file_txt.writelines(data_list)


def main():
    get_data("web_clients_correct.csv")


if __name__ == "__main__":
    main()
