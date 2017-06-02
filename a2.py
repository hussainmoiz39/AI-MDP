from __future__ import division
import copy
x = int(raw_input())
arr = [[[0,0] for i in range(6)] for j in range(6)]
check = [[2,1],[2,2],[2,3],[2,4],[3,1],[3,4],[4,1],[4,2],[4,3],[4,4]]
directions = [[-1,0],[0,1],[1,0],[0,-1]]

for cell in check:
    arr[cell[0]][cell[1]][1] = 1
arr[1][3][1] = 1
arr[3][2][1] = 1
arr[1][3][0] = x
arr[3][2][0] = -x
delta = x/20 
r = -x/20
maxchange = x

def checktype(temp, cell, a, b):
    if temp[cell[0]+a][cell[1]+b][1] == 0:
        return temp[cell[0]][cell[1]][0]
    else:
        return temp[cell[0]+a][cell[1]+b][0]
itno = 1
while maxchange > delta:
    print '#Iteration Number',itno
    print
    temp = copy.deepcopy(arr)
#    print temp
    maxchange = 0
    for cell in check:
        maxval = -10000
        for i in directions:
            if i[0] == 0:
                val = 0.8*checktype(temp, cell, i[0], i[1]) + 0.1*checktype(temp, cell, -1, 0) +0.1*checktype(temp, cell, 1, 0)
            else:
                val = 0.8*checktype(temp, cell, i[0], i[1]) + 0.1*checktype(temp, cell, 0, 1) +0.1*checktype(temp, cell, 0, -1)
            if val > maxval:
                maxval = val
#            print val
        if maxval - arr[cell[0]][cell[1]][0] - delta > maxchange:
            maxchange = -delta + maxval - arr[cell[0]][cell[1]][0]

        arr[cell[0]][cell[1]][0] = round(maxval - delta,2)
#        print maxval
    for i in [1,2,3,4]:
        for j in [1,2,3,4]:
            print arr[i][j][0],
        print
    print
    print
    itno += 1
    print 'maxchange',maxchange
    print
