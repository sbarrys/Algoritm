rsp = {(1, 1): 'draw', (1, 2): 'lose', (1, 3): 'win',
(2, 1): 'win', (2, 2): 'draw', (2, 3): 'lose',
(3, 1): 'lose', (3, 2): 'win', (3, 3): 'draw'}
def get_winner(a, b):
  result = rsp.get((li[a], li[b]))
  if result == 'win' or result == 'draw':
    return a
  return b

def game(s,e):
  if s>=e:
    return s
  mid = (s+e)//2
  w1  = game(s,mid)
  w2 = game(mid+1,e)
  
  return get_winner(w1,w2)

n= int(input())
for t in range(1,n+1):
  m= int(input())
  answer= 0
  li = list(map(int,input().split()))
  answer = game(0,len(li)-1)
  print('#%d %d' %(t,answer+1))