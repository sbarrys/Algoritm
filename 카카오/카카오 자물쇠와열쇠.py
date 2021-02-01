import copy
def turn360(key):
    n=len(key)
    temp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            temp[y][n-1-x]=key[x][y] 
    
    return temp
def putLockOnBoard(lock,bigBoard,sizeOfKey):
    
    for i in range(len(lock)):
        for j in range(len(lock)):
            bigBoard[i+sizeOfKey-1][j+sizeOfKey-1] = lock[i][j]
    return bigBoard
def checkNoZero(tempBoard,sizeOfKey,sizeOfLock):
    for i in range(sizeOfLock):
        for j in range(sizeOfLock):
            if tempBoard[i+sizeOfKey-1][j+sizeOfKey-1] ==0:
                return False
    return True
    

def checkLockOnBigBoard(key,bigBoard,sizeOfKey,sizeOfLock):
    #시작점
    for x in range(0,len(bigBoard)- (sizeOfKey-1)):
        for y in range(0,len(bigBoard)- (sizeOfKey-1)):
            tempBoard=copy.deepcopy(bigBoard)
            #검사
            for i in range(len(key)):
                for j in range(len(key)):

                    if bigBoard[i+x][j+y]!= key[i][j] :
                        tempBoard[i+x][j+y]=1

                    else:
                        tempBoard[i+x][j+y]=0
            if checkNoZero(tempBoard,sizeOfKey,sizeOfLock):
                return True
    return False
def solution(key, lock):
    answer = True
    n = len(lock)
    sizeOfKey= len(key)
    sizeOfLock= len(lock)
    #키를 비교 
    for _ in range(4):
        bigBoard= [[1]*(n+ (sizeOfKey-1)*2) for _ in range( n+ (sizeOfKey-1)*2 )]
        bigBoard = putLockOnBoard(lock,bigBoard,sizeOfKey)

        key =turn360(key)    
        answer =checkLockOnBigBoard(key,bigBoard,sizeOfKey,sizeOfLock)
        if answer == True:
            return True
    return False