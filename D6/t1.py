import numpy as np

lines = open('D6/test.txt').readlines()
input = []
for i in range(len(lines)):
        input.append(lines[i].rstrip())

print(input)

arr = []
for row in input:
    arr.append(row.split())
print(arr)

signs = arr[-1]
matrix = []
for row in arr[:-1]:
    new_row = []
    for j in row:
        new_row.append(int(j))
    matrix.append(new_row)

# print(matrix)

nums = np.array(matrix)

# print(signs)
# print(nums)

result = 0
for k in range(len(nums[0])):
    if signs[k] == '*':
        column = nums[:, k]
        # print(column)
        local_res = 1 
        for i in column:
            local_res *= i
        result += local_res
    if signs[k] == '+':
        column = nums[:, k]
        # print(column)
        local_res = 0 
        for i in column:
            local_res += i
        result += local_res
     
print(result)
