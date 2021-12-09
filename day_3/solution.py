def read_input():
    with open('data.txt') as f:
        _input_data = [line.rstrip() for line in f]
        return _input_data


data = read_input()

list_numbers = [0] * len(data[0])

for line in data:
    for index in range(len(line)):
        if line[index] == '1':
            list_numbers[index] += 1
        elif line[index] == '0':
            list_numbers[index] -= 1

gamma_rate_binary = []
epsilon_rate_binary = []

for item in list_numbers:
    if item < 0:
        gamma_rate_binary.append(0)
        epsilon_rate_binary.append(1)
    elif item >= 0:
        gamma_rate_binary.append(1)
        epsilon_rate_binary.append(0)

gamma_rate_int = int("".join(str(i) for i in gamma_rate_binary), 2)
epsilon_rate_int = int("".join(str(i) for i in epsilon_rate_binary), 2)

power_consumption = gamma_rate_int * epsilon_rate_int

print(power_consumption)
