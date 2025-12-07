lines = open('D7/test.txt').readlines()
input = []
for i in range(len(lines)):
        input.append(lines[i].removesuffix('\n'))

# for row in input:
#     print(row)

lazers = {}
for i in range(len(input)):
    lazers[i] = 0
lazers[input[0].index('S')] = 1

def get_lazers(dic):
    output = []
    for i in range(len(dic)):
        if dic[i] > 0:
            output.append(i)
    return output

# print(get_lazers(lazers))

for y in range(1, len(input)):
    for x in get_lazers(lazers):
        if input[y][x] == '^':
            lazers[x-1] += lazers[x]
            lazers[x+1] += lazers[x]
            lazers[x] = 0     

    # print(input[y], list(lazers.values()))

values = list(lazers.values())
print(sum(values))
