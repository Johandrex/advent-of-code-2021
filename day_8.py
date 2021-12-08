def read_input():
    with open('day_8_data.txt') as file:
        return [_line.split('|') for _line in file.readlines()]


data = read_input()

appearances = 0
for line in data:
    for item in (line[1].split()):
        print(item)
        print(item.strip())
        if len(item) == 2:  # one contains 2 unique characters
            appearances += 1
        elif len(item) == 4:  # four contains 4 unique characters
            appearances += 1
        elif len(item) == 3:  # seven contains 3 unique characters
            appearances += 1
        elif len(item) == 7:  # eight contains 7 unique characters
            appearances += 1

print(appearances)