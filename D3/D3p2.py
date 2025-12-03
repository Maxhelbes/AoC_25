import numpy as np
# Решение, после исправлений (не стыдно показывать)
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

def max_in_window(row: list, start: int, size: int) -> int:
    if size == 0:
        return 0
    size -= 1
    end = len(row)-size
    first = np.max(row[start:end])
    first_i = start + np.argmax(row[start:end])
    start = first_i + 1
    return first * 10**size + max_in_window(row, start, size)

result =  0
for row in input2:
    size = 12
    start = 0
    result += max_in_window(row, start, size)

print(result)