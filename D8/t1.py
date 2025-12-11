def distance_old(x1, y1, z1, x2, y2, z2):
    return abs(((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5)

def distance(point1, point2):
    if point1 == point2:
          return None
    return abs(((point2[0]- point1[0])**2 + (point2[1]-point1[1])**2 + (point2[2]-point1[2])**2))**0.5

lines = open('D8/test.txt').readlines()
input = []
for i in range(len(lines)):
        input.append(lines[i].removesuffix('\n'))

# for i in input:
#     print(i)
# print(input)

points = []
for row in input:
      x, y, z = row.split(',')
      points.append((int(x),int(y),int(z)))

# print(points)

dists = [] 

for m in points:
    for n in points:
        if m == n:
            pass
        else:
            dists.append((distance(m, n), m, n))
            # print(dists[-1])

print(len(dists))

# print(min(dists))

def in_pair_in_old(point, chains):
    for chain in chains:
        if point in chain:
            return True
    return False

def in_pair_in(point1, point2, chains):
    for chain in chains:
        if point1 in chain and point2 in chain:
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

dists = sorted(dists)

def get_lens(chains):
    lens = []
    for chain in chains:
        # print('test', chain)
        lens.append(len(chain))
    
    return lens

# new_dist = []
# for d in dists:
#     print(d)

chains = []
for point in points:
    chains.append([point])
# print(chains)

def main():
    if True:
        # print(dists)

        # chains = []
        points = 0
        connections = 1
        while True:
            for i in range(0, len(dists), 2):
                pair = dists[i]
            # for pair in dists:
                if chains == []:
                    # print('do', len(chains))
                    chains.append([pair[1], pair[2]])
                    # print('posle',len(chains))
                    print('Стартовые точки: ', pair[1], pair[2])
                    points += 2
                    connections += 1
                    dists.remove(pair)
                    # print('====', counter, '====', chains)
                    print('points', points, 'cons', connections, 'points in chain', get_lens(chains))
                    # pass
                else:
                    i1, i2 = check_cheins(pair[1], pair[2], chains)
                    # print(chains[i1])
                    # print(chains[i2])
                    # print(i1, i2)
                    if i1 == 'Empty' and i2 == 'Empty':
                        print('Две точки без цепей: ', pair[1], pair[2])
                        

                        chains.append([pair[1], pair[2]])
                        points += 2
                        connections += 1
                        dists.remove(pair)
                        # print('====', counter, '====', chains)
                        print('points', points, 'cons', connections, 'chains', get_lens(chains))

                        # pass
                    elif i1 != 'Empty' and i2 == 'Empty':
                        print('Точка 1 в цепи: ', pair[1], pair[2])
                        chains[i1].append(pair[2])
                        points += 1
                        connections += 1
                        dists.remove(pair)
                        # print('====', counter, '====', chains)
                        print('points', points, 'cons', connections, 'chains', get_lens(chains))
                        # pass
                        # print('two', 1, i2) 
                    elif i1 == 'Empty' and i2 != 'Empty':
                        print('Точка 2 в цепи: ', pair[1], pair[2])
                        chains[i2].append(pair[1])
                        points += 1
                        connections += 1
                        dists.remove(pair)
                        # print('====', counter, '====', chains)
                        print('points', points, 'cons', connections, 'chains', get_lens(chains))
                        # pass
                        # print('tree',i1, i2) 
                    elif (i1 != i2):
                        print('Обе точки в цепи: ', pair[1], pair[2])
                        # print('индексы цепей', i1, i2)
                        # print('количество цепей', len(chains))
                        # print('ch1', chains[i1])
                        # print('ch2', chains[i2])
                        new_chain = chains[i1] + chains[i2]
                        # print(i1, i2)

                        ch1, ch2 = chains[i1], chains[i2]
                        # chains.pop(i2)
                        # chains.pop(i1)
                        chains.remove(ch1)
                        chains.remove(ch2)

                        chains.append(new_chain)
                        points += 0
                        connections += 1
                        dists.remove(pair)
                        # print('====', counter, '====', chains)
                        print('points', points, 'cons', connections, 'chains', get_lens(chains))


                        # pass
                    elif i1 == i2:
                        # print('точки в одной цепи не соединяем')
                        dists.remove(pair)
                        connections += 1
                        print('points', points, 'cons', connections, 'chains', get_lens(chains))
                        # pass
                    else:
                        print('нифига')
                        dists.remove(pair)
                        # connections += 1
                        # print('points', points, 'cons', connections, 'chains', get_lens(chains))
                        # pass
                print('--------------------------', connections)
                if connections > 9:
                    print('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSUKA 1')
                    return chains
            # if connections > 10:
            #         print('bomboclad 2')
            #         break
            # counter += 1
            # print(counter)

        # print(chains)

# lens = []


# lens = get_lens(main())

# lens = sorted(lens)
# print()
# print()

# print()

# print()
# print()

# print(lens)

# print('RESLUT', lens[-1] * lens[-2] * lens[-3])

# print('cons', connections)
# print('points', points)
