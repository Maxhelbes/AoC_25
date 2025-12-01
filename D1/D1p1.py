lines = open('D1/test.txt').readlines()

input = []
for line in lines:
    clean_line = line.rstrip()
    turn = clean_line[0]
    value = clean_line[1:]
    input.append((turn, int(value)))

# print(input)


position = 50
result = 0
for step in input:
    if step[0] == 'L':
        position = (position - step[1]) % 100
    elif step[0] == 'R':
        position = (position + step[1]) % 100
    if position == 0:
        result += 1

print('pos =', position)
print('res =',result)