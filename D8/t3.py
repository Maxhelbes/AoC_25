def distance(point1, point2):
    if point1 == point2:
          return None
    return abs(((point2[0]- point1[0])**2 + (point2[1]-point1[1])**2 + (point2[2]-point1[2])**2))**0.5

lines = open('D8/input.txt').readlines()
input = []
for i in range(len(lines)):
        input.append(lines[i].removesuffix('\n'))

points = []
for row in input:
      x, y, z = row.split(',')
      points.append((int(x),int(y),int(z)))

chains = []
for point in points:
    chains.append([point])

dists = {}
for m in range(len(points)):
    for n in range(m + 1, len(points)):        
        dists[distance(points[m], points[n])] = (points[m], points[n])
# print(dists)

inds = sorted(dists)
distans = []
for i in inds:
    p1, p2 = dists[i]
    distans.append((i, p1, p2))
    
# print(distans[-1])
# print(chains)

def get_chains_id(p1, p2):
    p1_i = None
    p2_i = None
    for id in range(len(chains)):
        if p1 in chains[id]:
            p1_i = id
        if p2 in chains[id]:
            p2_i = id
    return p1_i, p2_i

def merge_chains(i1, i2):
    new_ch1 = chains[i1]
    new_ch2 = chains[i2]
    if i2 > i1:
        chains.pop(i2)
        chains.pop(i1)
    else:
        chains.pop(i1)
        chains.pop(i2)
    chains.append(new_ch1 + new_ch2)

def get_lens():
    lens = []
    for ch in chains:
        lens.append(len(ch))

    lens = sorted(lens)
    return lens[::-1], len(lens)

# print(get_chains_id((16222, 817, 812), (126, 618, 57)))

cons = 0
trye = 0
fake = 0
p1, p2 = 0, 0
# print(cons, get_lens())
for pair in distans:
    if trye >= 1000-1:
        break

    i1, i2 = get_chains_id(pair[1], pair[2])

    if i1 == None or i2 == None:
        print("ERROR", pair[1], pair[2], i1, i2)

    if i1 == i2:
        fake += 1
        # break
        pass
    if i1 != i2:
        merge_chains(i1, i2)
        trye += 1
        p1, p2, = pair[1], pair[2]
    
    cons = fake + trye
    print(cons, (trye, fake), get_lens())

cut = get_lens()[0][0:3]

# print(cut)
# print(cut[0] * cut[1] * cut[2])
print(p1, p2)
print(p1[0], p2[0])
print(p1[0] * p2[0])