import turtle
import numpy as np
import matplotlib.pyplot as plt


roadMap={
    'x':{'hair': 10, 'home' : 20},
    'home':{'x':20, 'superm':10, 'y':30},
    'y':{'home':30, 'academy':10},
    'hair':{'x':10, 'superm':20, 'z':30},
    'superm':{'home':10, 'hair':20, 'academy':30, 'restourant':17,'bank':30},
    'academy':{'y':10,'superm':30,'school':30},
    'restourant':{'superm':17,'bank':17},
    'z':{'hair':30, 'bank': 20},
    'bank':{'z':20,'restourant':17,'superm':30,'school':30},   
    'school':{'bank':30,'academy':30}
}### fastWay={place:[visit, lenth, whereBefore]}
fastWay={}
for i in roadMap.keys():
    fastWay[i]=[0, 99999999, 0]#{home:[1, 0, home]
#print(fastWay)
def findNext():#place명으로 안에서 dic을 가공하는게 나을지도 -> 함수 안에서 visit을 1로 하는게 이상적일듯 -> 전체경로중 방문하지 않은 가장 작은걸 스캔하는거였음
    nextPlace='noWay'
    min=99999999
    for i in fastWay.keys():
        if fastWay.get(i)[0]==0 and min > fastWay.get(i)[1]:
            nextPlace=i
            min=fastWay.get(i)[1]
    return nextPlace
def markingPath(place):#내가 어디서 왔는지도 써야하는데.. 최초 시작점은 반복문 밖에 before을 0으로 하여 경로추적시 0에서 끝나게
    #fastWay.get(place)[2]=before
    for i in roadMap.get(place).keys():#방문한곳엔 마킹하면 안됨, 기존에 있던 lenth보다 자기의 lenth+그곳으로 가는 lenth가 낮으면 마킹
        if fastWay.get(i)[0]==0 and fastWay.get(i)[1] > fastWay.get(place)[1] + roadMap.get(place).get(i):
            fastWay.get(i)[1] = fastWay.get(place)[1] + roadMap.get(place).get(i)
            fastWay.get(i)[2] = place
#start='home'
start=input('시작점을 입력하세요 : ')
finish=input('도착점을 입력하세요 : ')
fastWay.get(start)[0]=1#최초 시작점 방문처리
fastWay.get(start)[1]=0#최초 시작점 거리0
fastWay.get(start)[2]='start'
markingPath(start)                #print()
while True:                                             #거리 마킹
    move = findNext() # 다음 가야할곳은 hair
    if move=='noWay':break
    fastWay.get(move)[0]=1#vist
    markingPath(move)
    #start=move
rootWay=[]
result=''
lenth=fastWay.get(finish)[1]
while True:                                             #경로 작성
    if finish=='start':break
    #print(finish)
    rootWay.append(finish)
    finish=fastWay.get(finish)[2]
#시작점에서 marking path를 하고 전체중에 제일 짧은곳을 scan한다음(findNext) 다시 그곳에서 marking!
while rootWay:
    result += rootWay.pop()+' '
print('최단경로는 : ' + result + ' 거리는 : ' + str(lenth))
print(fastWay)

z = np.array([[0,0]])
bank = np.array([[20,0]])
school = np.array([[50,0]])
restourant = np.array([[10,15]])
hair = np.array([[0,30]])
superm = np.array([[20,30]])
academy = np.array([[50,30]])
x = np.array([[0,40]])
home = np.array([[20,40]])
y = np.array([[50,40]])
print(result)
spot = result.split(' ')
spot.pop()
a = np.array([[0,0]])
for i in spot:
    if(i == 'home'):
        a = np.vstack([a,home])
    elif(i == 'bank'):
        a = np.vstack([a,bank])
    elif(i == 'school'):
        a = np.vstack([a,school])
    elif(i == 'academy'):
        a = np.vstack([a,academy])
    elif(i == 'y'):
        a = np.vstack([a,y])
    elif(i == 'x'):
        a = np.vstack([a,x])
    elif(i == 'superm'):
        a = np.vstack([a,superm])
    elif(i == 'restourant'):
        a = np.vstack([a,restourant])
    elif(i == 'hair'):
        a = np.vstack([a,hair])




#for i in result:
 #   t.goto(i)
