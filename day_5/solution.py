def read_input():
    with open('data.txt') as f:
        _input_data = [line.rstrip().split(' -> ') for line in f]
        return _input_data


data = read_input()

xMax = -999999999
yMax = -999999999


def createGrid(_x1, _x2, _y1, _y2):
    global xMax, yMax
    if _x1 > xMax:
        xMax = _x1 + 1
    if _x2 > xMax:
        xMax = _x2 + 1
    if _y1 > yMax:
        yMax = _y1 + 1
    if _y2 > yMax:
        yMax = _y2 + 1


entries = []

# add entries which are horizontal or vertical
for entry in data:
    firstEntry = entry[0].split(',')
    x1 = int(firstEntry[0])
    y1 = int(firstEntry[1])
    secondEntry = entry[1].split(',')
    x2 = int(secondEntry[0])
    y2 = int(secondEntry[1])
    if x1 == x2 or y1 == y2:
        createGrid(x1, x2, y1, y2)
        entries.append(entry)

# create grid
grid_line = []
for i in range(xMax):
    grid_line.append(0)
grid = []
for i in range(yMax):
    grid.append(list(grid_line))

for entry in entries:
    firstEntry = entry[0].split(',')
    x1 = int(firstEntry[0])
    y1 = int(firstEntry[1])
    secondEntry = entry[1].split(',')
    x2 = int(secondEntry[0])
    y2 = int(secondEntry[1])
    while x1 != x2:
        grid[y1][x1] += 1
        if x1 < x2:
            x1 += 1
        elif x1 > x2:
            x1 -= 1
    while y1 != y2:
        grid[y1][x1] += 1
        if y1 < y2:
            y1 += 1
        elif y1 > y2:
            y1 -= 1

    grid[y1][x1] += 1

sum = 0

for row in grid:
    # print(row)
    for entry in row:
        if entry >= 2:
            sum += 1

print(sum)
