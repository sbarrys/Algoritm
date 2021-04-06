import heapq
from collections import deque
def delete(distance,s,e ):
  q = deque()
  
  q.append(e)
  while q:
    now = q.popleft()
    if now == s:
      continue
    for before_node , before_cost in reverse_adj_list[now]:
            if distance[before_node] + before_cost== distance[now]:
              if visited[before_node][now]==False:
                  visited[before_node][now]=True
                  q.append(before_node)


def dik(distance,pq):  
    #다익스트라#
    while pq:

      dist , now = heapq.heappop(pq)
      if now  == e:
        break
      if dist >distance[now]:
        continue

      for nxt ,cost  in adj_list[now]:
        dist = distance[now]+cost
        if dist <distance[nxt] and visited[now][nxt]==False:
          heapq.heappush(pq,(dist,nxt))
          distance[nxt] = dist

while True:
  
  N, Ne = map(int, input().split())
  if N==0 and Ne==0:
    break
  s,e = map(int,input().split())
  edges = []
  for _ in range(Ne):
    edges.append(map(int,input().split()))# from , to,  cost

  adj_list=[[] for _ in range(N+1)]
  reverse_adj_list=[[] for _ in range(N+1)]
  for a , b , cost in edges:
    adj_list[a] .append((b,cost))
    reverse_adj_list[b].append((a,cost))

  #첫번째 다익스트라
  visited= [ [False]*(N+1) for _ in range(N+1)]
  distance = [1e9]*(N+1)
  pq = []
  heapq.heappush(pq,(0,s))
  distance[s]=0
  dik(distance,pq)

  if distance[e]==1e9:
    print(-1)
    continue
  delete(distance,s,e)


  #두번째 다익스트라
  distance = [1e9]*(N+1)
  pq = []
  heapq.heappush(pq,(0,s))
  distance[s]=0
  dik(distance,pq)
  if distance[e]!=1e9:
    print(distance[e])
  else:
    print(-1)

