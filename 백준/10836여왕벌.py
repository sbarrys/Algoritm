n,target_day= map(int,input().split())
#날짜수  갯수만큼
#제일 왼쪽열과 위쪽행의 애벌레들이 자라는 정도가 다음의 형식으로 주어진다
def setting_sizeUpBaord(zero,one,two):
  global sizeUpBoard
  SIZE = len(board)
  temp= 0
  for i in range(zero):
    if SIZE-1-i>=0:
      sizeUpBoard[SIZE-1-i][0] +=0
    else:
      sizeUpBoard[0][i-SIZE+1]+=0
  for j in range(one):
    if SIZE-1-zero-j>=0:
      sizeUpBoard[SIZE-1-zero-j][0]+=1
    else:
      sizeUpBoard[0][zero+j -SIZE+1]+=1
  for k in range(two):
    if SIZE -1-zero -one - k>=0:
      sizeUpBoard[SIZE-1-zero-one-k][0]+=2
    else:
      sizeUpBoard[0][zero+one+k-SIZE+1]+=2

def print_Board_edge(board):
  result =[]
  for i in range(len(board)):
    for j in range(len(board)):
      print(board[i][j],end=" ")
    print("")

def calculate_sizeUpBoard():
  global sizeUpBoard
  global board
  global n
  #위 왼쪽 왼쪽위
  for i in range(n-1,-1,-1):
    board[i][0]+=sizeUpBoard[i][0]
  for j in range(1,n):
    board[0][j]+=sizeUpBoard[0][j]

  for i in range(1,n):
    for j in range(1,n):
      sizeUpBoard[i][j]=max(sizeUpBoard[i][j-1], sizeUpBoard[i-1][j-1], sizeUpBoard[i-1][j])
      board[i][j]+=sizeUpBoard[i][j]

board= [[1]*n for _ in range(n)]
sizeUpBoard =[[0]*n for _ in range(n)]

for _ in range(target_day):

  zero, one, two = map(int,input().split())
  setting_sizeUpBaord(zero,one,two)


calculate_sizeUpBoard()
print_Board_edge(board)