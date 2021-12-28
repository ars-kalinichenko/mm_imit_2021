def read_file(name: str) -> int:
    int_list = []
    with open(name, "r") as f:
        lines = f.readlines()
        for line in lines:
            int_list.append(int(line.strip()))
    if int_list[-1] == 0:
        raise ValueError
    return sum(int_list)


if __name__ == '__main__':
    print(read_file("test3.txt"))
