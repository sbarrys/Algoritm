from collections import deque

n ,m  = map(int, input().split())
graph=[]

for _ in range(n):
  graph.append(list(map(int,input())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

visited=[[False]*m for _ in range(n)]
q =[]

def BFS(x,y):
  q= deque()
  q.append((x,y))

  visited[x][y]=True

  while q : 
    nowx,nowy = q.popleft()

    for i in range(4):
      nextx=nowx+dx[i]
      nexty=nowy+dy[i]
      if 0<=nextx<n and 0<=nexty<m:
        if graph[nextx][nexty] == 1:
          if visited[nextx][nexty]==False:
              visited[nextx][nexty]=True
              graph[nextx][nexty]=graph[nowx][nowy]+1
              q.append((nextx,nexty))


visited[0][0]=True
BFS(0,0)

print(graph[n-1][m-1])