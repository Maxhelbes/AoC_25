lines = open('D2/input.txt').readline()
lines = lines.split(',')

data = []
for i in range(len(lines)):
    (st, fi) = lines[i].split('-')
    data.append((st, fi))

def check_valid(str):
    if len(str) % 2 == 1:
        return 0
    
    else:
        left, right = str[:len(str)//2], str[len(str)//2:]
        if left == right:
            return int(str)
        else:
            return 0
        
result = 0
for step in data:
    for k in range(int(step[0]), int(step[1])+1):
        result += check_valid(str(k))
        
print(result)
