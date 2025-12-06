lines = open('D5/test.txt').readlines()
input = []
for i in range(len(lines)):
    input.append(lines[i].rstrip())

# print(input)
isFirst = True

ranges = []
for row in input:
    if isFirst:
        if '-' in row:
            (lft, rght) = row.split('-')
            ranges.append((int(lft), int(rght)))
        else:
            break

ranges = sorted(ranges)
print(ranges)


i = 0
while i < len(ranges):
    (x1, y1) = ranges[i-1]
    (x2, y2) = ranges[i]

    if (x1 <= x2 and x2 <= y1):
        print((x1, y1), (x2, y2))
        ranges[i] = (x1, max(y1, y2))
        ranges.pop(i-1)
        i -= 1
    i += 1

print(ranges)
    
result = 0
for range in ranges:
    result += range[1] - range[0] + 1

print(result)
    
# out = []
# out.append(ranges[0])

# for range in ranges:
#     for stars in out:
#         if is_in(stars[0], stars[1], range[0]):
#             print('s',range)
    



# print(out)