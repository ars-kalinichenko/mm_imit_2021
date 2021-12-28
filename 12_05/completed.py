def get_min():
    mini = float("+inf")
    value = int(input("Введите число или -1, чтобы выйти: "))
    while value != -1:
        if value < mini:
            mini = value
        value = int(input("Введите число или -1, чтобы выйти: "))

    print("Минимум: ", mini)


def get_max():
    value = int(input("Введите число или -1, чтобы выйти: "))
    maxi = value
    while value != -1:
        if value > maxi:
            maxi = value
        value = int(input("Введите число или -1, чтобы выйти: "))

    print("Максимум: ", maxi)


def get_sum():
    summ = 0
    value = int(input("Введите число или -1, чтобы выйти: "))
    while value != -1:
        summ = summ + value
        value = int(input("Введите число или -1, чтобы выйти: "))

    print("Сумма: ", summ)


def get_arithmetic_mean():
    summ = 0
    count = 0
    value = int(input("Введите число или -1, чтобы выйти: "))
    while value != -1:
        summ = summ + value
        count += 1
        value = int(input("Введите число или -1, чтобы выйти: "))
    ar = summ / count
    print("Арифметическое среднее: ", ar)
