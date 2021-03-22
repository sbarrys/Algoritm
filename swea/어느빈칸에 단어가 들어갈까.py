t= int(input())
def check(board,x,y,a,b):
  maxx=0
  cnt=0
  if x-1>=0 and board[x-1][y]==0:
    for idx in range(x,a):
      if board[idx][y]==1:
        cnt+=1
      else:
        break
    if cnt==b:
      maxx+=1
    cnt=0
  if y-1>=0 and board[x][y-1]==0:
    cnt=0
    for idx in range(y,a):
      if board[x][idx]==1:
        cnt+=1
      else:
        break
    if cnt==b:
      maxx+=1
    cnt=0
  if x==0 :
    for idx in range(x,a):
      if board[idx][y]==1:
        cnt+=1
      else:
        break
    if cnt==b:
      maxx+=1
    cnt=0
  if y==0 :
    cnt=0
    for idx in range(y,a):
      if board[x][idx]==1:
        cnt+=1
      else:
        break
    if cnt==b:
      maxx+=1
    cnt=0
    
  
  
  return maxx

for tc in range(t):
  summ=0
  a,b =map(int,input().split())
  board=[]
  for _ in range(a):
    board.append(list(map(int,input().split())))
  for x in range(a):
    for y in range(a):
      if board[x][y]==1:
        summ+=(check(board,x,y,a,b))
  print("#",end="")
  print(tc+1,end=" ")
  print(summ)
