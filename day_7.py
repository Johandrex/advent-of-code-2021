def read_input():
    with open('day_7_data.txt') as file:
        return [int(x) for x in file.read().split(',')]


data = read_input()

max_n = max(data)
min_n = min(data)

fuel = 9999999999

for num in range(min_n, max_n+1, 1):
    sum = 0
    for number in data:
        if number > num:
            sum += number-num
        elif number < num:
            sum += num-number

    if sum < fuel:
        fuel = sum

print(fuel)

