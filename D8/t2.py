chains = [[(162, 817, 812), (425, 690, 689)], [(162, 800, 812), (500, 690, 100)]]
print(len(chains))

    
def in_pair_in(point, chains):
    for chain in chains:
        if point in chain:
            return True
    return False



    
def check_cheins(point1, point2, chains):
    p1_ind = 'Empty'
    p2_ind = 'Empty'
    for i in range(len(chains)):
        if point1 in chains[i]:
            p1_ind = i
        if point2 in chains[i]:
            p2_ind = i
    return p1_ind, p2_ind


# i1, i2 = check_cheins((162, 817, 812), (500, 690, 100), massive)

# print(i1, i2)
pair = [0, (162, 817, 812), (425, 690, 689)]

i1, i2 = check_cheins(pair[1], pair[2], chains)
# print(i1, i2)
if i1 == 'Empty' and i2 == 'Empty':
    # print('one')
    chains.append([pair[1], pair[2]])
elif i1 != 'Empty' and i2 == 'Empty':
    chains[i1].append(pair[2])
    # print('two', 1, i2) 
elif i1 == 'Empty' and i2 != 'Empty':
    chains[i2].append(pair[1])
    # print('tree',i1, i2) 
elif (i1 != i2):
    # print('four',i1, i2)
    new_chain = chains[i1] + chains[i2]
    chains.pop(i2)
    chains.pop(i1)
    chains.append(new_chain)
elif i1 == i2:
    print('точки в одной цепи не соединяем')
else:
    print('нифига')

print(chains)








points = [1,2,3,4,5]

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        print(i, j)