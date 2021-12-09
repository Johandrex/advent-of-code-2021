with open('data.txt') as f:
    data = [line.rstrip() for line in f]

last_input = -99999999
count = -1

for line in data:
    if int(line) < last_input:
        pass
    else:
        count += 1

    last_input = int(line)

print(count)
