from collections import deque
n,m,k,x= map(int,input().split())
adj  = dict()
q=deque()
# mindis1 = [0  for _ in range(n+1)]
mindis = [1e9]*(n+1)
print(mindis)
for  i in range(n+1):
  adj[i]=[]
for _ in range(m):
  a,b  = map(int,input().split())
  adj[a].append(b)
for next in adj[x]:
  q.append(next)
  mindis[next]=1

while q:
  now = q.popleft()
  for next in adj[now]:
    if mindis[next]>mindis[now]+1:
      mindis[next]= mindis[now]+1
      q.append(next)
num=0
for i in range(n+1):
  if mindis[i]==k:
    print(i)
    num+=1
if num==0:
  print("-1")

