#PART 1

#opening and reading file
file = open("day2-data.txt")
data = file.readlines()
file.close()


#transform data into lists
lis = []

for gidx, game in enumerate(data):
    g = data[gidx].split(': ')
    g[1] = g[1].split('; ')
    draws = []
    
    for draw in g[1]:
        d = draw.split(', ')
        col = []
        
        for color in d:
            c = color.split()
            c[0] = int(c[0])
            col.append(c)
            
        draws.append(col)
        
    lis.append(draws)


#create bag with maximum cubes per color
bag = {'red' : 12, 'green' : 13, 'blue' : 14}


#find games not possible
fal = []
for gidx, game in enumerate(lis):
    for didx, draw in enumerate(game):
        for cidx, color in enumerate(draw):
            if color[0] > bag[color[1]]:
                if gidx+1 not in fal:
                    fal.append(gidx+1)
                  

#find all possible games and adding up the indices
tr = []
res = 0
for gidx, game in enumerate(lis):
    if gidx+1 not in fal:
        tr.append(gidx+1)
        res += gidx+1


        
#PART 2

#create suitable list
lis2 = []
for game in lis:
    gamel = []
    for draw in game:
        for color in draw:
            gamel.append(color)
    lis2.append(gamel)


#solve
lmax = []
res2 = 0

for game in lis2:
    r = 0
    g = 0
    b = 0
    for cidx, color in enumerate(game):
        if color[1] == 'red':
            #print(color[1])
            if color[0] > r:
                r = color[0]
        if color[1] == 'green':
            if color[0] > g:
                g = color[0]
        if color[1] == 'blue':
            if color[0] > b:
                b = color[0]
    lmax.append([r, g, b])
    res2 += r * g * b
