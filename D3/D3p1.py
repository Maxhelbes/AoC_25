import numpy as np

lines = open('D3/input.txt').readlines()

input = []
for i in range(len(lines)):
    input.append(lines[i].rstrip())

input2 = []
for i in range(len(lines)):
    row = []
    for j in input[i]:
        row.append(int(j))
    input2.append(np.array(row))

result =  0
for row in input2:
    left = row[:-1].max()
    right = row[row[:-1].argmax()+1:].max()
    result += left * 10 + right

print(result)