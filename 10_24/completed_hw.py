import random


def is_palindrome(my_str: str) -> bool:
    return my_str == my_str[::-1]


def get_factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def get_first_index(my_str: str, char: str) -> int:
    return my_str.find(char)


def add_random(int_list: list) -> list:
    for index in range(len(int_list)):
        int_list[index] += random.randint(1, 10000)

    return int_list
