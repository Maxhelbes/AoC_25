lines = open('D5/input.txt').readlines()
input = []
for i in range(len(lines)):
    input.append(lines[i].rstrip())

# print(input)
isFirst = True

ranges = []
idefs = []
for row in input:
    if isFirst:
        if '-' in row:
            (lft, rght) = row.split('-')
            ranges.append((int(lft), int(rght)))
        else:
            isFirst = False
    else:
        idefs.append(int(row))

result = 0
for num in idefs:
    for range in ranges:
        if range[0] <= num and num <= range[1]:
            print(range[0], '>', num, '<', range[1])
            result += 1
            break

    

print(ranges)
print(idefs)
print('res', result)