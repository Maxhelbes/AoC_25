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

# print(len(idefs))

all_valids = []
# print(ranges)
count = 0
for step in ranges:
    for i in range(step[0], step[1]+1):
        if i not in all_valids:
            all_valids.append(i)
            count += 1
        if count % 1000 == 0:
            print(i)
        

# print(len(all_valids))
result = 0

for n in idefs:
    if n in all_valids:
        result += 1

print('res', result)
print('count', count)

# print(ranges)
# print(idefs)