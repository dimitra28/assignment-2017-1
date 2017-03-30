matches = []
with open("matches.txt") as m:
     for line in m:
         line = line.split()
         matches.append(line)

days = []
days.append(matches[0])

for i in range(1, len(matches)):
    j = 0
    flag = False
    while (j < len(days)) and (flag == False):
        for v in matches[i]:
            if v in days[j]:
                flag = False
                j = j+1
                break
            else:
                flag = True
                k = j
    if flag == True:
        days[k].append(matches[i][0])
        days[k].append(matches[i][1])
    else:
        days.append(matches[i])


dayss = []
for x in range(len(days)):
    for c in range(0, len(days[x]), 2):
        dayss.append([days[x][c],days[x][c+1],x])

for i in range(len(dayss)):
    if dayss[i][0]> dayss[i][1]:
        d = dayss[i][0]
        dayss[i][0] = dayss[i][1]
        dayss[i][1] = d

for i in range(len(dayss)):
    dayss.sort()
    print('(', dayss[i][0], ',', dayss[i][1], ')', dayss[i][2] )