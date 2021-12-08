from collections import deque

fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def read_input():
    global fishes

    _file = open('day_6_data.txt')
    _input = []
    for line in _file:
        numbers = line.split(',')
        for number in numbers:
            fishes[int(number)] += 1

        return [int(number) for number in numbers]


read_input()
print(f'Initial state:\t {str(fishes)}')


def add_internal_timer(current_day):
    global fishes

    temp = int(fishes[0])
    fishes = deque(fishes)
    fishes.rotate(-1)
    fishes = list(fishes)

    fishes[6] += temp

    return f'After {current_day} days: \t{str(fishes)}'


def after_days(days):
    current_day = 1

    for day in range(days):
        print(add_internal_timer(current_day))
        current_day += 1


after_days(256)  # loop through days

sum = 0
for fish in fishes:
    sum += fish

print(f'\nTotal fishes: {sum} ')
