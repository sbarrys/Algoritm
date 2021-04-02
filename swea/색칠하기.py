t =int(input())
for tc in range(t):
  li=[]
  board=[[0]*10 for _ in range(10)]
  #색칠할 영역 갯수
  n =int(input())
 
  for _ in range(n):
    cnt=0
    p = list(map(int,input().split()))
    color = p[4]
    for i in range(p[0],p[2]+1):
      for j in range(p[1],p[3]+1):
        if board[i][j] != color:
          if board[i][j] != 0 :
            cnt+=1
            board[i][j]=3
          if board[i][j] == 0:
            board[i][j] = color
   
  print("#",end="")
  print(tc+1, end=" ")
  print(cnt)