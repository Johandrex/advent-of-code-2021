def read_input():
    _file = open('day_6_data.txt')
    _input = []
    for line in _file:
        numbers = line.split(',')
        return [int(number) for number in numbers]


fishes = read_input()  # read input
print(f'Initial state:\t {str(fishes)}')


def add_internal_timer(current_day):
    global fishes

    for index, value in enumerate(fishes):
        if (fishes[index] == 0):
            fishes.append(9)
            fishes[index] = 6
        else:
            fishes[index] -= 1

    return f'After {current_day} days: \t{str(fishes)}'


def after_days(days):
    current_day = 1

    for day in range(days):
        print(add_internal_timer(current_day))
        current_day += 1


after_days(80)  # loop through days

print(f'\nTotal fishes: {len(fishes)} ')