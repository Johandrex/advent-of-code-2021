def read_input():
    with open('data.txt') as file:
        return_data = []
        for _line in file:
            tmp_list = []
            return_data.append(tmp_list)
            for char in _line:
                if char == '\n':
                    continue
                tmp_list.append(char)

        return return_data


data = read_input()

syntax = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points = 0
buffer = []

for line in data:
    buffer = []
    for item in line:
        if item in syntax.keys():
            buffer.append(item)
        elif item == syntax[buffer[-1]]:
            buffer.pop()
        else:  # found corrupt chunk
            if item == ')':
                points += 3
            elif item == ']':
                points += 57
            elif item == '}':
                points += 1197
            elif item == '>':
                points += 25137
            break

print(points)
