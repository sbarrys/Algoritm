def dfs(graph,x,y,visited):
  global dx,dy
  visited[x][y] = True

  for i in range(4):
    nextx = x+ dx[i]
    nexty = y+ dy[i]
    if 0<=nextx<n and 0<=nexty<m: 
      if graph[nextx][nexty] ==0 and visited[nextx][nexty] ==False:
        dfs ( graph,nextx,nexty,visited)




n ,m = map(int, input().split())


dx=[0,0,1,-1]

dy=[1,-1,0,0]
graph=[]
visited= [ [False]*m for _ in range(n)]
for _ in range(n):
  graph.append( list(map(int,input())))

# print(visited)
cnt= 0 

for x in range(n):
  for y in range(m):
    # print(graph[x][y],visited[x][y])
    if graph[x][y]==0 and visited[x][y]==False:
      # print(visited)
      cnt+=1
      dfs(graph,x,y,visited)
print(cnt)