import numpy as np

lines = open('D6/input.txt').readlines()
input = []
for i in range(len(lines)):
        input.append(lines[i].removesuffix('\n'))

# print(input)

signs = input[-1].replace(' ', '')
# print(signs)
print(len(signs))

index = 0
numbers = []
row = []
for x in range(len(input[0])):
    # for y in range(0,2):
    y = 0
    x = int(x)
    num = input[y][x] +  input[y+1][x] + input[y+2][x] + input[y+3][x]

    # print(row)

    if num.replace(' ', ''):
        # print(num)
        row.append(num)
    else:
        new_row = row.copy()
        numbers.append(new_row)
        row = []
new_row = row.copy()
numbers.append(new_row)

# print(numbers)


for y in range(len(numbers)):
    for x in range(len(numbers[y])):
        numbers[y][x] = int(numbers[y][x])

# print(numbers)
print(len(numbers))

result = 0    
for x in range(len(numbers)):
    if signs[x] == '*':
        local_res = 1 
        for i in numbers[x]:
            local_res *= i
        result += local_res 

    if signs[x] == '+':
        local_res = 0 
        for i in numbers[x]:
            local_res += i
        result += local_res

print(result)

    
     
