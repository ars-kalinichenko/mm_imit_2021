def input_journal(path: str):
    journal = {}
    count = int(input("Введите количество записей: "))
    for i in range(count):
        name = input("Введите Имя и Фамилию: ")
        mark = int(input(f"Введите оценку для {name}: "))
        journal[name] = mark
    with open(path, "w") as file:
        file.write(str(journal))


def update_dict(my_dict: dict, key, value: str):
    if key in my_dict.keys() and isinstance(my_dict[key], list):
        my_dict[key].append(value)

    if key in my_dict.keys() and not isinstance(my_dict[key], list):
        my_dict[key] = [my_dict[key], value]

    if key not in my_dict.keys():
        my_dict[key] = value


if __name__ == '__main__':
    input_journal("test3.txt")
    d = {"1": 1}
    update_dict(d, "1", "10")
    update_dict(d, "1", "qwerty")
    update_dict(d, "2", "xxx")
    print(d)
