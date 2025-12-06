import numpy as np
import cv2
lines = open('D4/input.txt').readlines()

input = []
for i in range(len(lines)):
    input.append(list(lines[i].rstrip()))

# print(input)

matrix = np.zeros((len(input), len(input[0])), dtype=np.uint8)
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '@':
            matrix[i][j] = 255

# print(matrix)

def replace_char_in(matrix: list, y: int, x: int, char: str):
    matrix[y][x] = char
    # matrix[y] = matrix[y][:x] + '.' + matrix[y][x+1:]

def count_of_paper(array: list) -> int:
    count = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '@':
                count += 1
    return count

result = 0
steps = []
iteration = 25
while True:
    iteration += 5
    steps.append(input)
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
                    replace_char_in(input, y, x, str(iteration))
                    result += 1
                    # print(x, y)
               
    new_count = count_of_paper(input)
    if old_cound == new_count:
        break

# Красивое...
# for k in input:
#     print(k)

print(input[0])
print(iteration)

# print(result)
matrix = np.zeros((len(input), len(input[0])), dtype=np.uint8)

for i in range(len(input)):
    for j in range(len(input[i])):
        match input[i][j]: 
            case '@':   
                matrix[i][j] = iteration
            case '.':
                matrix[i][j] = 0
            case _:
                matrix[i][j] = int(input[i][j])


norm_matrix = cv2.normalize(matrix, None, 0, 200, cv2.NORM_MINMAX, cv2.CV_8U)

# print(matrix)


scale_factor = 7
height, width = norm_matrix.shape
display_matrix = cv2.resize(norm_matrix, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_NEAREST)

cv2.imshow('visual', display_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()