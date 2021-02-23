    def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  pa=  find_parent(parent,a)
  pb = find_parent(parent,b)
  if pb>pa:
    parent[pb]=pa
  else:
    parent[pa]=pb

n = int(input())
galaxy =[]
xlist=[]
ylist=[]
zlist=[]

for i  in range(n):
  x,y,z =  map(int,input().split())
  xlist.append((x,i))
  ylist.append((y,i))
  zlist.append((z,i))
  

xlist.sort()
ylist.sort()
zlist.sort()
edges=[]
for i in range(n-1):
  x1,i1 = xlist[i]
  x2,i2 =xlist[i+1]
  edges.append((x2-x1,i1,i2))
  y1,i1 = ylist[i]
  y2,i2 =ylist[i+1]
  edges.append((y2-y1,i1,i2))
  z1,i1 = zlist[i]
  z2,i2 =zlist[i+1]
  edges.append((z2-z1,i1,i2))

edges.sort()
parent=[0]*(n+1)
for i in range(n+1):
  parent[i]=i
sum=0
for cost,i1,i2 in edges:
  
  if find_parent(parent,i1)==find_parent(parent,i2):
    continue
  else:
    union_parent(parent,i1,i2)
    sum+=cost
print(sum)