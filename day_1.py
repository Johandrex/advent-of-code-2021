INPUT_FILE = 'day_1_data.txt'
INPUT = []

with open(INPUT_FILE) as f:
    INPUT = [line.rstrip() for line in f]

last_input = -99999999
count = -1

for line in INPUT:
    if int(line) < last_input:
        pass
    else:
        count += 1

    last_input = int(line)

print(count)
