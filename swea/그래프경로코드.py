def dfs(Now,To,adj,visited):
   
  visited[Now]=True
  path.append(Now)
  for Next in adj[Now]:
    if visited[Next]==False:
      visited[Next]=True
      dfs(Next,To,adj,visited)
      visited[Next]=False
  return
 
 
T = int(input()) 
for testcase in range(T):
  path=[]
  V,E = map(int,input().split())
  adj =[[] for _ in range(V+1)]
  visited =[False]*(V+1)
  for _ in range(E):
    nodeA,nodeB= map(int,input().split())
    adj[nodeA].append(nodeB)
  From,To=map(int,input().split())
 
  dfs(From,To,adj,visited)
  if To in path :  
    print("#",end="")
    print(testcase+1,end=" ")
    print("1")
  else:
    print("#",end="")
    print(testcase+1,end=" ")
    print("0")