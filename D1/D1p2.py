lines = open('D1/input.txt').readlines()


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
        for click in range(step[1]):
            position = (position - 1) % 100
            if position == 0:
                # print(step[0], step[1], '-')
                result += 1  
        # print('step', step, 'move to', position)  
    elif step[0] == 'R':
        for click in range(step[1]):
            position = (position + 1) % 100
            if position == 0:
                # print(step[0], step[1], '+')
                result += 1
        # print('step', step, 'move to', position)  


print('pos =', position)
print('res =',result)