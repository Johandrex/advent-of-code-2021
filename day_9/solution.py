def read_input():
    with open('data.txt') as file:
        numbers = []
        for _line in file:
            tmp_list = []
            numbers.append(tmp_list)
            for number in _line:
                try:
                    tmp_list.append(int(number))
                except ValueError as ex:
                    continue

        return numbers


data = read_input()

bottoms = []


def index_exists(line, item):
    if line <= -1 & item <= -1:
        return False

    if line >= len(data):
        return False

    if item >= len(data[line]):
        return False

    return True


for line in range(len(data)):
    for item in range(len(data[line])):
        if index_exists(line, item - 1):
            if data[line][item] >= data[line][item - 1]:
                continue
        if index_exists(line, item + 1):
            if data[line][item] >= data[line][item + 1]:
                continue
        if index_exists(line - 1, item):
            if data[line][item] >= data[line - 1][item]:
                continue
        if index_exists(line + 1, item):
            if data[line][item] >= data[line + 1][item]:
                continue

        bottoms.append(data[line][item]+1)

print(bottoms)
print(sum(bottoms))
