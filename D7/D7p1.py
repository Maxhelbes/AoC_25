lines = open('D7/test.txt').readlines()
input = []
for i in range(len(lines)):
        input.append(lines[i].removesuffix('\n'))

# for row in input:
#     print(row)

lazers = {input[0].index('S')}
# print(0, lazers, 1)

result = 0
for y in range(1, len(input)):
    new_lazers = set()
    for x in lazers:
        
        if input[y][x] == '.':
            new_lazers.add(x)
        
        if input[y][x] == '^':
            result += 1
            new_lazers.add(x-1)
            new_lazers.add(x+1)
            # print(y, lazers, result)
    lazers = new_lazers

print(result)