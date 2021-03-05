import heapq
def dik( adj,start, end) :
  distance= [1e9]*(v+1)
  pq=[]
  distance[start]=0
  heapq.heappush(pq,(0,start)) #시작지점 입력 
  while pq:
    cost , now = heapq.heappop(pq)
    if now == end :
      break
    if distance[now]<cost:
      continue
    for next,nextcost in adj[now]:
      if cost+nextcost < distance[next]:
        heapq.heappush(pq,(cost+nextcost,next))
        distance[next] = cost+nextcost
  return distance[end]



v,e,p= map(int,input().split())  #건우

adj = [[] for _ in range(v+1)]
for _ in range(e):
  a,b,cost = map(int,input().split())
  adj[a].append((b,cost))
  adj[b].append((a,cost))

minFull  = dik(adj,1,v)
minTo  = dik(adj,1,p)
minFrom = dik(adj,p,v)

if minFull == minTo + minFrom:
  print("SAVE HIM")
else:
  print("GOOD BYE")