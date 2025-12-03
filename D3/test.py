import numpy as np
# Оригинальное решение, которым я дал ответ в 09:10 утра)
lines = open('D3/input.txt').readlines()

input = []
for i in range(len(lines)):
    input.append(lines[i].rstrip())

input2 = []
for i in range(len(lines)):
    row = []
    for j in input[i]:
        row.append(int(j))
    input2.append(np.array(row))

result =  0
for row in input2:
    size = 12
    start = 0

    size -= 1
    end = len(row)-size
    first = np.max(row[start:end])
    first_i = start + np.argmax(row[start:end])
    start = first_i + 1
    print(first, '[',first_i,']', start, end)

    size -= 1
    end = len(row)-size
    second = np.max(row[start:end])
    second_i = start + np.argmax(row[start:end])
    start = second_i + 1
    print(second, '[',second_i,']', start, end)
    
    size -= 1
    end = len(row)-size
    tree = np.max(row[start:end])
    tree_i = start + np.argmax(row[start:end])
    start = tree_i + 1
    print(tree, '[',tree_i,']', start, end)
    
    size -= 1
    end = len(row)-size
    four = np.max(row[start:end])
    four_i = start + np.argmax(row[start:end])
    start = four_i + 1
    print(four, '[',four_i,']', start, end)
        
    size -= 1
    end = len(row)-size
    five = np.max(row[start:end])
    five_i = start + np.argmax(row[start:end])
    start = five_i + 1
    print(five, '[',five_i,']', start, end)    

    size -= 1
    end = len(row)-size
    six = np.max(row[start:end])
    six_i = start + np.argmax(row[start:end])
    start = six_i + 1
    print(six, '[',six_i,']', start, end)   
     
    size -= 1
    end = len(row)-size
    seven = np.max(row[start:end])
    seven_i = start + np.argmax(row[start:end])
    start = seven_i + 1
    print(seven, '[',seven_i,']', start, end)   
     
    size -= 1
    end = len(row)-size
    eit = np.max(row[start:end])
    eit_i = start + np.argmax(row[start:end])
    start = eit_i + 1
    print(eit, '[',eit_i,']', start, end)    

    size -= 1
    end = len(row)-size
    nine = np.max(row[start:end])
    nine_i = start + np.argmax(row[start:end])
    start = nine_i + 1
    print(nine, '[',nine_i,']', start, end)  
     
    size -= 1
    end = len(row)-size
    ten = np.max(row[start:end])
    ten_i = start + np.argmax(row[start:end])
    start = ten_i + 1
    print(ten, '[',ten_i,']', start, end)    

    size -= 1
    end = len(row)-size
    ell = np.max(row[start:end])
    ell_i = start + np.argmax(row[start:end])
    start = ell_i + 1
    print(ell, '[',ell_i,']', start, end)   

    size -= 1
    end = len(row)-size
    tw = np.max(row[start:end])
    tw_i = start + np.argmax(row[start:end])
    start = tw_i + 1
    print(tw, '[',tw_i,']', start, end)
    
    print(first * 10**11 + second * 10**10 + tree * 10**9 + four * 10**8 + five * 10**7 + six * 10**6 + seven * 10**5 + eit * 10**4 + nine * 10**3 + ten * 10**2 + ell * 10**1 + tw * 10**0)
    result += first * 10**11 + second * 10**10 + tree * 10**9 + four * 10**8 + five * 10**7 + six * 10**6 + seven * 10**5 + eit * 10**4 + nine * 10**3 + ten * 10**2 + ell * 10**1 + tw * 10**0

print(result)