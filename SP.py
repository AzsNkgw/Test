# -*- coding: utf-8 -*-

    #初期値設定
Distance = [[0,2,8,4,-1,-1,-1],
            [2,0,-1,-1,3,-1,-1],
            [8,-1,0,-1,2,3,-1],
            [4,-1,-1,0,-1,8,-1],
            [-1,3,2,-1,0,-1,9],
            [-1,-1,3,8,-1,0,3],
            [-1,-1,-1,-1,9,3,0]]      #地点間の距離
nPoint = len(Distance)      #地点数Ｎ
sp = 0          #出発地の地点番号
dp = 6          #目的地の地点番号
sDist = float('inf')       #出発地から目的地までの最短距離
sRoute = [-1] * nPoint    #最短経路上の地点の地点番号
pRoute = [0] * nPoint    #地点jの直前の経由地の地点番号
pDist = [sDist] * nPoint   #出発地から各地点までの最短距離
pFixed = [False] * nPoint    #各地点の最短距離の確定状態

pDist[sp] = 0       #出発地から出発地自体への最短距離に0を設定

def ShortestPath(sp,dp):
    while True:
        i = 0
        while i < nPoint:
            if pFixed[i] == False:break
            i += 1
        if i == nPoint:break
        j = i + 1
        while j < nPoint:
            if pFixed[j] == False and pDist[j] < pDist[i]:
                i = j
            j += 1
        sPoint = i
        pFixed[sPoint] = True
        j = 0
        while j < nPoint:
            if Distance[sPoint][j] > 0 and pFixed[j] == False:
                newDist = pDist[sPoint] + Distance[sPoint][j]
                if newDist < pDist[j]:
                    pDist[j] = newDist
                    pRoute[j] = sPoint
            j += 1
    sDist = pDist[dp]
    j = 0
    i = dp
    while i != sp:
        sRoute[j] = i
        i = pRoute[i]
        j += 1
    sRoute[j] = sp
    return sDist,pDist

        #出発地から目的地までの最短距離と出発地から各地点までの最短距離を出力して終了

