import numpy as np

lines = open('D4/input.txt').readlines()

input = []
for i in range(len(lines)):
    input.append(lines[i].rstrip())


def replace_char_in(matrix: list, y: int, x: int):
    matrix[y] = matrix[y][:x] + '.' + matrix[y][x+1:]

def count_of_paper(array: list) -> int:
    count = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '@':
                count += 1
    return count

result = 0

while True:
    old_cound = count_of_paper(input)
    for y in range(len(input)):
        for x in range(len(input[y])):
            status = 0
            if input[y][x] != '@':
                continue
            else:
                if y > 0:
                    if input[y-1][x] == '@':
                        status += 1

                    if x > 0:
                        if input[y-1][x-1] == '@':
                            status += 1

                if x < len(input[y]) - 1:
                    if input[y][x+1] == '@':
                        status += 1        

                    if y > 0: 
                        if input[y-1][x+1] == '@':
                            status += 1

                if y < len(input) - 1:
                    if input[y+1][x] == '@':
                        status += 1     

                    if x < len(input[y]) - 1:
                        if input[y+1][x+1] == '@':
                            status += 1 

                if x > 0:
                    if input[y][x-1] == '@':
                        status += 1    
                            
                    if y < len(input) - 1: 
                        if input[y+1][x-1] == '@':
                            status += 1 
                
                if status < 4:
                    replace_char_in(input, y, x)
                    result += 1
                    # print(x, y)
                    
    new_count = count_of_paper(input)
    if old_cound == new_count:
        break

# Красивое...
for k in input:
    print(k)

print(result)