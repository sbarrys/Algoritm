def find_parent(x,parent):
  if x == parent[x]:
    return x
  else: 
    return find_parent(parent[x],parent)

def union_parent( a,b,parent):
  pa = find_parent(a,parent)
  pb = find_parent(b,parent)

  if pa<pb:
    parent[pb] = pa
  else:
    parent[pa] = pb


    
while True:
  n,m = map(int,input().split())
  if n==0 and m==0 : 
    break
  visited = [False]*(n)

  parent = [0]*(n)
  for i in range(n):
    parent[i]=i

  adj_list = []
  summ=0
  all_summ=0

  for _ in range(m):
    a,b, cost = map( int, input().split())
    all_summ+=cost
    adj_list. append((cost,(a,b)))
  adj_list.sort()

  for cost,node  in adj_list :
    if find_parent(node[0],parent)==find_parent(node[1],parent):
      continue
    else:
      union_parent(node[0],node[1],parent)
      summ+=cost
  print(all_summ-summ)
