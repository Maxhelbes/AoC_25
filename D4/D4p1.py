import numpy as np

lines = open('D4/input.txt').readlines()

input = []
for i in range(len(lines)):
    input.append(lines[i].rstrip())

print(input[0][0])

def count_of_paper(array: list) -> int:
    count = 0
    for i in range(len(array)):
        for j in range(len(array[y])):
            if array[y][x] == '@':
                count += 1
    return count

result = 0
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
                
                result += 1
                # print(x, y)

print(result)