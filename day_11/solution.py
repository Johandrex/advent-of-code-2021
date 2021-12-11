def read_input():
    with open('data.txt') as file:
        return_data = []
        for _line in file:
            tmp_list = []
            return_data.append(tmp_list)
            for char in _line:
                if char == '\n':
                    continue
                tmp_list.append(int(char))

        return return_data


data = read_input()
neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
flashed = set()
flashes = 0
loops = 100

for loop in range(loops):
    for x in range(len(data)):
        for y in range(len(data[0])):
            data[x][y] += 1
    found = True
    while found:
        found = False
        for x in range(len(data)):
            for y in range(len(data[0])):
                if data[x][y] > 9 and (x, y) not in flashed:
                    found = True
                    flashed.add((x, y))
                    for neighbor in neighbors:
                        xN = x + neighbor[0]
                        yN = y + neighbor[1]
                        if 0 <= xN < len(data):
                            if 0 <= yN < len(data[x]):
                                data[xN][yN] += 1

    for flash in flashed:
        flashes += 1
        data[flash[0]][flash[1]] = 0

    flashed.clear()

print(flashes)
