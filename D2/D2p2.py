lines = open('D2/input.txt').readline()
lines = lines.split(',')

data = []
for i in range(len(lines)):
    (st, fi) = lines[i].split('-')
    data.append((st, fi))

def check_valid_new(str_num):
    for step_size in range(1, (len(str_num) // 2) + 1):

        if len(str_num) % step_size == 0:
            steps_num = int(len(str_num) / step_size)

            parts = [] 
            for i in range(steps_num):
                parts.append(str_num[i * step_size : (i + 1) * step_size])

            if [parts[0]] * len(parts) == parts:
                return int(str_num)
    return 0  
      
result = 0
for step in data:
    for k in range(int(step[0]), int(step[1])+1):
        result += check_valid_new(str(k))
        
print(result)
