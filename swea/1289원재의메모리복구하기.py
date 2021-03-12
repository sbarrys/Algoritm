n = int(input())

def setOrigin(string):
  origin=["0"]*len(string)
  return origin
for i in range(n):
  a = list(input())
  origin =setOrigin(a)
  #돌아가면서 확인하기
  cnt=0
  for idx in range(len(origin)):
    if a[idx] != origin[idx]:
      for temp_idx in range(idx+1,len(origin)):
        if a[idx]=='1':
          a[idx]='0'
        else:
          a[idx]='1'
          
      cnt+=1

  print("#",i," ",cnt)