
def rotation():
  global negu
  global b
  global count
  global exist
  while(1):
    count+=1

  #한칸씩 이동해준다.
    for i in range(LEN-1,-1,-1):
      if i == LEN-1: 
         temp = negu[i]
      else:
        negu[i+1]= negu[i]
        exist[i+1]=exist[i]
        exist[i]=False
    negu[0]=temp        
  #마지막 칸은 버려준다.
    exist[a-1]=False
  #로봇이 이동할수 있다면 한칸 앞으로 이동해준다.
    for i in range(a-2,-1,-1):
      if  exist[i]==True and negu[i+1]>0 and exist[i+1]==False:
        negu[i+1]-=1
        exist[i+1]=True
        exist[i]=False
  #마지막 칸은 버려준다.
    exist[a-1]=False
  #첫번쨰 칸이 내구도가 남아있다면 하나 탑승시켜준다.

    if negu[0]>0:
      exist[0]=True
      negu[0]-=1

  #갯수가 넘으면 리턴  
    if checkNegu()>=b:
      return count

def checkNegu():
  global negu
  return negu.count(0) 



a,b = map(int,input().split())
LEN = 2*a

negu =[0 for _ in range(LEN)]
negu  = list( map (int , input().split()))

exist = [False for _ in range(LEN)]
count = 0

print(rotation())