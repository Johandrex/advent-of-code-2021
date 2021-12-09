with open('data.txt') as f:
    data = [line.rstrip() for line in f]


horizontal = 0
depth = 0


def navigate(way, steps):
    global horizontal
    global depth

    if way == "forward":
        horizontal += steps
    elif way == "backwards":
        horizontal -= steps
    elif way == "up":
        depth -= steps
    elif way == "down":
        depth += steps
    else:
        print("ERROR")


for line in data:
    commands = line.split(' ')
    print(commands[0], commands[1])
    navigate(commands[0], int(commands[1]))


print(f'horizontal: {horizontal}, depth: {depth}\ncalculated position: {horizontal * depth}')
